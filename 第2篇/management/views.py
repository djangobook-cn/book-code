from django.contrib import auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from management.models import Book, Image


def index(request):
    user = request.user if request.user.is_authenticated else None
    context = {
        'active_menu': 'homepage',
        'user': user
    }
    return render(request, 'management/index.html', context)


def sign_up(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if password == '' or repeat_password == '':
            state = 'empty'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '')
            if User.objects.filter(username=username):
                state = 'user_exist'
            else:
                new_user = User.objects.create_user(username=username, password=password,
                                                    email=request.POST.get('email', ''))
                new_user.save()
                state = 'success'
    context = {
        'active_menu': 'homepage',
        'state': state,
        'user': None
    }
    return render(request, 'management/sign_up.html', context)


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            target_url = request.GET.get('next', reverse('homepage'))
            return HttpResponseRedirect(target_url)
        else:
            state = 'not_exist_or_password_error'
    context = {
        'active_menu': 'homepage',
        'state': state,
        'user': None
    }
    return render(request, 'management/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage'))


@login_required
def change_password(request):
    user = request.user
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif new_password != repeat_password:
                state = 'repeat_error'
            else:
                user.set_password(new_password)
                user.save()
                state = 'success'
        else:
            state = 'password_error'
    content = {
        'user': user,
        'active_menu': 'homepage',
        'state': state,
    }
    return render(request, 'management/change_password.html', content)


@login_required
def book_list(request, category='all'):
    user = request.user
    category_list = Book.objects.values_list('category', flat=True).distinct()
    if Book.objects.filter(category=category).count() == 0:
        category = 'all'
        books = Book.objects.all()
    else:
        books = Book.objects.filter(category=category)

    paginator = Paginator(books, 5)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {
        'user': user,
        'active_menu': 'view_book',
        'category_list': category_list,
        'query_category': category,
        'book_list': books
    }
    return render(request, 'management/book_list.html', context)


@login_required
def book_detail(request, book_id=1):
    user = request.user
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return HttpResponseRedirect(reverse('book_list', args=('all',)))
    content = {
        'user': user,
        'active_menu': 'view_book',
        'book': book,
    }
    return render(request, 'management/book_detail.html', content)


@user_passes_test(lambda u: u.is_staff)
def add_book(request):
    user = request.user
    state = None
    if request.method == 'POST':
        new_book = Book(
            name=request.POST.get('name', ''),
            author=request.POST.get('author', ''),
            category=request.POST.get('category', ''),
            price=request.POST.get('price', 0),
            publish_date=request.POST.get('publish_date', '')
        )
        new_book.save()
        state = 'success'
    context = {
        'user': user,
        'active_menu': 'add_book',
        'state': state,
    }
    return render(request, 'management/add_book.html', context)


@user_passes_test(lambda u: u.is_staff)
def add_img(request):
    user = request.user
    state = None
    if request.method == 'POST':
        try:
            new_img = Image(
                name=request.POST.get('name', ''),
                description=request.POST.get('description', ''),
                img=request.FILES.get('img', ''),
                book=Book.objects.get(pk=request.POST.get('book', ''))
            )
            new_img.save()
        except Book.DoesNotExist as e:
            state = 'error'
            print(e)
        else:
            state = 'success'
    content = {
        'user': user,
        'state': state,
        'book_list': Book.objects.all(),
        'active_menu': 'add_img',
    }
    return render(request, 'management/add_img.html', content)
