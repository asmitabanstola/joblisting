"""joblisting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('list/',views.list,name='list'),
    path('contactus/', views.contactus, name='contactus'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.signin,name='signin'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.signout,name='signout'),
    path('create-post/',views.create_post,name='create_post'),
    path('edit-job/<int:id>',views.editpost,name='edit_post'),
    path('delete-job/<int:id>', views.deletepost, name='delete_post'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
