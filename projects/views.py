from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Project
from .forms import ProjectForm, ReviewForm

@login_required(login_url="login")
def projects(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    #projects= Project.objects.filter(title__icontains=search_query)
    projects = Project.objects.filter(Q(title__icontains=search_query) | Q(composer__icontains=search_query))
    context = {'projects':projects, 'search_query':search_query}
    print("search: ", search_query)
    # projects = Project.objects.all()
    # context = {'projects': projects}

    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    profile = request.user.profile
    print(profile.voice)
    form = ReviewForm()
    
    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        #Update project votecounter
        messages.success(request, 'Your review was successfully submitted')
        return redirect('project', pk=projectObj.id)

    return render(request, 'projects/single-project.html', {'projectObj': projectObj, 'profile':profile, 'form':form} )

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)   

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)  

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context) 

