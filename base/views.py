from django.shortcuts import render

# Create your views here.
def accept(request):
    context = {}
    return render(request, 'base/accept.html', context)