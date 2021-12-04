from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# from angrylab_dj_bkend.recognitors_api.recognitors.car_number_recognitor import alpnr2_0
from .tasks import xsum, mul, add, recognize_car_number_task, recognize_buckwheat_task
from celery.result import AsyncResult
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os 
# from .recognitors.car_number_recognitor.alpnr2_0 import Recognitor
from .recognitors.buckwheat_recognitor.garbage_detector_predict import Garbage_Detector


# @csrf_exempt
# def rec_number_get_status(request, task_id):
    # task_result = AsyncResult(task_id)

    # result = {
    #     "task_id": task_id,
    #     "status": task_result.status, # 'FAILURE', 'SUCCESS', 'PENDING'
    #     "result": task_result.result
    # }

    


    # Recognitor(path)

    # return JsonResponse(result, status=200)


# @csrf_exempt
# def rec_number_create_task(request):
    
#     try:
#         image = request.FILES['photo']
#     except KeyError:
#         raise Exception('Request has no resource file attached')

#     image_path = os.path.join(settings.MEDIA_ROOT, image.name)
    
#     destination = open(image_path, 'wb+')

#     for chunk in image.chunks():
#         destination.write(chunk)

#     destination.close()

#     result = Recognitor(image_path)

#     # task = recognize_car_number_task.delay(image_path)
#     # return JsonResponse({"task_id": task.id}, status=202)
#     JsonResponse(result)


# @csrf_exempt
# def rec_buckwheat_status(request, task_id):
#     task_result = AsyncResult(task_id)

#     result = {
#         "task_id": task_id,
#         "status": task_result.status, # 'FAILURE', 'SUCCESS', 'PENDING'
#         "result": task_result.result
#     }

#     return JsonResponse(result, status=200)


@csrf_exempt
def rec_buckwheat_create_task(request):
    try:
        image = request.FILES['file']
    except KeyError:
        raise Exception('Request has no resource file attached')
        
    image_path = os.path.join(settings.MEDIA_ROOT, image.name)
    
    destination = open(image_path, 'wb+')

    for chunk in image.chunks():
        destination.write(chunk)

    destination.close()

    result = Garbage_Detector(image_path)

    print(type(result))
    return JsonResponse({'result': result}, status=202)

    # task = recognize_buckwheat_task.delay(image_path)
    # return JsonResponse({"task_id": task.id}, status=202)
