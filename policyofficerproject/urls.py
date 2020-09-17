"""policyofficerproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from policy import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.home, name= "home"),
    path('suit/', views.suit, name= "suit"),
    path('view/', views.view, name= "view"),
    path('login/', LoginView.as_view(), name= "login"),
    path('mind/', views.mind, name= "mind"),
    path('mypage/', views.mypage, name= "mypage"),
    path('signup/', views.signup, name= "signup"),
    path('search', views.search, name='search'),
    path('detail/<int:policy_id>/', views.detail, name = "detail"),
    path('blog1/', views.blog_gugic, name= "blog_gugic"),
    path('blog2/', views.blog_education, name="blog_education"),
    path('filter/', views.filteraside, name="filteraside"),
    # path('category/', views.category, name="category"),
    path('logout/', LogoutView.as_view(), name="logout"),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


