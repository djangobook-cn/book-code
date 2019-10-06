from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from mood.models import Mood
from utils.mixins import AjaxResponseMixin
from website.mixins import FrontMixin


class MoodCreateView(LoginRequiredMixin, AjaxResponseMixin, CreateView):
    login_url = reverse_lazy('user-login')
    model = Mood
    fields = ['title', 'content', 'mood_type', 'image']
    success_url = reverse_lazy('mood-list')

    def get_context_data(self, **kwargs):
        context = super(MoodCreateView, self).get_context_data(**kwargs)
        context['active_page'] = 'mood-add'
        return context

    def get_template_names(self):
        if self.request.META['HTTP_USER_AGENT'].lower().find('mobile') > 0:
            return 'mood/mode_create_form_mobile.html'
        else:
            return 'mood/mood_create_form.html'


class MoodListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user-login')
    model = Mood
    context_object_name = 'mood_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MoodListView, self).get_context_data(**kwargs)
        context['active_page'] = 'mood-list'
        return context


class MoodUpdateView(LoginRequiredMixin, AjaxResponseMixin, UpdateView):
    login_url = reverse_lazy('user-login')
    model = Mood
    context_object_name = 'mood'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('mood-list')
    fields = ['title', 'content', 'mood_type', 'image']

    def get_context_data(self, **kwargs):
        context = super(MoodUpdateView, self).get_context_data(**kwargs)
        context['active_page'] = 'mood-update'
        return context


class MoodDeleteView(LoginRequiredMixin, AjaxResponseMixin, DeleteView):
    login_url = reverse_lazy('user-login')
    model = Mood
    success_url = reverse_lazy('mood-list')

    def post(self, request, *args, **kwargs):
        super(MoodDeleteView, self).post(request, *args, **kwargs)
        return JsonResponse({'state': 'success'})


class MoodTimeLineView(FrontMixin, ListView):
    model = Mood
    paginate_by = 20
    template_name = 'mood/mood_time_line.html'
    context_object_name = 'mood_list'
