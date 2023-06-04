from django.urls import path
from .views import Authorize

urlpatterns=[
    path('authorize/',Authorize.as_view(),name="Authorize")
]