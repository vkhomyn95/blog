# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from home.forms import BookAddForm
from home.models import News, Carusel, Gallery, Comment, Events
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home(request):
    news = News.objects.all()

    carusels = Carusel.objects.all()
    ##pagination
    paginator = Paginator(news, 4)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)
    return render(request, 'main.html', {'news': news, 'carusels': carusels})



def page_gallery(request):
    gallery = Gallery.objects.prefetch_related('photo').all()
    return render(request, 'gallery.html', {'gallery': gallery})


def book_page(request, book_id):
    news = get_object_or_404(News, id=book_id)
    comments = Comment.objects.filter(news=news)
    form = BookAddForm(request.POST or None)
    url = 'https://graph.facebook.com/FB_USER_ID/picture'
    # paginator

    page = request.GET.get('page')
    paginator = Paginator(comments, 3)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    added = False
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.news = news
            comment.picture = url
            comment.save()
            added = True
            return HttpResponseRedirect(reverse('single_book', kwargs={'book_id': book_id}))
    return render(request, 'single_new.html', {'new': news, 'comments': comments, 'form': form, 'added': added})


def events_page(request):
    events = Events.objects.all()
    return render(request, 'events.html', {'events': events})
