 #marhale aval vasl kardan path be view
#esm pooshe asli hatma zekr beshe inja / dar vaghe tooye directory feli ke code man dare ejra mishe , 
#yani dar kenar urls.py donbal views begard , dar gheyr in soorat hatma bayad esm pooshe ro zekr konim.
#chon dare az root asli be proje nagah mikone
# .views ha mishe goft , yani mige az tooye pooshe ie ke file urls man dare ejra mishe behesh naga kon
#hich farghi nadare che begim mysite.views / che .views

from django.urls import path
from website.views import *
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
    path("" , index_view),
    path("about" , about_view),
    path("contact" , contact_view),
    path("json-test" , json_test)

]
#agar mesl path avali chizi tooye "" ke parametr aval hast nanevisim , vaghti migim 
#127.0.0.1:8000/website , safhe home baramoon miad bala
#hala baghie safaht ro be soorat website/contact ya ghar chiz dige ie mitoonim load konim.
#dar vaghe ba khali gozashtan "" dar parameter aval mitoonim shakhe asli (home) ro ba neveshtan
#website khali call konim. age 2 ta ya bishtar sho khali bezarim faghat avali ro negah mikone.
#va tasiri nadare ke baghie khalie va ejra nemishan
#agaram khali bashe esmesho jeloye website benevisim error 404 page not found migirim


