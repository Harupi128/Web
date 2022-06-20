from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.ReviewList.as_view(), name='review_list'),
    path('detail/<int:pk>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('create/', views.ReviewCreate.as_view(), name='review_create'),
]