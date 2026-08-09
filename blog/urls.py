from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('' , blog_view , name='index'),
    path('<int:pid>' , blog_single , name='single'), #injoori behesh migim age post man ba ye id hamgam bood to miri be view 
    #marboot be blog single moraje mikoni, hala chon bana shod faghat id bedim , post- az avalesh pak mikonim va faghat id midim
    path('category/<str:cat_name>' , blog_category , name='category'),
    path('test' , test , name='test'),

]


#khob kari ke mikhaym anjam bedim ine ke eleman hayi ijad konim ke be soorat dinamic parameter haro az tarigh url daryaft konand
#va tooye safhe bahemoon namayesh bedan
#tooye path ie ke test ro neveshtim be onvan url bayad biaim va parametr voroodi bedim
#aval az hame migim be jaye jaygahi ke man daram test ro vared mikonam (avalin test (url)) mikham be soorat dinamic ye reshte vared konam
#va dar nahayat ye esm behesh midim ke inja esmesho gozashtim name be in soorat <str:name>
#yani migam az in be baad inja ye moteghayer voroodi ba esm name behet midam. hala in name ro bayad tooye view estefade kard.
#hala mitoonim bejaye 1 parameter 2 ya chand parameter bezarim , be in soorat <str:name>/<str:family_name/<int:age>
#pas alan fahmidim mitoonim parametr hayi ke lazem darim ro az tarigh url ham be view ha bedim
#masala hata mishe behesh style dad be in soorat <str:name>/lastname/<str:family_name>/age/<int:age>
#va url ham bayad be hamin soorat bashe : http://127.0.0.1:8000/blog/sepehr/lastname/abbaspour/age/22
#chon alan sakhtar jadid barash tarahi kardam. pas mishe ye jahayi ham beinesh static darnazar gereft mesl inja 

#pid ke esm moteghayer mast eshare mikone be inja eshare mikone be hamoon id hayi ke be ezaye eleman hamoon tooye data base dashtim.
 
