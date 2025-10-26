import json

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from dashboard.models import ProgrammingLog
from dashboard.forms import ProgrammingLogForm


@login_required
def dashboard_view(request):
    logs = ProgrammingLog.objects.filter(user=request.user).order_by('-date')
    active_logs = logs.filter(hours__gt=0)
    paginator = Paginator(active_logs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    total_hours_by_language = {
        log.get_language_display(): float(log.hours)
        for log in logs
    }

    chart_labels = list(total_hours_by_language.keys())
    chart_data = list(total_hours_by_language.values())

    context = {
        "chart_labels": json.dumps(chart_labels),
        "chart_data": json.dumps(chart_data),
        "languages": [{"name": k, "hours": v} for k, v in total_hours_by_language.items()],
        "best_language": max(total_hours_by_language, key=total_hours_by_language.get),
        "logs": page_obj,
        "form": ProgrammingLogForm(),
    }

    return render(request, "dashboard.html", context)


@login_required
def add_log(request):
    if request.method == 'POST':
        form = ProgrammingLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
    return redirect('dashboard')


@login_required
def edit_log(request, pk):
    log = get_object_or_404(ProgrammingLog, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProgrammingLogForm(request.POST, instance=log)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProgrammingLogForm(instance=log)
    return render(request, 'dashboard/edit_log.html', {'form': form, 'log': log})


@login_required
def delete_log(request, pk):
    log = get_object_or_404(ProgrammingLog, pk=pk, user=request.user)
    if request.method == 'POST':
        log.delete()
    return redirect('dashboard')
