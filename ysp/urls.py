
from django.urls import path

from . import views

app_name = 'ysp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('action/', views.ActionView.as_view(), name="action"),
    path('news/', views.NewsView.as_view(), name="news"),
    path('interview/', views.InterviewView.as_view(), name='interview'),
    path('oldnews/', views.OldnewsView.as_view(), name='oldnews'),
    path('news_detail/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('clean/', views.CleanView.as_view(), name='clean'),
    path('sdgs/', views.SdgsView.as_view(), name='sdgs'),
    path('achieve/', views.AchieveView.as_view(), name='achieve'),
    path('omote/', views.OmoteView.as_view(), name='omote'),
    path('member/', views.MemberView.as_view(), name='member'),
    path('outside/', views.OutsideView.as_view(), name='outside'),
]
