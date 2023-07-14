from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'item',
        'title',
        'body',
        'date',
       
    )

    ordering = ('-date',)


admin.site.register(Review, ReviewAdmin)