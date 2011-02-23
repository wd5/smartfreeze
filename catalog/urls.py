from django.conf.urls.defaults import *

urlpatterns = patterns('',
                      url(r'^$', 'catalog.views.index', name="main-page"),
                      url(r'^cats/$', 'catalog.views.cats', name="categories-main-page"),
                      url(r'^cats/all-goods/$', 'catalog.views.all_goods', name="all-goods"),
                      url(r'^cats/(?P<category_slug>[-\w]+)/$', 'catalog.views.show_category', name="catalog-page"),
                      url(r'^products/(?P<product_slug>[-\w]+)/$', 'catalog.views.show_product', name="product-page"),
                      url(r'^about$', 'catalog.views.about', name="about-page"),
                      url(r'^blog$', 'catalog.views.blog', name="blog-page"),
                      url(r'^test$', 'catalog.views.test', name="test-page"),
                      url(r'^test_json/(?P<series_id>[-\w]+)/$', 'catalog.views.test_json', name="test-json"),
                      url(r'^delivery$', 'catalog.views.delivery', name="delivery-page"),)

