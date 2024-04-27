
from django.urls import path
from.import views
urlpatterns = [
    path('', views.home, name="home"),
    path('criminels', views.criminels_view, name="criminels"),
    path('alertes', views.alertes_view, name="alertes"),
    path('basededonnées/', views.basededonnées_view, name='basededonnées'),
    path('logout_user', views.logout_user, name='logout'),
    path('', views.home1, name="home1"),
    
]