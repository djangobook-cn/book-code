from django.db import models

MOOD_TYPE_CHOICE = (
    ('T', 'Text'),
    ('I', 'Image'),
    ('B', 'block_quote')
)


class Mood(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    mood_type = models.CharField(max_length=1, choices=MOOD_TYPE_CHOICE, default='T')
    image = models.ImageField(upload_to='./image/mood/%Y/%m/%d/', null=True, blank=True)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-create_time']
