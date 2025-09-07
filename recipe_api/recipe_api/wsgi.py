"""
WSGI config for recipe_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Path to the project root
project_home = '/home/Swiss003/Recipe_Management_API/recipe_api'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'recipe_api.recipe_api.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
