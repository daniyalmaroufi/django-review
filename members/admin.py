from django.contrib import admin
from . import models
# Register your models here.

class MembersAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname','phone','joined_date')
    list_filter=('firstname','lastname','phone','joined_date')
    search_fields=('firstname','lastname','phone','joined_date')
    list_per_page=25
    prepopulated_fields = {"slug": ("firstname", "lastname")}

admin.site.register(models.Member,MembersAdmin)
