from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mysite/index.html')

def about_us(request):
    return render(request, 'mysite/about.html')

def services(request):
    return render(request, 'mysite/service.html')

def projects(request):
    return render(request, 'mysite/project.html')

def features(request):
    return render(request, 'mysite/feature.html')

def blogs(request):
    return render(request, 'mysite/blog.html')

def our_team(request):
    return render(request, 'mysite/team.html')

def testimonial(request):
    return render(request, 'mysite/testimonial.html')

def error_page(request):
    return render(request, 'mysite/404.html')

def contacts(request):
    return render(request, 'mysite/contact.html')