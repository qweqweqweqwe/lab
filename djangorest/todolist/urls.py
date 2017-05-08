from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TaskCreateView, TaskDetailsView

urlpatterns = {
    url(r'^todolists/$', TaskCreateView.as_view(), name="create"),
    url(r'^todolists/(?P<pk>[0-9]+)/$', TaskDetailsView.as_view(), name="detail"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
