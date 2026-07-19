from django.contrib import admin
from blog.models import Post #esm classi ke tooye models blog sakhtim 

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post , PostAdmin) #ba in ravesh rejister mikonim class moon (model moon) ro ke tooye panel admin betoonim model moon ro bebinim


#migim bia va ye seri moshakhase be registration ie ke alan dari ezafe kon , az ye class vaset estefade mikonam va oon class ro be
#onavan ye arguman pas midam

#estandard khsi baraye esm gozari vojood nadare vali mishe injoori begim ke (dar inja) kodoom model ro mikham barash shakhes taien konam?
#Post ro . che amaliati mikhaym anjam bedim ? admin ro mikhaym taghir bedim pas darim class PostAdmin().
#az koja bayad ers bari kone? az tooye admin.ModelAdmin. hala in az koja miad in ? tooye documention django ino gofte :)

#hala chejoori behesh begam eleman hayio ke
