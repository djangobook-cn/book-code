from navbar.models import NavItem


class NavBarMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(NavBarMixin, self).get_context_data(*args, **kwargs)
        context['nav_item_list'] = NavItem.objects.all()
        return context