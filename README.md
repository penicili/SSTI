# Prototype vulnerable templating CTF

This prototype creates a small Flask app that uses Jinja2 to render user-supplied templates. It's intentionally vulnerable so players can exploit template injection to read a flag file baked into the container at /flag/flag.txt.

Files added/updated:

- `main.py` - generates a random flag and writes it to `./flag/flag.txt`.
- `app.py` - Flask app that renders user-supplied Jinja2 templates and provides `flag` in the template context.
- `Dockerfile` - builds a container exposing the app on port 5000.
- `requirements.txt` - Python dependencies.

Usage (local, without Docker):

1. Create a venv and install dependencies:
```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
```
2. Generate the flag:
```powershell
python main.py
```
3. Run the app:
```powershell
python app.py
```

Usage (Docker):

1. Generate the flag locally (creates `./flag/flag.txt`):
```powershell
python main.py
```
2. Build the image:
```powershell
docker build -t ctf-proto .
```
3. Run the container (the flag file will be baked into the container filesystem):
```powershell
docker run --rm -p 5000:5000 ctf-proto
```

Then point your browser to http://localhost:5000 and exploit the template engine to locate `/flag/flag.txt`.
