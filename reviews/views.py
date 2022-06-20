from django.shortcuts import render
from .models import Review
from django.views import generic
from django.urls import reverse_lazy
from .forms import ReviewCreateForm
# Create your views here.
class ReviewList(generic.ListView):
    model = Review

class ReviewDetail(generic.DetailView):
    model = Review

class ReviewCreate(generic.CreateView):
    model = Review
    form_class = ReviewCreateForm
    success_url = reverse_lazy('reviews:review_list')