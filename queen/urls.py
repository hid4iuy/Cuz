from django.urls import path
from . import views
from .views import topViews,resultViews,detailViews

urlpatterns = [
    path('', topViews.as_view(), name='top'),
    path('detail/<nameKN>', detailViews.as_view(), name='detail'),
    path('result', views.resultViews, name='result'),
]