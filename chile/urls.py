from django.urls import path
from .views import TestChileView, ProChileView

urlpatterns = [
     path('test/sign/', TestChileView.as_view(), name='sign'),
     path('pro/sign/', ProChileView.as_view(), name='sign'),
]
