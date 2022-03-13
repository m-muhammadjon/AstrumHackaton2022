from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from health.models import Submission
from .forms import LoginForm, ProfileForm, UserRegistrationForm, UserEditionForm, ProfileEditForm
from .models import Doctor


def home_page(request):
    doctors = Doctor.objects.all()
    return render(request, 'index.html', {'doctors': doctors})


def register(request):
    user_form = UserRegistrationForm()
    profile_form = ProfileForm()
    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_profile = profile_form.save(commit=False)
            cd = user_form.cleaned_data
            new_user.set_password(cd['password'])
            new_user.save()
            new_profile.user = new_user
            new_profile.save()
            messages.success(request, 'Akkaunt muvaffaqiyatli yaratildi!')
            return redirect('account:user_login')
        else:
            errors = str(profile_form.errors) + str(user_form.errors)
            return render(request, 'auth/register.html',
                          {'u_form': user_form, 'p_form': profile_form, 'errors': errors})
    return render(request, 'auth/register.html', {'u_form': user_form, 'p_form': profile_form})


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Muvaffaqiyatli tizimga kirdi!')
                print(request.GET.get('next'))
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('account:home_page')
    return render(request, 'auth/log-in.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('account:home_page')


def profile(request, username):
    user = User.objects.get(username=username)
    submissons = Submission.objects.filter(user=user).order_by('-id')
    return render(request, 'profile.html', {'user': user,
                                            'submissions': submissons})


@login_required(login_url='/login/')
def edit_profile(request):
    user_form = UserEditionForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UserEditionForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profil'
                                      ' muvaffaqiyatli saqlandi!')
            return redirect(reverse('account:profile', kwargs={'username': str(request.user.username)}))
        print(user_form.errors, profile_form.errors)
    return render(request, 'edit-profile.html', {'u_form': user_form,
                                                 'p_form': profile_form})


@login_required(login_url='/login/')
def doctor_add_or_remove(request, id):
    doctor = Doctor.objects.get(id=id)
    if doctor in request.user.profile.doctors.all():
        request.user.profile.doctors.remove(doctor)
    else:
        request.user.profile.doctors.add(doctor)
    return redirect('account:doctors')


@login_required(login_url='/login/')
def doctors(request):
    doctors = request.user.profile.doctors.all()
    print(doctors)
    return render(request, 'doctors.html', {'doctors': doctors})
