from django.urls import path #eyn ghabla ke app misakhtim amal mikonim.
from . import views #ye ravesh dige be jaye from accounts.views import * montaha bayad be in soorat bahash kar konim , masala
# views.login_view / hatma bayad birim esm file views ro / oon . ham mige az tooye hamin pooshe (app) ie ke toosh hasti yani accounts 

app_name = 'accounts'

urlpatterns = [
    #login
    path('login' , views.login_view , name='login'),

    #logout
    path('logout' , views.logout_view , name='logout'),

    #registration / sign up
    path('signup' , views.signup_view , name='signup'),
]
