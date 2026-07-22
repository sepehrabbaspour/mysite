from django.contrib import admin
from blog.models import Post #esm classi ke tooye models blog sakhtim 

# Register your models here.

@admin.register(Post) #az daroon admin , register va be onvan arg voroodi esm modeli ke sakhte boodim ro behesh pas midim
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    #fields = ('title',) #deghat kon ke in ye tuple hast va az ghavanin tuple peyravi mikone
    # yani daroon () bashe , agar tedad eleman ha zaid boodan ba (,) az ham joda shoon mikonim 
    # va agar tak eleman bood mesl inja , oon eleman ro minevisim va ye (,) baadesh mizarim. daghigha mesl inja
    list_display = ('title' , 'counted_views' , 'status' , 'published_date' , 'created_date')
    list_filter = ('status',) #deghat kon age yedoone ham bood be soorat tuple midim 
    #ordering = ['-created_date'] #deghat kon be soorat liste !!
    search_fields = ['title' , 'content'] #deghat kon be soorat liste !!

#admin.site.register(Post , PostAdmin) #ba in ravesh rejister mikonim class moon (model moon) ro ke tooye panel admin betoonim model moon ro bebinim


#migim bia va ye seri moshakhase be registration ie ke alan dari ezafe kon , az ye class vaset estefade mikonam va oon class ro be
#onavan ye arguman pas midam

#estandard khsi baraye esm gozari vojood nadare vali mishe injoori begim ke (dar inja) kodoom model ro mikham barash shakhes taien konam?
#Post ro . che amaliati mikhaym anjam bedim ? admin ro mikhaym taghir bedim pas darim class PostAdmin().
#az koja bayad ers bari kone? az tooye admin.ModelAdmin. hala in az koja miad in ? tooye documention django ino gofte :)

#hala chejoori behesh begam eleman hayio ke mikham tooye PostAdmin benevisam ro bast bedam va tooye model biari va neshoon bedi? 
#behesh migim gharare in class ro be onvan voroodi amalkard baraye modelet dar nazar begiri yani : admin.site.register(Post , PostAdmin)

#hala bejaye in ravesh mishe az decorator (@) ha ham estefade kard. dar vaghe bejaye admin.site.register(Post , PostAdmin),
#mitoonim az decorator ha estefade konim 

#nokte : ma ghabl az har class ya fanction ie bakhaym az decorator estefade konim va bakhaym begim dar bar begir class ya function ie ke
#daram ziret migam ro bayad begim @esm decorator ke momkene az dakhel ye class ya ye function dige bashe 

#amma dar nahayat farghi nadare az che raveshi berim jelo, har kodoom rahat tarim 


#ye chizi ke mishe estefade kard date_hierarchy hast ke be che dardi mikhore ? bar asas zaman hayi ke post haye man montasher shode 
#bekhaym ye dastresi filteri zamani dashte bashe.

#hala eleman voroodi ash bayad az noe time bashe dige. time haro ro koja darimeshoon ? tooye models.py attribute haye published_date,
#created_date va updated_date. hala kodoom baramoon moheme ? published_date , created_date. vali inja mikhaym az 
#created date estefade bokonim ke ino bayad be soorat string pas bedim be date_hierarchy yani : date_hierarchy = 'created_date'

#hala age safhe admin ro baz konim mibin ke ye eleman baramoon ezafe shode ke be man ejaze mide ke tamam object hayi ke 
#ijad kardam ro bar asas time ijad shodanesh be soorat daste bandi dashte bashamesh.
#ina dar asl hamoon query hayi hastand ke tooye data base mizanim montaha ba in fargh ke ina baraye man az pish taein shodan 
#va ba ye attribute koochik mesl date_hierarchy mitoonim azash estefade konim 

# empty_value_display = '-empty-' : inja migim eleman hayi ke meghdar voroodi haye oona hanooz hichi hast (mesl oonayi ke null hastand)
# be jaye inke khali neshoonesh bedi value display sho barabar empty bezar.
#deghat kon ke age empty_value_display ro nadshe bashim , oonjahayi ke khali bashe ro - mide va dige empty neminevise ke behesh miresim.

