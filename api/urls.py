#encoding:utf-8

from django.urls import path
from .view import v1
app_name = "api"

urlpatterns = [
    path('v1/client/<ip>/',v1.ClinetView.as_view(),name='client'),
    path('v1/client/<ip>/resource/',v1.ResourceView.as_view(),name='resource'),

]
