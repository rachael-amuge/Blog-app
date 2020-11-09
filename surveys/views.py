from django.shortcuts import render
from .models import *
from django.views import generic

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def index(request):
    post = Post.objects.all()[:10]
    context = {
        ' title': 'latest posts',
        'post': post
    }
    return render(request, 'index.html', context)


def details(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'details.html', context)


def login(request):
    search_form = SearchForm()
    add_form = AddForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                search_form = SearcForm()
                add_form = AddForm()
                new_user = NewUser.objects.all()
                render(request, 'newuser.html', {
                       'form': search_form, 'addform': add_form, 'newuser': new_user})
            else:
                pass

        else:
            form = LoginForm()
            context = {
                "form": form
            }
            return render(request, 'newuser.html', context)
