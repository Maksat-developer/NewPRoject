from django.contrib import admin
from .models import Category, SubCategories, Announcement

admin.site.register(Category)
admin.site.register(SubCategories)
admin.site.register(Announcement)

