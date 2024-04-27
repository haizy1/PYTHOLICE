from django.shortcuts import render

# Create your views here.
def basededonnées_view(request):
    return render(request, 'basededonnées/basededonnées.html')
def criminels_view(request):
    return render(request, 'criminels/criminels.html')
def alertes_view(request):
    return render(request, 'alertes/alertes.html', {})
def home(request):
    return render(request, 'events/home.html', {})
def search_criminals(request):
    search_query = request.GET.get('search')
    criminals = Criminal.objects.filter(name__icontains=search_query)
    return render(request, 'basededonnees/basededonnees.html', {'criminals': criminals})

def add_criminal(request):
    if request.method == 'POST':
        # Process the form data and create a new criminal object
        # Adjust the code based on your model and form fields
        new_criminal = Criminal(name=request.POST['name'], image=request.POST['image'], description=request.POST['description'])