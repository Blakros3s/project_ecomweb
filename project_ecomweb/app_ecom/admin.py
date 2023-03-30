from django.contrib import admin
from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

class ProductAdmin(admin.ModelAdmin): 
    list_display = ('title', 'desc', 'category', 'price', 'quantity', 'cod', 'discount')
    search_fields = ('title', 'desc',)
    list_filter = ('title', 'category', 'user')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)

#customizing Admin panel
admin.site.site_title = 'Ecom' # page title
admin.site.site_header = 'ECOM' #brand name
admin.site.index_title = 'Admin Panel' # panel name