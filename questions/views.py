from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from questions.models import Question
from questions.forms import QuestionForm
from django.template import RequestContext
from django.core.paginator import Paginator
from django.conf import settings
from django.core.urlresolvers import reverse

def question_list(request):
    page = request.GET.get('page', 1)
    try:
        perpage = settings.QUESTIONS_PER_PAGE
    except AttributeError:
        perpage = 10
    pager = Paginator(Question.objects.filter(published=True), perpage)
    return render_to_response('questions/index.html', {'questions': pager.page(page).object_list, 'order': None, 'page': pager.page(page), 'pager': pager}, context_instance = RequestContext(request))
'''
def question_detail(request, pk):
    q = get_object_or_404(Question, pk=pk)
    return render_to_response('questions/detail.html', {'question': q,}, context_instance = RequestContext(request))
'''
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                q = form.save(commit=False)
                q.user = request.user
                q.save()
            else:
                form.save()
            return HttpResponseRedirect(reverse(index))
    else:
        form = QuestionForm()
    return render_to_response('questions/ask.html', {'question_form': form,}, context_instance = RequestContext(request))
