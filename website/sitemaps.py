#tooye aksar site agar deghat konim ye bakhshi dare be esm sitemap ke yuejoor estandard mahsoob mishe
#be in soorat mishe behesh dastresi dasht ke begim masala maktabkhooneh.org/sitemap.xml

#hala ina chie ? addres haye safahati ke vojood dare tooye ye site ke mikhaym begim robat ha bian va behesh
#negah konand ro negah dari mikonam. be joz robat ha kheli application haye dige ie hastand ke az in site map estefade mikonnnad

#yeki az estefade hash ine ke mitoonam safahati ke daram ro rahat tar index beshe ro dar ekhtiar robat ha bezaram.

#baraye setup kardan aval 'django.contrib.sitemaps' tooye bakhsh installed apps tooye file settings.py ezafe mikonim.
#baad bayad app_dirs ro moshakhas konim tooye tooye template ha ke anjam shode az ghabl. va dar nahayt site framework ro ham bayad barash
#faal konim. ke ghbla in karo kardim.
# hala baraye estefade momkene ye seri safahat dashte bashim ke halat static daran va ye seri az safahat hast ke halat dynamic daran.

#aval berim soragh static ha : baraye in kar ye file sitemaps.py be ezaye har app ijad mikonim (mesl inja ke tooye app website sakhtim ino)
#hala baraye in ke site map ok beshe bayad 2 ja taghirat bedim , ke yekish tooye urls.py proje hast , yani dar inja pooshe mysite ke proje
#django ma oonjast. hala vase inke bekhaym url ro ezafe konim , mitooni har chizi dari dar nazar begiri va 
# path(
#         "sitemap.xml",
#         sitemap,
#         {"sitemaps": sitemaps},
#         name="django.contrib.sitemaps.views.sitemap",
#     )
#be urlpattern ha ha ezafe koni. faramoosh nakon hatma ghablesh from django.contrib.sitemaps.views import sitemap ro balaye file urls.py 
#asli benevisim

#in ro ham be onvan ye dicionary balaye file urls.py asli , zir django.contrib.sitemaps.views import sitemap ezafe mikonim.

# sitemaps = {
#     "static": StaticViewSitemap,
# }

#hala sitemaps az koja dare miad ? safahati ke site map sh ro dorost kardim.
#hala StaticViewSitemap az koja dare miad ? in daghigha hamoon classi hast ke tooye file sitemaps.py yani in file misazamesh.
#yadet nare inam bayad import konim tooye urls asli : from website.sitemaps import StaticViewSitemap 
#ke be in soorate : 
from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap): #classi ke gharare az sitemaps.Sitemap ers bari kone
    priority = 0.5 #in mige cheghad zood tar olaviat dare ke in index beshe. (baraye robat darim taien sh mikonim)
    changefreq = "daily" #mige cheghadr momkene taghirat dashte bahse be ezaye ye baze ie ke masala migim daily ya roozane
    #albate ina hamash dare baraye robat taien mishe. be joz roozane mitoonim begim masala haftegi ya har chizi.


    def items(self):
        return ['website:index', 'website:about', 'website:contact']
        #item hayi ke mikham biari va static hasho static hasho ijad konam az koja miad ? 
        #inja tooye return mitoonim asami sho biarim va ya biaim query bezanim ke ma mikhaym query bezanim.
        #vali asami ghesmat haro inja minevisim.

    def location(self, item):
        return reverse(item)

#inaro tooye google search kardim django site map va az ducumetion khode django ina ro bardashtim.

#amma django urls reverse chkar mikone ? be ma in ejaze ro mide ke bekhaym ye esm va application ie ke darim ke ghabla bahash kar kardim 

#class StaticViewSitemap(sitemaps.Sitemap): #classi ke gharare az sitemaps.Sitemap ers bari kone
#pas migim gharare ye class ie dashte basham ke gharare az  ers bari kone.

#amma dar in halat xml site nemiad bala baraye in ke pattern ie ke man sakhtam ro nemifahme.
#tooye app ha yadete barash app name tarif mikardim ke tooye url ha betoonim be in soorat behesh dastresi dashte bashim : 
#website:index.
#inja ham daghigha hamoon sakhtar ro tooye function items darim yani az in  return ["index", "about", "contact"]
#bayad be in taghir kone : return ['website:index', 'website:about', 'website:contact']

#in alan kar mikone va deghat kon ke url hash alan baraye man miad.

#hala inja motavjeh shodim site framwork ro baraye chi sakhtim. alan url haye ma 127.0.0.1:8000 dare miad khob , 
#chon ke tooye setting SITE_ID ro barabar ba 2 dadim. agar barabar ba 1 bedim hame url haye ma barabar example.com mishan.
#amma alan mizarim hamoon 2 bemoone
#hala zamani ke bekhaym site ro deploy konim bayad oon addres dorost domain ro behesh bedim ke behesh miresim.

#ta alan be soorat static in karo anjam dadim amma alan mikhaym be soorat dynamic safahat blog ro ham biarim toosh.
#chetory ? (yekami hasase deghat kon) be in soorat ke: 





