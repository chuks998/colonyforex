from django.shortcuts import render
from django.views.generic import ListView
from .models import Signal



def index_view(request):
    template = 'signals.html'
    return render(request, template)

class SignalView(ListView):
    model = Signal
    template_name = 'signals.html'
    ordering = ['-date_posted']
    paginate_by = 10
    context_object_name = 'signal'