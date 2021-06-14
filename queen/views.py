from django.views.generic import TemplateView,ListView# ❶
from django.db import models
import plotly.express as px
from django_pandas.io import read_frame
from django.shortcuts import render, redirect
from plotly.offline import plot as p
from queen.models import VOTE ,CANDIDATE ,AREA
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CandidateForm
import logging


# INOTSUME
def resultViews(request):
    vote_data = VOTE.objects.all().values('candidateCd__name', 'totalCount')
    df = read_frame(vote_data, fieldnames=['candidateCd__name','totalCount']).sort_values('totalCount')
    fig = px.bar(df, x='totalCount', y='candidateCd__name')
    fig.update_xaxes(title_text='得票数')
    fig.update_yaxes(title_text='')
    fig.update_layout(height=300, width=1300)
    plot = p(fig, output_type='div', include_plotlyjs=False)

    return render(request, 'queen/result.html', {'plot': plot})
        
# YAMASHITA
class CandidateList(ListView):
    model = CANDIDATE
    template_name = 'list.html'
    
class AreaList(ListView):
    model = AREA

class VoteList(ListView):
    model = VOTE
    
# def areacand(request ,area_n):
#     params = {
#         'data':[]
#     }
#     ['data'] = Candidate.objects.get(areaName=area_n)
#     return render(request , 'areacand.html',params)

def vote(request, uuid):
    result = uuid
    vote = VOTE.objects.get(candidateCd=uuid)
    if request.method == 'POST':
        vote.totalCount += 1
        vote.save()
    return redirect(to='/list')
    #return HttpResponse(result)
    
def create(request):
    if (request.method == 'POST'):
        obj = CANDIDATE()
        candidate = CandidateForm(request.POST ,instance=obj)
        # name = request.POST['name']
        # nameKN = request.POST['nameKN']
        # sex = request.POST['sex']
        # birthYMD = request.POST['birthYMD']
        # partyCd = request.POST['partyCd']
        # mail = request.POST['mail']
        # link = request.POST['link']
        # candidate = CANDIDATE(name=name,nameKN=nameKN,sex=sex,birthYMD=birthYMD,partyCd=partyCd,mail=mail,link=link)
        # candidate.save()
        if candidate.is_valid():
            logging.debug("検証に成功しました。データを保存します")
            candidate.save()
        else:
            logging.debug("検証に失敗したので、データを保存しません。検証に失敗した理由を次に表示します。")
            logging.debug(candidate.errors)
        return redirect(to='/list')
    params = {
        'form': CandidateForm(),
    }
    return render(request, 'queen/create.html',params)