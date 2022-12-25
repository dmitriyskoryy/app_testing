from django.urls import path
from .views import index, QuestionView, Finish_test

urlpatterns = [
    path('', index, name='index'),
    path('test/<slug:slug>/', QuestionView.as_view()),
    path('finish_test/', Finish_test.as_view()),
]