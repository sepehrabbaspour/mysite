from django.shortcuts import render
from django.http import HttpResponse , JsonResponse , HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm , ContactForm , NewsLetterForm
from django.contrib import messages #in mal zamanie ke 
#yanio aval models ro misazim , tooye form import sh mikonim , ba forms.modelsform form sh ro misazim. baad form ro tooye views import mikonim
from django.contrib import messages #in mal zamanie ke karbar ma masala behemoon ticket zade , doroste ke ma daryaft mikonim alan ticket
#ro , vali ticket che dorost bashe che eshtebah , ba barname ma karbar barmigarde tooye safhe asli , va hich peyghami nadarim mabni bar inke
#ticket to masala daryaft shod , ba freamwork message mishe in karo kard. 
# Create your views here.

#hamoon vaseti hast ke daroon sh function misakhtim va hamoon chizie ke url mano be etelaati ke,
#karbar dare darkhast mide motasel mikone. ghabla in file ro be soorat jodagoone sakhtim.

#url hayi ke ghabla dashtim tooye ye file jodaye views mikhaym biarimesh tooye in file ke 
#tooye app mast
#yadet nare package hasho import koni.
#hala mitoonim oon file views ghabli ke tooye proje mysite sakhte boodim ro pakesh konim.

def index_view(request):
    return render(request , "website/index.html")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST) #yani karbar data ye voroodi sho mifreste az tarigh form , chon tooye model hamoon darim field hasho
        #pas miam va az hamoon form ie ke ba model kar mikone estefade mikonam , dar vaghe ba request.POST voroodi haro migirim
        if form.is_valid():
            form.save()
            messages.add_message(request , messages.SUCCESS , 'your ticket submited successfully')
            #injoori bayad ba message hga kar konim ke : mikhaym ye message az noe add message dashte bashim ke betoonim 
            #ye message ezafe konim , in message be request karbar man motesel mishe va dige lazem nist baresh gardoonam
            #noe message SUCCESS bashe , va matnsh ham har chizi mitoone bashe 
        else:
            messages.add_message(request , messages.ERROR , 'Your ticket didnt submited')
            #dar gheyr in soorat agar if anjam nashod va form save nashod ya har moshkeli pish oomad , 
            #eyn hamoon balayi vali tip sh az noe error bashe , matn sh ham ke har chizi mitoone bashe.
            #amma in alan kar nemikone , chon tooye template nagoftim jaye neshoon dadan in message koja bashe.
    form = ContactForm() #dige dade hasho nemikham , faghat mikhaym ino tooye safhe bargardoonim , indent haro deghat kon
    return render(request , "website/contact.html" , {'form':form})

def about_view(request):
    return render(request , "website/about.html")

def json_test(request):
    return JsonResponse({"name" : "samim"})

def http_test(request):
    return HttpResponse("this is test for http-response")

def newsletter_view(request): #in baraye bakhsh newsletter ha , agar request karbar man az noe post bood , mikhaym bast sh bedim be ye formi
    #form ro misazim 
    if request.method == 'POST':
        form = NewsLetterForm(request.POST) #hala inja oon form ie ke import kardim ro mirizim tooye object form 
        #va ba request.POST etelaati ke karbar ferestade ro daryaft mikonim 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/') #ba in kar mirim (redirect mishim) be safhe asli 
    else: #agar dakhat karbar get bood , ya be har dalili anjam nashod if ma
        return HttpResponseRedirect('/') #bazam redirect sho tooye safhe asli.
        #dar har soorat mikham bargarde tooye safhe asli.
        #faghat yadet bashe ke HttpResponseRedirect oon bala tooye from django.http import konim

context = {'name' : 'sepehr' , 'lastname' : 'abbaspour'}

