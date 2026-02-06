from django.urls import path
from . import views

app_name ="ipl_app"

urlpatterns = [
    path("",views.home,name="home"),
    path('register/',views.register,name='register'),
    path('login/',views.login_pr,name='login'),
    path('register-franchise/',views.register_franchise,name='register_franchise'),
    path('franchise_list/',views.franchise_list,name='franchise_list'),
    path('franchise_details/<int:id>/',views.fr_details,name='franchise_details'),
    path('franchise_update/<int:id>/',views.fr_update,name='franchise_update'),
    path('franchise_delete/<int:id>/',views.fr_delete,name='franchise_delete'),
    path('register_player/',views.register_player,name='register_player'),
    path('players_list/',views.player_list,name='players_list'),
    path('update_player/<int:id>/',views.update_player,name='update_player'),
    path('delete_player/<int:id>/',views.delete_player,name='delete_player'),
    path('stadium/',views.register_stadium,name='register_stadium'),
    path('stadium_list/',views.stadium_list,name='stadium_list'),
    path('stadium_update/<int:id>/',views.stadium_update,name='stadium_update'),
    path('stadium_delete/<int:id>/',views.stadium_delete,name='stadium_delete'),
    path('register_user/',views.register_user,name='register_user'),
    path('login_user/',views.login_user,name='login_user')
]