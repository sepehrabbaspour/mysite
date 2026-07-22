from django.db import models

# Create your models here.

class Post(models.Model): #table esm class be onvan esm table dar nazar gerefte mishe 
    #image
    #author
    title = models.CharField(max_length=255) #feild #hamoon attribute ha be onvan field mahsoob mishan
    content = models.TextField() #field 
    #tag
    #category
    counted_views = models.IntegerField(default=0) #(default=0) migim meghdar avaliesh 0 bashe
    status = models.BooleanField(default=False) #yani meghdar avalie ash false bashe
    published_date = models.DateTimeField(null=True) #ino chon khodemoon gharare tarif konim va bana nist az jayi biad khali mizarim
    created_date = models.DateTimeField(auto_now_add=True) #auto_now_add=True
    #in yanoi zaman sakhte shodan field, hamin alan bokhore zaman sakhte shodanesh
    updated_date = models.DateTimeField(auto_now=True) #in yani zamani ke field dare update mishe zamansh barabar ba hamoon zamani 
    #ke dare update mishe

    class Meta:
        ordering = ['-created_date']
        # verbose_name = 'پست'
        # verbose_name_plural = 'پست ها'
        

#tooye char field hatma bayad benevisim ke chand karacter mikhaynm vared konim hadaksar. estandard khasi ham nadare.

#deghat kon agar bana shod joori kar konim ke bada maghadir ro ezafe konim mesl alan , 
#maghadir hatma bayad barash meghdar null ya defult barash taien konim mesl alan

#amma age avalin bar hast ke darim makemigratin anjam midim hich iradi nakhahad gereft

    def __str__(self): #
        return "{} - {}".format(self.title , self.id) #inja dar vaghe darim migim ye function ezafe mikonam ke ghavaed classam ro over write konam 
#inja object self ma dare az eleman haye marboot be modelasion miad doroste? 
#hala migim be jaye inke biai va object haro tooye modelasion neshoom bedi bia va title haro neshon bede yani : 
#return self.title. ba function __str__ ham ke migim bejaye object ha bia va title ha sho be man bargardoon.
#dar vaghe title har posti ie ke marboot be khodeshe. faghat deghat kon ke tooye class bayad bashe in function va dar asl ye method hast
#alan asami ke tooye orm mibinim asami object ha va id ha ke ghabl az in method midim nist va dare title hasho neshoon mide behemoon.
#hala masala man age biam bagem self.content , eleman content haro namayesh mide 
#hala agar bekhaym kenaresh shomare id haro ham namayesh bedim mitoonim az formated string estefade konim ke be in soorat haske ke:
#return "{} - {}".format(self.title , self.id). migim ham title haro behem namayesh bede va ham id haro  



#class meta : koja tarif mishe ? bayad jayi ke class ma baraye modelmoon tarif shode , daroonesh ye classi tarif koni be esm meta
#hala tamam attribute haye dige ie ke darim dakhel meta gharar migirand.
# ye seri eleman haro hatma lazem nist az tarigh admin anjam bedim. vaghti darim attribute hayi ke 
#marboot be namayesh tooye safhe admin hastand taghir midim , zamani ke mikhaym query bezanim va dade haro begirim oonja taghiri nakardan
# class meta be ma in dastresi ro mide ke bekhaym in filter va kheyli chizayi ke darim anjam midim ro biaim va be soorat generali
#rooye model moon dashte bashim
#pas in class behemoon ye dastresi belghove ie mide ke biaim va ye seri taghirat baraye tamam model dashte basham ke faghat 
#tooye zaman namayesh oona dashte basham.

#app_label : agar ma modeli ro darim ijad mikonim ke daroon ye app digast vali marboot be ye app digast az in meta estefade mikonim
#ke tamayoz beinesh ijad konim. masala do app darim ke ye class dakhel model aval darim ke mikhaym begim in class tavasot ye app 
#dige dare modiriat va kontrol mishe va marboot be in app nist ke ba estefade az app label mitoonim in karo anjam bedim.


#db_table : oon esm table ie ke darim vase mode moon ro mitoonim tagir bedim moghe namayesh va kheili kar haye dige
#ke jahayi ke mikhaym query bezanim ham in esm table mitoone motafavet bashe.

#ordering : yadete sakhtimesh tooye admin app blog?
# ke bar asas tarikh morab mikard field haro ? ma mitoonim ino be soorat general benevisimesh.
#dar vaghe oon ordering ke tooye admin neveshte boodim serfa tooye safhe admin behem namayesh midad, na zamani ke 
#query mikham bezanam va dade hamo mikham begiram. vali inja be soorat koli dare emal mishe.
#hata zamani ke darim data haro query mizanim va select mizanam ke daryaft konam az data base , in dare emal mishe.
#farghesh injoorie.
#alan in halat be soorat general hast va dige faghat marboot be admin nist :    
# class Meta:
    #ordering = ['-created_date'] ke khob injoori kheyli behtare.
#alan deghat kon ke ordering ro tooye admin.py comment sh kardim.
#order faghat bar asas zaman nist. masala mitoonim begim che zamani montasher shode va ki montasher karde ke be in soorate:

#verbose_name : tooye safhe admin oon bala hasta ke neveshte Select post to change , in kalame post ro mishe avazesh kard.
#be har chizi ke delemoon mikhad. be in soorat ke verbose_name = 'پست' hala in taghir tooye Blog adminastrator ham etefagh miofte
#va minevise پستs :)))) ino be in soorat mishe halesh kard ke : verbose_name_plural = 'پست ها'
#dar vaghe migam oonja hayi ke esm jam gharare bashe benevisim پست ها :))))
#hala chera az in estefade mikonim ? gahi niaz mishe ma asami ro bar asas zaban haye motafaveti avaz konim vali nemikhaym 
#asami marboot be modelasion ro taghir bedim. yani nemikham class poost ro biam ye chiz dige bezaram va taghir bedam
#vali mikham moghe namayesh az ye chiz dige estefade konam. inja in ravesh be kar miad.
#ke albate inja fela verbose_name , verbose_name_plural be karemoon nemiad va commentesh mikonam