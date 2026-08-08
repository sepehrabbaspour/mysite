from django import template
from blog.models import Post #baraye post ha
from blog.models import Category #baraye category ha

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

#khob ye model az filter haro didim ke hamoon truncatechars:100 bood ke ba function snippet sakhtimesh

@register.filter #in bar register ma az noe filter hast
def snippet(value , arg=20):
    return value[:arg] + '...'

#inja migim #rigister.filter yani chi ? 
#tooye ijad kardan function ha hich tafavoti vojood nadare
#dar vaghe ye function darim be esm snippet ke ye voroodi dare be nam value
#dar edame ham migim in value ro 100 kalame avalesh ro baram joda kon yani return value[:20]
#registeri ke in bar mikhaym anjam bedim az noe filter hast 
#hala ino chetor mishe test kard ? 
#post ie ke tooye for dovom test.html daram ro be onvan voroodi behet midam montaha filter ha be in soorat nistand
#ke be soorat arguman behesh pas bedim.
#vaghti ye filteri ro anjam midim saze ash be in sootare ke post|snippet
#dar vaghe elemani ke mikahym pas bedim gharare yeki az voroodi ha bashe , hamooni ke ghabl az | gharar migire
#hala gharare che amaliati roosh anjam beshe ? snippet dige. dar vaghe hamchin halati khahim dasht {{post|snippet}}
#amma dar in soorat error darim chon khode post ro nemitoonim roosh snippet bezarim. gharar bood ba content in karo bokonim.
#pas darim {{post.content|snippet}} dar in soorat kar khahad kard. 
#hala agar bekhaym tedad kalamt ro be soorat defult dashte bashe yani tooye voroodi haye function migim :
#def snippet(value , arg=20) injoori dige har jayi tooye function esmi az arg biarim hamoon tedad 20 ta mishine sar jash
#yani injoori return value[:arg] be jaye arg meghdar 20 mishine magar injoori beginm ke [:100] injoori 100 mishine jash
#amma inja ma arg tarif kardim ke ino taghir nadim dige , mitoonim tooye safhe be soorat dasti voroodi bedim masla :
#{{post.content|snippet:50}} inja 50 dar nazar gerefte mishe bejaye arg ke 20 tarif karde boodim. dar vaghe bejaye 20 kalame aval 
#50 kalame aval namayesh dade mishe
# in '...' akharesh ham migim baraye inke neshoon bedim in matn edame dare
#dar vaghe amalkard marboot be truncat ro khodemoon sakhtim.



#inclusion tag: inclusion tag be ma in tavanayi ro mide ke betoonim dar hengami ke darim ye meghdari ro barmigardoonim
#az tarigh ye safhe in karo anjam bedim yani chi ? yani man ye safhe asli daram ke tooye oon safhe function man dare anjam mishe
#hala ma ba include kar karde boodim dige yani ye safhe dige bood ke ejaze midad too oon safhe ie ke man include sh mikardam
#ezafe beshe mohtavaitsh. hala inclusion tag hami karop anjam mide ba in fargh ke ye function sakhtari hastesh ke miad va ye seri
#amaliat ro anjam mide , amaliat anjam dade shode ro mirizie daroon safhe va
#ye chizi taghriba shabih kar ba view va render kardan template bood tooye safahat
#ye makhlooti az inast ke be ma tavanayi mide ke tasir bishtari tooye safahat dashte basham.

#dar vaghe kari ke mikhaym anjam bedim ine ke chizayi ke darim tooye test.html tooye safhe barmigardoonim
#biaim va az ye safhe dige in etelat ro biarim. oon ye safhe dige popularposts hastesh ke tooye pooshe template misazimesh

