from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Developer


def index(request):
    developers = Developer.objects.order_by("name").filter(is_working=True)
    paginator = Paginator(developers, 10)
    page = request.GET.get("page")
    paged_developers = paginator.get_page(page)

    context = {"developers": paged_developers}

    return render(request, "developers/developers.html", context)


def developer(request, developer_id):
    developer = get_object_or_404(Developer, pk=developer_id)
    context = {"developer": developer}
    return render(request, "developers/developer.html", context)


""" def search_developer(request):
    queryset_list = Developer.objects.order_by("name")

    # Name of developer
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            queryset_list = queryset_list.filter(name__icontains=keywords) """
