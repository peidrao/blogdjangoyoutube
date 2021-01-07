from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.
from .models import Contact
from .forms import ContactForm

from post.models import Post, Category, Comment

def index(request):
    post_random = Post.objects.order_by('?')[:4]
    post_latest = Post.objects.order_by('id')[:3]
    category = Category.objects.all()

    context = {
        'post_random': post_random,
        'post_latest': post_latest,
        'category': category
    }
    return render(request, 'index.html', context)

def blog(request):
    post = Post.objects.all()
    category = Category.objects.all()
    post_latest = Post.objects.order_by('id')[:3]


    paginator = Paginator(post, 4) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'category': category,
        'post_latest': post_latest,
    }
    return render(request, 'pages/blog.html', context)
    

def post_detail(request, id, slug):
    post = Post.objects.get(pk=id)
    comments = Comment.objects.filter(post_id=id, status='Lido')
    total = 0
    for i in comments:
        total = total + 1
    
    context = {
        'post': post,
        'comments': comments,
        'total': total}

    return render(request, 'pages/post_detail.html', context)
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']

            data.save()
            return HttpResponseRedirect('/contact/')
    form = ContactForm
    context = {
        'form': form
    }

    return render(request, 'pages/contact.html', context)

def about(request):
    return render(request, 'pages/about.html')