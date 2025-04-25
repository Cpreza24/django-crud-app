from django.contrib import admin
from .models import Candy

@admin.register(Candy)
class CandyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'created_at', 'updated_at')
    list_filter = ('type',)
    search_fields = ('name', 'type')
