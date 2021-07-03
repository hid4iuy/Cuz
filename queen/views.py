from django.views.generic import TemplateView,ListView,DetailView
from django.db import models
import plotly.express as px
from django_pandas.io import read_frame
from django.shortcuts import render, redirect
from plotly.offline import plot as p
from queen.models import VOTE ,CANDIDATE ,AREA, IMAGE
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CandidateForm
import logging


# INOTSUME
class topViews(ListView):
    model = CANDIDATE
    template_name = 'queen/top.html'
    
    def get_queryset(self):
        return CANDIDATE.objects.all()

def resultViews(request):
    labels = []
    data = []

    queryset = VOTE.objects.all().order_by('totalCount').reverse()
    for vote in queryset:
        labels.append(vote.candidateCd.name)
        data.append(vote.totalCount)

    return render(request, 'queen/result.html', {
        'labels': labels,
        'data': data,
    })
        
class detailViews(DetailView):
    model = CANDIDATE
    template_name = 'queen/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        candidate = context.get("object")
        context.update({
            'image': IMAGE.objects.filter(candidateCd=candidate.uuid),
        })
        return context
        
    def get_object(self):
        return CANDIDATE.objects.get(nameKN=self.kwargs['nameKN'])