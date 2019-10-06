from django.db import models


class Blog(models.Model):
    title = models.CharField('标题', max_length=200)
    author = models.ForeignKey(
        'auth.User', on_delete=models.SET_NULL,
        null=True, verbose_name='作者'
    )
    content = models.TextField('内容')

    def __str__(self):
        return self.title

    def author_name(self):
        return '%s' % self.author.first_name
    author_name.short_description = '作者名称'
