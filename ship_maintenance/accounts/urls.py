from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.user_register),
    path('login/',views.user_login),
    path('admin/list/',views.users_list),
    path('admin/detail/<int:id>/',views.user_detail),
    path('admin/update/<int:id>/',views.user_update),
    path('admin/delete/<int:id>/',views.user_delete),
]