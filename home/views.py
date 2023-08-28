from django.shortcuts import render
from .forms import CaptchaForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = CaptchaForm(request.POST)

        if form.is_valid():
            return HttpResponse('Dados preenchidos com sucesso!')
        else:
            return render(request, 'home.html', {'form': form})
    else:
        form = CaptchaForm()
        return render(request, 'home.html', {'form': form})
