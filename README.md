# 🧠 Databricks Hierarchical RAG

Un sistema **End-to-End RAG (Retrieval-Augmented Generation)** de grado empresarial construido sobre la **Databricks Data Intelligence Platform**.

Este proyecto implementa una arquitectura **layout-aware** para procesar documentos técnicos complejos (tablas, encabezados, normativas), orquestando la ingesta con **Delta Lake** y desplegando una interfaz segura aplicando principios **SOLID** y **Clean Code**.

---

## 📸 Demo

- Arquitectura lógica  
- Interfaz de usuario  
- Estrategia de *Layout-aware Chunking*  
- Chatbot citando fuentes  

*(ver carpeta `/assets`)*

---

## 🚀 Características Clave

### 1. Backend: Ingesta Jerárquica Inteligente

A diferencia de los RAGs tradicionales que fragmentan texto sin contexto, este sistema utiliza **Unstructured** y **Apache Spark** para:

- Detectar y respetar la estructura del documento (títulos, secciones, tablas).
- Generar **resúmenes sintéticos por sección** usando **Llama 3**, mejorando la recuperación semántica.
- Almacenar **metadatos enriquecidos** en **Delta Lake**.

---

### 2. Data Engineering: Orquestación Robusta

Implementación de una **malla de trabajos** con **Databricks Workflows**, diseñada para producción:

- ✅ **Carga Incremental**  
  Solo procesa archivos nuevos en el Data Lake.

- ✅ **Blocking Sync**  
  Garantiza consistencia esperando a que **Vector Search** finalice la indexación.

- ✅ **Auto-validación**  
  Ejecuta un *Golden Dataset* de preguntas para validar calidad antes de finalizar el job.

---

### 3. Frontend: Ingeniería de Software

La interfaz no es un script aislado. Es una **Databricks App (Streamlit)** diseñada con arquitectura de software:

- **Patrón Factory**  
  Para la gestión de clientes y conexiones.

- **DTOs (Data Transfer Objects)**  
  Tipado estricto para documentos recuperados.

- **Service Principals (OIDC)**  
  Autenticación segura sin credenciales hardcodeadas.

---

## 🛠️ Tech Stack

- **Plataforma**: Databricks Data Intelligence Platform  
- **Compute**: Spark Serverless & Databricks Apps  
- **Storage**: Unity Catalog (Volumes & Delta Tables)  
- **Vector Database**: Databricks Vector Search (Hybrid Index)  
- **LLM Serving**: Meta Llama 3 (70B Instruct) vía Model Serving  
- **Frontend**: Streamlit  

---

## 📂 Estructura del Proyecto

```bash
databricks-hierarchical-rag/
├── app/
│   ├── app.py
│   └── requirements.txt
├── notebooks/
│   ├── 01_ingest_table.py
│   ├── 02_sync_index.py
│   └── 03_validate_rag.py
├── utils/
│   └── parsing_utils.py
├── assets/
└── README.md
```

---

## 🔧 Configuración y Despliegue

### Prerrequisitos

- Workspace de Databricks con Unity Catalog habilitado.
- Endpoint de Model Serving activo.
- Endpoint de Databricks Vector Search.

---

### Paso 1: Configurar el Backend

```python
CATALOG = "workspace"
SCHEMA = "default"
VOLUME_PATH = "/Volumes/workspace/default/mydocuments/"
```

---

### Paso 2: Desplegar la App

1. Crear una nueva Databricks App.
2. Vincular la carpeta `app/`.
3. Configurar permisos del Service Principal en Unity Catalog.

---

## 🧠 Decisiones de Arquitectura

### ¿Por qué Layout-aware Chunking?

Preserva la jerarquía semántica y mejora la precisión del RAG.

### ¿Por qué Blocking Sync?

Evita inconsistencias por indexación eventual.

### Principios SOLID en el Frontend

SRP aplicado separando conexión, lógica RAG y UI.

---

## 🤝 Contribución

Abre un issue antes de enviar un PR.

---

## 📝 Licencia

Licencia myprojects.

---

## 👨‍💻 Autor

**Tu Nombre** Johnkl27
Data Engineer In Progress | Cloud Architecture Student  
