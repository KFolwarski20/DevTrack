import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import ProgrammingLog
from django.db.models import Sum


@login_required
def dashboard_view(request):
    # Example data
    total_hours_by_language = {
        "Python": 10,
        "JavaScript": 14,
        "C#": 20,
    }

    chart_labels = list(total_hours_by_language.keys())
    chart_data = list(total_hours_by_language.values())

    context = {
        "chart_labels": json.dumps(chart_labels),
        "chart_data": json.dumps(chart_data),
        "languages": [{"name": k, "hours": v} for k, v in total_hours_by_language.items()],
        "best_language": max(total_hours_by_language, key=total_hours_by_language.get),
    }

    return render(request, "dashboard.html", context)
