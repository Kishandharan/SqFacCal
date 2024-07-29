from django.shortcuts import render
from app2.forms import inputweb
from math import factorial

def home(request):
	if request.method == "POST":
		form1 = inputweb(request.POST)
		if form1.is_valid():
			data = form1.cleaned_data
			num1 = data.get("inp1")
			return render(request, 'app2/index.html', {'param1':num1*num1, 'param2':factorial(num1), 'param3':num1, 'form':form1})
	else:
		form1 = inputweb()
	return render(request, 'app2/index.html', {'form':form1})
