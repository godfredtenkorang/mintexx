from django.contrib import admin
from .models import *

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    

@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_completed')
    list_filter = ('title', 'category')
    search_fields = ('title', 'category__name')
    ordering = ('-date_completed',)
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('author',)
    search_fields = ('title', 'author')
    ordering = ('-published_date',)
    
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')
    ordering = ('name',)
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'profession')
    search_fields = ('client_name', 'profession')
    ordering = ('client_name',)
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    ordering = ('-created_at',)
    
