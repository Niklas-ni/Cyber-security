from django.urls import path
from .views import HomePageView, addView, removeView

urlpatterns = [
    path('', HomePageView , name = 'home'), 
    path('add/', addView, name ='add'),
    path('remove/', removeView, name = 'remove'),

]