from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('announcements/', include('announcements.urls'), name='announcements'),
    path('<int:pk>', views.CoverDetailView.as_view(), name='cover_detail'),
    path('<slug:slug>/', views.TopPlayerDetailView.as_view(), name='detail'),
]

from django.contrib.flatpages import views
urlpatterns += [
    path('about/', views.flatpage, {'url': '/about/'}, name='about'),
    path('contact/', views.flatpage, {'url': '/contact/'}, name='contact'),
    path('team/', views.flatpage, {'url': '/team/'}, name='team'),
    path('faq/', views.flatpage, {'url': '/faq/'}, name='faq'),
    path('blog/', views.flatpage, {'url': '/blog/'}, name='blog'),
]
