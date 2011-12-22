from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template import RequestContext
from paste.text.models import Text
from django.utils.datastructures import MultiValueDictKeyError
from django.core.urlresolvers import reverse


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

def show(request, paste_id):
    paste = Text.objects.get(id=paste_id)
    return render_to_response('paste/paste.html', {'paste': paste}, context_instance = RequestContext(request))

@login_required
def new(request):
    return render_to_response('paste/new.html', {}, context_instance = RequestContext(request));

@login_required
def create(request):
    try:
        description = request.POST['description']
        content = request.POST['content']
    except MultiValueDictKeyError:
        return HttpResponseRedirect(reverse('text.views.new'))
    else:
        user = request.user
        past = Text(user=user, content=content, description=description)
        past.save()
        return HttpResponseRedirect(reverse('text.views.show', args=[past.id]))
