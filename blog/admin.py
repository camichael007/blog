from django.contrib import admin
from blog.models import Host, Publisher, Author, Book

# Register your models here.

class HostAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'ip']

admin.site.register(Host, HostAdmin)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
