from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Contact, Project

global footer
footer = "<a rel=\"license\" href=\"http://creativecommons.org/licenses/by-sa/4.0/\"><img alt=\"Creative Commons License\" style=\"border-width:0\" src=\"https://i.creativecommons.org/l/by-sa/4.0/80x15.png\" /></a><br />This work is licensed under a <a rel=\"license\" href=\"http://creativecommons.org/licenses/by-sa/4.0/\">Creative Commons Attribution-ShareAlike 4.0 International License</a>."

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
