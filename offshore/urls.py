"""offshore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path

# my imports
from landing_page.views import index_view
from auths.views import Login
from dashboard.views import ProfileView, login_user, transfer, transfer_view
# end of my imports

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('login/', login_user, name='login'),
    path('dashboard/', ProfileView.as_view(), name='dashboard'),
    path('make$transfer/', transfer, name='make_transfer'),
    path('history/', transfer_view, name='history')
]
