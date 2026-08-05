from django import template
from blog.models import Post

register = template.Library()

# in hatma bayad neveshte magar na kar nakhahad kard in file blgo_test ma har chand tooye oon safhe html ie ke ke niazesh darim 
# ba {% load esm file %} ke dar inja darim {% load blog_tags %} load karde bashim file haro ]
#sakhtar file ha ham bayad daghigha be hamin soorat bashe ke tooye app ie ke mikhaym template tag besazim khodemoon (dar inja app blog)
#ye folder ijad mikonim be esm templatetags va tooye in folder ye file __init__.py misazim.
#hala ye file dige ham misazim ke esm oon file be in soorat hast ke aval esm app va baad kari ke mikhaym ba oon file anjam bedim
#masala inja esm in file blog_tags hast yani template tag haye marboot be app blog
#in sakhtar bala ham tooye har file ie ke mikhaym azash be onvan template tag estfade konim vajebe 
#alan ta inja template tag ma asmadast ta bahash ye seri kara anjam bedim
#dar asl template tag ha shkhes hayi hastand ke mitoonim tooye safahat azash estefade konim be jaye inke khodemoon ro dargir view konim.


@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count() 
    #inja migim baad az inke filter kardi bar asas oonyi ke status shoon barabar 
    #1 ya true hast bai va ba count tedadesh ro beshmar , agar in nabashe natije query ro mibinim
    #method count ham baramoon mishmore tedad sho
    return posts
@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts
#inja mikhaym post haro az hamin blog_tags peyda konim , alan tam post hayi ke ijad shode ro query sho mikhaym 

#khob deghat kon ke baraye inke betoonim ye simple tag besazim tooye hamin file ke marboot be template tag haye blog hast
#ye function misazim ba esm delkhah va baad masala migim ye reshte ro bargardoon serfa ok ? 
#hala in function bayad register beshe , be in soorat ke ke balaye function migim @register.simple_tag 
#chon fela darim az simple tag ha estefade mikonim ino migim va deghat kon tooye oon safhe ie ke mikham in function ro call konim
#dar inja safhe test.html bayad be in soorat bashe ke {% esm funtion %} dar inja mishe {% hello %} 
#va hamchenin balaye safhe ba {% load esm file %} dar inja {% load blog_tags %} hatma load sh konim.

#nokte : agar funtion ie ro sakhtim , function ma bayad marboot be oon template tagi bashe ke dare load sh mikone
#template tag baad az inke load shod , oon tabe load shode bayad register shode bashe mesl inja 
#hala esmesh moshakhase in mishe ke chetor gharare bahash barkhord beshe , masala mesl inja simplte tag ye eleman sade hast
#ke kar sade ie ham anjam mide.
#masala ye az kar ha hamini ke alan bahash anjam dadim yani return kardan ye reshte (string)
#dar hal hazer code ine : 
# @register.simple_tag
# def hello():
#     return 'hello' 
#hala berim bahash ye amaliat riazi anjam bedim
#khob alan code ma ine 
# @register.simple_tag
# def function(num_1):
#     return num_1 + 2

#deghat kon inja ke esm function avaz shode bayad tooye safhe html ham avaz beshe , dar inja be in soorat : {% funtion %}
#hala bayad arguman a ro ham behesh bedim tooye safhe test.html amma chetor ? khonb bayad ye adadi bashe ke tooye function ma
#ba 2 jam beshe va natije bargarde dige
#pas be in soorat tooye function oon adad voroodi mored nazar moon ro minevisim : {% function 2 %}
#alan arguman voroodi function moon ke num_1 hast ye adad dare ke tooye test.html goftim behesh (dar inja 2)
#hala 2 mishine jaye num_1 ba 2 jam mishe va natinje tooye safhe namayesh dade mishe. be in soorat adad moarefi mikonim

#pas hala fahmidim ke mitoonim ye seri amaliat anjam bedam , ye seri voroodi ha bedam va azash bekham ke kari ro baram anjam bede

#khob hala mitoonim ye seri amaliat ha ham anjam bedim ke khorooji ye chizi ro dashte bashe manzoor chie ? 
#masala mikhaym ye function tarahi konim ke tedad post hayi ke ta alan nashr dadim ro behem bargardoone 

#hala ma mitoonim baraye simple_tag (@register.simple_tag) ye sei khosoosiat ha ham barash tarif konim 
#masala @register.simple_tag(takes_contntex=True) yani eleman hayi ke tooye safhe ham dare miad ro to mitooni dar nazar begiri 
#ke az tarigh view dare miad.

#ye chiz dige ham ke vojood dare bahs name hast ke ma miroonim esm in function ro avaz konim masala
# @register.simple_tag(name=minustwo) ke tooye mesal khodemoon code ro be in soorat taghir midim:

# @register.simple_tag(name='plustwo')
# def function(num_1):
#     return num_1 + 2

#hala deghat kon ke tooye safhe ie ke darim voroodi be arguman voroodish pas midim dige nabayad benevisim function
#bayad esm simple tag ro biarim yani tooye safhe html darim {% plustwo 5 %}
#dige esmi ke be simple_tag dadim ro estefade mikonim.

#hata mitoonim mesl khode python tooye function ha baraye voroodi meghdar defult taien konim yani :
#def function(num_1 = 3)
#hala age dige tooye safhe voroodi pas nadim in kar mikone va meghdar defult be onvan voroodi daryaft mishe
#agar ham voroodi behesh pas bedim tooye safhe ke hamoon meghdar ro dar nazar migire


#hala ma mikhaym chikar konim ? tedad post hayi ke ijad kardim ro begirim ke dar edame code ro minevisim
#alan ma mikhaym tedad post hayi ke ijad kardim ro baramoon beshmore va tedadesh ro bargardoone
#chetor in karo bokonim ? tooye daraje aval lazeme ke models marboot be app blog ke post ha daroonesh hastand ro import konam
# chejoori ? from blog.models import Post  

#inam az code sh:


# @register.simple_tag(name='totalposts')
# def function():
#     posts = Post.objects.filter(status=1).count()
#     return posts

#masala gaha mikhaym tedad post haye nashe peyda karde ro dashte bashim ke in ye raheshe

#hala be farz agar bekhaym post haro az haminja peyda konim chetor ?  

