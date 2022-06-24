from django.urls import path
from music.views import orders_views as views
'''
This file is in charge of connecting views to our URLs
'''

urlpatterns = [

    # path('', views.getOrders, name='orders'),
    path('add/', views.addOrderItems, name='orders-add'),
    path('myorders/', views.getMyOrders, name='myorders'),
    path('myitems/<str:pk>', views.getOrderItemsUser, name='items-by-user'),

    #path('<str:pk>/deliver/', views.updateOrderToDelivered, name='order-delivered'),

    path('<str:pk>/', views.getOrderById, name='user-order'),
    # path('<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
]


