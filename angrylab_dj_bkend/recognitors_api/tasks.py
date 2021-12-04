# Create your tasks here

# from demoapp.models import Widget
from h5py._hl.files import File
from angrylab_dj_bkend.celery import app
from celery import shared_task
import os
from PIL import Image
from io import BytesIO
from base64 import b64decode, b64encode

# from .recognitors.car_number_recognitor.alpnr2_0 import Recognitor
from .recognitors.tomato_garbage_detector.garbage_detector_predict import Garbage_Detector as tomatoGD
from .recognitors.buckwheat_recognitor.garbage_detector_predict import Garbage_Detector as buckwheatGD

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


# @app.task

@shared_task
def recognize_car_number_task(image_path):
    
    result = tomatoGD(image_path)
    
    if result.status == 'SUCCESS':
        os.remove(image_path)

    return result


@shared_task
def recognize_buckwheat_task(image_path):

    result = buckwheatGD(image_path)
    
    # if result.status == 'SUCCESS':
    #     os.remove(image_path)

    return result
    

# @shared_task
# def count_widgets():
#     return Widget.objects.count()


# @shared_task
# def rename_widget(widget_id, name):
#     w = Widget.objects.get(id=widget_id)
#     w.name = name
#     w.save()