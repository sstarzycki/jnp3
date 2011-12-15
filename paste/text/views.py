# Create your views here.
from django.shortcuts import render_to_response


def show_main(request):

    return render_to_response('base.html', {})
