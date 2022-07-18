from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from mysite.models import Category, Tag, Product


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name',)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name',)


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    # form = PostAdminForm
    # save_as = True
    list_display = ('id', 'name', 'quantity', 'slug', 'category', 'price', 'created_at', 'get_photo',)
    list_display_links = ('name',)
    search_fields = ('name', 'id')
    list_filter = ('category', 'tags', 'price')
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = (
        'name', 'slug', 'quantity', 'price', 'category', 'tags', 'description', 'photo', 'get_photo', 'views', 'created_at',)

    def get_photo(self, obj, ):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50px">')
        return '--'

    get_photo.short_description = 'Миниатюра'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Product, ProductAdmin)