def test_view(request):
    if request.method == 'POST':
        #form = NameForm(request.POST)
        form = ContactForm(request.POST) #be ezaye Contact form ham mikhaym dade haye voroodi ro daryaft konam
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # subject = form.cleaned_data['subject']
            # message = form.cleaned_data['message']
            # print(name , email , subject , message)
            form.save()
            return HttpResponse('done') 
        else:
            return HttpResponse ('not valid')
        #inja migim ye form darim ke esmesh name form hast
        #hala etelaat requesti karbaram ro mikham beriazam tooye in form ke sakhtim objectesh ro hamin alan
        #yani masala name har chizi ke hastesh ro mikhad ba in form barabar bezare ke mishe in khat form = NameForm(request.POST)
        #va chio barresi kone ? bebine az tooye formi ke dare miad etelaatesh ba shakhes hayi ke vase ma tarif shode tooye fom ma barabari 
        #dare ya na! masala ma darim ye type khasi mifrestim ke text nist vali oontaraf goftam ke hatma bayad text bashe.
        #masala injoori man tooye field name daram email mifresdtam , khob in mire oonja barresi mishe ke aya man daram etelaat dorosti
        #mifrestam ya na ke tooye in khate : if form.is_valid()
        #ba http response ham tooye ye safhe dige baresh migardoonam. yani in done ro tooye hamoon safhe behemon barmigardoone
        #hala deghat kon age man biam va oon shakhes name ro be soorat dasti name sh ro avaz konam ke tooye test.hrml app website
        #daram in karo mikonam in dige kar nemikone. post mishe vali dade rad mishe
        #pas dade hayi ke mifrestim bayad ba field haye form moon ke tarif kardim barabari bokone ta anjam beshe gheyr az in anjam nemishe
        #<input name="sname" type="text"> masala inja darim ke name barabar sname hast va inja chon yeki nistan anjam nemishe

        
        #in ravesh estandardesh hast
        # name = request.POST.get('name') #baraye daryaft eleman ha az method post
        # email = request.POST.get('email')
        # subject = request.POST.get('subject')
        # message = request.POST.get('message')
        # #baraye inke betoonan daryaft beshan bayad chizi ke dare get mishe ba name input yeki bashe
        # #in name az koja oomade ? tooye app website , test.html baraye input ye attribute name tarif kardm , in hamoone
        # c = Contact() #c contactor man hast , lazeme ke az tooye webste.models Contact ro import konim 
        # c.name = name #injoori behesh attribute midadim , name sh barabar name ie hast ke man daram migiram va midam , 
        # #yani hamin name ie ke balatar dadim behesh , baraye baghie ham be hamin soorat
        # c.email = email
        # c.subject = subject
        # c.message = message
        # c.save() #dar nahayat object c sakhte shode ro save kontooye data base. method haye dige mesl delete , ... darim ke tooye ducmetion bekhoon
        #print(name) #email , subject , message

    #form = NameForm()
    form = ContactForm() #bejaye nameform , contact form hast ke barmigardoonim
    return render(request , "website/test.html" , {'form':form}) #context ro hazf kardim alan


#hala bebinim chetor mishe be jaye inke khodemoon hey matn bedim be http response , 
#biaim va az safahat araste shode estefade konim be jaye http response

#tooye sakhtar django tarif shode ke agar app ie dashte bashid tooye setting , ghesmat template sh 
#tarif shode.

#dar vaghe agar applicationi dashte bashim ke lazem bashe be template ha rojoo kone va safahat 
#web ro az toosh biare va namayesh bede , yeki az rahkar hash ine ke be directory app ie ke vojood
#dare negah mikone . masala agar directory app man ye pooshe ie be esm masala templates toosh bashe ,
#oon ro be onvan folder pish farz dar nazar migire ke toosh donbal file hayi ke darim ijad mikonim,
#begarde. pas tooye app website ye pooshe misazim , too halat pish farz dakhel app donbal oon pooshe
#migarde , vali rah dare ino ke ye folder kamel dar nazar begire ke tamamn app hamoon 
#bian va faghat be in folder rojoo konand ke rajeb shoon sohbat mishe.
#hala tooye pooshe ie ke sakhtim ye file html be nam index misazim ke ye seri eleman bezarim toosh

#berim tooye file html

#khob hala mikhaym in eleman hayi ke tooye file html neveshtim ro bebinim tooye web server django
#amma koja va chetor sedash bezanam ? 

#deghat kon ke url taghir nemikone. in views ha hastand ke bayad taghir konand.
#dar vaghe bar asas karkard djago in view hast ke mikhad be template he eshare kone 
#va kari ba url nadarim
#pas amala view bayad template haro call kone va namayesh shoon bede.

#hala ba dastoori be nam render in karo anjam midim ke az django.shortcuts miad yani be in soorat
#from django.shortcuts import render

#vaghti app ro misazim render oon bala hast , nabood ham ya hefz ya search
#hala yeki az function haro ba render jaygozin mikonim 

