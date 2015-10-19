from django.shortcuts import render_to_response, get_object_or_404
from gospel_preaching.nt_reading.models import Book, Chapter
from django.template import RequestContext

def index(request):
    all_books = Book.objects.all()
    return render_to_response('nt_reading/index.html', {'all_books': all_books}, context_instance = RequestContext(request))

def chapter(request, book, chapter):
    c = get_object_or_404(Chapter, book__slug__exact=book, chapter__exact=chapter)
    return render_to_response('nt_reading/chapter.html', {'chapter': c}, context_instance = RequestContext(request))

def book(request, book):
    b = get_object_or_404(Book, slug__exact=book)
    chapters = b.chapter_set.all()
    return render_to_response('nt_reading/book.html', {'book': b, 'chapters': chapters}, context_instance = RequestContext(request))
