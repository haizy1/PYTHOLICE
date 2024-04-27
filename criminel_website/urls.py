from django.urls import path
from .import views

urlpatterns = [
    path('', views.home1, name="home1"),
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('alertes/', views.alertes_view, name='alertes'),
    path('criminels/', views.criminels_view, name='criminels'),
    path('events/', views.home, name="home"),
    path('basededonnées/', views.basededonnées_view, name='basededonnées'),
    

    ]
