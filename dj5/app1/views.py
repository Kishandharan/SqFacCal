from django.shortcuts import render
import math

def home(request):
	num1 = 3
	return render(request, 'app1/index.html', {'param1':num1, 'param2':math.factorial(num1)})
