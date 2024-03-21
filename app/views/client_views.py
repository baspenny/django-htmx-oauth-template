from django.shortcuts import render
from app.models import Client
from django.db.models import Q


def list(request):
    qs = Client.objects.all()

    if request.htmx:
        params = request.GET
        if 'search-clients' in params:
            qs = qs.filter(
                Q(name__icontains=params['search-clients']) |
                Q(acumatica_id__icontains=params['search-clients'])
            )


        return render(request, 'partials/client/client_list.html', context={'clients': qs})

    return render(request, 'clients.html', context={'clients': Client.objects.all()})


def detail(request, id):
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass
    return render(request, 'partials/client/client_detail.html', context={'client': Client.objects.get(id=id)})
