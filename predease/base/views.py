from django.shortcuts import render,HttpResponse
import pandas as pd
import pickle
from base.symptoms import List_of_symp
# Create your views here.

def home(request):
    q=request.GET.get("q")
    user_symp_list=q.split(",")
    def convert(user_symp_lst):
        inp_data=pd.DataFrame(0,index=range(1),columns=range(132))
        for item in user_symp_lst:
            if item in List_of_symp:
                t=List_of_symp.index(item)
                inp_data[t]=1
        return inp_data
    
    inp_to_model = convert(user_symp_list)

    pickled_model = pickle.load(open('base\models\model.pkl', 'rb'))
    res = pickled_model.predict(inp_to_model)
    if q:
        context = res
        return render(request, "base/home.html", context)
    else:
        return render(request, "base/home.html")


    

def about(request):
    return render(request,'base/about.html')

def result(request):
    return HttpResponse("You seem to likely have .....")
