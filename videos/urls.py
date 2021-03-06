from django.urls import path
from . import views
app_name = 'videos'

urlpatterns = [
    path('', views.VideoList.as_view(), name='video_list'),
    path('play/<int:pk>/', views.VideoDetail.as_view(), name='video_detail')
]