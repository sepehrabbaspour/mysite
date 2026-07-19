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



