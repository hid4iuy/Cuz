from django.views.generic import TemplateView,ListView,DetailView
from django.db import models
from django_pandas.io import read_frame
from django.shortcuts import render, redirect
from queen.models import VOTE ,CANDIDATE ,AREA, IMAGE, COMMENTS
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CandidateForm,CommentForm
from django.db.models import Max
import logging,datetime
from django.http.response import JsonResponse

def resultViews(request):
    labels = []
    data = []
    dict = []
    comments = COMMENTS.objects.all().order_by('posted_at').reverse()
    queryset = VOTE.objects.all().order_by('totalCount').reverse()
    for vote in queryset:
        labels.append(vote.candidateCd.name)
        data.append(vote.totalCount)
        dict.append(vote.candidateCd.name)
    for i in range(len(queryset)):
        vote=queryset[i]
        nowrank = i+1
        lastrank = vote.lastrank
        if nowrank > lastrank:
            before = 'down'
        elif nowrank < lastrank:
            before = 'up'
        else :    
            before = 'keep'
        dict[i] = {'name' : vote.candidateCd.name,'nameKN' : vote.candidateCd.nameKN,'icon' : vote.candidateCd.icon, 'totalCount' : vote.totalCount , 'nowrank' : nowrank ,'lastrank' : lastrank, 'before' : before}
    # print(dict)
    if request.method == "POST":
    # データベースに投稿されたコメントを保存
        post = COMMENTS()
        post.cmt_user = request.POST["comment_user"]
        post.cmt_text = request.POST["comment_text"]
        post.cmt_id = COMMENTS.objects.count() + 1
        post.save()

    return render(request, 'queen/result.html', {
        'labels': labels,
        'data': data,
        'obj': dict,
        'comments': comments,
        'form':CommentForm(),
    })
        
class detailViews(DetailView):
    model = CANDIDATE
    template_name = 'queen/detail.html'
       
    def get_object(self):
        return CANDIDATE.objects.get(nameKN=self.kwargs['nameKN'])

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
        response = render(request, 'queen/votefin.html', params)
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

def lastrank(request):
    
    queryset = VOTE.objects.all().order_by('totalCount').reverse()
    for i in range(len(queryset)):
        vote=queryset[i]
        vote.lastrank = i+1
        vote.save()
        
    return render(request, 'queen/top.html')
    
def like(request,cmt_id):
    comment = COMMENTS.objects.get(cmt_id=cmt_id)
    comment.cmt_good += 1
    comment.save()
    return redirect(to='result')

def bad(request,cmt_id):
    comment = COMMENTS.objects.get(cmt_id=cmt_id)
    comment.cmt_bad += 1
    comment.save() 
    return redirect(to='result')