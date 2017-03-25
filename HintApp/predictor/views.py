from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from . import NEO
from . import get_online_data
# Create your views here.

from .NEO import Get_UserData

def index(request):
    return render(request,'index.html',{'title':'Welcome To Train Prediction'})

def handle_query(request):
    if request.method == 'POST':
        HttpResponseRedirect("/predict")

    else:
        return render(request, 'index.html', {'title': 'Welcome To Train Prediction'})

def result(request):
    l = Get_UserData()
    train_no = l[0]
    date = l[1]
    myneon = NEO.Neon_Engine()
    myneon.getdata_and_train(train_no=train_no)
    res = myneon.predict_delay(data=date)
    mymsg = ' '
    if res == 0:
        mymsg = 'Delay'
    elif res == 2:
        mymsg = 'Before'

    else:
        mymsg = 'On Time'
    return render(request, 'result.html', {'title': 'Status',
                                           'result': mymsg}
                  )

