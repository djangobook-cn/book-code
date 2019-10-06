from django.contrib import admin
from mood.models import Mood


class MoodAdmin(admin.ModelAdmin):
    search_fields = ('title', 'mood_type', 'content', 'create_time')
    list_display = ('title', 'mood_type', 'content', 'create_time')


admin.site.register(Mood, MoodAdmin)
