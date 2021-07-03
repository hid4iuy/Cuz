from django.views.generic import TemplateView,ListView
from django.db import models
import plotly.express as px
from django_pandas.io import read_frame
from django.shortcuts import render, redirect
from plotly.offline import plot as p
from queen.models import VOTE ,CANDIDATE
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from .forms import CandidateForm,VoteInfoForm
import logging,datetime


def vote(request, uuid):
    can = CANDIDATE.objects.get(uuid=uuid)
    vote = VOTE.objects.get(candidateCd=uuid)
    params = {
        'twt': "日本大統領選挙！私は"+ can.name + "さんに投票しました！"
    }
    now = datetime.datetime.now()
    today = now.strftime("%Y/%m/%d")
    lastpoll = request.COOKIES.get('lastpoll')
    if today == lastpoll:
        response = HttpResponse('本日は投票済みです')
        return response

    response = render(request, 'queen/voteaft.html',params)
    
    poll = now.strftime("%Y/%m/%d")
    response.set_cookie('lastpoll', poll, max_age=365*24*60*60)
    if request.method == 'POST':
        vote.totalCount += 1
        if request.POST['age'] != '':
            age = int(request.POST['age'])
            if age >= 18:
                vote.overEighteenCount += 1
            else:
                vote.underEighteenCount += 1
        if request.POST['sex'] != 'X':
            sex = request.POST['sex']
            if sex == '0':
                vote.maleCount += 1
            elif sex == '1':
                vote.femaleCount += 1
    vote.save()
    return response

def index(request):
    return render(request, 'queen/top.html')
