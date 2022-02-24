from django.urls import path
from .views import ChileView

urlpatterns = [
    path('sign/', ChileView.as_view(), name='sign'),
]
