from django.shortcuts import render, redirect


from django.views import generic
from django.views.generic import TemplateView

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
    list_id = []
    paginate_by = 1

    def __init__(self):
        self.list_id = [id_q.id for id_q in Question.objects.all()]


    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if self.request.GET.get("select_number"):
            if self.request.GET.get("quest_id"):
                quest_id = self.request.GET.get("quest_id")
                try:
                    self.list_id.remove(int(quest_id))
                except:
                    print("id None")

        qs = Question.objects.filter(nametest__slug=slug, id__in=self.list_id)
        return qs


    def get(self, request, *args, **kwargs):
        result = self.request.GET.get("select_number")
        btn_test = self.request.GET.get("btn_test")
        if btn_test == "btn_finish":
            print(f'btn_finish    {result}')
            return redirect(f'/finish_test/')
        elif btn_test == "btn_next":
            print(f'btn_next    {result}')
        return super().get(request, *args, **kwargs)



class Finish_test(TemplateView):
    template_name = 'tests/finish_test.html'




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
