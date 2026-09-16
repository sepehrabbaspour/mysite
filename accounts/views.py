from django.shortcuts import render , redirect #baraye redirect be ye safhe dige
from django.contrib.auth import authenticate, login , logout #/ login baraye login / logout baraye logout / 
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm  #baraye estefade az form haye bulit-in django , estefade az user creation (mal hamoon bulid in django forms) 
from django.contrib.auth.decorators import login_required #baraye decorator login_required
from django.urls import reverse #baraye bargashtan be ye safhe dige
# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)

            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('/')

            message = 'Username or password is incorrect.'

        else:
            form = AuthenticationForm()
            message = ''

        context = {'form': form, 'message': message}
        return render(request, 'accounts/login.html', context)

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

@login_required
def logout_view(request):
    #if request.user.is_authenticated: #migim agar karbar ma login karde bood , betoone logout kone. dar gheyr in soorat redirect beshe be safhe asli
    logout(request) #request karbar ro mizarim tooye function logout / bala ham import sh kardim.
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:  # agar user login nakarde bood safhe signup behesh neshoon bede
        if request.method == 'POST':  # agar request method ma post bood
            form = UserCreationForm(request.POST)  # ye form ba UserCreationForm ijad kon be ezaye dade ie ke karbar dare post mikone

            if form.is_valid():  # agar form valid bood
                form.save()  # save sh kon
                return redirect('/')

                # return redirect('accounts/login')
                # return reverse('accounts:login')
                # amma serfa mikhaym bargardim tooye safhe asli moon pas:
                # return redirect('/')
        else:
            form = UserCreationForm()  # agar request GET bood, ye form khali besaz

        context = {'form': form}
        return render(request, 'accounts/signup.html', context)

    else:
        return redirect('/')
