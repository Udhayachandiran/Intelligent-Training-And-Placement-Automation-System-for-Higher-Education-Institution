"""
ASGI config for Intelligent_Training_And_Placement_Automation_System_For_Higher_Education_Institution project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Intelligent_Training_And_Placement_Automation_System_For_Higher_Education_Institution.settings')

application = get_asgi_application()
