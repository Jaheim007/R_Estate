from django.urls import path

from Front import views

urlpatterns = [
    path('', views.Home.as_view() , name='home'),
    path('about/', views.About.as_view() , name='about'),
    path('contact/', views.Contact.as_view() , name='contact'),
    path('service/', views.Service.as_view() , name='service'),
    
]

