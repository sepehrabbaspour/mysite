from django.shortcuts import render , get_object_or_404
from blog.models import Post #table post ro inja import mikonim
#from django.shortcuts import get_object_or_404 : in chizi ke import kardim mikhaym kari konim ke vaghti ke safhe ie peida nemishe 
#be jaye error , khataye 404 begirim :) vali khob niazi be tarif dobarash nist va chon django.shortcuts ro bala darim 
#faghat get_object_or_404 ro import mikonim 
#hala query variable post paien ro berim be shekli benevisim ke aval biad barresi kone , age vojood dasht namayesh bede , 
#agar vojood nadasht , be jaye error , 404 behemoon bargardoone
from django.utils import timezone


def blog_view(request , **kwargs):
    posts = Post.objects.filter(
        status=1,
        published_date__lte = timezone.now()
    )
    if kwargs.get('cat_name') != None:   
        posts = posts.filter(category__name=kwargs['cat_name'])

    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])

        #baraye kwargs tooye paratez gozashtan faghat baraye method get hast. 
        #agar kwargs khali oomad bayad begim kwargs['cat_name'] , mesl halat list
        #inam bastegi be khodemoon dare ke tak tak eleman bedim ya az kwargs estefade konim farghi nadare.
        #zamani mishe az kwargs estefade kard ke mesl inja eleman ha key value ie bian
        #vaghti ham mikhaym ba ye meghdari moghayese beshe bayad be in soorat bedim hatma author__username=kwargs['author_username']
        #dar vaghe mige agar vojood dasht meghdaresh ro bezar baraye author__username
        #if kwargs.get('cat_name') != None inja ham migim agar barabar ba none nabood , yani agar vojood dasht.
        #baraye in ke be error ie nakhorim

    
    context = {'posts':posts}
    return render(request , 'blog/blog-home.html' , context)

def blog_single(request , pid):
    post = get_object_or_404(
        Post,
        pk=pid,
        status = 1 , 
        published_date__lte = timezone.now()
    )

    post.counted_views +=1
    post.save()

    context = {'post':post}
    return render(request , 'blog/blog-single.html' , context)

def test(request):
    return render(request , 'test.html')

def blog_category(request , cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name) #deghat kon 2 ta underline (__) mikhad baraye inke betoonim be esm category dastresi peyda konim
    context = {'posts' : posts}
    return render(request , 'blog/blog-home.html' , context)



#noskhe ghabli bedoon kwargs
# def blog_view(request , cat_name=None , author_username=None):
#     posts = Post.objects.filter(
#         status=1,
#         published_date__lte = timezone.now()
#     )
#     if cat_name:
#         posts = posts.filter(category__name=cat_name)

#     if author_username:
#         posts = posts.filter(author__username=author_username)
    
#     context = {'posts':posts}
#     return render(request , 'blog/blog-home.html' , context)
