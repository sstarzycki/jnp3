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
from text.forms import NewTextForm
from django.views.generic import \
        CreateView, TemplateView, DeleteView, \
        DetailView, FormView, ListView

def show_main(request):
    return render_to_response('base.html', {})

class ListTextView(ListView):
    def get_queryset(self):
        return Text.objects.all()
    template_name = 'paste/list.html'

class ShowTextView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(ShowTextView, self).get_context_data(**kwargs)
        context['object'] = Text.objects.get(id=kwargs['pk'])
        return context

    template_name = 'paste/show.html'

class NewTextView(FormView):
    form_class = NewTextForm
    template_name = 'paste/new.html'

    def form_valid(self, form):
        text = Text(content=form.cleaned_data['content'],
            title=form.cleaned_data['title'])
        text.save()
        return render_to_response('paste/added.html', { "id": text.id })
