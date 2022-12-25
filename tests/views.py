
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

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
    context_object_name = 'quests'
    paginate_by = 1


    def get_queryset(self):
        slug = self.kwargs.get('slug')
        qs = Question.objects.filter(nametest__slug=slug)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get("select_number"):
            answer = self.request.GET.get("select_number")
            print(answer)
        return context



def ResultAnswerView(request):
    return HttpResponse("Подтверждение ответа")


class ResultTestView(generic.View):
    template_name = 'tests/result_test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # if self.request.GET.get("resp_delete"):
        #     resp_id = self.request.GET.get("resp_delete")
        #     delete_response(resp_id)

        return context

    # if request.method == 'POST':
    #     print(f'gggggggggggggggg    {request}')
    #
    # return render(request, '/')







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
