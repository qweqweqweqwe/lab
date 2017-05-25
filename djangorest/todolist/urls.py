from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import TasklistCreateView, TasklistDetailsView, TaskDetailsView, CreateUserView, TaskCreateView

urlpatterns = {
    url(r'^todolists/$', TasklistCreateView.as_view(), name="lists"),
    url(r'^todolists/(?P<pk>[0-9]+)/$', TasklistDetailsView.as_view(), name="list-detail"),
    url(r'^todolists/(?P<list_id>[0-9]+)/tasks', TaskCreateView.as_view(), name="tasks"),
    url(r'^todolists/(?P<list_id>[0-9]+)/tasks/(?P<pk>[0-9]+)', TaskDetailsView.as_view(), name="task-detail"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^register/$', CreateUserView.as_view(), name='user')
}

urlpatterns = format_suffix_patterns(urlpatterns)
