from django.urls import path
from criminels import views

urlpatterns = [
    # ... autres URL ...
    path('criminels/', views.criminels_view, name='criminels'),
    path('alertes', views.alertes_view, name="alertes"),
    path('', views.home, name="home"),
    path('basededonnées/', views.basededonnées_view, name='basededonnées'),
    path('logout_user', views.logout_user, name='logout'),
    path('', views.home1, name="home1"),
]