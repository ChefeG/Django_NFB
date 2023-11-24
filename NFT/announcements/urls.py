from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnnouncementsListView.as_view(), name='announcements_list_view'),
    path('<slug:slug>/', views.AnnouncementsDetailView.as_view(), name='announcements_detail'),
]
