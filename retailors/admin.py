from django.contrib import admin
from .models import Retailor

# Register your models here.
class RetailorAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'email', 'hire_date')
	list_display_links = ('id', 'name')
	search_fields = ('name',)
	list_per_page = 20

admin.site.register(Retailor,RetailorAdmin)
