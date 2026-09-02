#ravand koli kar ine : sitemaps.py ro tooye app moon dorost mikonim. motaviatesh ro tooye dictionary ke urls asli proje moon hast 
#ezafe mikonim va baaes load shodanesh tooye sitemap mishe.

#baraye inke bekhaym in karo anjam bedim kafie hast ke tooye google serach konim django sitemap
#va baraye jahayi ke mikhaym query bezaninm in tike ro az ducumetion copy sh konim 


from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "weekly" #ino barabar ba weekly mizarim ke har hafte taghir kone va ne har rooz. never ham dare ke mishe be hich onvan
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date

#tarighba mesl ghabli mimoone , montaha Entry taghir midim be post chon ma post darim entry ke nadarim.
#va be jaye Entry post haro mikhaym query konim.
#is_draft ro ham be status taghir midim. va meghdaresh ro true mikonim. 
#tooye return obj.pub_date , bejaye pub_date bayad begim published_date
#nokte injast chon ke az ducumetion copy kardim ino , maghadir ro be hamoon chizayi ke khodemoon darim taghir midim.

#in ro ham bayad be url asli proje ezafe konim.

#amma bazam kar nemikone chera ? in error ro darim ke 'Post' object has no attribute 'get_absolute_url'
#yani chi ? mige post ma attribute ie be nadare. in ye shakhesi hast ke tooye model be ye seri az adavati ke serfa gharare farakhani beshan
#ya jahayi bekhan index beshan va estefade beshan , gharare ye function ie dashte bashim ke ba estefade az in function ie ke hastesh 
#kar farakhooni url hasho anjam bedim. yani bayad tooye modelasion post ye function dorost konim be nam get_absolute_url
#berim tooye modelasion marboot be Post.

#khob ba in taghirati ke dadim alan dare kar mikone vali url haro dare none behemoon barmigardone , in be dard ma nemikhore
#dota rah darim. ya bayad location sh ro dashte bashim , yani ye function tooye in file besazim be in soorat
def location(self , item):
    return reverse('blog:single',kwargs={'pid':item.id})
#va tooye inja addres haro reverse konim va bareshoon gardoonim.

#ya inke bayad az tarigh get_absolute_url berim jelo. hala in get_absolute_url ro chetor benevisam ? ba estefade az reverse
#ke tooye models blog moon ezafe ah mikonim.

#baghie tozihat tooye models.py blog

#yadet nare age inja khasti bahash kar koni bayad from django.urls import reverse oon bala import koni eyn modelasion.

#oon tike codi ke tooye modelasion neveshtim baraye in bahs inja ham sadeghe faghat dige nemitoonim begim self id. be jash bayad begim 
#migan oon item ie ke man daram barat mifrestam az tooye def items ke query zadim (ina az pish tarif shode hast) 
#oon item hayi ke man query kardam va daryaft kardam ro mikham tak tak ba estefade
#az item behet bedamesh. pas object man dige esmesh self nist item hast.
#dar vaghe agar begim item.id man ro bede , post id ro behem mide.