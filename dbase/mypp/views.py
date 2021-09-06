from django.shortcuts import render
from . models import User,company,customer,order


# Create your views here.
def index(request):

    user = User.objects.all()
    comp = company.objects.all()


    return render(request , 'mypp/index.html' ,{'user':user, 'company':comp})


def myorder(request):
    cust = customer.objects.all()
    orders = order.objects.all()

    

    return render(request , 'mypp/order.html' , {'cust':cust,'order':orders})