import numpy as np
from django.shortcuts import render, get_object_or_404, redirect
from .models import Questions
from .forms import AnswerForm
from django.http import HttpResponse, JsonResponse
import json
from django.db import connection
from sklearn.metrics.pairwise import cosine_similarity
from core import logger
from core import model

def question_list(request):
    questions = Questions.objects.all()
    return render(request, 'core/question_list.html', {'questions': questions})

def view_question(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            # Process the submitted answer
            # For example, you can save the answer to the database
            # and redirect to a success page
            return redirect('')
    else:
        form = AnswerForm()
    return render(request, 'core/view_question.html', {'question': question, 'form': form})

def submit_form_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        question_id = request.POST.get('question_id')
        sql = "SELECT core_possibilities.match_id_id, core_possibilities.phrase FROM core_matches INNER JOIN core_possibilities ON core_matches.match_id = core_possibilities.match_id_id WHERE core_matches.question_id_id = %s"
        print(question_id, user_input)
        query_params = (question_id,)
        max_mean = -1;
        max_match = 0;
        with connection.cursor() as cursor:
            cursor.execute(sql, query_params)
            results = cursor.fetchall()
            result_dict = {}
            for key, value in results:
                if key not in result_dict:
                    result_dict[key] = [value]
                else:
                    result_dict[key].append(value)
            ans_dic = {}
            for key in result_dict:
                sentences = [user_input]
                sentences.extend(result_dict[key])
                # print(sentences)
                sentence_vecs = model.encode(sentences)
                ans_ar = cosine_similarity([sentence_vecs[0]], sentence_vecs[1:])
                ans_dic[key] = ans_ar

            for key in ans_dic:
                x = np.mean(ans_dic[key])
                print(x)
                if x > max_mean:
                    max_mean = x
                    max_match = key
            print(ans_dic)
            sql = "SELECT core_replies.phrase from core_replies WHERE core_replies.match_id_id = %s";
            query_params = (max_match,)
            cursor.execute(sql, query_params)
            results = cursor.fetchall()
            print(max_mean)
            print(results[0][0])
            if max_mean > 0.88:
                data = {
                    'data': results[0][0],
                    'similarity_score': str(max_mean)
                }
            else:
                data = {
                    'data': "wrong answer",
                    'similarity_score': str(max_mean)
                }
        return JsonResponse(json.dumps(data), safe=False)
    return render(request, 'my_app/my_form.html')


def log_test(request):
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    return HttpResponse("success")