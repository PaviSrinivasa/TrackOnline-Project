from django.contrib import admin

from .models import Info
    #Info,Details

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    pass

class MyModelAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.created_by != request.user:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.created_by != request.user:
            return False
        return True


#@admin.register(Info)
#class InfoAdmin(admin.ModelAdmin):
#    pass #list_display, search_fields, list_filter

#@admin.register(Details)
#class DetailsAdmin(admin.ModelAdmin):
#    pass

#admin.site.register(Info)

#admin.site.register(Details)
