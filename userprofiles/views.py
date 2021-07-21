from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.contrib import messages
from mainapp.models import Challenges, ChallengeAudience, ChallengeTag
from .models import Profile
from users.models import CustomUser
# Create your views here.
@login_required
def profile(request):
    user = request.user
    favourite_posts = Challenges.objects.all().filter(favourite=user)[:4]
    avatar_list = []
    avatar_name = request.user.username
    for ava in avatar_name:
        avatar_list.append(ava)
    
    avatar_holder = avatar_list[0]
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('userprofiles:profile')
        else:
            messages.warning(request, 'Please correct the errors shown.')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
    'p_form':p_form,
    "account_page":"active",
    'favourite_posts':favourite_posts,
    'avatar_holder':avatar_holder
    }
    return render(request, 'users/profile.html', context)
    

@login_required
def get_user_details(request, id):
    # user = CustomUser.username
    the_user = get_object_or_404(Profile, id=id)
    favourite_posts = Challenges.objects.all().filter(favourite=the_user.user)
    view_contact_info = False
    view_bookmarks = False

    avatar_list = []
    avatar_name = the_user.user.username
    for ava in avatar_name:
        avatar_list.append(ava)
    
    avatar_holder = avatar_list[0]

    if the_user.consent_to_view_my_bookmarks == True:
        view_bookmarks = True

    if the_user.consent_to_share_my_information == True:
        view_contact_info = True
    context = {
        'the_user':the_user,
        'favourite_posts':favourite_posts,
        'view_bookmarks':view_bookmarks,
        'view_contact_info':view_contact_info,
        'avatar_holder':avatar_holder,
    }
    return render(request, 'users/the_user.html', context)

