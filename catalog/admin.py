from django.contrib import admin

from catalog.models import Series, Models, ProductsPhoto, Categories, Sections, Features, FeaturesName, Values, Brands

class PhotoInline(admin.StackedInline):
    model = ProductsPhoto

class FeaturesInline(admin.StackedInline):
    model = Features

admin.site.register(ProductsPhoto)

class SeriesAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, FeaturesInline]
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

admin.site.register(Categories, CategoriesAdmin)

class SectionsAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Sections, SectionsAdmin)

admin.site.register(FeaturesName)

class ValuesInline(admin.StackedInline):
    model = Values

class ModelsAdmin(admin.ModelAdmin):
    inlines = [ValuesInline]

admin.site.register(Models, ModelsAdmin)
admin.site.register(Brands)
admin.site.register(Values)

