from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_name', 'site',)
    list_filter = ['site']
    search_fields = ['user', 'user__first_name', 'user__last_name', 'site']
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"
    readonly_fields = ('data_criacao',)

    def get_name(self, obj):
        return obj.user.get_full_name()
    get_name.short_description = 'Nome completo'
    get_name.admin_order_field = 'user__first_name'

# Register your models here.
admin.site.register(Profile, ProfileAdmin)