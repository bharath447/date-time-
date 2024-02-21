from django.shortcuts import render
from datetime import datetime
# Create your views here.

def wish(request):
    date = datetime.now()
    msg = "Hello Guest Very Good"
    h = int(date.strftime('%H'))

    if h<12:
        msg += "Morning"
    elif h<16:
         msg += "Afternoon"
    elif h<21:
        msg += "Evening"
    else:
        msg += "Night"
    
    my_dict = {"insert_date":date,"insert_msg":msg}
    return render(request,'testapp/wish.html',context=my_dict)


def usaView(request):
    return render(request, 'testapp/usa.html')


def indView(request):
    return render(request, 'testapp/ind.html')