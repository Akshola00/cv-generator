from django.shortcuts import render
from .models import *
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        previous_work = request.POST.get("previous_work", "")
        skills = request.POST.get("skills", "")

        profile = Profile.objects.create(
            name=name,
            email=email,
            phone=phone,
            summary=summary,
            degree=degree,
            school=school,
            university=university,
            previous_work=previous_work,
            skills=skills,
        )
        profile.save()

    context = {}
    return render(request, "base/accept.html", context)

def resume(request, id):
    userProfile = Profile.objects.get(pk=id)
    template = loader.get_template('base/resume.html')
    html = template.render({
        'userProfile':userProfile
    })
    options = {
        'page-size' : 'letter',
        'encoding': 'UTF-8'
    }
    pdf = pdfkit.from_string(html, False, options)
    context = {
        'userProfile':userProfile
    }
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = 'resume.pdf'
    return response

def profile(request):
    allprofiles = Profile.objects.all()
    context = {
        'allprofiles':allprofiles
    }
    return render(request, 'base/profile.html', context)