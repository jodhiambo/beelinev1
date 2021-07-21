from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from .forms import CreatePreapprovedChallengeForm
from django.db.models import Q, F
from django.utils import timezone
from datetime import datetime
from .models import Challenges, ChallengeTag, ChallengeAudience
from userprofiles.models import Profile
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import JsonResponse
from django.template.loader import render_to_string

"""This is a filter for Challenges with tags e.g Education, Science, Energy e.t.c"""
def tagged(request, id):
    tag = get_object_or_404(ChallengeTag, id=id)
    the_challenges = Challenges.objects.all().filter(Q(status='Open') | Q(status='Rolling'))
    challenges = the_challenges.filter(tags=tag).order_by('-date_posted')
    the_tags = ChallengeTag.objects.all()[:12]

    paginator = Paginator(challenges, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    context = {
        'tag':tag,
        'the_tags':the_tags,
        'challenges':posts
    }
    return render(request, 'mainapp/tagged-detail.html', context)


"""This is a filter for Challenges listed under Audiences e.g Youth, Women e.t.c"""
def audience_tagged(request, id):
    audience = get_object_or_404(ChallengeAudience, id=id)
    the_challenges = Challenges.objects.all().filter(Q(status='Open') | Q(status='Rolling'))
    challenges = the_challenges.filter(targeted_audience=audience).order_by('-date_posted')
    the_audiences = ChallengeAudience.objects.all()[:12]

    paginator = Paginator(challenges, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    context = {
        'audience':audience,
        'the_audiences':the_audiences,
        'challenges':posts
    }
    return render(request, 'mainapp/audience_detail.html', context)

def error_404(request, exception):
    data = {}
    return render(request, 'mainapp/404.html', data)

def error_500(request):
        data = {}
        return render(request,'mainapp/500.html', data)

"""This displays *some* of the challenges in the system"""
def home(request):
    user = request.user
    latest_challenges = Challenges.objects.all().filter(status='Open').order_by('-date_posted').reverse()[:12]
    the_tags = ChallengeTag.objects.all()[:10]
    the_audiences=ChallengeAudience.objects.all()[:10]

    ten_audiences = the_audiences[:10]
    context = {
    'latest_challenges':latest_challenges,
    'the_tags':the_tags,
    'the_audiences':the_audiences
    }
    return render(request, 'mainapp/index.html', context)

def all_categories(request):
    allcategories = ChallengeTag.objects.all()
    return render(request, 'mainapp/allcategories.html', {'allcategories':allcategories })

"""This displays all the latest challenges in the system"""
def challenges(request):
    ctx = {}
    url_parameter = request.GET.get("q")
    if url_parameter:
        posts_list = Challenges.objects.filter(offered_by__icontains=url_parameter)
    else:
        posts_list = Challenges.objects.all().filter(Q(status='Open') | Q(status='Rolling')).order_by('-id')

    ctx["posts_list"] = posts_list
    the_tags = ChallengeTag.objects.all()[:10]
    the_audiences=ChallengeAudience.objects.all()[:10]
    paginator = Paginator(posts_list, 18)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    if request.is_ajax():
        html = render_to_string(
            template_name = "mainapp/challenges-partial.html",
            context={"posts":posts}
        )
        data_dict = {"html_from_view":html}
        return JsonResponse(data=data_dict, safe=False)

    context = {
    'the_tags':the_tags,
    'posts':posts,
    'the_audiences':the_audiences
    }
    return render(request, 'mainapp/challenges.html', context)


def open_challenges(request):
    challenges = Challenges.objects.all().filter(status='Open').order_by('date_posted')
    the_tags = ChallengeTag.objects.all()[:10]
    the_audiences=ChallengeAudience.objects.all()[:10]
    paginator = Paginator(challenges, 4)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    context = {
        'challenges':posts,
        'the_tags':the_tags,
        'the_audiences':the_audiences
        }
    return render(request, 'mainapp/open-challenges.html', context)

def coming_soon_challenges(request):
    challenges = Challenges.objects.all().filter(status='Coming Soon').order_by('date_posted')
    the_tags = ChallengeTag.objects.all()[:10]
    the_audiences=ChallengeAudience.objects.all()[:10]
    paginator = Paginator(challenges, 18)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    context = {
        'challenges':posts,
        'the_tags':the_tags,
        'the_audiences':the_audiences
    }
    return render(request, 'mainapp/coming-soon-challenges.html', context)

def archived_challenges(request):
    challenges = Challenges.objects.all().filter(status='Archived').order_by('date_posted')
    the_tags = ChallengeTag.objects.all()[:10]
    the_audiences=ChallengeAudience.objects.all()[:10]
    paginator = Paginator(challenges, 18)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    context = {
        'challenges':posts,
        'the_tags':the_tags,
        'posts':posts,
        'the_audiences':the_audiences
        }
    return render(request, 'mainapp/archived-challenges.html', context)

def rolling_challenges(request):
    challenges = Challenges.objects.all().filter(status='Rolling').order_by('date_posted')
    the_tags = ChallengeTag.objects.all()[:10]
    the_audiences=ChallengeAudience.objects.all()[:10]
    paginator = Paginator(challenges, 18)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    context = {
        'challenges':challenges,
        'the_tags':the_tags,
        'posts':posts,
        'the_audiences':the_audiences
    }
    return render(request, 'mainapp/rolling-challenges.html', context)


def about(request):
    return render(request, 'mainapp/about.html')

def privacy_policy(request):
    return render(request, 'mainapp/privacy_policy.html')


"""This displays the details of a selected Challenge"""
def challenge_detail(request, id, slug):
    the_tags = ChallengeTag.objects.all()
    allchallenges = Challenges.objects.all().order_by('-date_posted')[:3]
    the_post = get_object_or_404(Challenges, id=id, slug=slug)
    interested_people = []
    for cha in the_post.favourite.all():
        interested_people.append(cha)

    is_favourite = False
    if the_post.favourite.filter(id=request.user.id).exists():
        is_favourite = True

    related_challenges = []
    for rel_cha in allchallenges:
        if rel_cha.id != the_post.id:
            related_challenges.append(rel_cha)
    the_list = related_challenges[:3]

    context = {
        'the_post':the_post,
        'allchallenges':the_list,
        'is_favourite':is_favourite,
        'interested_people':interested_people
        }
    return render(request, 'mainapp/detail.html', context)

def interested_challenges_list(request, id, slug):
    the_post = get_object_or_404(Challenges, id=id, slug=slug)

    interested_people = []
    the_tags=[]
    the_audiences=[]

    for tag in ChallengeTag.objects.all():
        the_tags.append(tag)

    for audience in ChallengeAudience.objects.all():
        the_audiences.append(audience)

    for cha in the_post.favourite.all():
        hisprofile = Profile.objects.get(user=cha)
        interested_people.append(hisprofile)

    ten_tags = the_tags[:10]
    ten_audiences = the_audiences[:10]

    context = {
        'interested_people':interested_people,
        'ten_tags':ten_tags,
        'ten_audiences':ten_audiences
        }
    return render(request, 'users/users.html', context)

def favourite_challenge_list(request):
    user = request.user
    favourite_posts = Challenges.objects.all().filter(favourite=user).order_by('date_posted')
    paginator = Paginator(favourite_posts, 18)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts':posts
    }
    return render(request, 'mainapp/favourite_challenge_list.html', context)

def favourite_post(request, id, slug):
    post = get_object_or_404(Challenges, id=id, slug=slug)
    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)
    else:
        post.favourite.add(request.user)
    return HttpResponseRedirect(reverse('mainapp:detail', args=(post.id, post.slug)))

