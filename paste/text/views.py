# Create your views here.
from django.shortcuts import render


def show_main(request):

    return render('base.html', {})
