from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Travel
from .forms import OrderForm


def travellist(request):
    travel = Travel.objects.all()
    return render(request, 'travels/travellist.html', {'travel': travel})

# Create your views here.
class traveldetail(DetailView):
    model = Travel
    template_name = 'travels/travel_detail.html'
    context_object_name = 'travel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(initial={'user_travel_name': self.object.travel_name})
        return context



def create_order(request):
    success_message = None

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = 'Замовлення успішно створено!'
    else:
        form = OrderForm()

    context = {'form': form, 'success_message': success_message}
    return render(request, 'travels/create_order.html', context)