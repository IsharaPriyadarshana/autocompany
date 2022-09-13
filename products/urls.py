from django.urls import path
from . import views

urlpatterns = [
    path("", views.products, name="products"),
    path("detail", views.detail, name="detail"),
]