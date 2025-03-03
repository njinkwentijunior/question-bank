from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Exam, Category
from .forms import SignUpForm
import random

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_bank/question_list.html', {'questions': questions})

def exam_detail(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    return render(request, 'question_bank/exam_detail.html', {'exam': exam})

@login_required
def generate_exam(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        num_questions = int(request.POST.get('num_questions'))
        questions = Question.objects.filter(category_id=category_id)
        selected_questions = random.sample(list(questions), num_questions)
        exam = Exam.objects.create(name="Generated Exam", created_by=request.user)
        exam.questions.set(selected_questions)
        return render(request, 'question_bank/exam_detail.html', {'exam': exam})
    
    categories = Category.objects.all()
    return render(request, 'question_bank/generate_exam.html', {'categories': categories})
