from django.shortcuts import render, redirect
from models import Auction

def index(request):
    context = {}

    auctions = Auction.objects.filter(status__exact=Auction.ACTIVE).order_by('-id').all()
    context['auctions'] = auctions

    return render(request, 'core/index.html', context)

def set_language(request, language):
    request.session['django_language'] = language
    next = request.GET.get('next', default='/')

    if request.user.is_authenticated():
        request.user.language = language
        request.user.save()
        
    return redirect(next)

def after_login(request):
    request.session['django_language'] = request.user.language
    return redirect('/')
    