from django.urls import path
from . import views
from .views import resultViews,detailViews

urlpatterns = [
    path('', views.index,name='top'),
    path('detail/<nameKN>', detailViews.as_view(), name='detail'),
    path('result', views.resultViews, name='result'),
    path('vote/<uuid>', views.vote, name='votecan'),
    path('lastrank' , views.lastrank ),
    path('result/like/<cmt_id>', views.like ,name='like'),
    path('result/bad/<cmt_id>', views.bad ,name='bad'),
    path('reserve', views.reserve ,name='reserve'),
]
