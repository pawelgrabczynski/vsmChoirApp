from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import  News
from .forms import NewsForm

# Create your views here.
def news(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'news/news.html', context)

def projectss(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def singleNews(request, pk):
    newsObj = News.objects.get(id=pk)
    
    context = { 'newsObj': newsObj}
   
    return render(request, 'news/single-news.html', context )

@login_required(login_url="login")
def createNews(request):
    profile = request.user.profile
    form = NewsForm()

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            newsObj = form.save(commit=False)
            newsObj.owner = profile
            newsObj.save()
            return redirect('news')

    context = {'form': form}
    return render(request, "news/news_form.html", context)   

@login_required(login_url="login")
def updateNews(request, pk):
    profile = request.user.profile
    news = profile.news_set.get(id=pk)
    form = NewsForm(instance=news)

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance = news)
        if form.is_valid():
            form.save()
            return redirect('news')

    context = {'form': form}
    return render(request, "news/news_form.html", context)  

@login_required(login_url="login")
def deleteNews(request, pk):
    profile = request.user.profile
    news = profile.news_set.get(id=pk)
    if request.method == "POST":
        news.delete()
        return redirect("news")
    context = {'object': news}
    return render(request, 'news/delete_news.html', context) 