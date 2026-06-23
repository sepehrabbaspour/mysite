#hala bayad function view ro besazim. chon goftim view function (tabe) dare.
#ye tabe makhsoos khode url ie ke tooye file urls ijad kardim misazim

from django.http import HttpResponse 
#yani migim az http method hayi ke vojood dare pasokh mikham ijad konam baraye karbar
#(HttpResponse) #in marboot be line 38 ta 40 file urls.py hast (babat errori ke dashtim tooye run kardan)

def http_test(request):
    return HttpResponse("<h5>welcome to http-test page</h5>") #hala pasokh ma bayad peygham maro dar bar begire

#hala bayad bebinin sakhtar tabe baraye javab dadan (oon voroodi hayi ke behesh midim) ,
#vaghti dare az ye url behesh vasl mishe ye seri shakhes hayi gharare biad toosh.
#in shakhes ha yeki sh request hast . yani darkhast karbar man vared tabe mishe
#be onvan arg voroodi avalie.
#dar vaghe darkhast karbar man bayad tooye tabe bashe ke barresi beshe ke khob
#shayad ye chizi ferestade bashe ya tooye darkhstesh post ya get karde bashe ya yeseri dade dige.
#ghabeliat dastresi be ino az tarigh object reqest behemoon mide.

#hala age bana bashe in dade ie ke daryaft kardam ro (albate alan kar khasi ba request nadarim) , 
#faghat dar javab vaghti ke url baz shod ye peygham bedam , in karo ba return anjam midim.
#har chizi mitoone bashe masala ye string

#hala tooye in peygham (tooye hamoon return) momkene ke bekhaym code html bargardoonim.
#masala matn ro mitoonim bezarim bein tag <h1>
#hamoon tag behesh emal mishe 
#haminjoori ke ino save mikonim va mire jelo , ba estefade az DEBUG = True ,
#khodesh amaliat ro anjam mide va be vasete mini apachi ke vojood dare tooye django hey anjam mide
#va bar migardoone0 faghat kafie baad az save safhe web ro refresh bezanim
#alan ke tag html gozashtim az safhe web moon inspect begirim mibinim ke ye dige text khali nist.
#html hast