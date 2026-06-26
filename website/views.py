from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
# Create your views here.

#hamoon vaseti hast ke daroon sh function misakhtim va hamoon chizie ke url mano be etelaati ke,
#karbar dare darkhast mide motasel mikone. ghabla in file ro be soorat jodagoone sakhtim.

#url hayi ke ghabla dashtim tooye ye file jodaye views mikhaym biarimesh tooye in file ke 
#tooye app mast
#yadet nare package hasho import koni.
#hala mitoonim oon file views ghabli ke tooye proje mysite sakhte boodim ro pakesh konim.

def index_view(request):
    return render(request , "index.html")

def contact_view(request):
    return render(request , "website-pages/contact.html")

def about_view(request):
    return render(request , "website-pages/about.html")

def json_test(request):
    return JsonResponse({"name" : "samim"})

def http_test(request):
    return HttpResponse("this is test for http-response")


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
