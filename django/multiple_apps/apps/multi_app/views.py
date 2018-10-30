from django.shortcuts import render, redirect
  
def index(request):
    
    return render(request, 'multi_app/index.html')
