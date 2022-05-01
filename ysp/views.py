import logging

import self

from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.views import generic

from .forms import InquiryForm

from django.contrib import messages

from .models import Ysp

from django.http import HttpResponse

from django.core.mail import BadHeaderError, send_mail

from django.conf import settings


logger = logging.getLogger(__name__)


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'


class ActionView(generic.TemplateView):
    template_name = 'action.html'


class NewsView(generic.TemplateView):
    model = Ysp
    template_name = 'news-ysp.html'


class IndexView(generic.TemplateView):
    template_name = "index.html"


class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('ysp:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('inquiry sent by{}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


class InterviewView(generic.TemplateView):
    template_name = "interview.html"


class OldnewsView(generic.ListView):
    model = Ysp
    template_name = "oldnews.html"

    def get_queryset(self):
        yspes = Ysp.objects.filter(user=self.request.user).order_by('-created_at')
        return yspes


class NewsDetailView(generic.DetailView):
    model = Ysp
    slug_field = "subject"
    slug_url_kwarg = "subject"
    template_name = 'news_detail.html'


class CleanView(generic.TemplateView):
    template_name = "others/clean.html"


class SdgsView(generic.TemplateView):
    template_name = "others/sdgs.html"


class AchieveView(generic.TemplateView):
    template_name = "others/achieve.html"


class OmoteView(generic.TemplateView):
    template_name = "others/omote.html"


class MemberView(generic.TemplateView):
    template_name = "others/member.html"


class OutsideView(generic.TemplateView):
    template_name = "others/outside.html"

class News1View(generic.TemplateView):
    template_name = "news2022/news1.html"
