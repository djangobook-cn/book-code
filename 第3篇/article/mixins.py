from article.models import Category
from django.db.models import Count


class CategoryMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(CategoryMixin, self).get_context_data(*args, **kwargs)
        context['category_list'] = Category.objects.annotate(blog_number=Count('blog')).order_by('name')
        return context
