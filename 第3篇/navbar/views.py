from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from navbar.models import NavItem
from utils.mixins import AjaxResponseMixin, AtomicMixin


class NavItemCreateView(LoginRequiredMixin, AtomicMixin, AjaxResponseMixin, CreateView):
    login_url = reverse_lazy('user-login')
    model = NavItem
    fields = ['title', 'show_order', 'url']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('navbar-list')

    def get_context_data(self, **kwargs):
        context = super(NavItemCreateView, self).get_context_data(**kwargs)
        context['active_page'] = 'navbar-add'
        return context


class NavItemListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user-login')
    model = NavItem
    context_object_name = 'navbar_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NavItemListView, self).get_context_data(**kwargs)
        context['active_page'] = 'navbar-list'
        return context


class NavItemUpdateView(LoginRequiredMixin, AtomicMixin, AjaxResponseMixin, UpdateView):
    login_url = reverse_lazy('user-login')
    model = NavItem
    context_object_name = 'navitem'
    template_name_suffix = '_update_form'
    reverse_lazy('navbar-list')
    fields = ['title', 'show_order', 'url']

    def get_context_data(self, **kwargs):
        context = super(NavItemUpdateView, self).get_context_data(**kwargs)
        context['active_page'] = 'navbar-update'
        return context


class NavItemDeleteView(LoginRequiredMixin, AtomicMixin, AjaxResponseMixin, DeleteView):
    login_url = reverse_lazy('user-login')
    model = NavItem
    success_url = reverse_lazy('navbar-list')

    def delete(self, request, *args, **kwargs):
        super(NavItemDeleteView, self).delete(request, *args, **kwargs)
        return JsonResponse({'state': 'success', 'msg': ''})
