from link.models import Link


class LinkListMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(LinkListMixin, self).get_context_data(*args, **kwargs)
        context['link_list'] = Link.objects.all()
        return context
