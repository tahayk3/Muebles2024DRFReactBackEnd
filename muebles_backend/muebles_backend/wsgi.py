import os
from django.core.wsgi import get_wsgi_application

# Cambia el módulo a 'muebles_backend.muebles_backend.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'muebles_backend.muebles_backend.settings')

application = get_wsgi_application()

