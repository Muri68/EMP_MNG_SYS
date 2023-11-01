from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render(request, 'home.html')



def costomer_page(request):
    return render(request, 'home.html')



def courier_page(request):
    return render(request, 'home.html')