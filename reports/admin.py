from django.contrib import admin
from .models import InfrastructureReport

@admin.register(InfrastructureReport)
class InfrastructureReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'issue_type', 'status', 'reported_at', 'reported_by')
    list_filter = ('issue_type', 'status')
    search_fields = ('title', 'description', 'location_description')
    readonly_fields = ('reported_at',)
