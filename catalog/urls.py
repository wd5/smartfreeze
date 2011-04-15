from django.conf.urls.defaults import *

urlpatterns = patterns('',
                      url(r'^$', 'catalog.views.index', name="main-page"),
                      url(r'^search/$', 'catalog.views.search', name="search-page"),
                      url(r'^search/(?P<search_world>[-\w]+)/$', 'catalog.views.search', name="search-page"),
                      url(r'^cat/$', 'catalog.views.cats', name="categories-main-page"),
                      url(r'^cat/all-goods/$', 'catalog.views.all_goods', name="all-goods"),
                      url(r'^section/(?P<section_slug>[-\w]+)/$', 'catalog.views.show_section', name="section-page"),
                      url(r'^cat/(?P<category_slug>[-\w]+)/$', 'catalog.views.show_category', name="catalog-page"),
                      url(r'^cat/(?P<category_slug>[-\w]+)/(?P<brand_slug>[-\w]+)/$', 'catalog.views.show_category_brand', name="catagory-brand-page"),
                      url(r'^product/(?P<product_slug>[-\w]+)/$', 'catalog.views.show_product', name="product-page"),
                      url(r'^about/$', 'catalog.views.about', name="about-page"),
                      url(r'^test_json/(?P<series_id>[-\w]+)/$', 'catalog.views.test_json', name="test-json"),
                      url(r'^delivery/$', 'catalog.views.delivery', name="delivery-page"),)

