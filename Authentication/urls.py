from django.urls import path

from Authentication import views

urlpatterns = [
    path('login/', views.Login.as_view() , name='login'),
    path('signup/', views.SignUp.as_view() , name='signup'),
    path('profile/' ,views.Profile.as_view(), name='profile'),
    path('logout/', views.Logout.as_view(), name='logout'),
    # path('edit/' , views.Edit.as_view(), name='edit'),
        
]

