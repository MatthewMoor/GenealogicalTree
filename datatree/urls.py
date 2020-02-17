from django.urls import path
from datatree import views

urlpatterns = [
    path('tree', views.show_tree, name="show_tree"),
]