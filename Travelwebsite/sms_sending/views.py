from django.shortcuts import render
from twilio.rest import Client
from django.http import HttpResponse


def sending_details(request):
    account_sid = '{your_account sid}'
    auth_token = 'your stoken'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                     body="Hlw bro, Dajngo says Kaise Ho Lokesh",
                     from_='+17177272675',
                     to='+'
                 )

    print(message.sid)
    return HttpResponse('<h1 style="color:cyan;">Sms_send Succesfully</h1>')

