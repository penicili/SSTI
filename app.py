from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# serve a simple page that renders a user-provided template string
# intentionally vulnerable to allow Jinja2 template injection for CTF

TEMPLATE = '''
<h1>Welcome to CTF template playground</h1>
<form method="POST">
  <label for="tpl">Template:</label><br>
  <textarea id="tpl" name="tpl" rows="6" cols="60">{{ 'Hello, world' }}</textarea><br>
  <button type="submit">Render</button>
</form>
<hr>
<h2>Rendered output</h2>
<div style="padding:10px;border:1px solid #ccc;background:#f8f8f8">{{ rendered|safe }}</div>
'''


def read_flag():
    # read flag from known path inside container
    flag_path = os.path.join('/', 'flag', 'flag.txt')
    # fall back to local folder when running outside container
    if not os.path.exists(flag_path):
        flag_path = os.path.join(os.getcwd(), 'flag', 'flag.txt')
    try:
        with open(flag_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return 'FLAG_NOT_FOUND'


@app.route('/', methods=['GET', 'POST'])
def index():
    rendered = ''
    if request.method == 'POST':
        tpl = request.form.get('tpl', '')
        # render the user-provided template inside a context that includes flag
        # intentionally include the flag in the globals for exploitation
        context = {
            'flag': read_flag(),
            'os': os,
        }
        try:
            rendered = render_template_string(tpl, **context)
        except Exception as e:
            rendered = f"Template error: {e}"
    return render_template_string(TEMPLATE, rendered=rendered)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
