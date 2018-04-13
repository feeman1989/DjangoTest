from django.shortcuts import render
from .models import UserMessage
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt 
def getform(request):
    if request.method == "GET":
        all_message = UserMessage.objects.all()
        for message in all_message:
            print message.name
        return render(request, 'message_form.html')
    elif request.method == "POST":
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
        user_message = UserMessage()
        user_message.name = name 
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.save()