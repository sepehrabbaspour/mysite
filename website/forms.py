#in file baraye sakhtan form ha hast 
#mesl sakhtan model ha bayad az class madar sh estefade konim ta behesh befahmoonim ke in ye forme
from django import forms

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
