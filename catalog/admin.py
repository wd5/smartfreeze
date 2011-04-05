from django.contrib import admin

from catalog.models import Series, Model, ModelsPhoto, Category, Section, Feature, FeaturesName, Value, Brand
from django import forms
import models

class PhotoInline(admin.TabularInline):
    model = ModelsPhoto

class FeaturesInline(admin.TabularInline):
    model = Feature

class ValuesInline(admin.TabularInline):
    model = Value

class ModelsAdmin(admin.ModelAdmin):
    inlines = [ValuesInline]

class ModelsInline(admin.TabularInline):
    model = Model
    inlines = [ValuesInline]

admin.site.register(ModelsPhoto)

class SeriesAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, FeaturesInline, ModelsInline]
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Series, SeriesAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description',]
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoriesAdmin)

class SectionsAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Section, SectionsAdmin)

admin.site.register(FeaturesName)


admin.site.register(Model, ModelsAdmin)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Brand, BrandAdmin)
admin.site.register(Value)

