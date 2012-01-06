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

from text.tasks import add_language_to_paste

def show_main(request):
    return render_to_response('base.html', {})

class ListTextView(ListView):
    def get_queryset(self):
        return Text.objects.all().limit(50)
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
        if self.request.user.is_authenticated():
            text.user_id = self.request.user.id;
        text.save()
        add_language_to_paste.delay(text)
        return render_to_response('paste/added.html', { "id": text.id })

class EditTextView(FormView):
    form_class = NewTextForm
    template_name = 'paste/edit.html'

    def get(self, request, *args, **kwargs):
        text = Text.objects.get(id=kwargs['pk'])
        form = NewTextForm({'title': text.title, 'content': text.content});
        context = self.get_context_data(**kwargs)
        context['form'] = form;
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form, request, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    def form_valid(self, form, request, **kwargs):
        text = Text.objects.get(id=kwargs['pk'])
        text.content = form.cleaned_data['content']
        text.title = form.cleaned_data['title']
        if request.user.is_authenticated:
            if text.user_id:
                if request.user.id == text.user_id:
                    text.save()
                    add_language_to_paste.delay(text)
        return render_to_response('paste/edited.html', { "id": text.id });
