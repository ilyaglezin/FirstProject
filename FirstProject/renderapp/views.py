from django.shortcuts import render

def main(request):
    return render(request, 'renderapp/main.html')

def lightvehicles(request):
    return render(request, 'renderapp/light vehicles.html')

def history(request):
    return render(request, 'renderapp/history.html')

def heavyvehicles(request):
    return render(request, 'renderapp/heavy vehicles.html')

def feedback(request):
    return render(request, 'renderapp/feedback.html')

def buses(request):
    return render(request, 'renderapp/buses.html')


