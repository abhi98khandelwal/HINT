from django.shortcuts import render
from Neon import NEO
from Neon import get_online_data
# Create your views here.



def index(request):
    return render(request,'index.html',{'title':'Welcome To Train Prediction'})

def handle_query(request):
    if request.menthod == 'POST':
        train_no = request['train_no']
        myneon = NEO.Neon_Engine()
        myneon.getdata_and_train(train_no=train_no)
        res = str(myneon.predict_delay())
        return render(request,'result.html',{'title':'Status',
                                             'result':res}
                      )


