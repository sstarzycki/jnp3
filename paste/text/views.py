# Create your views here.
from django.shortcuts import render, render_to_response
from text.models import Text


def show_main(request):

    return render('base.html', {})

def new(request):
    return render_to_response('paste/new.html', {});

