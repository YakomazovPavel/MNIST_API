# from rest_framework import generics
# from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from my_model import raspoznavanie
import numpy as np


class mnist_api_view(APIView): # прописывается в маршрутах urls.py
    def post(self, request):
        # str(request)
        # title = request.data['array']
        b = 'пусто'
        try:
            b = request.data['_array']
            # print(str(request.data['_array']))
            # print(type(b))
            c = np.array(b)
            # c = nparray_list(b)
            # print(c)
            res = raspoznavanie(c)
            res = list(np.round(res[0], 2))

            print(f'Результат: {res}')
            return Response({'title': res})
        except:
            print('ошибка')
            return Response({'title': 'error'})



# class mnist_serializer(serializers.ModelSerializer):
#  pass