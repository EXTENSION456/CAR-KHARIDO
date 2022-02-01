
"""car_company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 
from customers import views
from Administrator import views as aviews
from cars import views as cviews
from Staticpages import views as sviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',sviews.home),
    path('home/aboutus.html/',sviews.home),
    path('home/contactus.html/',sviews.home),
    path('signup/',views.signup),
    path('home/signup.html/',views.signup),
    path('home/login.html/',views.login),
    path('home/login admin.html/',aviews.login_admin),
    path('home/login admin.html/customer_info.html',aviews.get_queryset),
    path('home/login admin.html/delete.html',aviews.delete_user),
    path('home/login admin.html/onecust.html',aviews.onecust),
    path('home/login admin.html/cars.html/',cviews.picupload),
    path('home/login admin.html/viewcars.html/',cviews.picget),
    path('home/login admin.html/editrate.html/',aviews.editrate),
    path('home/login.html/editpassword.html',views.useractivity),
    path('home/login.html/bookcars.html',views.bookcar),
 
    
     
    
]
if settings.DEBUG:
        urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

