from django.shortcuts import render , get_object_or_404
from blog.models import Post #table post ro inja import mikonim
#from django.shortcuts import get_object_or_404 : in chizi ke import kardim mikhaym kari konim ke vaghti ke safhe ie peida nemishe 
#be jaye error , khataye 404 begirim :) vali khob niazi be tarif dobarash nist va chon django.shortcuts ro bala darim 
#faghat get_object_or_404 ro import mikonim 
#hala query variable post paien ro berim be shekli benevisim ke aval biad barresi kone , age vojood dasht namayesh bede , 
#agar vojood nadasht , be jaye error , 404 behemoon bargardoone


def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request , 'blog/blog-home.html' , context)

def blog_single(request):
    context = {'title' : 'bitcoin crashed again!' , 'content' : 'bitcoin was flying but now grounded as always' , 'author' : 'Sepehr Abbaspour'}
    return render(request , 'blog/blog-single.html' , context)

def test(request , pid): #migim gharare baraye to ye motagher voroodi be esm name biad
    #posts = Post.objects.all()
    post = get_object_or_404(Post , pk=pid)
    #inja migim ke bro barresi kon , agar dakhel model post man shakhesi ba filteri ke alan behet dadam (pk ke hamoon primery key hast)
    #(mitoonim ba id ham benevisim hich farghi nadare) vojood dare ya na ke primery key ham barabar hamoon pid ke beheah dadim bashe
    #vaghti query ejra mishe agar safhe vojood dasht neshoon bede , agar safhe vojood nadasht , bejaye error 404 bede.
    #yani shakhes aval man tooye get_object_or_404 modelam hast , shakhes dovom fiteri ke gharare roosh emal beshe

    #post = Post.objects.get(id=pid) #yani migim boro az tooye post va object hash ooni ro peida kon ke id sh barabar pid voroodi mane
    #id khob tooye admin har post ye id dasht dige , va pid ham oon id hast ke man daram tooye safhe am az url migiram
    #yani migam boro oon posti ke id sh ba pid safhe man yeki bood ro biar va berizesh tooye variable post
    #hala age vojood dasht post ro baraye man bargardoon be soorat line ie ke context ro toosh neveshtim baadi 
    #yadet nare tooye safhe html ham pasesh bedi object ro ba jinja
    #agar vojood nadashte bashe khata darim , mige in query ke zadi vojood nadare 
    #age vojood dashte bashe ba tavajoh be chizi ke tooye test.html pas dadim behemoon barmigarde
    context = {'post':post} #inja migim age name oomad bia va tooye safhe behem erja esh bede
    return render(request , 'test.html' , context)

#vakeshi kardan etelaat az data base

#ye masale ie baraye filter kardan shoon masala begam oonayi ke status shoon 1 hast yani goftam ke montasher beshan.
#osooli tarin rah in kar tooye views.py be soorat zir anjam beshe : posts = Post.objects.filter(status=1)
#query ro az all ke hamasho begire kardimesh filter. ghabla in bood : posts = Post.objects.all()
#dar in soorat ke filter bokonim dige hamaro behem neshoon nemide va faghat ooni ro neshoon mide ke montasher shode
#age status 0 bashe oonayi ro neshoon mide ke status shoon barabar 0 hast ya hanoon montasher nashodan.
#vali alan baraye dark behtar if dar jinja ino all mizarim ta ba jinja shart benevisim.



#dynamic kardan url ha : 

#har chand ta shakhesi ke tooye urls tarif karde bashim inja bayad neveshte bashan va tooye context ham neveshte beshan
#masala dar inja seta parametr bayad be url bedim ta kar kone : 2 ta string , ye doone int

