import os
import uuid
from unstructured.partition.pdf import partition_pdf  # <--- ¡ESTO FALTA AQUÍ!
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.serving import ChatMessage, ChatMessageRole

def normalizar_ruta(ruta):
    """Limpia la ruta para asegurar comparaciones exactas."""
    # Quitar prefijo dbfs: si existe
    ruta = ruta.replace("dbfs:", "")
    # Asegurar que no haya espacios extra al inicio/fin
    return ruta.strip()

def parsear_con_jerarquia(ruta_archivo):
    # (Tu función de parsing original - sin cambios)
    try:
        elements = partition_pdf(filename=ruta_archivo, strategy="fast")
        sections = []
        current_section = {"title": "Introducción / General", "content": []}
        for el in elements:
            texto = str(el)
            if len(texto) < 10: continue
            if el.category == "Title":
                if current_section["content"]:
                    sections.append({"title": current_section["title"], "text": "\n".join(current_section["content"])})
                current_section = {"title": texto, "content": []}
            elif el.category in ["NarrativeText", "Table", "ListItem", "UncategorizedText"]:
                current_section["content"].append(texto)
        if current_section["content"]:
            sections.append({"title": current_section["title"], "text": "\n".join(current_section["content"])})
        return sections
    except Exception as e:
        print(f"⚠️ Error parseando {ruta_archivo}: {e}")
        return []

def generar_abstract(texto_seccion):
    # (Tu función de LLM original - sin cambios)
    w = WorkspaceClient()
    prompt = f"Resume este contenido técnico en 3 oraciones densas:\n{texto_seccion[:3500]}"
    try:
        response = w.serving_endpoints.query(
            name="databricks-meta-llama-3-1-8b-instruct",
            messages=[ChatMessage(role=ChatMessageRole.USER, content=prompt)],
            max_tokens=200, temperature=0.1
        )
        return response.choices[0].message.content
    except Exception as e:
        return texto_seccion[:200]