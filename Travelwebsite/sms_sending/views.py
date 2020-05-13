from django.shortcuts import render
from twilio.rest import Client
from django.http import HttpResponse


def sending_details(request):
    account_sid = 'AC828dbef1042ff22b9127bdf30212da88'
    auth_token = 'dbc86e145e8264b8a5459422a6bd07f9'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                     body="Hlw Mosaji This is the Message OTP is 4843838 mayank",
                     from_='+17177272675',
                     to='+919691896105'
                 )

    print(message.sid)
    return HttpResponse('<h1 style="color:cyan;">Sms_send Succesfully</h1>')

