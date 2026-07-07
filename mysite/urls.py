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
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static


#marhale aval vasl kardan path be view
#esm pooshe asli hatma zekr beshe inja / dar vaghe tooye directory feli ke code man dare ejra mishe , 
#yani dar kenar urls.py donbal views begard , dar gheyr in soorat hatma bayad esm pooshe ro zekr konim.
#chon dare az root asli be proje nagah mikone
# .views ha mishe goft , yani mige az tooye pooshe ie ke file urls man dare ejra mishe behesh naga kon
#hich farghi nadare che begim mysite.views / che .views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , include("website.urls")),
    path("blog/" , include("blog.urls")) #in masala baraye ye safhe dige hast ke marboot be chizaei ke ma load mikonim 
    #tooye server asli django nadare va joda hast


    #http-test hamoon addresi hast ke tooye url bala browser mibinim. 
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
    #yadet nare age chand ta url dashtim hatma ba (,) az ham dige jodashoon konim

    #deghat kon age tooye ghesmat wievs app moon (website) , function haro neveshtim
    #vaghti mikhaym import konim function haro inja , bayad esm app moon ro begim

    #hala barye inke ghesmat url khalvat tar beshe bayad ye pooshe urls.py 
    # tooye app moon (website) besazim , va url haro be oonja montaghel konim.
    #file urls tooye app vojood nadare pas khodemoon misazim.
    
    #deghat kon ke be joz ghesmat admin va package hash ke import shode ;
    #baghie ro be hamrah package hayi ke import kardim 
    #deghat kon ke import path ham bayad copy beshe.

    #hala bayad in url hayi ke copy shodan tooye file urls.py app ma 
    #bayad be in soorat beheshoon dastresi peida konim : 
    #ebteda include ro dar django.urls jeloye path import mikonim.
    #dar edame, dar object path aval esm app va baad yedoone / jelosh tooye " "
    #hala baraye parametr dovom include ro minevisim va tooye parantez jelosh aval esm app , 
    #sepas (.) mizanim va esm file urls ro minevisim tooye " "
    #yani nahayata be in soorat mishe : path("website/" , include("website.urls"))
    #hala vaghti mikhaym khorooji begirim tooye moror gar bayad be in soorat benevisim
    #baad az run kardan server migim 127.0.0.1:8000/website/http-test 
    #ya masala 127.0.0.1:8000/website/json-test ta bian bala safahatmoon.


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)#static root
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media root
 

#inja ba in ravesh url pattern asli proje moon static url haro ezafe mikonim
#deghat kon ke bayad kharej az bracet url pattern bashe neveshtan in mozoo.

#in dar vaghe mige boro be static hayi ke ma darim ye bakhsh dige ezafe kon ke dar bar girande file haye
#static man hastesh.

#albate bayad majule haye marboote ro ham bala import konim ke be soorat zire:
# from django.conf import settings --> file settings.py ro miare baram ke static files va static root ro
#azash dar biarim

# from django.conf.urls.static import static --> ye doone ham khode shakhes amalkard kar ba static haro 
# baramoon miare

#deghat kon ke ham static root va ham media root dar file settings.py tarif shodand

#ham media ro be url pattern ezafe mikonim va ham static haro

#alan age local host ro search bokonim va ye addres bikhodi bedim toosh mibinim ke dastresi be file haye media ham 
#baram ijad shode , alave bar oon be file haye static ham dastresi darim.

#ina addres dehi haye asli bood ke bayad behesh ezafe mikardim baraye static va media
#ama ye chizi : ma bayad directory static hamoon ro ye jaye general (koli) barash dar nazar begirim ke tamoom
#static hamoon ro betoonim az oonja farakhooni konim.

#amma baraye in kafie ye directory baraye static ijad konam ke in karo baram anjam bede ke be in soorat hast ke bayad 
#tooye file setting neveshte beshe zir staticurl va media_url

#deghat kon ke in static_url va media_url bayad tooye file url asli proje set beshan 

#mantegh in kar be  in soorat hast ke mige man gharare static hayi dashte basham ke url sh tooye file 
#settings man tarif shode 

#hala dar in soorat miotoonim ba estefade az addres hayi ke joda baraye man ijad mishe be file haye static ham 
#dastresi dashte basham.
#chon vaghti ye url bedim ke vojood nadare ye addres static behemoon namayesh mide.


#in file dar haghighat shemaye url amalkard haye mano negah dari mikone ke bar farz mesal ye addresi ke man baraye site am daram , 
#oon addres ha inja bayad tarif beshe 

#masala ye addres masala aparat.com/shorts ya hala har chizi , in addres ha inja tarif shodan.
#hala ya zir shakhe ha az jaye dige dare tamin mishe ya khode addres mostaghima inja tarif shode.

#baraye tarif addres miaim tooye url patterns (line 20) , tooye list pattern hayi az url ke darim , 
#migim banast man ye pattern ya path gharare dashte basham ke esm path man gharare az 'admin/ biad
#(bejaye admin har chizi mishe gozashgt)