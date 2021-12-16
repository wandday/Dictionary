from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name= 'index'),
    path('word_search', views.word_search, name= 'word_search'),
    
]