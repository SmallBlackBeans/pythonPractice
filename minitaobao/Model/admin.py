from django.contrib import admin

# Register your models here.
from Model.models import Test, Tag, Contact


class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main',{
            'fields': ('name', 'email'),
        }],
        ['Advance',{
            'classes':('collapse',), #CSS
            'fields':('age',),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])
