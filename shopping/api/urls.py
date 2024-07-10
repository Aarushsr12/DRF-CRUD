from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiView, name='home'),
    path('create/',views.add_items, name='add-items'),
]