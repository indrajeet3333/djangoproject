import requests
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from .models import client, appointments, AuthUser
from django.contrib.auth.hashers import check_password
def appointment(request):
    allAppointments = appointments.objects.all()
    return render(request, 'patiladmin/appointments.html', {'appointments': allAppointments})
def schedule(request):
    '''
    ~~~~~~~~~~~~~~~~ AJAX REQUEST POST PARAMS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    test : Name of the Client to schedule meeting with,
    placeA: Place of the meeting - Either Chamber or Office,
    withA: Person of the meeting - Advocate to meet with,
    dateA : Date and Time of the Meeting
    '''
    nameofclient = request.POST["test"]
    mPlace = request.POST["placeA"]
    mWith = request.POST["withA"]
    dateTimeStr = request.POST["dateA"]

    firstname = nameofclient.split()[0]
    contact = client.objects.filter(first_name=firstname)[0].contact
    
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
    msg = "Hello " + firstname + ",%0aYour appointment with "+ mWith +" is now scheduled for " + \
        date + " at " + time + " %0aPlace: " + mPlace + "%0a %0aRegards,%0aAdv. Prashant Patil"
    r = requests.get("http://api.msg91.com/api/sendhttp.php?country=91&sender=TESTIN&route=4&mobiles="+str(contact)+"&authkey=256187AKWh6ZGX9j5c385774&message=" + msg)
    print("SMS Status Code " + str(r))
    appointment_data = appointments(person=nameofclient,dtOfApmt=date,tmOfApmt=time)
    appointment_data.save()
    ajResponse = {'request':'ok', 'for': nameofclient, 'date': date,'time': time}
    return JsonResponse(ajResponse)
    #return render(request, 'patiladmin/schedule.html', {'name': firstname,'date': date,'time':time})
def clientlist(request):
    clist = client.objects.all()
    return render(request, 'patiladmin/clients.html', {'clients': clist})
def index(request):
    return render(request,'patiladmin/index.html')
def submit(request):  
    synopsis = request.POST["cSynop"]
    if synopsis:
        client_data = client(first_name=request.POST["firstName"],
                            last_name=request.POST["lastName"],
                            contact=request.POST["contact"],
                            email=request.POST["email"],
                            pVisit=request.POST["pVisit"],
                            address=request.POST["address"],
                            city=request.POST["city"],
                            state=request.POST["state"],
                            zipcode=request.POST["zip"],
                            toMeet=request.POST["toMeet"],
                            hAbout=request.POST["hAbout"],
                            caseSynopsis=request.POST["cSynop"])
    else:
        client_data = client(first_name=request.POST["firstName"],
                        last_name=request.POST["lastName"],
                        contact=request.POST["contact"],
                        email=request.POST["email"],
                        pVisit=request.POST["pVisit"],
                        address=request.POST["address"],
                        city=request.POST["city"],
                        state=request.POST["state"],
                        zipcode=request.POST["zip"],
                        toMeet=request.POST["toMeet"],
                        hAbout=request.POST["hAbout"])
    client_data.save()
    return render(request, 'patiladmin/submit.html')

def clientSynopsis(request):
        contact = request.POST.get('mobile')
        try:
            cSynopsis = client.objects.filter(contact=contact)[0]
            return HttpResponse(cSynopsis.caseSynopsis)
        except IndexError:
            return HttpResponse("failure")
            
def clientAddress(request):
        contact = request.POST.get('mobile')
        try:
            cSynopsis = client.objects.filter(contact=contact)[0]
            return HttpResponse(cSynopsis.address)
        except IndexError:
            return HttpResponse("failure")

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
    
