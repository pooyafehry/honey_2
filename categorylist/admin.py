from django.contrib import admin
from .models import Category, Cart, CartItem,Comment
# Register your models here.




@admin.register(Comment)
class commentadmin(admin.ModelAdmin):
    pass


from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    search_fields = ('name',)
    list_filter = ('name',)
