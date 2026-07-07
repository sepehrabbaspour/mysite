 #marhale aval vasl kardan path be view
#esm pooshe asli hatma zekr beshe inja / dar vaghe tooye directory feli ke code man dare ejra mishe , 
#yani dar kenar urls.py donbal views begard , dar gheyr in soorat hatma bayad esm pooshe ro zekr konim.
#chon dare az root asli be proje nagah mikone
# .views ha mishe goft , yani mige az tooye pooshe ie ke file urls man dare ejra mishe behesh naga kon
#hich farghi nadare che begim mysite.views / che .views

from django.urls import path
from website.views import *

app_name = "website"
#marhale aval vasl kardan path be view
#esm pooshe asli hatma zekr beshe inja / dar vaghe tooye directory feli ke code man dare ejra mishe , 
#yani dar kenar urls.py donbal views begard , dar gheyr in soorat hatma bayad esm pooshe ro zekr konim.
#chon dare az root asli be proje nagah mikone
# .views ha mishe goft , yani mige az tooye pooshe ie ke file urls man dare ejra mishe behesh naga kon
#hich farghi nadare che begim mysite.views / che .views

#marhale aval vasl kardan path be view
#esm pooshe asli hatma zekr beshe inja / dar vaghe tooye directory feli ke code man dare ejra mishe , 
#yani dar kenar urls.py donbal views begard , dar gheyr in soorat hatma bayad esm pooshe ro zekr konim.
#chon dare az root asli be proje nagah mikone
# .views ha mishe goft , yani mige az tooye pooshe ie ke file urls man dare ejra mishe behesh naga kon
#hich farghi nadare che begim mysite.views / che .views

urlpatterns = [
    path("" , index_view , name="index"),
    path("about" , about_view , name="about"),
    path("contact" , contact_view , name="contact"),
    path("json-test" , json_test),
    path("http-test" , http_test),
    path("test" , test_view , name="test")

]
#agar mesl path avali chizi tooye "" ke parametr aval hast nanevisim , vaghti migim 
#127.0.0.1:8000/website , safhe home baramoon miad bala
#hala baghie safaht ro be soorat website/contact ya ghar chiz dige ie mitoonim load konim.
#dar vaghe ba khali gozashtan "" dar parameter aval mitoonim shakhe asli (home) ro ba neveshtan
#website khali call konim. age 2 ta ya bishtar sho khali bezarim faghat avali ro negah mikone.
#va tasiri nadare ke baghie khalie va ejra nemishan
#agaram khali bashe esmesho jeloye website benevisim error 404 page not found migirim

#khob deghat kon ke agar bekhaym be har kodoom az in url ha dastresi dashte bashim , bayad url ro daghia benevesim 
#tooye search bar 

#amma vaghti behesh ye esm kootah bedim dige kari ba url ma nadare va tooye oon url ie ke mikhaym tarif konim migim
#ba estefade az method url boro too url boro in addres ro tooye app man peyda kon va bazesh kon   

#hala agar sharayeti pish biad ke chandin app darim ba name haye moshabeh kheyli rahat tooyer file base.html
#esm app ro mibarim va be in soorat {% url "website:about" %}

#in sakhtar url ham baraye dastresi be name hayi hast ke tarif kardim 

#hala age ino tanha b enevisim be app ma vasl nemishe va bayad balaye hamin file ye variable tarif konim
#va esm app moon ro behesh bedim be in soorat ke : app_name = "website"

#deghat kon ke tooye file base.html mesl in mored {% url "website:about" %} , bayad baraye tamam safahat mojood 
#be in soorat tarif shavad