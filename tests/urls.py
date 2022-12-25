from django.urls import path
from .views import index, QuestionView, ResultTestView, ResultAnswerView

urlpatterns = [
    path('', index, name='index'),
    # path('question/<slug:q_slug>/<int:q_order>/', question, name='question')

    path('<slug:slug>/', QuestionView.as_view()),
    # path('<slug:slug>/', ResultAnswerView, name='resultanswer')

]