from django.contrib.syndication.views import Feed

from .models import Post
from .settings import SYNDICATION_FEED_TITLE, SYNDICATION_FEED_LINK, SYNDICATION_FEED_DESCRIPTION


class LatestPostFeed(Feed):
    title = SYNDICATION_FEED_TITLE
    link = SYNDICATION_FEED_LINK
    description = SYNDICATION_FEED_DESCRIPTION

    def items(self):
        return Post.objects.recent()

    def item_title(self, item):
        return item.subject

    def item_description(self, item):
        return item.short
