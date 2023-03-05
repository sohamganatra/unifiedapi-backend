from django.contrib import admin

from authapi.models import Auth

class AdminAuth(admin.ModelAdmin):
    # fields to be displayed
    list_display = ("customer_id", "platform_type")
    list_filter = ("customer_id", "platform_type")
     
# Register your models here.
admin.site.register(Auth, AdminAuth)