#khob vaghti render() ro jeloye return neveshtim , argument avalesh request hast ke karbar
#mikhaym ye seri chizaro bargardoonim . hala tooye argument dovomesh migim chia mikham bargardoonam ? 
#be onvan argument dovom safhe html tooye template (index.html) ro behesh pas midam.
#yani be in soorat : return render(request , "index.html")

#hala ye soal : chejoori mifahme file index.html ma tooye pooshe template hast ? 
#khob barash tarif shode. yani zamani ke man behesh migam ke bro index.html ro peida kon
#mire tooye app directory man , donbal templates migarde , va baad dakhel template donbal 
#index.html migarde. va alan dare kar mikone kheili rahat.

#hala mitoonim chandin safhe besazim va ba render bareshoon gardoonim. tooye hamoon pooshe
#template misazimesh baghie file haye html ro

#amma ye nokte : momkene render ye seri arguman dige ham dashte bashe ke baada behesh miresim.

#nokte baadi inke agar ma dakhel pooshe template ye pooshe dige dashte bashim be nam masala website
#etefaghi ke miofte ine ke dige render nemitoone tooye pooshe template ke barash tarif shode az ghabl
#file haye mano peyda kone ok? pas bayad be render addres file moon ro bedim hatma. be in soorat ke : 

#return render(request , "website-pages/about.html")

#alan ma ye pooshe dige tooye templates sakhtim va about va contact ro bordim too oon pooshe.
#index ro serfa baraye fahm bishtar nabordam tooye poosh ke mostaghima render konim file
#index.html ro va niaz be addres pooshe dadan nadashte bashe.

#agar file ha dakhel file templates bashand ya tooye ye pooshe dige tooye pooshe templates , 
#dar har do soorat be hich onvan niazi nist ke moghe addres dehi esm pooshe templates ro biarim.
#khodesh mifahme :)

#dar gheir in soorat error darim

#nokte baadi : agar darim file jadidi tooye proje misazim server django ro hatma stop,
#va dobare start konim. chera ke momkene sakhtar django natoone oon file jadid ro tashkhis bede.

#hala dede haro chetor daryaft konam ? inja baad az in ke dade ha dorost daryaft shod mitoonim dade haro clean shode 
#az form tahvil begirm be in soorat ke balaye if minevisim: name = form.cleaned_data['name']
#migim az tooye form ie ke dare miad oon bakhsh marboot be name ro clean data kon , deghat ke hatma bayad tooye braket bashe 
#va oon bakhshi ham ke mikhaym clean data konim tooye '' bayad bashe. pas name ma barabar form.cleaned_data['name'] mishe.
#baraye tamamesh in karo mitoonim anjam bedim.

#khob hala ma chetor mitoonim oon class ContactForm ie ke tooye forms.py dashtim ro biarim tooye view va tooye safhe namayesh bedim ? 
#aval az hame oon bala ContactForm ro az tooye forms.py import mikonim yani from website.forms import NameForm , ContactForm
#amma eleman haye ma fargh khasi nemikone chera ? braye in ke eleman haye ma ba eleman haye ghabli yeki hastan va faghat ravand kar avaz shode 
#alan ma darim name , email , message va subject ro bar asas chizi ke tooye model esm gozari shode mibinim.
#dar vaghe vaghti darim az forms.form estefade mikonim mesl in mimone ke form ma modelasion ie nadare ke bekhad behesh vasl bashe va 
#azash estefade bokone , vali tooye forms.Modelform bayad model ma be oon form vasl bashe ta kar kone , gheyr az in bashe kar nemikone.

#dar vaghe mige agar model formi darim ke gharare be onvan voroodi baramoon biad va etelaat karbar ro mikhay az toosh daryaft koni
#kheli rahat mitoonim begim form.save() tamam :)
#dalilesh ham ine ke form ma be model ma motasel hast tooye in ravesh.\ , vaghti migim form ro save kon yani boro tooye model man 
#savesh kon
#vali tooye halat forms.form , form ma ba model vasl nabood ke bayad ye object az model misakhtim va baad doone doone attribute haro 
#migerftim va save mikardim , kari ke balatar anjam dadim. amma dar in halat mostaghima in kar anjam mishe.
#yani be jaye in hame kar ke goftim clean data kon , .... , be hich kodoomniazi nist , kheli rahat migim form.save()
#yani migim boro tooye data base ino save sh kon

