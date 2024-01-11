from django.shortcuts import render, redirect
from django.http import HttpResponse


def view_404(request, *args, **kwargs):
    return redirect('https://vsm.herokuapp.com/news')