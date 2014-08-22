from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def enter(request):
    return render(request, 'login.html')

def get_facebook_id(user):
    if user.social_auth.filter(provider='facebook').exists():
        return user.social_auth.first().uid
    return None


@login_required
def home(request):
    setattr(request.user, 'facebook_id', get_facebook_id(request.user))
    context = {
        'user': request.user
    }
    return render(request, 'index.html', context)


def log_out(request):
   return redirect('enter')

