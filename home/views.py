from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def enter(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'index.html', {'username': request.user.username})


def log_out(request):
    logout(request)
    return redirect('enter')

def get_user_avatar(strategy, details, response, uid, user, *args, **kwargs):
    social = kwargs.get('social') or strategy.storage.user.get_social_auth(
        strategy.backend.name,
        uid
    )
    url = None
    if strategy.backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']

    if url:
        social.set_extra_data({'photo': url})