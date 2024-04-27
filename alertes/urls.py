from django.urls import path
from criminels import views
from django.urls import path
from . import views

urlpatterns = [
   
    path('alertes/', views.alertes_view, name='alertes'),
    path('criminels/', views.criminels_view, name='criminels'),
    path('', views.home, name="home"),
    path('basededonnées/', views.basededonnées_view, name='basededonnées'),
    #testtttttttttttttttttttttttttttttttttttt
    
]