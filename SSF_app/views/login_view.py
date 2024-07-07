from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Check user's group and redirect accordingly
            if user.groups.filter(name='föreningsadministratör').exists():
                return redirect('föreningsadmin_landing')
            elif user.groups.filter(name='domaradmin').exists():
                return redirect('domaradmin_landing')
            else:
                return redirect('home')  # Default redirection if no group matches
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'login.html')

@login_required
def home_view(request):
    return redirect('/')