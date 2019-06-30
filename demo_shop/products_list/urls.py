from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from .views import *


app_name = 'product_list'
urlpatterns = [
    re_path(r'^$', CatalogView.as_view(), name='productlist'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', CatalogView.as_view(), name='Catalog'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', ProductDetailView.as_view(), name='ProductDetail'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)