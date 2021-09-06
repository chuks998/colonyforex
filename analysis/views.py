from django.db import models
from django.http import request
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .models import Analysis
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

def post_like(request, pk):
    post = get_object_or_404(Analysis, id=request.POST.get('like'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('analysis_detail', args=[str(pk)]))

def post_dislike(request, pk):
    post = get_object_or_404(Analysis, id=request.POST.get('dislike'))
    if post.dis_likes.filter(id=request.user.id).exists():
        post.dis_likes.remove(request.user)
    else:
        post.dis_likes.add(request.user)
    return HttpResponseRedirect(reverse('analysis_detail', args=[str(pk)]))



class AnlysisListView(ListView):
    model = Analysis
    template_name = 'analysis.html'
    context_object_name = 'analysis'
    ordering = ['-date_created']
    paginate_by = 3


class UserPostListView(ListView):
    model = Analysis
    template_name = 'user-analysis.html'
    context_object_name = 'user_post'
    paginate_by = 15

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Analysis.objects.filter(author=user).order_by('-date_created')


class AnalysisDetail(DetailView):
    model = Analysis
    template_name = 'analysis_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        likes_connected = get_object_or_404(Analysis, id=self.kwargs['pk'])
        dis_likes_connected = get_object_or_404(Analysis, id=self.kwargs['pk'])
        dis_liked = False
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['total_likes'] = likes_connected.total_likes()
        data['post_is_liked'] =liked

        if dis_likes_connected.dis_likes.filter(id=self.request.user.id).exists():
            dis_liked = True
            data['total_dis_likes'] = dis_likes_connected.total_dis_likes()
            data['post_is_dis_liked'] = dis_liked
        return data



class AnalysisCreateView(LoginRequiredMixin,CreateView):
    model = Analysis
    template_name = 'create_post.html'
    fields = ['image', 'post_title', 'post_subject', 'post_body']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AnalysisCreateView, self).form_valid(form)

class AnalysisUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Analysis
    fields = ['image', 'post_title', 'post_subject', 'post_body']
    template_name = 'analysis_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AnalysisUpdateView, self).form_valid(form)


    def test_func(self):
        analysis = self.get_object()
        if self.request.user == analysis.author:
            return True
        else:
            return False

class AnalysisDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Analysis
    success_url = '/dashboard'
    template_name='analysis_confirm_delete.html'

    
    def test_func(self):
        analysis = self.get_object()
        if self.request.user == analysis.author:
            return True
        else:
            return False