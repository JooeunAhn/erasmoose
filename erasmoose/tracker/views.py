from django.shortcuts import render, redirect, get_object_or_404

from .forms import MooseForm
from .models import Moose


def index(request):
    moose_list = Moose.objects.all()
    return render(request, 'tracker/index.html', {"moose_list": moose_list})


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