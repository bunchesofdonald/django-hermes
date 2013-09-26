from django.contrib.syndication.views import Feed

from .models import Post
from .settings import (
    SYNDICATION_FEED_TITLE, SYNDICATION_FEED_LINK,
    SYNDICATION_FEED_DESCRIPTION, SYNDICATION_FEED_TYPE
)


class LatestPostFeed(Feed):
    title = SYNDICATION_FEED_TITLE
    link = SYNDICATION_FEED_LINK
    description = SYNDICATION_FEED_DESCRIPTION
    feed_type = SYNDICATION_FEED_TYPE

    def items(self):
        return Post.objects.recent()

    def item_title(self, item):
        return item.subject

    def item_description(self, item):
        return item.short

    def item_pubdate(self, item):
        return item.created_on

    def item_updateddate(self, item):
        return item.modified_on

    def item_categories(self, item):
        return [category.title for category in item.category.hierarchy()]

    def item_author_name(self, item):
        return "{first_name} {last_name}".format(
            first_name=item.author.first_name,
            last_name=item.author.last_name,
        )

    def item_author_email(self, item):
        return item.author.email
