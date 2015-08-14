from django.contrib import admin

from .models import Product, Category, ProductImage, Tag

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'description', 'current_price', 'order', 'categories', 'page')

    inlines = [TagInline, ProductImageInline]

    search_fields = ['title', 'description', 'price', 'category__title', 'category__description']
    list_filter = ['price', 'timestamp', 'updated']

    class Meta:
        model = Product

    def current_price(self, obj):
        if obj.sale_price > 0:
            return obj.sale_price
        else:
            return obj.price 

    def categories(self, obj):
        cat = []
        for i in obj.category_set.all():
            link = "<a href='../category/" + str(i.id) + "''>" + i.title + "</a>"
            cat.append(link)
        return ", ".join(cat)

    categories.allow_tags = True

    def page(self, obj):
        link = "<a href='../../../" + obj.slug + "''>" + obj.title + "</a>"
        return link

    page.allow_tags = True

admin.site.register(Product, ProductAdmin)


# class CategoryAdmin(admin.ModelAdmin):
#     class Meta:
#         model = Category


admin.site.register(Category)
