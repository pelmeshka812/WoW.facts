from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Post


def index(request):
    num_posts = Post.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_posts': num_posts,
                 'num_visits': num_visits},  # num_visits appended
    )


def home(request):
    postList = Post.objects.filter(visible='1')
    paginator = Paginator(postList, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        "posts": posts,
        "title": "Главная страница блога",
        "desc": "Описание для главной страницы",
        "key": "ключевые, слова",
    }
    return render(request, "partial/home.html", context)


def single(request, id=None):
    post = get_object_or_404(Post, id=id)

    context = {
        "post": post,
    }
    return render(request, "partial/single.html", context)

"""
def add_like(request, slug):
    try:
        post = get_object_or_404(Post, slug=slug)
        post.like += 1
        post.save()
    except ObjectDoesNotExist:
        return Http404
    return redirect(request.GET.get('next', '/'))
"""


@login_required
def add_like(request):

    ans_id = None
    if request.method == 'GET':
        ans_id = request.GET['answer_id']

    likes = 0
    if ans_id:
        ans = Post.objects.get(id=(int(ans_id)))
        if ans:
            likes = ans.likes + 1
            ans.likes = likes
            ans.save()

    return HttpResponse(likes)


def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/account/loggedout/")
