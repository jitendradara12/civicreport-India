from django.shortcuts import render
from django.views.generic import TemplateView
from .models import InfrastructureReport

class HomePageView(TemplateView):
    template_name = "reports/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'total_reports': InfrastructureReport.objects.count(),
            'resolved_reports': InfrastructureReport.objects.filter(status='RES').count(),
            'recent_reports': InfrastructureReport.objects.order_by('-reported_at')[:5]
        })
        return context
