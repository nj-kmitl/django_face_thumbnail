from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListProfileView.as_view(), name='list'),
    path("list", views.ListProfileView.as_view(), name='list'),
    path('create', views.profile_create, name='create_profile'),
    path('update/<str:pname>', views.profile_update, name='update_profile'),
]