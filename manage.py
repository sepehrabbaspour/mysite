#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


#in file modiriat amalkard ha va dastoorati hastesh ke ma bahashoon kar mikonim , in dastoorat serfa ba proje django
#ertebat bargharar mikonim.

#masala dastoorati mesl runserver , start project , ... tavasot in file modiriat mishan.

#age dastoorat ro yademoon raft vared mashim majazi moon mishim tooye terminal va migim pythom manage.py , bedoon hich dastoor dige.
#list dastoorat ro baramoon list mikone.

#hala ghesmat haye mokhtalef dare ke ba rang ghermez moshakhas shode har kodoom mal che bakhshi hast.

#masala ba runserver , ye mini server run kardim va ba startproject ye proje run kardim