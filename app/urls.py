from django.urls import path
from .views import index, tab1, tab2, tab3

urlpatterns = [
    path('', index, name='index'),
]