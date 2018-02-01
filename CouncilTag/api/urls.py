from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from CouncilTag.api import views

urlpatterns = [
    url(r'^agendas/$',views.list_agendas),
    url(r'^tags/$', views.list_tags),
    url(r'^login/$',views.login_user),
    url(r'^signup/$', views.signup_user),
    url(r'^tag/(?P<tag_name>[a-zA-Z _]+)/agenda/items', views.get_agendaitem_by_tag),
    url(r'^user/add/tag/$', views.add_tag_to_user),
]

urlpatterns = format_suffix_patterns(urlpatterns)