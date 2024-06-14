from django.shortcuts import render
from .models import Experience, Education, FutureInsight

# Create your views here.
def home(request):
    return render(request, 'myportfolio/home.html')

def experience(request):
    experiences = Experience.objects.all()
    return render(request, 'myportfolio/experience.html', {'experiences': experiences})

def education(request):
    educations = Education.objects.all()
    return render(request, 'myportfolio/education.html', {'educations': educations})

def future_insights(request):
    insights = FutureInsight.objects.all()
    return render(request, 'myportfolio/future_insights.html', {'insights': insights})