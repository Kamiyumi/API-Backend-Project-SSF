from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_view(request):
    return HttpResponse("Hello, welcome to the home page!")


@login_required
def föreningsadmin_landing_page(request):
    user = request.user
    if user.groups.filter(name='föreningsadministratör').exists():
        return render(request, 'föreningsadmin_landing.html')
    else:
        # Redirect to a login page or a page indicating insufficient permissions
        return redirect('no_permission')  # Ensure you have a URL named 'no_permission'


def no_permission_view(request):
    return render(request, 'no_permission.html')