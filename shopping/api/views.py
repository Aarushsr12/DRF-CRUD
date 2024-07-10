from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Item
from rest_framework import status
from rest_framework import serializers
# Create your views here.

@api_view(['GET'])
def apiView(request):
    api_urls = {
        'all_items': '/',
        'search_by_category': '/?category=category_name',
        'search_by_subcategory': '/?sub_category=category_name',
        'create':'/create',
        'update':'/update/pk',
        'delete':'/item/pk/delete'
    }
    return Response(api_urls)

@api_view(['POST'])
def add_items(request):
    item = ItemSerializer(data=request.data)

    #if already existing
    if Item.objects.filter(**request.data).exists():
        return serializers.ValidationError('already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)