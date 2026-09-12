from django.shortcuts import render

# Create your views here.

def login_view(request):
    # if request.user.is_authenticated: #inja ye attribute az request darim ke be ma mige aya karbar ma login karde ya na. parantez nadare !!
    #     message = f'user is authenticated as {request.user.username}'
    #     #inja ba formated string behesh migim ke az tooye request karbar man username user ro dar biar va benevis ke che user ie login karde
    # else:
    #     message = 'user is not authenticated'  

    # return render(request , 'accounts/login.html' , {'message' : message})

    return render(request , 'accounts/login.html')
    #deghat kon ke alan ma tooye view in barresi kardim ke karbar ma login hast ya na (comment shode) va message haro . be soorat
    #key value pas dadim tooye safhe va tooye template ham ba key mesage be soorat {{message}} darj sh kardim
    #hala berim hamin kar ro tooye templte anjam bedim

def logout_view(request):
    # return render(request , 'accounts/logout.html')
    pass

def signup_view(request):
    return render(request , 'accounts/signup.html')
