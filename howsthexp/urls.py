from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index, name='index'),
    path('register',views.Register,name='register_user'),
    path('login',views.Login,name='login_user'),
    path('dashboard/<user>',views.Dashboard,name='user_dashboard'),
    path('play/song/<user>/<emotion>',views.Play,name='play_song'),
    path('logout/<user>',views.Logout,name='logout_user'),

]
