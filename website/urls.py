from django.urls import path
from website.views import http_test , json_test #marhale aval vasl kardan path be view
#esm pooshe asli hatma zekr beshe inja / dar vaghe tooye directory feli ke code man dare ejra mishe , 
#yani dar kenar urls.py donbal views begard , dar gheyr in soorat hatma bayad esm pooshe ro zekr konim.
#chon dare az root asli be proje nagah mikone
# .views ha mishe goft , yani mige az tooye pooshe ie ke file urls man dare ejra mishe behesh naga kon
#hich farghi nadare che begim mysite.views / che .views

urlpatterns = [
    path("http-test" , http_test),
    path("json-test" , json_test)
]