#in file baraye sakhtan form ha hast 
#mesl sakhtan model ha bayad az class madar sh estefade konim ta behesh befahmoonim ke in ye forme
from django import forms
from website.models import Contact , NewsLetter #baraye sakhtan form ba forms.Modelform baraye har kodoom aval model ro misazim va 
#baad az oon inja tooye forms.py import sh mikonim 
class NameForm(forms.Form):  
    name = forms.CharField(max_length=255)#inam mesl hamoon kar ghbli ke goftim name input ha bayad yeki bashe ke tooye file test.html goftim
    #yani name ro harchi inja tarif konim mire mishine tooye jaye name input tooye file html
    #tooye models ha migoftim models.CharField , inja migim forms.CharField , max_lenght ham hamoon 255
    #baghie ham be hamin soorat
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea) #khob ma tooye form ha textfield nadarim. 
    #bekhaym az CharField estefade konim khob kheyli koochike jaye matnsh. pas bayad biaim va halat (widget) neveshtaresh ro avaz konim
    #yani begim forms.CharField(widget=forms.Textarea). be halat text aria daresh biarim char field ro.

    #inja az tooye forms be class madaresh rojoo mikonim eyn models ha , 
    #hala ye seri attribute behesh ezafe mikonim ke filed haye form mast



#hala berim form ro mabni bar models besazim , models marboot app website.


class ContactForm(forms.ModelForm):
   # lastname = forms.CharField(max_length=255) 
    class Meta:
        model = Contact #deghat kon ke parantez nemikhad
        fields = '__all__' #in hame field haro behemoon mide
        #fields = ['name' , 'email'] #inja mitoonim begim kodoom filed hari mikhaym , syntax sh be in soorate

        #albate in kar nemikone chera ke faghat darim in dota ro mifrestim.
        #mishe ye tadadi az field haro none , blank dar nazar gereft ke meghdar azamoon nakhad va masala ye ghesmat sho mesl 
        #hamin kari ke kardim , alan por konam va baghie sho time dige , in dast mast 

        #hata mishe exclude kard , yani begim hame field haro biar be joz masala filed name be in soorat :
        #exclude = ['name'] #dota eleman ham mishe behesh pas dad.

#esm ro be in soorat mizarim ke aval esm classi ke tooye models tarif kardim va badesh kalame form.
#vaghti mikhaym az ye mode ie ya ye chizi estefade konam bayad meghdar hayei ke lazem darim ro tooye safhe import konim.
#inja contact ro be in soorat import kardim from website.models import Contact.
#hala bayad model form haro ham biarim chon bayad az oon tabaieat konam be in soorat : from django.forms import ModelForm
#sar in soorat bayad class ma az ModelForm ers bari kone yani be in soorat class ContactForm(ModelForm):
#ya in ke mitoonim be in soorat tooye class azash ers bari konim class ContactForm(forms.ModelForm).
#class meta ke ghabla kar kardim tooye inja baraye ma taien mikone ke tooye classi ke ijad kardam ke gharare az koja nashat begirim va 
#che khosoosiat hayi gharare dashte bashan. masala inja tooye class meta migim gharare in form ma bar asas model marboot be Contact anjam beshe
#yani be in soorat : model = Contact()
#hala mitoonim tooye class meta behesh begim che field hayi gharare dashte bashe form ma ? yeki az rah ha ine ke biaim injoori begim
#field hayi ke gharare to dashte bashi hame oon chizi hast ke tooye model darim gharare field hash bashan 
#hala chejoori biarim tooye view va pasesh bedim tooye safhe ? 
#berim tooye view

#hala kheli rahat mishe form ro update kard , yani be in soorat ke tooye class ContactForm migim lastname = forms.CharField(max_length=255)
#kheyli rahat zir tamam eleman hamoon in ezafe mishe. hanooz ham mitoonim field haye dige ham ezafe konim. ke albate niazesh nadarim
#comment sh mikonam

class NewsLetterForm(forms.ModelForm): #inam form newsletter
    class Meta:
        model = NewsLetter #az model NewsLetter ke bala import sh kardim
        fields = '__all__' #tamam field hasho biar.