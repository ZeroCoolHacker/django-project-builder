from django.shortcuts import render
from .forms import AppForm

# Create your views here.
def create_app(request):
    form = AppForm()
    return render(request, template_name='dj_apps/create_app.html',context={'form': form})