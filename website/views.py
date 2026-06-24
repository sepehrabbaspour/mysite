from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
# Create your views here.

#hamoon vaseti hast ke daroon sh function misakhtim va hamoon chizie ke url mano be etelaati ke,
#karbar dare darkhast mide motasel mikone. ghabla in file ro be soorat jodagoone sakhtim.

#url hayi ke ghabla dashtim tooye ye file jodaye views mikhaym biarimesh tooye in file ke 
#tooye app mast
#yadet nare package hasho import koni.
#hala mitoonim oon file views ghabli ke tooye proje mysite sakhte boodim ro pakesh konim.

def http_test(request):
    return HttpResponse("this is first django project")

def json_test(request):
    return JsonResponse({"name" : "sepehr"})