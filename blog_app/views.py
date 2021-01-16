from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Contact, Project

global footer
footer = "Bam"

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'blog/post_list.html', {'posts': posts, 'footer': footer})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'footer': footer})

def home(request):
    return render(request, 'blog/home.html')

def contact(request):
    contacts = Contact.objects.order_by('url')
    return render(request, 'blog/contact.html', { 'contacts' : contacts, 'footer': footer})

def projects(request):
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'blog/projects.html', { 'projects': projects, 'footer': footer})
