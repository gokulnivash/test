from django.contrib import admin

# Register your models here.
from testapp.models import NameDetails, DateDetails


class NameDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(NameDetails,NameDetailsAdmin)

class DateDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(DateDetails,DateDetailsAdmin)
