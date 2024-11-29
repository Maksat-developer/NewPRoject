from django.contrib import admin
from .models import Bb, Rubric, Measure, Spare


class BboardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric','kind')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Bb, BboardAdmin)
admin.site.register(Rubric)
admin.site.register(Measure)
admin.site.register(Spare)



