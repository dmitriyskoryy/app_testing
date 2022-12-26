from django.urls import path
from .views import index, QuestionView

urlpatterns = [
    path('', index, name='index'),
    path('test/<slug:slug>/', QuestionView.as_view()),
]