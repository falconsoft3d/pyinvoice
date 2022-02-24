from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class ProChileView(View):    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        if request.body:
            jd = json.loads(request.body)
            datos = {'message': "error"}
        else:
            datos = {
                     'message': "ok", 
                     "invoice": { "folio" : 1}
                     }
        return JsonResponse(datos)

class TestChileView(View):    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        if request.body:
            jd = json.loads(request.body)
            datos = {'message': "error"}
        else:
            datos = {
                     'message': "ok", 
                     "invoice": { "folio" : 0}
                     }
        return JsonResponse(datos)