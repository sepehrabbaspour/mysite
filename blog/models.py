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
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True) #ino chon khodemoon gharare tarif konim va bana nist az jayi biad khali mizarim
    created_date = models.DateTimeField(auto_now_add=True) #auto_now_add=True
    #in yanoi zaman sakhte shodan field, hamin alan bokhore zaman sakhte shodanesh
    updated_date = models.DateTimeField(auto_now=True) #in yani zamani ke field dare update mishe zamansh barabar ba hamoon zamani 
    #ke dare update mishe

#tooye char field hatma bayad benevisim ke chand karacter mikhaynm vared konim hadaksar. estandard khasi ham nadare.

#deghat kon agar bana shod joori kar konim ke bada maghadir ro ezafe konim mesl alan , 
#maghadir hatma bayad barash meghdar null ya defult barash taien konim mesl alan

#amma age avalin bar hast ke darim makemigratin anjam midim hich iradi nakhahad gereft