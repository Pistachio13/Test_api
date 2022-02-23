from django.shortcuts import render

# Create your views here.
def my_templates(request):
    return render(request, "MyTemplates.html")