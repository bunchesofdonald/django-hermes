from django.conf import settings

SYNDICATION_FEED_TITLE = getattr(settings, 'SYNDICATION_FEED_TITLE', '')
SYNDICATION_FEED_LINK = getattr(settings, 'SYNDICATION_FEED_LINK', '/')
SYNDICATION_FEED_DESCRIPTION = getattr(settings, 'SYNDICATION_FEED_DESCRIPTION', '')
