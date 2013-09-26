from django.conf import settings
from django.utils.feedgenerator import Atom1Feed

SYNDICATION_FEED_TITLE = getattr(settings, 'SYNDICATION_FEED_TITLE', '')
SYNDICATION_FEED_LINK = getattr(settings, 'SYNDICATION_FEED_LINK', '/')
SYNDICATION_FEED_DESCRIPTION = getattr(settings, 'SYNDICATION_FEED_DESCRIPTION', '')
SYNDICATION_FEED_TYPE = getattr(settings, 'SYNDICATION_FEED_TYPE', Atom1Feed)
