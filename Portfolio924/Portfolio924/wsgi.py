import os
import sys
sys.path.append('/opt/bitnami/projects/Portfolio924')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/Portfolio924/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Portfolio924.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

