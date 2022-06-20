from unicodedata import category
from django import template
from django.shortcuts import render
from .models import Diary
from django.urls import reverse_lazy
from django.views import generic
from .forms import ContactForm
from django.shortcuts import redirect
# Create your views here.
def top(request):
    context = {
        'diary_list': Diary.objects.all(),
    }
    return render(request, 'diaries/diary_list.html', context)

class Top(generic.FormView):
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')
    template_name = 'diaries/contact.html'

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        text = form.cleaned_data.get('text')
        category = form.cleaned_data.get('category')
        return redirect('contact:thanks')

class Thanks(generic.TemplateView):
    template_name= 'diaries/thanks.html'