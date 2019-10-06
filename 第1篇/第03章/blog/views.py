from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView
from django.core.paginator import Paginator  # 引入分页组件
from django.http import JsonResponse
from blog.models import Blog


# 实现方式1，基于方法的视图

def blog_list(request):
    page = request.GET.get('page', 1)  # 第几页，默认第1页
    page_size = request.GET.get('page_size', 20)  # 默认每页20条

    blog_qs = Blog.objects.all()
    paginator = Paginator(blog_qs, page_size)

    current_page = paginator.get_page(page)
    blogs = current_page.object_list

    context = {
        'blog_list': [
            {
                'id': blog.id,
                'title': blog.title,
            } for blog in blogs
        ],
        'paginator': {
            'total_count': paginator.count,
            'num_pages': paginator.num_pages,
            'page_size': paginator.per_page,
            'page_number': current_page.number,
        }
    }
    return JsonResponse(context)


def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {
        'blog': {
            'id': blog.id,
            'title': blog.title,
            'content': blog.content,
            'author': {
                'id': blog.author.id,
                'username': blog.author.username,
            }
        }
    }
    return JsonResponse(context)


# 实现方式2，基于类的视图

class BlogListView(BaseListView):
    model = Blog
    paginate_by = 20  # 每页条数

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size') or self.paginate_by

    def render_to_response(self, context):
        paginator = context['paginator']
        current_page = context['page_obj']
        blogs = current_page.object_list

        data = {
            'blog_list': [
                {
                    'id': blog.id,
                    'title': blog.title,
                } for blog in blogs
            ],
            'paginator': {
                'total_count': paginator.count,
                'num_pages': paginator.num_pages,
                'page_size': paginator.per_page,
                'page_number': current_page.number,
            }
        }
        return JsonResponse(data)


class BlogDetailView(BaseDetailView):
    model = Blog

    def render_to_response(self, context):
        blog = context['object']
        data = {
            'blog': {
                'id': blog.id,
                'title': blog.title,
                'content': blog.content,
                'author': {
                    'id': blog.author.id,
                    'username': blog.author.username,
                }
            }
        }
        return JsonResponse(data)
