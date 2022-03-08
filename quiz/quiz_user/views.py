import re
from django.shortcuts import render,redirect,get_list_or_404

# Create your views here.

def userProfile(request):
    return render(request,'quiz_user/profile.html')

def questionsPage(request):
    details = {
            "name" : "ABC XYZ",
            "subject_name" : "Django / Flask",
            "total_marks" : "10",
            "total_time" : "10"
        }
    
    data = [
    {
        "question_id" : 1,
        "question_description" : "what is quantiphi?",
        "options" : [{
            "option_1":"1" ,
            "option_2" : "2",
            "option_3" : "3",
            "option_4" : "4"
        }],
        "correct_answer" : "2",
        "marks" : "1"
    },
     {
        "question_id" : 2,
        "question_description" : "what is quantiphi?",
        "options" : [{
            "option_1":"1" ,
            "option_2" : "2",
            "option_3" : "3",
            "option_4" : "4"
        }],
        "correct_answer" : "2",
        "marks" : "1"
    },
     {
        "question_id" : 3,
        "question_description" : "what is quantiphi?",
        "options" : [{
            "option_1":"1" ,
            "option_2" : "2",
            "option_3" : "3",
            "option_4" : "4"
        }],
        "correct_answer" : "2",
        "marks" : "1"
    },
     {
        "question_id" : 4,
        "question_description" : "what is quantiphi?",
        "options" : [{
            "option_1":"1" ,
            "option_2" : "2",
            "option_3" : "3",
            "option_4" : "4"
        }],
        "correct_answer" : "2",
        "marks" : "1"
    },
     {
        "question_id" : 5,
        "question_description" : "what is quantiphi?",
        "options" : [{
            "option_1":"1" ,
            "option_2" : "2",
            "option_3" : "3",
            "option_4" : "4"
        }],
        "correct_answer" : "2",
        "marks" : "1"
    },
     {
        "question_id" : 6,
        "question_description" : "what is quantiphi?",
        "options" : [{
            "option_1":"1" ,
            "option_2" : "2",
            "option_3" : "3",
            "option_4" : "4"
        }],
        "correct_answer" : "2",
        "marks" : "1"
    },
     {
        "question_id" : 7,
        "question_description" : "what is quantiphi?",
        "options" : [{
            "option_1":"1" ,
            "option_2" : "2",
            "option_3" : "3",
            "option_4" : "4"
        }],
        "correct_answer" : "2",
        "marks" : "1"
    },
     {
        "question_id" : 8,
        "question_description" : "what is quantiphi?",
        "options" : [{
            "option_1":"1" ,
            "option_2" : "2",
            "option_3" : "3",
            "option_4" : "4"
        }],
        "correct_answer" : "2",
        "marks" : "1"
    },
     {
        "question_id" : 9,
        "question_description" : "what is quantiphi?",
        "options" : [{
            "option_1":"1" ,
            "option_2" : "2",
            "option_3" : "3",
            "option_4" : "4"
        }],
        "correct_answer" : "2",
        "marks" : "1"
    },
     {
        "question_id" : 10,
        "question_description" : "what is quantiphi?",
        "options" : [{
            "option_1":"1" ,
            "option_2" : "2",
            "option_3" : "3",
            "option_4" : "4"
        }],
        "correct_answer" : "2",
        "marks" : "1"
    },
]
    context = {"data" : data , "details" : details}
    return render(request, 'quiz_user/questions.html',context)

