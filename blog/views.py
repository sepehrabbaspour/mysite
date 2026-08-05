from django.shortcuts import render , get_object_or_404
from blog.models import Post #table post ro inja import mikonim
#from django.shortcuts import get_object_or_404 : in chizi ke import kardim mikhaym kari konim ke vaghti ke safhe ie peida nemishe 
#be jaye error , khataye 404 begirim :) vali khob niazi be tarif dobarash nist va chon django.shortcuts ro bala darim 
#faghat get_object_or_404 ro import mikonim 
#hala query variable post paien ro berim be shekli benevisim ke aval biad barresi kone , age vojood dasht namayesh bede , 
#agar vojood nadasht , be jaye error , 404 behemoon bargardoone
from django.utils import timezone


def blog_view(request):
    posts = Post.objects.filter(
        status=1,
        published_date__lte = timezone.now()
    )

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