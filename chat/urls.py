from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name="home"),
    path('chat/<str:room>/',views.room,name="room"),
    path('ckeckview',views.checkview,name="checkview"),
    path('send',views.send,name="send"),
    path('getMessages/<str:room>/',views.getMessages,name="getMessages"),
    path('delete/', views.delete_message, name='delete'),
]