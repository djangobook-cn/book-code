from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=128, verbose_name='书籍名称')
    author = models.CharField(max_length=64, verbose_name='作者')
    price = models.FloatField(default=0.0, verbose_name='定价')
    publish_date = models.DateField(null=True, blank=True, verbose_name='出版日期')
    category = models.CharField(max_length=32, default='未分类', verbose_name='书籍分类')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='添加日期')

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=128, verbose_name='图片名称')
    description = models.TextField(default='', verbose_name='图片描述')
    img = models.ImageField(upload_to='image/%Y/%m/%d/', verbose_name='图片')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='所属书籍')

    def __str__(self):
        return self.name
