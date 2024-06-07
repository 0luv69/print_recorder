from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .api import *

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # API add staff
    path('api/staff/', StaffApi.as_view(), name="getprofile"),
]