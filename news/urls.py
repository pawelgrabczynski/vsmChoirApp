from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name="news"),
    path('single-news/<str:pk>/', views.singleNews, name="single-news"),

    path('create-news/', views.createNews, name="create-news"),

    path('update-news/<str:pk>/', views.updateNews, name="update-news"),

    path('delete-news/<str:pk>/', views.deleteNews, name="delete-news"),
]


