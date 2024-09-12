from django.urls import path
from . import views

urlpatterns = [
    path('view/<path:token>/<path:public_key>/', views.view_file, name='view_file'),
    path('', views.form, name="form"),
    path('download/', views.download_file, name='download_file'),
]