from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncMonth, TruncDay
from django.db.models import Count

from chartit import DataPool, Chart

from .forms import MooseForm
from .models import Moose


def index(request):
    moose_list = Moose.objects.all().order_by('-created_at')
    return render(request, 'tracker/index.html', {"moose_list": moose_list})


def about_us(request):
    return render(request, 'tracker/about_us.html', {})


def stat(request):
    import datetime
    today = datetime.datetime.now()
    total_count = Moose.objects.all().count()
    this_month = Moose.objects.filter(created_at__month=today.month).count()
    moose_list = \
    Moose.objects.annotate(date=TruncDay('created_at')).values('date').annotate(count=Count('id')).values('date', 'count')
    moose_data = DataPool(series=[{
        "options": {
            'source': moose_list},
        "terms": [
            'date',
            'count',
        ]
        }])
    cht = Chart(
        datasource=moose_data,
        series_options=[{
            'options': {
                "type": "line",
                "stacking": False
            },
            'terms': {
                'date': ['count']
            },
        }],
        chart_options={'title': {"text": "MOOSE ACCIDENT COUNT BY MONTH"}, "xAxis": {"title": {"text": "Date"}}})

    return render(request, "tracker/stat.html", {
        "total_count": total_count,
        "this_month": this_month,
        'line_chart': cht,
        })


@login_required
def moose_create(request):
    if request.method == "POST":
        form = MooseForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect("tracker:moose_detail", form.pk)
    else:
        form = MooseForm()
    return render(request, "tracker/moose_form.html", {"form": form})


def moose_detail(request, pk):
    moose = get_object_or_404(Moose, pk=pk)
    return render(request, "tracker/moose_detail.html", {"moose": moose})