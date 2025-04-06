
from django.contrib import admin
from django.urls import path
from Veg.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('admin/', admin.site.urls),
    path('recipe/',getting_recipe,name = 'getting_recipe'),
    path('recipe/delete/<id>/',delete,name = 'delete'),
    path('recipe/update/<id>/',update,name = 'update'),
    path('login/',login_page,name = 'login'),
    path('signup/',signup,name = 'signup'),
    path('logout/',logout_page,name = 'logout_page'),
    path('Reset-password/',Reset_password,name = 'Reset_password'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
