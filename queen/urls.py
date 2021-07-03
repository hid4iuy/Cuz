from django.urls import path
from . import views
from .views import topViews,resultViews,detailViews

urlpatterns = [
    path('', views.index,name='top'),
    path('detail/<nameKN>', detailViews.as_view(), name='detail'),
    path('result', views.resultViews, name='result'),
    path('vote/<uuid>', views.vote, name='votecan'),
]
