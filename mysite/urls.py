"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

#in file dar haghighat shemaye url amalkard haye mano negah dari mikone ke bar farz mesal ye addresi ke man baraye site am daram , 
#oon addres ha inja bayad tarif beshe 

#masala ye addres masala aparat.com/shorts ya hala har chizi , in addres ha inja tarif shodan.
#hala ya zir shakhe ha az jaye dige dare tamin mishe ya khode addres mostaghima inja tarif shode.