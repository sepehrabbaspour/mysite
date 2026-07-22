from django.contrib import admin
from website.models import Contact
# Register your models here.

#in file vase taghirat va dadan sakhtar ha be admin man gharare bashe ke orm admin hast
# ke rajebesh sohbat mishe.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin): 
    date_hierarchy = 'created_date'
    list_display = ('name' , 'email' , 'created_date')
    list_filter = ('email',)
    search_fields = ('name' , 'message')

#admin.site.register(Contact , ContactAdmin) #register dar safhe admin
#or (in ba decorator hich farghi nadare)