def search_results(request):
    query = request.GET.get('q')
    challenges = Challenges.objects.filter(offered_by__icontains=query)

    paginator = Paginator(challenges, 4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    context = {'posts':posts, 'query':query}

    return render(request, 'mainapp/search_results.html', context)


# def search_results(request):
#     query = request.GET.get('q')
#     challenges = Challenges.objects.filter(
#     Q(title__icontains=query) | Q(description__icontains=query) |
#     Q(challenge_summary__icontains=query) | Q(offered_by__icontains=query) |
#     Q(status__icontains=query) | Q(targeted_audience__name__icontains=query) |
#     Q(tags__name__icontains=query))

#     paginator = Paginator(challenges, 4)
#     try:
#         page = int(request.GET.get('page', '1'))
#     except:
#         page = 1
#     try:
#         posts = paginator.page(page)
#     except(EmptyPage, InvalidPage):
#         posts = paginator.page(paginator.num_pages)

#     context = {'posts':posts, 'query':query}

#     return render(request, 'mainapp/search_results.html', context)

@login_required
def submit_a_challenge(request):
    if request.method == 'POST':
        form = CreatePreapprovedChallengeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('mainapp:homepage')
    else:
        form = CreatePreapprovedChallengeForm()
    context = {'form':form}
    return render(request, 'mainapp/submit-a-challenge.html', context)
