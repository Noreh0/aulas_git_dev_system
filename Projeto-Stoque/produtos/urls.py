from django.urls import path
from produtos.views import index, produto

urlpatterns = [
    path('', index),
    path('produto/', produto, name='produto')
]