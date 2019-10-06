from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=16)
    title = models.CharField(max_length=32, blank=True, null=True)
    url = models.URLField()
    show_order = models.SmallIntegerField(default=1)

    class Meta:
        ordering = ['show_order']

    def __str__(self):
        return self.name
