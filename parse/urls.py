from django.urls import path, include
from .views import IndexViews

urlpatterns= [
    path('', IndexViews.as_view())
]