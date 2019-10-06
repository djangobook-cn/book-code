from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView

from article.models import Blog
from website.mixins import FrontMixin


class HomepageView(FrontMixin, ListView):
    template_name = 'website/frontend/homepage.html'
    model = Blog
    paginate_by = 5
    context_object_name = 'article_list'


class DashboardOverviewView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('user-login')
    template_name = 'website/backend/overview.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardOverviewView, self).get_context_data(**kwargs)
        context['active_page'] = 'overview'
        return context
