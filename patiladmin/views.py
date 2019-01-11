import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from .models import client
def schedule(request):
    nameofclient = request.POST["test"]
    firstname = nameofclient.split()[0]
    contact = client.objects.filter(first_name=firstname)[0].contact
    print(contact)
    msg = "Hello " + firstname + ". Your appointment with your lawyer is now scheduled for " + \
        request.POST["dateA"] + " at " + request.POST["timeA"]
    r = requests.get("http://api.msg91.com/api/sendhttp.php?country=91&sender=TESTIN&route=4&mobiles="+str(contact)+"&authkey=256187AKWh6ZGX9j5c385774&message=" + msg)
    return HttpResponse("Appointment Scheduled for " + firstname)
def clientlist(request):
    clist = client.objects.all()
    return render(request, 'patiladmin/clients.html', {'clients': clist})
def index(request):
    return render(request,'patiladmin/index.html')
def submit(request):
    name = request.POST["firstName"]
    mobile = request.POST["contact"]
    client_data = client(first_name=name,
                         last_name=request.POST["lastName"],
                         contact=mobile,
                         email=request.POST["email"],
                         pVisit=request.POST["pVisit"],
                         address=request.POST["address"],
                         city=request.POST["city"],
                         state=request.POST["state"],
                         zipcode=request.POST["zip"])
    client_data.save()
    return render(request, 'patiladmin/submit.html')



