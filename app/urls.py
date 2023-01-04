from django.urls import path
from app import views

urlpatterns = [
    path('categories/', views.api_categories, name='apiCategories' ),
    path('photos/', views.getPhotos, name='photos' ),
]