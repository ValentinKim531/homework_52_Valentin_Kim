from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from webapp.models import To_do


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'to_do_create.html')
    print(request.POST)
    to_do_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'execution_date': request.POST.get('execution_date'),
        'created_at': request.POST.get('created_at')
    }
    to_do = To_do.objects.create(**to_do_data)
    return redirect(f'/to_do/?pk={to_do.pk}')

def detail_view(request):
    to_do_pk = request.GET.get('pk')
    to_do = To_do.objects.get(pk=to_do_pk)
    context = {'to_do': to_do}
    return render(request, 'to_do.html', context=context)