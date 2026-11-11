# De notas a datos: plantilla del taller

Proyecto base del taller del PyDay La Paz. Cada archivo trae un ejemplo comentado de lo que vas a necesitar.

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate          # macOS / Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env          # macOS / Linux: cp .env.example .env
python manage.py check
```

Pega tu clave de [Google AI Studio](https://aistudio.google.com/apikey) en `GEMINI_API_KEY` dentro de `.env`.

El front: https://github.com/AASG2003/asistente-medico-frontend
