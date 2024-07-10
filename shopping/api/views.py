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
        raise serializers.ValidationError('already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])    
def get_items(request):
    if request.query_params:
        items = Item.objects.filter(**request.query_params.dict())
    else:
        items = Item.objects.all()

    if items:
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['DELETE'])
def delete_item(request,pk):
    item = Item.objects.get(id = pk)
    item.delete()

    return Response(status=status.HTTP_202_ACCEPTED)


