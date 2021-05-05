from django.shortcuts import render
from django.http import JsonResponse
from django.utils import translation
# Create your views here.
def freeFlowView(request, lang='he'):
    translation.activate(lang)
    return render(request, 'freeflow.html', {})
import json 

from .models import FreeFlowStores
from .serializers import FreeFlowStoresSerializer


from rest_framework import viewsets

class FfStoreViewSet(viewsets.ModelViewSet):
    queryset = FreeFlowStores.objects.all()
    serializer_class = FreeFlowStoresSerializer
'''
    print('api_FreeFlowStores')
    stores = FreeFlowStores.objects.all()
    data = []
    for store in stores:
        store_data = {
            'name': store.name,
            'lat': store.lat,
            'lng': store.lng,
            'img':store.img.url,
            'url':store.url,
        }
        data.append(store_data)
    print(data)
    response = JsonResponse(data)
    print( response.content)
    return response
'''