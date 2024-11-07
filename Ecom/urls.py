"""
URL configuration for Ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin# type: ignore
from django.urls import path , include # type: ignore
from . import views
from django.conf import settings  # type: ignore
from django.conf.urls.static import static  # type: ignore
from django.contrib.auth import views as auth_views # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.BASE, name ='base'),
    path('', views.Home, name ='home'),
    

    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('about', views.about, name='about'),
    path('order', views.order, name='order'),
    path('search', views.search_view, name='search'),
    


    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout', views.user_logout, name='logout'),
    
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    


    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),




] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)