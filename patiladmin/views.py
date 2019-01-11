from django.http import HttpResponse
from django.shortcuts import render
from .models import client
def clientlist(request):
    clist = client.objects.all()
    return render(request, 'patiladmin/clients.html', {'clients': clist})
def index(request):
    return render(request,'patiladmin/index.html')
def submit(request):
    client_data = client(first_name=request.POST["firstName"],
                         last_name=request.POST["lastName"],
                         contact=request.POST["contact"],
                         email=request.POST["email"],
                         pVisit=request.POST["pVisit"],
                         address=request.POST["address"],
                         city=request.POST["city"],
                         state=request.POST["state"],
                         zipcode=request.POST["zip"])
    client_data.save()
    return render(request, 'patiladmin/submit.html')
