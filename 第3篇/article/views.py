import datetime
import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, Http404
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, FormView, DetailView
from django.core.files.storage import default_storage

from article.models import Category, Blog, PurePage
from utils.mixins import AjaxResponseMixin
from website.mixins import FrontMixin

from uuid import uuid4


class CategoryCreateView(LoginRequiredMixin, AjaxResponseMixin, CreateView):
    login_url = reverse_lazy('user-login')
    model = Category
    fields = ['name']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('category-list')

    def get_context_data(self, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['active_page'] = 'category-add'
        return context


class CategoryListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user-login')
    model = Category
    context_object_name = 'category_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['active_page'] = 'category-list'
        return context


class CategoryArticleListView(FrontMixin, ListView):
    template_name = 'website/frontend/homepage.html'
    model = Blog
    paginate_by = 5
    context_object_name = 'article_list'

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Blog.objects.filter(category=category)


class CategoryUpdateView(LoginRequiredMixin, AjaxResponseMixin, UpdateView):
    login_url = reverse_lazy('user-login')
    model = Category
    context_object_name = 'category'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('category-list')
    fields = ['name']

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['active_page'] = 'category-update'
        return context


class CategoryDeleteView(LoginRequiredMixin, AjaxResponseMixin, DeleteView):
    login_url = reverse_lazy('user-login')
    model = Category
    success_url = reverse_lazy('category-list')

    def post(self, request, *args, **kwargs):
        super(CategoryDeleteView, self).post(request, *args, **kwargs)
        return JsonResponse({'state': 'success'})


class BlogCreateView(LoginRequiredMixin, AjaxResponseMixin, CreateView):
    login_url = reverse_lazy('user-login')
    model = Blog
    template_name_suffix = '_create_form'
    fields = ['title', 'content', 'summary', 'category']
    success_url = reverse_lazy('blog-list-backend')

    def get_context_data(self, **kwargs):
        context = super(BlogCreateView, self).get_context_data(**kwargs)
        context['active_page'] = 'blog-add'
        context['category_list'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.show_times = 0
        return super(BlogCreateView, self).form_valid(form)


class BackendBlogListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user-login')
    context_object_name = 'essay_list'
    template_name = 'article/blog_list.html'
    model = Blog

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BackendBlogListView, self).get_context_data(**kwargs)
        context['active_page'] = 'blog-list'
        return context


class BlogUpdateView(LoginRequiredMixin, AjaxResponseMixin, UpdateView):
    login_url = reverse_lazy('user-login')
    model = Blog
    context_object_name = 'blog'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('blog-list-personal')
    fields = ['title', 'category', 'summary', 'content']

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        blog = Blog.objects.get(pk=kwargs.get('pk'))
        if blog.author != user:
            raise Http404
        else:
            return super(BlogUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogUpdateView, self).get_context_data(**kwargs)
        context['active_page'] = 'blog-update'
        context['category_list'] = Category.objects.all()
        return context


class BlogDeleteView(LoginRequiredMixin, AjaxResponseMixin, DeleteView):
    login_url = reverse_lazy('user-login')
    model = Blog
    success_url = reverse_lazy('blog-list-personal')

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        blog = Blog.objects.get(pk=kwargs.get('pk'))
        if blog.author != user:
            raise Http404
        else:
            return super(BlogDeleteView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        super(BlogDeleteView, self).post(request, *args, **kwargs)
        return JsonResponse({'state': 'success'})


class BlogDetailView(FrontMixin, DetailView):
    model = Blog
    context_object_name = 'article'
    template_name = 'article/article_detail.html'

    def get_object(self, queryset=None):
        obj = super(BlogDetailView, self).get_object()
        obj.show_times += 1
        obj.save()
        return obj


class PurePageCreateView(LoginRequiredMixin, AjaxResponseMixin, CreateView):
    login_url = reverse_lazy('user-login')
    model = PurePage
    template_name_suffix = '_create_form'
    fields = ['title', 'content']
    success_url = reverse_lazy('pure-page-list')

    def get_context_data(self, **kwargs):
        context = super(PurePageCreateView, self).get_context_data(**kwargs)
        context['active_page'] = 'pure-page-add'
        return context


class PurePageUpdateView(LoginRequiredMixin, AjaxResponseMixin, UpdateView):
    login_url = reverse_lazy('user-login')
    model = PurePage
    template_name_suffix = '_update_form'
    context_object_name = 'page'
    fields = ['title', 'content']
    success_url = reverse_lazy('pure-page-list')

    def get_context_data(self, **kwargs):
        context = super(PurePageUpdateView, self).get_context_data(**kwargs)
        context['active_page'] = 'pure-page-update'
        return context


class PurePageDeleteView(LoginRequiredMixin, AjaxResponseMixin, DeleteView):
    login_url = reverse_lazy('user-login')
    model = PurePage
    success_url = reverse_lazy('pure-page-list')

    def post(self, request, *args, **kwargs):
        super(PurePageDeleteView, self).post(request, *args, **kwargs)
        return JsonResponse({'state': 'success'})


class PurePageListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user-login')
    model = PurePage
    context_object_name = 'page_list'
    template_name = 'article/purepage_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PurePageListView, self).get_context_data(**kwargs)
        context['active_page'] = 'pure-page-list'
        return context


@csrf_exempt
def image_upload_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 1, 'message': 'method error'})
    else:
        img = request.FILES.get('imgFile', None)
        if img:
            storage = default_storage
            today = datetime.datetime.today()
            random_file_name = uuid4()
            file_suffix = img.name.split('.')[-1]
            file_path = '%d/%d/%d/%s.%s' % (today.year, today.month, today.day, random_file_name, file_suffix)
            path = os.path.join(settings.MEDIA_PATH, file_path)
            storage.save(path, img)
            return JsonResponse({"error": 0, "url": settings.MEDIA_URL + file_path})
