from django.shortcuts import render
from .models import Project, ProjectCategory, Blog, TeamMember, Testimonial, Contact

# Create your views here.
def index(request):
    projects = Project.objects.all()[:4]  # Fetch only the latest 4 projects
    blogs = Blog.objects.all()[:3]  # Fetch only the latest 3 blogs
    teams = TeamMember.objects.all()[:4]
    testimonials = Testimonial.objects.all()
    context = {
        'projects': projects,
        'blogs': blogs,
        'teams': teams,
        'testimonials': testimonials,
        'title': 'Home'
    }
    return render(request, 'mysite/index.html', context)

def about_us(request):
    teams = TeamMember.objects.all()
    context = {
        'teams': teams,
        'title': 'About Us'
    }
    return render(request, 'mysite/about.html', context)

def services(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials,
        'title': 'Services'
    }
    return render(request, 'mysite/service.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'title': 'Projects'
    }
    return render(request, 'mysite/project.html', context)

def features(request):
    return render(request, 'mysite/feature.html')

def blogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
        'title': 'Blogs'
    }
    return render(request, 'mysite/blog.html', context)

def our_team(request):
    teams = TeamMember.objects.all()
    context = {
        'teams': teams,
        'title': 'Our Team'
    }
    return render(request, 'mysite/team.html', context)

def testimonial(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials,
        'title': 'Testimonials'
    }
    return render(request, 'mysite/testimonial.html', context)

def error_page(request):
    return render(request, 'mysite/404.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        project = request.POST.get('project')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save the contact message to the database
        contacts = Contact(name=name, email=email, phone=phone, project=project, subject=subject, message=message)
        contacts.save()
        
    context = {
        'title': 'Contact Us',
        'success': True
    }
    return render(request, 'mysite/contact.html', context)