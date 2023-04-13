from django.contrib import admin

from news.models import Ip, News

# Register your models here.
admin.site.register(Ip)
admin.site.register(News)