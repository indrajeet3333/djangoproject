from django.contrib import admin
from .models import client, appointments
# Register your models here.

class clientAdmin(admin.ModelAdmin):
    search_fields = ['first_name']
    list_display = ('combined_name','contact','email','pVisit','reference','dateofvisit')

    def combined_name(self, obj):
        return ("%s %s" % (obj.first_name, obj.last_name))
    combined_name.short_description = 'Name'
    def reference(self, obj):
        return ("%s" % (obj.hAbout))
    reference.short_description = 'Reference'
    def pVisit(self, obj):
        return ("%s" % (obj.pVisit))
    pVisit.short_description = 'Purpose of Visit'


   
    

admin.site.register(client,clientAdmin)
admin.site.register(appointments)

