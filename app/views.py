from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from app.forms import TODOForm
from app.models import TODO
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('priority')
        context = {
            "form": form,
            "todos": todos
        }
        return render(request, 'index.html',context=context)
    else:
        return render(request, 'index.html')

def login_view(request):

    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request,'login.html',context=context)
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # print(f"*****{user}******* Authenticated")
            if user is not None:
                login(request,user)
                return redirect('home')
        else:
            context = {
            "form": form
            }
            return render(request,'login.html',context=context)

def signup(request):
    if request.method == 'GET':

        form = UserCreationForm()
        context = {
            "form": form
        }
        return render(request,'signup.html',context=context)
    
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            "form": form
        }

        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account successfully created for' + username)
                return redirect('login')

        else:
            return render(request,'signup.html',context=context)

def logout_view(request):
    logout(request)
    return redirect('home')
    # Redirect to a success page.

def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            print(f"-------------{form.cleaned_data}---------------")
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect('home')
        else:
            return render(request,'index.html',context=context)

def delete_todo(request):
    print("------------URL CHANGED 1---------")
    if request.method == 'POST':
        id = request.POST.get('del_id')
        print("id = ",id)
        TODO.objects.filter(id=id).delete()
        return redirect('home')
    return redirect('home')

def change_status(request):
    print("-------URL CHANGE 2-----------")

    if request.method == "POST":
        value = request.POST.get('x')
        id = request.POST.get('id')
        print("DATA: ",value)
        print("id = ",id)
        todo = TODO.objects.get(pk = id)
        print(todo.status)
        todo.status = value
        todo.save()
        return redirect('home')
    return redirect('home')