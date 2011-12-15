from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from paste.text.models import Text

def show_main(request):

    return render_to_response('base.html', {})

def display_shouts(request):

    from settings import SHOUTS_ON_MAIN_PAGE_NUMBER

    shouts_list = Text.objects.all()
    paginator = Paginator(shouts_list, SHOUTS_ON_MAIN_PAGE_NUMBER)
    page = request.GET.get('page')
    try:
        shouts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        shouts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        shouts = paginator.page(paginator.num_pages)

    return render_to_response('shoutbox/shouts_list.html', {"shouts": shouts})

def new(request):
    return render_to_response('paste/new.html', {});

