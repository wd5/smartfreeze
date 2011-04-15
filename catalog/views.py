          # -*- coding: utf-8 -*-
import urllib
from django.db.models.query_utils import Q
from django.utils import simplejson
from django.shortcuts import get_object_or_404, render_to_response
from django.core import urlresolvers, serializers
from django.template import RequestContext
from catalog.models import Category, Series, Section, Feature, FeaturesName, Brand
from catalog.forms import ProductAddToCartForm
from django.http import HttpResponseRedirect, HttpResponse
from cart import cart

def index(request):
    special_price = Series.objects.filter(is_special_price=True)
    bestsellers = Series.objects.filter(is_bestseller=True)
    if request.method == 'POST':
        cart.add_to_cart(request)
    return render_to_response("main/index.html", locals(), context_instance=RequestContext(request))

def cats(request):
    cats = Section.objects.all()
    return render_to_response("main/section.html", locals(), context_instance=RequestContext(request))

def show_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = category.series_set.all()
    if request.method == 'POST':
        cart.add_to_cart(request)
    return render_to_response("main/catalog.html", locals(), context_instance=RequestContext(request))

def show_category_brand(request, category_slug, brand_slug):
    category = Category.objects.get(slug=category_slug)
    brand = Brand.objects.get(slug=brand_slug)
    products = Series.objects.filter(category=category, brand=brand)
    return render_to_response("main/catalog.html", locals(), context_instance=RequestContext(request))

def show_section(request, section_slug):
    section = Section.objects.get(slug=section_slug)
    cats = section.category_set.all()
    return render_to_response("main/section.html", locals(), context_instance=RequestContext(request))

def show_product(request, product_slug):
    if request.method == 'POST':
        cart.add_to_cart(request)
    product = get_object_or_404(Series, slug=product_slug)
    return render_to_response("main/product.html", locals(), context_instance=RequestContext(request))

def all_goods(request):
    if request.method == 'POST':
        cart.add_to_cart(request)
        url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(url)
    products = Series.objects.all()
    return render_to_response("main/catalog.html", locals(), context_instance=RequestContext(request))

def search(request):
    search_world = request.GET['s']
    products = Series.objects.filter(Q(name__icontains=search_world) | Q(mini_html_description__icontains=search_world) | Q(brand__name__icontains=search_world))
    return render_to_response("main/catalog.html", locals(), context_instance=RequestContext(request))

def about(request):
    page_title = "О нас"
    return render_to_response('main/about.html', locals(), context_instance=RequestContext(request))

def delivery(request):
    page_title = "Доставка и оплата"
    return render_to_response('main/delivery.html', locals(), context_instance=RequestContext(request))

def test_json(request, series_id):
    series = Series.objects.get(id=series_id)
    features = series.feature_set.all()
    features_name = []
    feature_count = 0
    for feature in features:
        features_name.append({feature_count : feature.name.id})
        feature_count += 1
    return HttpResponse( simplejson.dumps( features_name ), mimetype="application/json" )



