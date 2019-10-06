from mood.models import Mood


class LeastMoodMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(LeastMoodMixin, self).get_context_data(*args, **kwargs)
        last_mood = Mood.objects.last()
        if last_mood:
            context['mood'] = Mood.objects.last()
        return context
