from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from link.models import Link
from utils.mixins import AjaxResponseMixin


class LinkCreateView(LoginRequiredMixin, AjaxResponseMixin, CreateView):
    login_url = reverse_lazy('user-login')
    model = Link
    fields = ['name', 'title', 'url', 'show_order']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('link-list')

    def get_context_data(self, **kwargs):
        context = super(LinkCreateView, self).get_context_data(**kwargs)
        context['active_page'] = 'link-add'
        return context


class LinkListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user-login')
    model = Link
    context_object_name = 'link_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LinkListView, self).get_context_data(**kwargs)
        context['active_page'] = 'link-list'
        return context


class LinkUpdateView(LoginRequiredMixin, AjaxResponseMixin, UpdateView):
    login_url = reverse_lazy('user-login')
    model = Link
    context_object_name = 'link'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('link-list')
    fields = ['name', 'title', 'url', 'show_order']

    def get_context_data(self, **kwargs):
        context = super(LinkUpdateView, self).get_context_data(**kwargs)
        context['active_page'] = 'link-update'
        return context


class LinkDeleteView(LoginRequiredMixin, AjaxResponseMixin, DeleteView):
    login_url = reverse_lazy('user-login')
    model = Link
    success_url = reverse_lazy('link-list')

    def post(self, request, *args, **kwargs):
        super(LinkDeleteView, self).post(request, *args, **kwargs)
        return JsonResponse({'state': 'success'})
