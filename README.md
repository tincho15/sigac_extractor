# SIGAC Extractor

Scaffolding inicial de una API en Python con FastAPI, organizada siguiendo una arquitectura limpia.

## Requisitos

- Python 3.10 o superior
- `pip`

## Ejecutar localmente

Desde la carpeta raíz del proyecto, crea y activa un entorno virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

En macOS o Linux, activa el entorno con:

```bash
source .venv/bin/activate
```

Instala las dependencias de desarrollo y ejecuta la aplicación:

```bash
python -m pip install -r requirements-dev.txt
python -m uvicorn app.main:app --reload
```

La API estará disponible en <http://127.0.0.1:8000>. La documentación interactiva se encuentra en <http://127.0.0.1:8000/docs>.

## Health check

```text
GET /health
```

Respuesta esperada (`200 OK`):

```json
{"status":"ok"}
```

Ejecuta las pruebas con:

```bash
python -m pytest
```
