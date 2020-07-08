from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Predictresult
from django.http import HttpResponse
from .predict import flower_predict
 


def predict(request):
	if request.method == 'POST':
		r=flower_predict(1,2,2,4)
		print(r)
		print('Hello')
		return render(request,'pred_res.html',{'r':r})
	return render(request,'predict.html')



	

	
def view_results(request):
    # Submit prediction and show all
    data = {"dataset": Predictresult.objects.all()}
    return render(request, "results.html", data)















