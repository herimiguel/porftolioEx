from __future__ import unicode_literals
from django.shortcuts import render


def index(request):
    return render(request, 'portfolio_app/index.html')
def testimonials(request):
    return render(request, 'portfolio_app/testimonials.html')
