import re
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from .models import Choice, Info, Question, Studying, Pysyntax, DjangoInfo , Pyintro
from .forms import InfoForm, AuthenticationForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm
from django.urls import reverse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model

def index(request):
    return render(request, 'info/index.html')

def about(request):
    return render(request, 'info/about.html')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "info/login.html"
    
    def get_success_url(self):
        return reverse_lazy('info:register')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'info/register.html'
    success_url = reverse_lazy('login')

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()  # Call the function to get the user model class
    form_class = ProfileUserForm
    template_name = 'info/profile.html'
    
    def get_success_url(self):
        return reverse_lazy('info:profile')
    
    def get_object(self,queryset=None):
        return self.request.user
    





def log_out(request):
    logout(request)
    return HttpResponseRedirect("/info/login")

def python_introduction(request):
    contents = Pyintro.objects.all()
    return render(request, "info/intro.html",{'contents': contents})

def python_syntax(request):
    contents = Pysyntax.objects.all()
    return render(request, 'info/syntax.html', {'contents': contents})

def error(request):
    return render(request, "info/error.html")

def create(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/info/')
    else:
        form = InfoForm()
    
    return render(request, 'info/create.html', {'form': form})

def add_info(request):
    info = Info.objects.all()
    return render(request, 'info/infousers.html', {"info": info})

def django_info(request):
    contents = DjangoInfo.objects.all()
    return render(request, 'info/django.html', {'contents': contents})


def flask_info(request):
    return render(request, 'info/flask.html')

def pandas_info(request):
    return render(request, 'info/pandas.html')

def numpy_info(request):
    return render(request, 'info/numpy.html')


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "info/detail.html", {"question": question})


def results(request):
    # Retrieve all questions
    questions = Question.objects.all()
    
    # Check if there are no questions available
    if not questions:
        return render(
            request,
            "info/detail.html",
            {
                "error_message": "No questions available.",
            },
        )

    return render(request, "info/results.html", {"questions": questions})

def vote(request):
    questions = Question.objects.all()

    if request.method == 'POST':
        try:
            question_id = request.POST["question_id"]
            question = get_object_or_404(questions, pk=question_id)
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist, Question.DoesNotExist):
            return render(
                request,
                "info/detail.html",
                {
                    "questions": questions,
                    "error_message": "You didn't select a choice.",
                },
            )
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse("info:results"))

    return render(request, "info/detail.html", {"questions": questions})

def studying(request):
    content = Studying.objects.all()
    return render(request, 'info/studying.html',{"content":content})
        
class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("info:password_change_done")
    template_name = "info/password_change_form.html"