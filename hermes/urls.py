from django.conf.urls import patterns, url

from .views import ArchivePostListView, PostListView, PostDetail

urlpatterns = patterns('',
    url(
        regex=r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[\w-]+)/$',
        view=PostDetail.as_view(),
        name='hermes_post_detail',
    ),

    url(
        regex=r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$',
        view=ArchivePostListView.as_view(),
        name='hermes_archive_year_month_day',
    ),

    url(
        regex=r'^(?P<year>\d+)/(?P<month>\d+)/$',
        view=ArchivePostListView.as_view(),
        name='hermes_archive_year_month',
    ),

    url(
        regex=r'^(?P<year>\d+)$',
        view=ArchivePostListView.as_view(),
        name='hermes_archive_year',
    ),

    url(
        regex=r'^$',
        view=PostListView.as_view(),
        name='hermes_post_list',
    ),
)
