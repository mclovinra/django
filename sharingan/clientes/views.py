from django.shortcuts import render, redirect
from .forms import ClienteForm

def registro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'registro.html', {'form': form})
