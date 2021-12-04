from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import xsum, mul, add, recognize_car_number_task, recognize_buckwheat_task
from celery.result import AsyncResult
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os 


@csrf_exempt
def rec_number_get_status(request, task_id):
    task_result = AsyncResult(task_id)

    result = {
        "task_id": task_id,
        "status": task_result.status, # 'FAILURE', 'SUCCESS', 'PENDING'
        "result": task_result.result
    }

    return JsonResponse(result, status=200)


@csrf_exempt
def rec_number_create_task(request):
    
    try:
        # image = request.data['photo']
        # image = request.POST.get("photo")
        image = request.FILES['photo']
    except KeyError:
        raise Exception('Request has no resource file attached')
    
    # print('-'*10)
    # # help(image)
    # print(image.name)
    # print(type(image))
    # print('-'*10)
    image_path = os.path.join(settings.MEDIA_ROOT, image.name)
    
    destination = open(image_path, 'wb+')

    for chunk in image.chunks():
        destination.write(chunk)

    destination.close()

    task = recognize_buckwheat_task.delay(image_path)
    return JsonResponse({"task_id": task.id}, status=202)


# class RecognitorsAPI(APIView):

#     def get(self, request, task_id, *args, **kwargs):
#         # data = [
#         #     {"id": 1, "name": "John"},
#         #     {"id": 2, "name": "John2"}
#         # ]
#         task_result = AsyncResult(task_id)

#         result = {
#             "task_id": task_id,
#             "status": task_result.status, # 'FAILURE', 'SUCCESS'
#             "result": task_result.result
#         }
#         # return JsonResponse(result, status=200)

#         # res = recognize_car_number.delay()
#         # r = res.get(timeout=1)
#         return Response(result, status=200)


#     def post(self, request):

#         try:
#             image = request.data['photo']
#             # image = request.POST.get("photo")
#             # image = request.FILES['photo']
#         except KeyError:
#             raise Exception('Request has no resource file attached')
        
#         print(image)
        
#         task = recognize_car_number_task.delay(image)
#         # transaction.on_commit(lambda: recognize_car_number_task.delay(image))
#         return Response({"task_id": task.id}, status=202)

    # @detail_route(methods=['post'])
    # def upload_docs(request):
        
    # def post(self, request, *args, **kwargs):
    #     res = xsum([1, 2])
    #     return Response(status=201)
