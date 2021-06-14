from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Politic ,Vote
from django.views.generic import ListView
from django.views.generic import DetailView

class PoliticList(ListView):
    model = Politic
    # template_name = 'politic_list'
    # context_object_name = 'politic_list'
    # model = Politic
   
    # def get_context_data(self, **kwargs):
    #   context = super(PoliticListView, self).get_context_data(**kwargs)
    #   context.update({
    #         'vote_list': Vote.objects.all(),
    #     })
    #   return context
    # def get_queryset(self):
    #   return Politic.objects.all()
       
class PoliticDetail(DetailView):
    model = Politic

def index(request):
    params = {
        'title':'総選挙に参加しますか？',
        'message':'候補者一覧',
    }
    return render(request, 'hello/index.html',params)

def vote(request, politic_id):
    vote = Vote.objects.get(id=politic_id)
    if request.method == 'POST':
        vote.voteSum += 1
        vote.save()
        params = {
        'id':politic_id
        }
    return render(request, 'hello/politic_list.html')