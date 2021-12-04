from django.urls import path
from . import views


urlpatterns = [
    # path('car_number/<str:task_id>', views.rec_number_get_status, name='get_rec_number'), # get
    # path('car_number/', views.rec_number_create_task, name='create_rec_number'), # post

    # path('buckwheat/<str:task_id>', views.rec_buckwheat_status, name='get_rec_buckwheat'), # get
    path('buckwheat/', views.rec_buckwheat_create_task, name='create_rec_buckwheat'), # post
]
