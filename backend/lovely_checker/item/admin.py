from django.contrib import admin

from .models import Item, CategoryItem, ItemThroughIp, Comment

# Register your models here.
admin.site.register(Item)
admin.site.register(CategoryItem)
admin.site.register(ItemThroughIp)
admin.site.register(Comment)
