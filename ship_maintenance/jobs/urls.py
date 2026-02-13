from django.urls import path
from . import views

urlpatterns = [
    path("jobs/create/",views.jobs_create),
    path('jobs/list/',views.job_list),
    path('jobs/details/<int:id>/',views.job_details),
    path('jobs/update/<int:id>/',views.job_update),
    path('jobs/delete/<int:id>/',views.job_delete),
]