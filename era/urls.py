from django.urls import path
from django.utils import timezone
from django.views.generic import DetailView, ListView
from era.models import Facultad
from era.views import *
'''
from myrestaurants.models import Restaurant, Dish
from myrestaurants.forms import RestaurantForm, DishForm
from myrestaurants.views import RestaurantCreate, DishCreate, RestaurantDetail, review, LoginRequiredCheckIsOwnerUpdateView
'''
app_name = "era"

urlpatterns = [
    path('', ListView.as_view(queryset=Facultad.objects.order_by('-name'),
            context_object_name='facultad_list',
            template_name='era/facultadList.html'),
        name='facultad_list'),

    path('facultad/<int:pk>',
         FaculdadDetails.as_view(),
         name='facultad_details'),

    path('facultad/<int:pk>/career/<int:pkr>',
         CareerDetails.as_view(),
         name='career_details'),

    path('facultad/create',
         FacultadCreate.as_view(),
         name='create_facultad'),

    path('facultad/<int:pk>/career/create/',
         CareerCreate.as_view(),
         name='create_carrer'),
]