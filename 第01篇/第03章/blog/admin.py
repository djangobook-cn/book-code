from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # list_display用于设置列表页面要显示的不同字段
    list_display = ['title', 'author']

    # 参与搜索的字段列表
    search_fields = [
        'title', 'content', 'author__username',
        'author__first_name', 'author__last_name'
    ]

    readonly_fields = ['author']

    def save_model(self, request, obj, form, change):
        if not change:  # 如果不是修改，也就是“新建”的时候
            obj.author = request.user
        super(BlogAdmin, self).save_model(request, obj, form, change)
