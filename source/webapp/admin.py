from django.contrib import admin

from webapp.models import To_do


# Register your models here.

class To_do_Admin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'execution_date')
    list_filter = ('id', 'description', 'status', 'execution_date')
    search_fields = ('status', 'execution_date')
    fields = ('description', 'status', 'execution_date')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(To_do, To_do_Admin)