from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, ):
    #makes a list of the last 5 contact requests
    latest_contact_list = Contact.objects.order_by('-pubdate')[:5]
    #will print out a list of the messages in the contact list
    output=', 'join([q.message for q in latest_contact_list])
    return HttpResponse(output) 

def detail(request, contact_id):
    return HttpResponse("You're looking at contact %s." % contact_id)
