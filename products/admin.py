from django.contrib import admin

from .models import Product, Category, ProductImage, Tag, CategoryImage

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

    prepopulated_fields = {"slug": ('tag',)}
    extra = 1



class ProductImageInline(admin.TabularInline):
    model = ProductImage


class CategoryImageInline(admin.TabularInline):
    model = CategoryImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'description', 'current_price', 'order', 'categories', 'page')

    inlines = [TagInline, ProductImageInline]

    search_fields = ['title', 'description', 'price', 'category__title', 'category__description']
    list_filter = ['price', 'timestamp', 'updated']

    prepopulated_fields = {"slug": ('title',)}

    readonly_fields = ['categories', 'page', 'timestamp', 'updated']

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


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    inlines = [CategoryImageInline]

    class Meta:
        model = Category



admin.site.register(Category, CategoryAdmin)
