from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from posts.forms import AddPostForm
from posts.models import Post
from django.contrib.auth.models import Group, User
from group.forms import AddSubGroup
from group.models import SubGroup


# Create your views here.
def index(request):
    posts = Post.objects.all()
    groups = SubGroup.objects.all()
    return render(request, 'index.html', {'posts': posts, "groups": groups})


def addPost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                user=request.user,
                body=data['body'],
                posted_in=data['posted_in']
                # time_created=data['time_created']
            )
        return HttpResponseRedirect(reverse('home'))
    form = AddPostForm()
    return render(request, 'generic_form.html', {'form': form})


def addSubgroup(request):
    if request.method == 'POST':
        form = AddSubGroup(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            SubGroup.objects.create(
                created_by=request.user,
                group_name=data['group_name']
            )
        return HttpResponseRedirect(reverse('home'))
    form = AddSubGroup()
    return render(request, 'generic_form.html', {'form': form})