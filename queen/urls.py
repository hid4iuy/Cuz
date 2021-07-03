from django.urls import path
from . import views


urlpatterns = [
    path('vote/<uuid>', views.vote, name='votecan'),
    path('', views.index,name='top'),
]