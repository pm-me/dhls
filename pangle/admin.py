from django.contrib import admin
from pangle.models import Category, Blog, Download, Friends, About


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass


class BlogAdmin(admin.ModelAdmin):
    pass


class DownloadAdmin(admin.ModelAdmin):
    pass


class FriendsAdmin(admin.ModelAdmin):
    pass


class AboutAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Download, DownloadAdmin)
admin.site.register(Friends, FriendsAdmin)
admin.site.register(About, AboutAdmin)
