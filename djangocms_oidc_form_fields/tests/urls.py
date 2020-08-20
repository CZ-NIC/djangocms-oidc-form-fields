from aldryn_forms.urls import urlpatterns as aldryn_forms_urlpatterns
from cms.views import details
from django.conf.urls import url

urlpatterns = []
urlpatterns.extend(aldryn_forms_urlpatterns)
urlpatterns.append(url(r'^(?P<slug>[0-9A-Za-z-_.//]+)/$', details, name='pages-details-by-slug'))
