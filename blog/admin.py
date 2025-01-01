from django.contrib import admin
from .models import Banner,Catagary,Camputers,Mansclothers,Woman
# Register your models here.

admin.site.register(Banner)
admin.site.register(Catagary)
admin.site.register(Mansclothers)
admin.site.register(Woman)


@admin.register(Camputers)
class ComputersAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
