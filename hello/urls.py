from django.urls import path
from . import views
from .views import PoliticList
from .views import PoliticDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('list', PoliticList.as_view(), name='list'),
    path('detail/<int:pk>', PoliticDetail.as_view()),
    path('vote/<int:politic_id>', views.vote, name='vote'),

]