from mysite.settings import * #az tooye settings har chizi ke toosh hast. baraye inke in eleman hayi ke az tooyte setting avordim inja kar bokone
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zhz2#4y6zcx1bk61w-#1p!+9fde+45%)knas@4@@3dve!sxkw+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

#INSTALED_APPS = []

# site framworks
SITE_ID = 2 #in site id baraye majule site hast ke ham mishe az tooye data base in id ro be dast avord 
#va ham mishe vared panel admin shod va oonja tooye bakhsh site oon jayi ke ye addres jadid tarif kardim 
#rooye url tooye search bar bezanim id sh maloome 
#tooye meghdar site id ke inja tarif kardim hamoon adad ro minevisim

#albate yadet nare tooye admin tooye bakhsh site ye site jadid besazi ke vaghti app site ro inja tooye settingezafe kardim 
#bayad migrate konim 

#dar vaghe chizi ke be proje ezafe shode ine ke serfa oomadim va barash taien kardam ke gharare esm to va amalkardi ke
#banast dashte bashi bar asas in id va in name gharare bashe 
#in alan faghat setup bood , behesh miresim

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / "static/" #deghat kon zamani ke mikhay ye static besazi va file haye css ro oonja gharar bedi
#bayad ye static root besazi va base_dir ro be hamin soorat bala ba static tarkib konim ta css hayi ke neveshtim
#va link kardim be file html emal beshan
#link sade tarin halat motesal kardan file css be html hast ke dar file about.html mojood hast
#dar soorati ke inja STATIC_ROOT tarif nashode bashe nemitoonim be hich file dasteresi dashte bashim
#nokte badi in ke pooshe static bayad tooye app ma sakhte beshe va esmesham bayad hamoon static bashe

MEDIA_ROOT = BASE_DIR / "media/"

#hala ye media_url va media_root ham tarif mikonim baraye media ha 
#be hamin sadegi :)

STATICFILES_DIRS = [
    BASE_DIR / "statics", #inja mishe esm directory moshakhas kard
]

#CSRF_COOKIE_SECURE = True