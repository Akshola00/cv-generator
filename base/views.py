from django.shortcuts import render
from .models import *


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
    context = {
        'userProfile':userProfile
    }
    return render(request, 'base/resume.html', context)