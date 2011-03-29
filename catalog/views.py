          # -*- coding: utf-8 -*-
import urllib
from django.utils import simplejson
from django.shortcuts import get_object_or_404, render_to_response
from django.core import urlresolvers, serializers
from django.template import RequestContext
from catalog.models import Categories, Series, Sections, Features, FeaturesName
from catalog.forms import ProductAddToCartForm
from django.http import HttpResponseRedirect, HttpResponse
from cart import cart

def index(request):
    sections = Sections.objects.all()
    return render_to_response("main/index.html", locals(), context_instance=RequestContext(request))

def cats(request):
    return render_to_response("main/cats.html", locals(), context_instance=RequestContext(request))

def show_category(request, category_slug):
    if request.method == 'POST':
        cart.add_to_cart(request)
        url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(url)
    else:
        try:
            category = Categories.objects.get(slug=category_slug)
            products = category.products_set.filter(is_active=True)
        except :
            section = Sections.objects.get(slug=category_slug)
            category = section.categories_set.filter(is_active=True)
            products = []
            for cat in category:
                products += cat.products_set.filter(is_active=True)
    return render_to_response("main/catalog.html", locals(), context_instance=RequestContext(request))

def show_product(request, product_slug):
    product = get_object_or_404(Series, slug=product_slug)
    photos = product.productsphoto_set.all()
    features = product.features_set.all()
    # evaluate the HTTP method, change as needed
    if request.method == 'POST':
        #create the bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        #check if posted data is valid
        if form.is_valid():
            #add to cart and redirect to cart page
            cart.add_to_cart(request)
            # if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            url = urlresolvers.reverse('show_cart')
            return HttpResponseRedirect(url)
    else:
        #create the unbound form. Notice the request as a keyword argument
        form = ProductAddToCartForm(request=request, label_suffix=':')
    # assign the hidden input the product slug
    form.fields['product_slug'].widget.attrs['value'] = product_slug
    # set test cookie to make sure cookies are enabled
    request.session.set_test_cookie()
    return render_to_response("main/tovar.html", locals(), context_instance=RequestContext(request))

def all_goods(request):
    if request.method == 'POST':
        cart.add_to_cart(request)
        url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(url)
    products = Series.objects.all()
    return render_to_response("main/catalog.html", locals(), context_instance=RequestContext(request))

def about(request):
    page_title = "О нас"
    return render_to_response('main/about.html', locals(), context_instance=RequestContext(request))

def blog(request):
    page_title = "Блог"
    return render_to_response('main/blog.html', locals(), context_instance=RequestContext(request))

def delivery(request):
    page_title = "Доставка и оплата"
    return render_to_response('main/delivery.html', locals(), context_instance=RequestContext(request))

def test(request):
    return render_to_response('test.html', locals(), context_instance=RequestContext(request))

def test_json(request, series_id):
    series = Series.objects.get(id=series_id)
    features = series.features_set.all()
    features_name = []
    feature_count = 0
    for feature in features:
        features_name.append({feature_count : feature.name.id})
        feature_count += 1
    return HttpResponse( simplejson.dumps( features_name ), mimetype="application/json" )

