
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from project.views import Index, UserList, UserDetail, CurrentUserDetail

admin.autodiscover()

urlpatterns = patterns('',
    (r'^api/', include(patterns('',
        url(r'^user$', CurrentUserDetail.as_view(), name='user'),
        url(r'^users$', UserList.as_view(), name='user-list'),
        url(r'^users/(?P<pk>\d+)$', UserDetail.as_view(), name='user-detail'),
    ))),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
    url(r'^$', Index.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
)