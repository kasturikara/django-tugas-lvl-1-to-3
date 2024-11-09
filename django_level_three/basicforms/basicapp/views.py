from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['verify_email'])
            print(form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form': form})
