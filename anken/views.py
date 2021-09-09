from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Anken

from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'anken/index.html'
    context_object_name = 'latest_anken_list'

    def get_queryset(self):
        return Anken.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]