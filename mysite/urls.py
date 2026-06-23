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
from mysite.views import http_test #marhale aval vasl kardan path be view
#esm pooshe asli hatma zekr beshe inja / dar vaghe tooye directory feli ke code man dare ejra mishe , 
#yani dar kenar urls.py donbal views begard , dar gheyr in soorat hatma bayad esm pooshe ro zekr konim.
#chon dare az root asli be proje nagah mikone
# .views ha mishe goft , yani mige az tooye pooshe ie ke file urls man dare ejra mishe behesh naga kon
#hich farghi nadare che begim mysite.views / che .views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("http-test" , http_test) #http-test hamoon addresi hast ke tooye url bala browser mibinim. 
    #har chizi mitoone bashe. in serfa test hast va rajeb baghie url ha sohbat mishe
    #alan in addres bayad be ye view motasel beshe yani injoori : path(url addres , view)
    #be gheyr az view eleman haye dige ham mishe be path ezafe kard masala : path(url addres , view , name)
    #rajeb name sohbat mishe
    #in sakhtari ke alan pish mirim standard nist bada okay mishe vali alan be in soorat migim ke : 
    #ye file be nam views tooye pooshe proje (mysite) misazim
    #edame tooye file 
    #khob dar in halat (path("http-test" , http_test)) hata oon safhe asli django ro ham nadarim ,
    #chon darim over write mikonim chizayi ke az ghabl vojood dashte ro
    #hata age http-test ro check bokonim behemoon mige ke string object moon nemitoone get beshe
    #hala bayad ye tabe dige ro farakhooni konim ta in kar baramoon anjam beshe
    #baghie too file views.py 

]

#in file dar haghighat shemaye url amalkard haye mano negah dari mikone ke bar farz mesal ye addresi ke man baraye site am daram , 
#oon addres ha inja bayad tarif beshe 

#masala ye addres masala aparat.com/shorts ya hala har chizi , in addres ha inja tarif shodan.
#hala ya zir shakhe ha az jaye dige dare tamin mishe ya khode addres mostaghima inja tarif shode.

#baraye tarif addres miaim tooye url patterns (line 20) , tooye list pattern hayi az url ke darim , 
#migim banast man ye pattern ya path gharare dashte basham ke esm path man gharare az 'admin/ biad
#(bejaye admin har chizi mishe gozashgt)