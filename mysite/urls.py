from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about_us, name='about_us'),
    path('services/', views.services, name='service'),
    path('projects/', views.projects, name='project'),
    path('features/', views.features, name='feature'),
    path('blogs/', views.blogs, name='blog'),
    path('our-team/', views.our_team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('404/', views.error_page, name='error_page'),
    path('contact-us/', views.contacts, name='contact'),
    
]