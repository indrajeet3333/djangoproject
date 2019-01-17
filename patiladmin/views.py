import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from .models import client, appointments, AuthUser
from django.contrib.auth.hashers import check_password
def appointment(request):
    allAppointments = appointments.objects.all()
    return render(request, 'patiladmin/appointments.html', {'appointments': allAppointments})
def schedule(request):
    nameofclient = request.POST["test"]
    firstname = nameofclient.split()[0]
    contact = client.objects.filter(first_name=firstname)[0].contact
    dateTimeStr = request.POST["dateA"]
    months = ("Jan ", "Feb ", "Mar ", "Apr ", "May ", "Jun ", "Jul ", "Aug ", "Sep ", "Oct ", "Nov ", "Dec ")
    yr = dateTimeStr[0:4]
    mm = int(dateTimeStr[5:7])
    month = months[(mm-1)]
    day = dateTimeStr[8:11]
    date = day + month + yr
    hh = int(dateTimeStr[11:13])
    mm = dateTimeStr[14:16]
    if (hh > 12):
        Hr = (hh-12)
        fm = " PM"
    else:
        Hr = hh
        fm = " AM"
    time = str(Hr) + ":" + mm + fm
    print(date + " " + time)
    msg = "Hello " + firstname + ". Your appointment with your lawyer is now scheduled for " + \
        date + " at " + time
    r = requests.get("http://api.msg91.com/api/sendhttp.php?country=91&sender=TESTIN&route=4&mobiles="+str(contact)+"&authkey=256187AKWh6ZGX9j5c385774&message=" + msg)
    print("SMS Status Code " + str(r))
    appointment_data = appointments(person=nameofclient,dtOfApmt=date,tmOfApmt=time)
    appointment_data.save()
    return render(request, 'patiladmin/schedule.html', {'name': firstname,'date': date,'time':time})
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
def removeAppointment(request):
    if request.is_ajax():
        uName = request.POST.get('uName')
        passW = request.POST.get('passW')
        rmAppID = request.POST.get('rmvAppID')
        try:
            admin = AuthUser.objects.filter(username=uName)[0]
            if(check_password(passW, admin.password)):
                print("Authentication Valid! Deleting Appointment!")
                deleteStatus = appointments.objects.filter(id=rmAppID)[0].delete()
                return HttpResponse("success")
            else:
                return HttpResponse("failure")
        except IndexError:
            return HttpResponse("failure")
    
