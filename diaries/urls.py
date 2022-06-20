from django.urls import path
from . import views

app_name = 'diaries'

urlpatterns = [
    path('', views.top, name='top'),
    path('contact/', views.Top.as_view(), name='contact'),
    path('thanks/', views.Thanks.as_view(), name='thanks')
]
