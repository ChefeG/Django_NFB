from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import ModelNewsLine, ModelСover, ModelMatches, ModelTeams, ModelTopPlayer, ModelStatistics, \
    ModelTopMatches, ModelAnnouncements


def main(request):
    news = ModelNewsLine.objects.all()
    cover = ModelСover.objects.all()
    matches = ModelMatches.objects.all()
    team = ModelTeams.objects.all()
    top_player = ModelTopPlayer.objects.all()
    statistics = ModelStatistics.objects.all()
    top_matches = ModelTopMatches.objects.all()
    announcements = ModelAnnouncements.objects.all()
    return render(request, 'index.html', {'news_line': news, 'cover': cover, 'matches': matches, 'team': team,
                                          'top_player': top_player, 'statistics': statistics, 'top_matches':
                                              top_matches, 'announcements': announcements})

class TopPlayerDetailView(DetailView):
    model = ModelTopPlayer
    template_name = 'player-detail.html'
    slug_field = 'url'
    context_object_name = 'detail'

class CoverDetailView(DetailView):
    model = ModelСover
    template_name = 'fixture-detail.html'
    context_object_name = 'detail'

# class AnnouncementsDetailView(DetailView):
#     model = ModelAnnouncements
#     template_name = 'blog-detail.html'
#     slug_field = 'url'
#
#
# class AnnouncementsListView(ListView):
#     model = ModelAnnouncements
#     template_name = 'blog-large.html'
#     context_object_name = 'announcements_list_view'


# class NewsLineListView(ListView):
#     model = ModelNewsLine
#     template_name = 'include/NewsLine.html'
#     context_object_name = 'list'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         return context



def accounts(request):
    render(request, 'openid/login.html')
