from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, resolve_url
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Anken

from django.utils import timezone

from django.contrib import messages
from .forms import AnkenForm

class IndexView(generic.ListView):
    template_name = 'anken/index.html'
    context_object_name = 'latest_anken_list'

    def get_queryset(self):
        return Anken.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class AnkenCreate(generic.CreateView):
    model = Anken
    form_class = AnkenForm
    # 投稿に成功した時のURL
    success_url = reverse_lazy('anken:index')

    # 投稿に成功した時に実行される処理
    def get_success_url(self):
        messages.success(self.request, '記事を投稿しました。')
        return resolve_url('anken:index')