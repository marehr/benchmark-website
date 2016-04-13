from django.shortcuts import get_object_or_404, render, redirect
# from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import JsonResponse
from .forms import UploadFileForm

from .process import handle_uploaded_file, create_compare_json_file

def compare(request, benchmark_id1, benchmark_id2):
    # benchmark1 = get_object_or_404(Benchmark, pk=benchmark_id1)
    # benchmark2 = get_object_or_404(Benchmark, pk=benchmark_id2)
    context = {}
    return render(request, 'benchmark_app/compare.html', context)

def compare_json(request, benchmark_id1, benchmark_id2):
    # benchmark1 = get_object_or_404(Bechmark, pk=benchmark_id1)
    # benchmark2 = get_object_or_404(Bechmark, pk=benchmark_id2)
    result = create_compare_json_file([benchmark_id1, benchmark_id2])
    return JsonResponse(result, safe=False)

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('compare', benchmark_id1=1, benchmark_id2=2)
    else:
        form = UploadFileForm()
    return render(request, 'benchmark_app/upload.html', {'form': form})

def home(request):
    context = {}
    return render(request, 'benchmark_app/home.html', context)
