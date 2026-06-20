"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()



#in file pol ertebati hast ke ba sakhtar apach bargharar mikonim.
#hala apach chie ? ye server hast ke serfa ertebat bein amalkard hayi mesl database , bein safahat , 
#va dar haghighat oon request ha va oon darkhast hayi ke karbar mikhad bein ina rad va badal kone ro baramoon ijab mikone.
