from django.contrib import admin

from orzu.news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
