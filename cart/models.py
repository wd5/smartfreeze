          # -*- coding: utf-8 -*-
from django.db import models
from catalog.models import Series, Model
from django.utils.encoding import smart_unicode
from datetime import date


class CartProduct(models.Model):
    cartitem = models.ForeignKey('CartItem')
    product = models.ForeignKey(Model)
    quantity = models.IntegerField(default=1)

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()

class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField(Model, through=CartProduct)

    class Meta:
        db_table = 'cart_item'
        ordering = ['date_added']

    def total(self):
        return self.quantity * self.product.price

    def name(self):
        return self.product.name

    def price(self):
        return self.product.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()

STATUS_CHOICES = (
    ('PROCESS', 'Обработать'),
    ('CONTACT_AT', 'Связаться в назначенное время'),
    ('REFUSED', 'Снятие заявки клиентом'),
    ('WAYT', 'Ожидаем'),
    ('CASH_IN', 'Деньги внесены'),
)

DELIVERY_CHOICES = (
    ('EMS', 'EMS'),
    ('COURIER', 'Курьер'),
)

class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name="Город")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    company = models.CharField(max_length=300, blank=True, verbose_name="Компания")
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name="Адрес")
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    cart = models.ForeignKey(CartItem)
    ordered_at = models.DateTimeField(auto_now_add=True )
    subtotal = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, verbose_name="Сумма")
    discount = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, verbose_name="Скидка")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="Статус", default='PROCESS')
    referrer = models.URLField(verify_exists=False, max_length=500)
    comment = models.TextField(null=True, blank=True, verbose_name="Комментарий")
    order = models.TextField(null=True, blank=True)
    last_user = models.CharField(max_length=200, null=True, blank=True)
    change_log = models.TextField(null=True, blank=True)

    def get_order(self):
        cart_items = CartProduct.objects.filter(cartitem = self.cart.id)
        products = ""
        for item in cart_items:
            products += u"%s - %sшт; " % (item.product, item.quantity )
        return products

    class Meta:
        ordering = ['-ordered_at']

    def __unicode__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None):
        not_new = self.pk
        if not self.last_user:
            user = u"Сайт"
        else:
            user = self.last_user
        if not_new:
            old = Client.objects.get(pk=self.pk)
            for f in self._meta.fields:
                if f.value_from_object(old) != f.value_from_object(self):
                        if not f.name == 'change_log':
                            if not f.name == 'last_user':
                                    if f.name == 'status':
                                        if f.value_from_object(old):
                                            self.change_log += u"%s - %s изменил %s с %s на %s<br>\r" %\
                                              (date.today(), user, smart_unicode(Client._meta.get_field(f.name).verbose_name),
                                               old.get_status_display(), self.get_status_display())
                                        else:
                                            self.change_log += u"%s - %s добавил %s %s<br>\r" %\
                                                         (date.today(), user, smart_unicode(Client._meta.get_field(f.name).verbose_name),
                                                          self.get_status_display())
                                    else:
                                        if f.value_from_object(old):
                                            self.change_log += u"%s - %s изменил %s с %s на %s<br>\r" %\
                                              (date.today(), user, smart_unicode(Client._meta.get_field(f.name).verbose_name),
                                               f.value_from_object(old), f.value_from_object(self))
                                        else:
                                            self.change_log += u"%s - %s добавил %s %s<br>\r" %\
                                                         (date.today(), user, smart_unicode(Client._meta.get_field(f.name).verbose_name),
                                                          f.value_from_object(self))
        super(Client, self).save() # Call the "real" save() method.
        if not not_new == self.pk:
            client = Client.objects.get(pk=self.pk)
            client.change_log = u"%s - %s добавил клиента<br>\r" % (date.today(), user)
            client.save()
