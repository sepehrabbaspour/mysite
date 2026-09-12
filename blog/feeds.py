from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "Blog newest posts" #title sh
    link = "/rss/feed" #tooye blog hastim pas niazi nist khode blog ro benevisim 
    description = "best blog ever" #har chizi 

    def items(self):
        return Post.objects.filter(status=1) #item ha dare az class post tamin mishe ke status oona barabar 1 hast ke 
    #oonayi hast ke nashr dadim
    

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]
    #ma discription nemikhaym content mikhaym

#ina ro az link https://docs.djangoproject.com/en/6.1/ref/contrib/syndication/ avordim ba kami taghirat.

#hala cheto namayesh badam ino ? kafie berim tooye jayi ke mikhaym rss haro darj konim , url sh ro bezarim oonja 

#yani alan mikhaym tooye blog darj beshe dige , pas mirim tooye app blog , urls hash va package haye mored niaz ro import mikonim 
#va url sh ro ham hamoonja mizarimesh , inaro bazam az hamoon link bala miarim

#alan feed hayi ke dare generate mishe kole matn man ro dare miare chikar mishe kard ? content ro be in soorat taghir midim
#item.content[:100] , migim faghat 100 ta kalamasho bardar biar