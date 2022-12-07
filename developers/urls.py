from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="developers"),
    path("<int:developer_id>", views.developer, name="developer"),
]
