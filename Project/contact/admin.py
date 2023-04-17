from django.contrib import admin

from contact.models import contactEnquiry

class Authoralphaseries(admin.ModelAdmin):
    pass
admin.site.register(contactEnquiry, Authoralphaseries)

# Register your models here.
