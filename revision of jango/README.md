# Django 

# virtule environment
### uv env
- install uv
```bash
pip install uv
```
- create virtual environment
```bash
uv venv  # Create a virtual environment at .venv.
```
- activate virtual environment
```bash
source .venv/bin/activate
```
- lock current envrinment
```bash
uv pip freeze
```

### templates and statics
- after creatation of templates folder, you need to mention this in settings.py file in DIRS 
```python
TAMPLATE_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        "DIRS": [TAMPLATE_DIR],
    },
]
```
- after the creation of static folder, you need to mention this in settings.py file
- load static 
```python
{% load static %}
```
- in settings.py file write this after static url
```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```
- after this you able to link css file with herf tag
```python
link href="{% static 'css/style.css' %}"
```

### jinja2
- 