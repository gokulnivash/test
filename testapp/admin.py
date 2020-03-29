from django.contrib import admin

# Register your models here.
from testapp.models import NameDetails


class NameDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(NameDetails,NameDetailsAdmin)

