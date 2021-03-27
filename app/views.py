from django.shortcuts import render

questions = [
    {
        'id': idx,
        'title': f'Title number {idx}',
        'text': f'Some text for question #{idx}'
    } for idx in range(10)
]


def index(request):
    return render(request, 'index.html', {})


def hot_questions(request):
    return render(request, 'hot_questions.html', {'questions': questions})


def new_questions(request):
    return render(request, 'new_questions.html', {})


def one_question(request, pk):
    question = questions[pk]
    return render(request, 'question.html', {"question": question})

