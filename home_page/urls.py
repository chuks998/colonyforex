# from django.contrib import admin
from django.urls import path
from .views import SignalView

urlpatterns = [
    # path('', index_view, name='home'),
    path('', SignalView.as_view(), name='home'),
]
