from django.urls import path, include

from core import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('question/<int:question_id>/', views.view_question, name='view_question'),
    path('submit/', views.submit_form_view, name='submit_form'),
    path('logtest/',views.log_test, name='logger_test')
]
