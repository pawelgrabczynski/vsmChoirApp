from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm



def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Nazwa użytkownika nie istnieje.')
        
        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request, 'Nazwa użytkownika LUB hasło nieprawidłowe.')

    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'Użytkownik został wylogowany.')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "Konto zostało utworzone.")

            login(request, user)
            return redirect('edit-account')
        
        else:
            messages.success(request, "Podczas rejestracji wystąpił błąd.")

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)

@login_required(login_url='login')
def profiles(request):
    # search_query = ''

    # if request.GET.get('search-query'):
    #     search_query = request.GET.get('search-query')
    
    # profiles = Profile.objects.filter(name__icontains=search_query)
    # profiles = Profile.objects.filter(Q(name__icontains=search_query) | Q(short_intro__icontains=search_query))
    # context = {'profiles':profiles, 'search_query':search_query}
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    news = profile.news_set.all()
    projects = profile.project_set.all()
  
    context = {'profile': profile, 'news':news, 'projects':projects}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        
        if form.is_valid():
            form.save()
            

            return redirect('account')

    context = {'form':form}
    return render(request, 'users/profile_form.html', context)