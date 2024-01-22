from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login_pg, name='login'),
    path('loginhtpo/',views.login_ht_tpo, name='loginHTPO'),
    path('logout/',views.logout_view, name='logout'),
    path('login-redirect/', views.login_redirect_view, name='login_redirect'),
]