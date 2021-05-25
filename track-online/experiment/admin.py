from django.contrib import admin

from .models import Info
    #Info,Details

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    pass

#@admin.register(Info)
#class InfoAdmin(admin.ModelAdmin):
#    pass #list_display, search_fields, list_filter

#@admin.register(Details)
#class DetailsAdmin(admin.ModelAdmin):
#    pass

#admin.site.register(Info)

#admin.site.register(Details)
