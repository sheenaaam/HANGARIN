"""
WSGI config for hangarin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import sys
import os

# Add your project directory to the sys.path
project_home = '/home/shx15/HANGARIN'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hangarin.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()