# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm

# Home view with introduction and blog posts
def home(request):
    posts = Post.objects.all().order_by('-created_at')

    # Your introduction text
    introduction = """
    Hi, my name is Abida Begam Mohammad. I’m a Software Engineer with over two years of experience as a Backend Python Engineer.
    I’m experienced in Python, Flask, Fast API, and Django, and I use tools like Docker and AWS to make deploying and scaling applications simple.
    In my previous role at CMC Limited, I developed RESTful APIs for performance management systems, optimized database queries, and improved application performance using Oracle and PostgreSQL.
    During my internship, I worked on a personal finance tracker, gaining hands-on experience in designing and building backend systems.
    I enjoy working on open-source projects to learn new things and stay updated with the latest technologies.
    I’m also currently pursuing AWS Cloud Practitioner certification to enhance my cloud skills.
    I’m passionate about solving challenges in backend development and contributing to impactful projects.
    I have a bachelor’s degree in computer science from the University of the People, graduating with a GPA of 3.8.
    """

    return render(request, 'blog/home.html', {'posts': posts, 'introduction': introduction})

# Post detail view with comments functionality
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

# About view with information about the site or the author
def about(request):
    about_text = """
    Hi, my name is Abida Begam Mohammad. I’m a Software Engineer with over two years of experience as a Backend Python Engineer. 
I’m experienced in Python, Flask, Fast API, and Django, and I use tools like Docker and AWS to make deploying and scaling applications simple.
In my previous role in CMC Limited, I developed RESTful APIs for performance management systems, optimized database queries, and improved application performance using Oracle and PostgreSQL. 
During my internship, I worked on a personal finance tracker, gaining hands-on experience in designing and building backend systems.
I enjoy working on open-source projects to learn new things and stay updated with the latest technologies. 
I’m also currently pursuing AWS Cloud Practitioner certification to enhance my cloud skills. 
I’m passionate about solving challenges in backend development and contributing to impactful projects.
I have a bachelor’s degree in computer science from the University of the People, graduating with a GPA of 3.1
    """
    return render(request, 'blog/about.html', {'about_text': about_text})
