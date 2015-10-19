from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from articles.models import Article, Category, Tag, Author, Comment, Like
from articles.forms import CommentForm
from django.template import RequestContext
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.views import login
from django.core.urlresolvers import reverse

def index(request):
    order = request.GET.get('order', '-date')
    page = request.GET.get('page', 1)
    try:
        perpage = settings.ARTICLES_PER_PAGE
    except AttributeError:
        perpage = 10
    pager = Paginator(Article.objects.all().order_by(order), perpage)
    return render_to_response('articles/index.html', {'articles': pager.page(page).object_list, 'order': order, 'page': pager.page(page), 'pager': pager, 'cats': Category.objects.all()}, context_instance = RequestContext(request))

def detail(request, slug=None, pk=None):
    if slug:
        a = get_object_or_404(Article, slug__exact=slug)
    elif pk:
        a = get_object_or_404(Article, pk=pk)
    else:
        raise Http404

    liked = False
    if request.user.is_authenticated():
        liked = (a.like_set.all() and a.like_set.filter(user=request.user))

    if request.method == 'POST':
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse(login))
        form = CommentForm(request.POST)
        if form.is_valid():
            c = Comment(article=a, user=request.user, text=form.cleaned_data['comment_text'])
            c.save()
            return HttpResponseRedirect(a.get_absolute_url())
    else:
        form = CommentForm()
    return render_to_response('articles/detail.html', {'article': a, 'comment_form': form, 'liked': liked }, context_instance = RequestContext(request))

def cat(request, slug):
    order = request.GET.get('order', '-date')
    page = request.GET.get('page', 1)
    try:
        perpage = settings.ARTICLES_PER_PAGE
    except AttributeError:
        perpage = 10
    c = get_object_or_404(Category, slug__exact=slug)
    pager = Paginator(c.article_set.all().order_by(order), perpage)
    return render_to_response('articles/cat.html', {'cat': c, 'articles': pager.page(page).object_list, 'order': order, 'page': pager.page(page), 'pager': pager, 'cats': Category.objects.all()}, context_instance = RequestContext(request))

def tag(request, slug):
    order = request.GET.get('order', '-date')
    page = request.GET.get('page', 1)
    try:
        perpage = settings.ARTICLES_PER_PAGE
    except AttributeError:
        perpage = 10
    t = get_object_or_404(Tag, slug__exact=slug)
    pager = Paginator(t.article_set.all().order_by(order), perpage)
    return render_to_response('articles/tag.html', {'tag': t, 'articles': pager.page(page).object_list, 'order': order, 'page': pager.page(page), 'pager': pager, 'cats': Category.objects.all()}, context_instance = RequestContext(request))

def author(request, slug):
    order = request.GET.get('order', '-date')
    page = request.GET.get('page', 1)
    try:
        perpage = settings.ARTICLES_PER_PAGE
    except AttributeError:
        perpage = 10
    a = get_object_or_404(Author, slug__exact=slug)
    pager = Paginator(a.article_set.all().order_by(order), perpage)
    return render_to_response('articles/author.html', {'author': a, 'articles': pager.page(page).object_list, 'order': order, 'page': pager.page(page), 'pager': pager, 'cats': Category.objects.all()}, context_instance = RequestContext(request))

@login_required
def like(request, slug=None, pk=None):
    if slug:
        a = get_object_or_404(Article, slug__exact=slug)
    elif pk:
        a = get_object_or_404(Article, pk=pk)
    else:
        raise Http404
    if a.like_set.all():
        ol = a.like_set.filter(user=request.user)
        if ol:
            ol[0].delete()
        else:
            l = Like(article=a, user=request.user)
            l.save()
    else:
        l = Like(article=a, user=request.user)
        l.save()
    
    return HttpResponseRedirect(a.get_absolute_url())

@login_required
def remove_comment(request, pk):
    c = get_object_or_404(Comment, pk=pk)
    if (c.user == request.user) or request.user.is_superuser:
        c.delete()
    return HttpResponseRedirect(c.article.get_absolute_url())

def author_partial(request):
    q = request.GET.get('q', '')
    try:
        num = settings.AUTHOR_PARTIAL_NUM
    except AttributeError:
        num = 5
    authors = Author.objects.filter(name__icontains=q)
    more = False
    if len(authors) > num:
        more = True
        authors = authors[:num]
    return render_to_response('articles/author_partial.html', {'authors': authors, 'more': more}, context_instance = RequestContext(request))

def tag_partial(request):
    q = request.GET.get('q', '')
    try:
        num = settings.TAG_PARTIAL_NUM
    except AttributeError:
        num = 10
    tags = Tag.objects.filter(name__icontains=q)
    more = False
    if len(tags) > num:
        more = True
        tags = tags[:num]
    return render_to_response('articles/tag_partial.html', {'tags': tags, 'more': more}, context_instance = RequestContext(request))
