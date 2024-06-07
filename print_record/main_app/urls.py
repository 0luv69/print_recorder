from django.urls import path
from . import views

from .api import *
# from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('api/staff/', StaffApi.as_view(), name="getprofile"),
    path('api/std/', stdApi.as_view(), name="getstd"),
]