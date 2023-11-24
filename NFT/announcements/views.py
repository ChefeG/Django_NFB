from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import ModelAnnouncements



class AnnouncementsListView(ListView):
    model = ModelAnnouncements
    template_name = 'blog-large.html'
    context_object_name = 'announcements_list_view'

class AnnouncementsDetailView(DetailView):
    model = ModelAnnouncements
    template_name = 'blog-detail.html'
    slug_field = 'url'
    context_object_name = 'announcements'
