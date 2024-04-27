from django.urls import path
from criminels import views

urlpatterns = [
    # ... autres URL ...
    path('basededonnées/', views.basededonnées_view, name='basededonnées'),
    path('criminels/', views.criminels_view, name='criminels'),
    path('alertes', views.alertes_view, name="alertes"),
    path('', views.home, name="home"),
]