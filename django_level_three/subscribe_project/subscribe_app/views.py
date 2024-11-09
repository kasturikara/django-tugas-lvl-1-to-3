from django.shortcuts import render
from subscribe_app.models import Customer
from subscribe_app.forms import NewSubscriber


def index(request):
    return render(request, 'subscribe_app/index.html')

def customers(request):
    customers_list = Customer.objects.order_by('first_name')
    customers_dict = {'customers': customers_list}
    return render(request, 'subscribe_app/customers.html', context=customers_dict)
  
  
def subscribe(request):
    form = NewSubscriber()
    if request.method == 'POST':
        form = NewSubscriber(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return customers(request)
        else:
            print("Error: Form invalid")
    return render(request, 'subscribe_app/subscribe.html', {'form': form})