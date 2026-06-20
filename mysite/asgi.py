"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()


#in file baraye task ha ya amalkard hayi hast ke marboot be shakhes hayi mesl web sooket va kheili chizaye dige mesl : 
#channel va in dastana mishe ke baada rajebshoon sohbat mishe.