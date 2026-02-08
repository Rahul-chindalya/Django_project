from django.urls import path
from . import views

urlpatterns=[
    path('create/',views.create_item),
    path('',views.list_view),
    path('detail/<int:id>/',views.detail_view),
    path('update/<int:id>/',views.update),
    path('delete/<int:id>/',views.delete),
]