from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from userprofiles.models import Profile
from .forms import CreateNewsForm, EditNewsForm
from django.utils.text import slugify
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def news_view(request):
    news_posts = News.objects.all().order_by('-date_posted')
    paginator = Paginator(news_posts, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try: 
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    context = {
        'news_posts': posts
    }
    return render(request, 'news/front-page.html', context)


def news_details_page(request, id, slug):
    news_post = get_object_or_404(News, id=id, slug=slug)
    context = {
        'news_post': news_post,
        # 'full_name':full_name
    }
    return render(request, 'news/detail.html', context)
