from django.shortcuts import render
from django.http import HttpResponse , JsonResponse , HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm , ContactForm , NewsLetterForm
from django.contrib import messages
from django.contrib import messages

def index_view(request):
    return render(request , "website/index.html")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request , messages.SUCCESS , 'your ticket submited successfully')
        else:
            messages.add_message(request , messages.ERROR , 'Your ticket didnt submited')

    form = ContactForm()
    return render(request , "website/contact.html" , {'form':form})

def about_view(request):
    return render(request , "website/about.html")

def json_test(request):
    return JsonResponse({"name" : "samim"})

def http_test(request):
    return HttpResponse("this is test for http-response")

def newsletter_view(request): 
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/') 
    else:
        return HttpResponseRedirect('/')

context = {'name' : 'sepehr' , 'lastname' : 'abbaspour'}

def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done') 
        else:
            return HttpResponse ('not valid')

    form = ContactForm()
    return render(request , "website/test.html" , {'form':form})
