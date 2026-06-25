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
    return HttpResponse("<h1>welcome to home page</h1>")

def contact_view(request):
    return HttpResponse("<h1>welcome to contact page</h1>")

def about_view(request):
    return HttpResponse("<h1>welcome to about page</h1>")

def json_test(request):
    return JsonResponse({"name" : "samim"})
