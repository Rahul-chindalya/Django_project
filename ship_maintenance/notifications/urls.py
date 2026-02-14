from django.urls import path
from . import views

urlpatterns=[
    path('notifications/create/',views.notification_create),
    path('notifications/list/',views.notification_list),
    path('notifications/all/list/',views.all_notifications),
    path('notifications/mark_as_read/<int:id>',views.mark_as_read),
    path('notifications/delete/<int:id>',views.notification_delete), 
]