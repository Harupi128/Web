from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import ContactForm
from django.shortcuts import redirect
# Create your views here.

class Top(generic.FormView):
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')
    template_name = 'contact/top.html'
    def form_valid(self,form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        text = form.cleaned_data.get('text')
        category = form.cleaned_data.get('category')
        return redirect('contact:thanks')


class Thanks(generic.TemplateView):
    template_name = 'contact/thanks.html'