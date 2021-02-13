from django.contrib import admin
from django.urls import path

from recommendation.views import *

urlpatterns = [
    path('', index, name="home"),
    path('recommendation/', show_recommendation, name="recommendation"),
    # path('pdf/', get, name="pdf"),
]
