"""ColonyForex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.models import Group
from django.urls import path, include
from django.views.generic.edit import UpdateView
from analysis.views import AnlysisListView, UserPostListView, AnalysisDetail, AnalysisCreateView, AnalysisDeleteView, AnalysisUpdateView, post_like, post_dislike 
from users.views import DashBoard, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    # FOR ANALYSIS
    path('analysis/', AnlysisListView.as_view(), name='analysis'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('analysis/<int:pk>/', AnalysisDetail.as_view(), name='analysis_detail'),
    path('analysis_like/<int:pk>',post_like, name='analysis-like'),
    path('analysis_dislike/<int:pk>',post_dislike, name='analysis-dislike'),
    path('analysis/<int:pk>/update/', AnalysisUpdateView.as_view(), name='analysis-update'),
    path('analysis/<int:pk>/delete/', AnalysisDeleteView.as_view(), name='analysis-delete'),
    path('dashboard/', DashBoard.as_view(), name='profile'),
    path('dashboard/create', AnalysisCreateView.as_view(), name='new analysis'),
    # FOR AUTHENTECATION
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




admin.site.site_header = 'COLONY FOREX ADMIN'
admin.site.site_title = 'COLONY'
admin.site.index_title = 'COLONY FOREX ADMIN CONTROL'

admin.site.unregister(Group)