from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("account_settings")
    context = {}
    return render(request, "accounts/login.html", context)

def logout_user(request):
    logout(request)
    return redirect("login_page")

