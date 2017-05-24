from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TasklistCreateView, TasklistDetailsView, TaskCreateView, TaskDetailsView, UserViewSet, CreateUserView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


urlpatterns = {
    # url(r'^', include(router.urls)),
    url(r'^todolists/$', TasklistCreateView.as_view(), name="lists"),
    url(r'^todolists/(?P<pk>[0-9]+)/$', TasklistDetailsView.as_view(), name="list-detail"),
    url(r'^todolists/(?P<list_id>[0-9]+)/tasks', TaskCreateView.as_view(), name="tasks"),
    url(r'^todolists/(?P<list_id>[0-9]+)/tasks/(?P<pk>[0-9]+)', TaskDetailsView.as_view(), name="task-detail"),
    url(r'^register/$', CreateUserView.as_view(), name='user')
}



urlpatterns = format_suffix_patterns(urlpatterns)