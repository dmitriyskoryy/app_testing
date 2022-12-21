from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from .models import SetTests, NameTest, Question, Answer


def index(request):
    settests = SetTests.objects.all()
    nametests = [{'title': s.title, 'tests': NameTest.objects.filter(settest=s)} for s in settests]
    return render(request, 'tests/index.html',
                  {'title': 'Главная страница сайта', 'settests': settests, 'nametests': nametests})


class QuestionView(generic.ListView):
    model = Question
    template_name = 'tests/question.html'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        q_id = self.kwargs.get('pk')
        quest = Question.objects.get(pk=q_id)
        context['quest'] = quest
        context['answers'] = Answer.objects.filter(question=quest)
        print(context)
        return context

# def question(request, q_slug, q_order):
#     nametest = get_object_or_404(NameTest, slug=q_slug)
#     quest = get_object_or_404(Question, order=q_order, nametest=nametest)
#     answer = Answer.objects.filter(question=quest)
#     number_question = q_order
#     if request.method == 'POST':
#         print(request.POST['select'])
#         if len(request.POST) == 1:
#             return render(request, 'tests/question.html',
#                           {'nametest': nametest, 'quest': quest, 'title': 'Вопрос', 'answer': answer,
#                            'error_message': "Пожалуйста, выберете один из вариантов ответа!"})
#         number_question += 1
#         return redirect(f'/question/{nametest.slug}/{number_question}')
#     return render(request, 'tests/question.html',
#                   {'nametest': nametest, 'quest': quest, 'title': 'Вопрос', 'answer': answer})





# def result(request, q_id, q_slug):
#     nametest = get_object_or_404(NameTest, slug=q_slug)
#     quest = get_object_or_404(Question, order=q_id, nametest=nametest)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['select'])
#     except (KeyError, Answer.DoesNotExist):
#         return render(request, 'tests/question.html', {
#             'question': quest,
#             'error_message': "Вы не выбрали ни одного варианта",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return redirect(reverse('results', args=(question.id,)))
