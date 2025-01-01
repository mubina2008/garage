from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import Profile
from .forms import ProfileEditForm, UserEditForm

def dashboard_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'pages/user_profile.html', context=context)



def user_register(request):
    if request.method =="POST":
        user_form = UserRegistrationForm(request.POST)
        new_user = user_form.save(commit=False)
        new_user.sit_password(
            user_form.cleaned_data["password"]
        )
        new_user.save()
        Profile.objects.create(user=new_user)
        context = {
            'new_user': new_user
        }
        return render(request,'account/register_done.html',context=context)

    else:
        user_form = UserRegistrationForm()
        context = {
            "user_form": user_form
        }
        return render(request,'account/register.html',context=context)


def edit_user(request):
    if request.mothod =="POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request,'account/profile_edit.html',{"user_form": user_form, "profile_form": profile_form})