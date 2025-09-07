from django.db import models

# Project Category Model
class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    # description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Projects Model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/')
    date_completed = models.DateField()

    def __str__(self):
        return self.title


# Team Model

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)

    def __str__(self):
        return self.name


# Blog Model

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)

    def __str__(self):
        return self.title


# Testimonial Model

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    feedback = models.TextField()
    client_photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.client_name
    
    
# Contact Model (if needed in future)
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=15)
    project = models.CharField(max_length=200, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} <{self.email}>"