#fields : marboot be eleman hayi mishe ke ma tooye bakhsh marboot be har kodoom az object hamoon mitoonim behesh dastresi dashte bashim 
#va emkan edit dashte bashim. hala agar biaim va field hayi ro taien konim tooye attribute fields , tooye safhe marboot be
#dastkari har field mitoonam faghat oon field haye moshakhas shode am ro bebinam 
#masala age begim fields = ('title',) faghat mitoonim title ro tooye safhe marboot be har field bebinim.
#alan niazesh nadarim vali baada niaz mishe

#list_display = nokte aval fields ba list display motafavete : fields marboot be safhe ie hast ke eleman ha mesl title va ststus va ina 
#toosh hast, dar vaghe vaghti click mikonim rooye ye field va in tanzimat baramoon baz mishe 
#amma list display jayie ke dar vaghe esm jadval man va title hash daran namayesh dade misham.
#ye nokte : title ha va id shoon ro ham goftim chetor neshoon bedim ke albate bayad tooye file models.py app neveshte beshe va injoorie:
#def __str__(self): #
    #return "{} - {}".format(self.title , self.id)
#hala bebinim che emkani be ma mide : ma tooye safhe ie ke table ha va jadavel namayesh dade mishan , ma faghat darim
#field marboot be tag object ro mibinim. mikhaym hamin ja tooye hamin safhe bebinim ke kodoom ha masala montasher shodan
#kodooma che tarikhi dashtan , chand ta view khordan va kheili chizaye dige. be jaye inke tak tak bazeshoon konim ,
#hame ro tooye ye table (chart) bebinam. 
#hala be in soorat amal mikonim ke list_display = ('title' , 'counted_views' , 'status' , 'published_date' , 'created_date')
#har chizi sho ke niaz dashte bashim va tooye in attribute benevisim tooye safhe ie field haye table moon ro mibinim, be ma namayesh mide va dige lazem nist 
#har kodoom ro tak tak baz konim. mohem hasho list mikonim. vali oonyi ke matn toolani dare mesl content ro neminevisim.

#filter : mitoonim bar asas object ha va eleman hayi ke mikham filter konam , masla : kodoom post ha nashr peida kardan va kodoom ha nashr peida nakardan ? 
#migim eleman hayi ke mikhay bar asasesh filtering anjam bedi chiast ? masala mikhaym bar asas status anjam bedim filter ro
#ke be in soorate : list_filter = ('status',)
#hala baraye man ye side bar ezafe mikone ke bahamoon mige ke kodoomha nashr peida kardan va kodoom ha nashr peida nakardan.

#ordering : migim in field hayi ke dari be man tooye safhe neshoon midi , mikham by defult baram bar asas ye chizi orderesh koni 
#ke be in soorate : ordering = ['created_date']
#inja masala goftim bia va bar asas tarikh sakhte shodan field ha , baram moratebesh kon ke bar asas ghadimi tarin ta jadid tarin
#hastesh va dar vaghe ghadimi tarin bala va jadid tarin paieen list field haye mast.
#amma agar bekhaym jadid tarin haro bebiraim bala va az jadid be ghadimi moratabesh konim bayad ye (-) posht created_date bezarim yani :
#ordering = ['-created_date']. in kar list field hamoon ro az jadid be ghadimi neshoon mide. jaygasht ha avaz mishe.

#search_fields : momkene bekhaym dakhel eleman hayi ke ijad kardim search anjam bedim hala bar asas chi search kone ? injoori migim ke:
#search_fields = ['title' , 'content'] migim bia va bar asas title va content tooye eleman hamoon search anjam bede
#yani masala ba in sharayeti ke tarif kardim search bokonim post natayeji ke miare momke tooye title sh kalame post dashte bashe
#va ya momkene tooye contect sh kalame post vojood dashte bashe 
#hala ye search field ham baramoon ezafe mishe.

#ina kheli tedadesh zaide vali ina bishtarin chizayi bood ke niaze. ke mishe shakhsi sazi ham kard ke tooye proje haye vaghei
#behesh miresim

