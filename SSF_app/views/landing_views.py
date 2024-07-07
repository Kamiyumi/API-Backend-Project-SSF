from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def föreningsadmin_landing_page(request):
    user = request.user
    if user.groups.filter(name='Föreningsadministratör').exists():
        return render(request, 'föreningsadmin_landing.html')
    else:
        return render(request, 'no_permission.html')

@login_required
def domaradmin_landing_page(request):
    user = request.user
    if user.groups.filter(name='Domaradministratör').exists():
        return render(request, 'domaradministratör_landing.html')
    else:
        return render(request, 'no_permission.html')

@login_required
def no_permission_view(request):
    return render(request, 'no_permission.html')


