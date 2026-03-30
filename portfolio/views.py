from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, Education, ContactMessage
from .forms import ContactForm


def home(request):
    profile = Profile.objects.first()
    featured_projects = Project.objects.all()[:3]
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'active': 'home',
    }
    return render(request, 'portfolio/home.html', context)


def about(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile,
        'active': 'about',
    }
    return render(request, 'portfolio/about.html', context)


def skills(request):
    profile = Profile.objects.first()
    languages = Skill.objects.filter(category='language')
    frameworks = Skill.objects.filter(category='framework')
    tools = Skill.objects.filter(category='tool')
    others = Skill.objects.filter(category='other')
    context = {
        'profile': profile,
        'languages': languages,
        'frameworks': frameworks,
        'tools': tools,
        'others': others,
        'active': 'skills',
    }
    return render(request, 'portfolio/skills.html', context)


def projects(request):
    profile = Profile.objects.first()
    all_projects = Project.objects.all()
    context = {
        'profile': profile,
        'projects': all_projects,
        'active': 'projects',
    }
    return render(request, 'portfolio/projects.html', context)


def education(request):
    profile = Profile.objects.first()
    all_education = Education.objects.all()
    context = {
        'profile': profile,
        'education_list': all_education,
        'active': 'education',
    }
    return render(request, 'portfolio/education.html', context)


def contact(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent! I will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    context = {
        'profile': profile,
        'form': form,
        'active': 'contact',
    }
    return render(request, 'portfolio/contact.html', context)
