import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.hashers import check_password
from .models import client, appointments, AuthUser
from djppproject.settings import EMAIL_HOST_PASSWORD


def index(request):
    return render(request, 'patiladmin/index.html', {'testdata': EMAIL_HOST_PASSWORD})


def clientlist(request):
    clist = client.objects.all()
    return render(request, 'patiladmin/clients.html', {'clients': clist})


def appointment(request):
    def getKey(key):
        return key.schOn

    appDbData = appointments.objects.all()
    allAppointments = [app for app in appDbData]
    allAppointments.sort(key=getKey, reverse=True)
    for app in allAppointments:
        print(app.schOn)
    return render(request, 'patiladmin/appointments.html', {'appointments': allAppointments})


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
                deleteStatus = appointments.objects.filter(id=rmAppID)[
                    0].delete()
                return HttpResponse("success")
            else:
                return HttpResponse("failure")
        except IndexError:
            return HttpResponse("failure")


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
                             caseSynopsis=synopsis)
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


def schedule(request):
    '''
    ~~~~~~~~~~~~~~~~ AJAX REQUEST POST PARAMS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    test : Name of the Client to schedule meeting with,
    placeA: Place of the meeting - Either Chamber or Office,
    withA: Person of the meeting - Advocate to meet with,
    dateA : Date and Time of the Meeting - Format of String: "23rd Jan 2019 at 10:30 AM"
    '''
    nameofclient = request.POST["test"]
    mPlace = request.POST["placeA"]
    mWith = request.POST["withA"]
    dateTimeStr = request.POST["dateA"].split(" at ")
    date = dateTimeStr[0]
    time = dateTimeStr[1]
    firstname = nameofclient.split()[0]
    contact = client.objects.filter(first_name=firstname)[0].contact
    '''~~~~~~~~~~~~~~~~ Save Appointment to DB ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    appointment_data = appointments(
        person=nameofclient, dtOfApmt=date, tmOfApmt=time)
    appointment_data.save()
    '''~~~~~~~~~~~~~~~~ Construct & Send Email ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    email_subject = 'Lawyer: Your is meeting scheduled for ' + date + " at " + time
    email_body = "<h4>Hello " + firstname + ",<br>Your meeting with " + mWith + " is now scheduled for " + \
        date + " at " + time + "<br>Place: " + mPlace + \
        "<br><br>Regards,<br>Adv. Prashant Patil</h4>"
    html_email = render_to_string('patiladmin/email_template.html', {
                                  'firstname': firstname, 'mWith': mWith, 'mPlace': mPlace, 'date': date, 'time': time})
    email_to = client.objects.filter(first_name=firstname)[0].email
    emailResponse = send_mail(email_subject, '', 'Lawyer',
                              [email_to], fail_silently=False, html_message=html_email)
    print("Number of Emails sent : " + str(emailResponse))
    '''~~~~~~~~~~~~~~~~ Construct & Send SMS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    # sms = "Hello " + firstname + ",%0aYour meeting with " + mWith + " is now scheduled for " + \
    #     date + " at " + time + " %0aPlace: " + mPlace + \
    #     "%0a %0aRegards,%0aAdv. Prashant Patil"
    # r = requests.get("http://api.msg91.com/api/sendhttp.php?country=91&sender=TESTIN&route=4&mobiles=" +
    #                  str(contact)+"&authkey=256187AKWh6ZGX9j5c385774&message=" + sms)
    # print("Sms Status Code " + str(r))
    return JsonResponse({'request': 'ok', 'for': nameofclient,
                         'date': date, 'time': time})
