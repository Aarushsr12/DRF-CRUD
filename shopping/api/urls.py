from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiView, name='home'),
    path('create/',views.add_items, name='add-items'),
    path('all/',views.get_items, name='get-items'),
    path('item/<int:pk>/delete',views.delete_item, name='delete-items'),
]