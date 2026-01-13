from django.contrib import admin

from .models import AdminUIConfig


@admin.register(AdminUIConfig)
class AdminUIConfigAdmin(admin.ModelAdmin):
    list_display = ('navbar_style',)



# Register your models here.

    