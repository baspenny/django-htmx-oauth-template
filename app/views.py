from django.shortcuts import render
from app.models import Client
from django.db.models import Q


def index(request):
    qs = Client.objects.all()

    if request.htmx:
        params = request.GET
        if 'search-clients' in params:
            qs = qs.filter(
                Q(name__icontains=params['search-clients']) |
                Q(acumatica_id__icontains=params['search-clients'])
            )


        return render(request, 'partials/clients.html', context={'clients': qs})

    return render(request, 'home.html', context={'clients': Client.objects.all()})
