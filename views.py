from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

# from .models import Benchmark

def compare(request, benchmark_id1, benchmark_id2):
    # benchmark1 = get_object_or_404(Benchmark, pk=benchmark_id1)
    # benchmark2 = get_object_or_404(Benchmark, pk=benchmark_id2)
    context = {}
    return render(request, 'benchmark_app/compare.html', context)

def upload(request):
    context = {}
    return render(request, 'benchmark_app/upload.html', context)

def home(request):
    context = {}
    return render(request, 'benchmark_app/home.html', context)
