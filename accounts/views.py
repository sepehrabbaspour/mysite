from django.shortcuts import render , redirect #baraye redirect be ye safhe dige
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import AuthenticationForm #baraye estefade az form haye bulit-in django
# Create your views here.

def login_view(request):
    if not request.user.is_authenticated: #agar user login nakarde bood inaro behesh neshoon bede , tooye else migim agar login karde bood , bargard be safhe asli
        if request.method == 'POST': #agar request post barat oomad etelaatesh ro daryaft kon
            form = AuthenticationForm(request=request , data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password) #in user ie ke dare miad asa vojood dare ya na , majule authenticate
                #be hamin manzoor import shode
                if user is not None: #agar user khali nabood (vojood dasht) nokte : in karo nakonim be in soorate ke mige in user vojood nadare vali rafti baraye login , exception mikhore
                    login(request , user) #be ezaye requesti ke ferestade va etelaat karbar (user) agar dorost bood login sh mikonim , function login ro ham bala import kardim
                    return redirect('/') #baraye redirect be ye safhe dige dar soorat login movafagh / inja redirect mishe be safhe asli

        form = AuthenticationForm()
        context = {'form' : form}
        return render(request , 'accounts/login.html' , context) #agar movafaghiat amiz nabood bargarbe be hamin safhe , va mitoone ye seri peygham ha bede

    else:
            return redirect('/')



    # if request.user.is_authenticated: #inja ye attribute az request darim ke be ma mige aya karbar ma login karde ya na. parantez nadare !!
    #     message = f'user is authenticated as {request.user.username}'
    #     #inja ba formated string behesh migim ke az tooye request karbar man username user ro dar biar va benevis ke che user ie login karde
    # else:
    #     message = 'user is not authenticated'  

    # return render(request , 'accounts/login.html' , {'message' : message})

    #deghat kon ke alan ma tooye view in barresi kardim ke karbar ma login hast ya na (comment shode) va message haro . be soorat
    #key value pas dadim tooye safhe va tooye template ham ba key mesage be soorat {{message}} darj sh kardim
    #hala berim hamin kar ro tooye templte anjam bedim

def logout_view(request):
    # return render(request , 'accounts/logout.html')
    pass

def signup_view(request):
    return render(request , 'accounts/signup.html')
