from navbar.mixins import NavBarMixin
from mood.mixins import LeastMoodMixin
from link.mixins import LinkListMixin
from article.mixins import CategoryMixin


class FrontMixin(NavBarMixin, LeastMoodMixin, LinkListMixin, CategoryMixin):
    def get_context_data(self, *args, **kwargs):
        return super(FrontMixin, self).get_context_data(*args, **kwargs)
