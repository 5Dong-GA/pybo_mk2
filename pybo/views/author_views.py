from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Question, Answer, Comment


@login_required(login_url='common:login')
def author_activity(request, question_id):

    question_list = Question.objects.filter(author=question_id).order_by('-create_date')
    answer_list = Answer.objects.filter(author=question_id).order_by('-create_date')
    comment_list = Comment.objects.filter(author=question_id).order_by('-create_date')

    context = {'question_list': question_list, 'answer_list': answer_list, 'comment_list': comment_list}
    return render(request, 'pybo/activity_form.html', context)