#hala baraye in kar mesl hamishe ye function minevisim : 

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}
    #order_by mige moratab kon bar asas har chizi , masala alan inja published_date gozashtim ke begim kodoom post ha jadid tar oomadan
    #khob hala dige baraye return kardan nemigim posts ro return kon , mikhaym begim too oon safhe return sh kon
    #ma tooye safahat key value ie eleman midadim doroste ? 
    #decoratoresh be in soorat mishe @register.inclusion_tag (az tag inclusion tag estefade mikonim)
    #yeki az arguman hayi ke tooye inclusion tag bayad bedim oon safhe ie hast ke mikhaym eleman haro be oonja pas bedim.
    #hala addres oon safhe (popularposts) chie ? tooye pooshe template ye file darim be nam popularposts.html dige.
    #mesl hamishe niaz nist khode template ro benevisim faghat migim : 'popularposts.html'
    #dar nahayat tag inclision ma be in soorat dar miad @register.inclusion_tag('popularposts.html')
    #hala baraye return kardanesh bayad be soorat key value ie baresh gardoonim , chon tooye safaht ham ke mikhastim bargardoonim 
    #etelaat rop goftim be soorat key value ie amal mikardim.va hamchenin agar faghat begim return posts
    #tooye file popularposts.html mikhaym ye object ie ro bargardoonim nemishe azash estefade kard 
    #pas bayad be soorat key value ie baresh gardoonim yani return {'posts' : posts}
    #dar vaghe migim ye kilid darim be nam posts ke eleman haye marboot be posts man darooneshe
    #ye seri tozihat daroon popularposts.html vojood dare.
    #be onvan ghadam akhar bayad call sh konam chetori ? 
    #be in soorat ke tooye file test.html minevisim {% esm function %} ke dar inja popularpots hast yani be ebarati darim
    #{% popularposts %}
    #hala kheyli kar haye dige ham mishe kard masala mitoonim 1 post akhar ro ba list slice begirim yani:
    #posts = Post.objects.filter(status=1).order_by('published_date')[:1]
    #ye chizi agar tooye order_by ke goftim bar asas published dateinaro namayesh bede , 
    #in bar asas jadid tarin post ha az lahaz tarikh oona ro moratab mikone
    #agar biaim va ye (-) bezarim poshtesh yani : order_by('-published_date')
    #in amalkard baraks khahad shod yani az post haye ghadimi be jadid namayesh dade mishan.
    #hala mishe safahat moteaded ezafe kard va kar haye bishtari niz anjam dad ba hamin seta register mitoonim dashte bashim.

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all() 
    cat_dict = {}
    #categories : inam mesl post , migim har chi object tooye category darim bardar biar tamam category hamo
    #hala kari ke mikhaym bokonim ine ke chetor behesh begim tamam post hayi ke daram tedad category hayi ke marboot 
    #be oon post hastesh ro shomaresh konam va dar kenar esm sh bezar 
    #tedad post haro ba count() dar miavordim amma in be dard kar ma nemikhore.
    #pas bayad in karo bokonim : behesh begim boro be ezaye name hayi ke tooye categories hastand check kon bebin kodoom post ha
    #shamel in mishe ba for 
    
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count() 
    return {'categories' : cat_dict}
        #migim boro tooye post ha filter kon bar asas oonayi ke category shoon barabar name category ie hastesh ke
        #man daram behesh midam , yani migam boro doone doone tamam post hamo negah kon bebin kodoom hashoon ba in category ie ke esmesho
        #daram tak tak behet midam yekie 
        #hala ye masale ie : inaro man chetor zakhie konam va bargardoonam ? mishe ba dictionary ino halesh kard.
        #daghigha zir variable categories daram minevisamesh. ye dicionary khali misazam va miam behesh eleman ezafe mikonam
        #eleman ha banast chi bashe ? key ash barabar esm oon category hast , va value barabar tedad post hayi ke marboot be oon category hastesh
        #hala migim chi ? cat_dict[name] = posts.filter(category=name).count()
        #yani dar vaghe darim migim ke tooye halghe for bia har bar be cat_dict ie ke balatar sakhtam , bar asas key ke esmet bood
        #chio ezafe kon ? post haro begard peyda kon bar asas oon chizi ke name sh moshabeh ine va ba count tedadesh ro shomaresh kon
        #ba in ravesh man mitoonam be oon dictionary ke daram misazam eleman hayi ke mortabet hasto vasl konam va berizam toosh
        #hala chetor baresh gardoonim ?
        #ye esm behesh midam masala categories va value sho barabar cat dict mizarim yani be in soorat : return {'categories' : cat_dict}
        

