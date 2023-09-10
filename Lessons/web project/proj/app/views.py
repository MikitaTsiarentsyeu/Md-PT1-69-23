from django.shortcuts import render, HttpResponse, redirect
import datetime
from .models import Author, Post
from .forms import AddPost, AddPostModelForm

# Create your views here.
def test(request):
    # print("test view")
    now = datetime.datetime.now()
    items = [1,2.0,"three"]
    return render(request, 'test.html', {"current_time":now, "items":items})


def post(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
    except:
        p = False
    return render(request, 'post.html', {'post':p})

def posts(request):
    posts = Post.objects.all()
    
    return render(request, 'posts.html', {'posts':posts})

def add_post(request):
    if request.method == "POST":
        form = AddPost(request.POST, request.FILES)

        if form.is_valid():
            post_entry = Post()
            post_entry.author = Author.objects.all()[0]
            post_entry.issued = datetime.datetime.now()
            post_entry.title = form.cleaned_data['title']
            post_entry.content = form.cleaned_data['content']
            post_entry.post_type = form.cleaned_data['post_type']
            post_entry.image = form.cleaned_data['image']
            post_entry.save()

            return redirect("posts")
    else:
        form = AddPost()
    return render(request, 'add_post.html', {'form':form})

def add_model_post(request):
    if request.method == "POST":
        form = AddPostModelForm(request.POST, request.FILES)

        if form.is_valid():
            post_entry = form.save(commit=False)
            post_entry.author = Author.objects.all()[0]
            post_entry.issued = datetime.datetime.now()
            post_entry.save()
            # form.save_m2m()

            return redirect("posts")
    else:
        form = AddPostModelForm()
    return render(request, 'add_post.html', {'form':form})