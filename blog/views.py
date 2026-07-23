from django.shortcuts import render
from blog.models import Post #table post ro inja import mikonim

def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request , 'blog/blog-home.html' , context)

def blog_single(request):
    context = {'title' : 'bitcoin crashed again!' , 'content' : 'bitcoin was flying but now grounded as always' , 'author' : 'Sepehr Abbaspour'}
    return render(request , 'blog/blog-single.html' , context)

def test(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request , 'test.html' , context)

#ye masale ie baraye filter kardan shoon masala begam oonayi ke status shoon 1 hast yani goftam ke montasher beshan.
#osooli tarin rah in kar tooye views.py be soorat zir anjam beshe : posts = Post.objects.filter(status=1)
#query ro az all ke hamasho begire kardimesh filter. ghabla in bood : posts = Post.objects.all()
#dar in soorat ke filter bokonim dige hamaro behem neshoon nemide va faghat ooni ro neshoon mide ke montasher shode
#age status 0 bashe oonayi ro neshoon mide ke status shoon barabar 0 hast ya hanoon montasher nashodan.
#vali alan baraye dark behtar if dar jinja ino all mizarim ta ba jinja shart benevisim.

