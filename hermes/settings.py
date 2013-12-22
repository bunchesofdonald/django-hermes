from django.conf import settings
from django.utils.feedgenerator import Atom1Feed

import renderers

SYNDICATION_FEED_TITLE = getattr(settings, 'SYNDICATION_FEED_TITLE', '')
SYNDICATION_FEED_LINK = getattr(settings, 'SYNDICATION_FEED_LINK', '/')
SYNDICATION_FEED_DESCRIPTION = getattr(settings, 'SYNDICATION_FEED_DESCRIPTION', '')
SYNDICATION_FEED_TYPE = getattr(settings, 'SYNDICATION_FEED_TYPE', Atom1Feed)

try:
    import markdown
    MARKUP_RENDERER = getattr(settings, 'MARKUP_RENDERER', renderers.markdown)
except:
    MARKUP_RENDERER = getattr(settings, 'MARKUP_RENDERER', None)
