from django import template

register = template.Library()

# in hatma bayad neveshte magar na kar nakhahad kard in file blgo_test ma har chand tooye oon safhe html ie ke ke niazesh darim 
# ba {% load esm file %} ke dar inja darim {% load blog_tags %} load karde bashim file haro ]
#sakhtar file ha ham bayad daghigha be hamin soorat bashe ke tooye app ie ke mikhaym template tag besazim khodemoon (dar inja app blog)
#ye folder ijad mikonim be esm templatetags va tooye in folder ye file __init__.py misazim.
#hala ye file dige ham misazim ke esm oon file be in soorat hast ke aval esm app va baad kari ke mikhaym ba oon file anjam bedim
#masala inja esm in file blog_tags hast yani template tag haye marboot be app blog
#in sakhtar bala ham tooye har file ie ke mikhaym azash be onvan template tag estfade konim vajebe 
#alan ta inja template tag ma asmadast ta bahash ye seri kara anjam bedim