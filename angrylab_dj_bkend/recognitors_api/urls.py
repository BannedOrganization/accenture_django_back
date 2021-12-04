from django.urls import path
from . import views


urlpatterns = [
    path('car_number/<str:task_id>', views.rec_number_get_status, name='get_rec_number'), # get
    path('car_number/', views.rec_number_create_task, name='create_rec_number'), # post


    # path('tomato', ..., name='tomato'), # get, post
    # path('buckwheat', ..., name='buckwheat'), # get, post
]
