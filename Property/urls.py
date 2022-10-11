from django.urls import path

from Property import views

urlpatterns = [
    path('property/' , views.Property.as_view() , name='property'), 
    path('single_property/<int:details>/' , views.Single.as_view() , name='single_property'), 
    path('add_property/', views.AddProperty.as_view() , name='add_property'),
    path('view_property/' , views.ViewProperty.as_view(), name='view_property')
]