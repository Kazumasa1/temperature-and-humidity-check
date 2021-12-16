import logging

from django.views import generic
# from .forms import InquiryForm
# from django.urls import reverse_lazy
# from django.contrib import messages
# from django.shortcuts import render

# Create your views here.

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"