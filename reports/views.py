from django.shortcuts import render
from django.views.generic import TemplateView
from .models import InfrastructureReport

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import ReportForm
from django.contrib.auth.decorators import login_required

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

# New registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# New view for creating reports
@login_required
def create_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.reported_by = request.user
            report.save()
            return redirect('reports:home')
    else:
        form = ReportForm()
    return render(request, 'reports/create_report.html', {'form': form})
