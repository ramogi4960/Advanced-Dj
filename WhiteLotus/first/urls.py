from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('dynamic/<str:pk>', views.dynamic, name='dynamic'),
    path('forms', views.forms, name='forms'),
    path('update_forms/<str:pk>', views.update_forms, name='update_forms'),
    path('delete_forms/<str:pk>', views.delete_forms, name='delete_forms'),
]
