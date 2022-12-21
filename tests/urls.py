from django.urls import path
from .views import index, QuestionView

urlpatterns = [
    path('', index, name='index'),
    # path('question/<slug:q_slug>/<int:q_order>/', question, name='question')
    path('question/<int:pk>/', QuestionView.as_view(), name='question')
]