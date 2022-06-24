from django.urls import path
from music.views import user_views as views
'''
This file is in charge of connecting views to our URLs
'''

urlpatterns = [

    path('login/', views.MyTokenObtainPairView.as_view(),
     name='token_obtain_pair'),    
    path('profile/', views.getUserProfile, name="user-profile"),
    path('profile/update/', views.updateUserProfile, name="user-update"),
    path('', views.getUsers, name="user"),
    path('register/', views.registerUser, name="registerUser"),
    path('delete/<str:pk>/', views.deleteUser, name='user-delete')
    
]


