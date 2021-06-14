from django.urls import path
from . import views
from .views import CandidateList,AreaList,VoteList,resultViews

urlpatterns = [
    path('', resultViews),
    path('list', CandidateList.as_view()),
    path('area', AreaList.as_view()),
    path('vote/<uuid>', views.vote, name='votecan'),
    path('vote', VoteList.as_view()),
    path('create', views.create,name='create'),
    # path('list/<chr:area_n>', views.areacand, params),
]