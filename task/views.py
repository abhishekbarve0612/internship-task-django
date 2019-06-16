from django.shortcuts import render
from task.models import *
from task.forms import userForm
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = userForm(request.POST or None)
        if form.is_valid():
            a = request.POST['email']
            e =  user.objects.filter( email = a)
            if e:
                messages.error(request, "User with same Email already exist")
                messages.error(request, "Some Error Occured!!!")
                return render(request, "signup.html", { "form": form })
            alert = 1
            instance = form.save(commit=False)
            instance.is_active = False
            instance.save()
            messages.success(request, 'Registered Successfully')
        else:
            alert = 0
            messages.error(request, "Some Error Occured!!!")
    else:
        alert = None
        form = userForm()
    context = {
        "name": "name",
        "form": form,
        "email": "email",
        "alert": alert,
    }
    return render(request, "signup.html", context)

