from django.urls import path
 
from . import views
 
app_name = 'anken'
 
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create', views.AnkenCreate.as_view(), name="anken_create"),
]