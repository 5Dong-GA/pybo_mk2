from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.db import transaction
from common.forms import UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


@transaction.atomic
def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, '변경사항이 저장되었습니다.')
        elif profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Bio 변경사항이 저장되었습니다.')
        else:
            messages.error(request, '무언가 잘못 되었습니다.')
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'common/profile.html', context={
        'user': request.user, 'user_form': user_form, 'profile_form': profile_form})


def page_not_found(request, exception):
    """
    404 Page Not Found
    """
    return render(request, 'common/404.html', {})