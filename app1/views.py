from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person

# Create your views here.




def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            if age < 0:
                error_message = "Error: Age cannot be less than 0."
                return render(request, 'add_person.html', {'form': form, 'error_message': error_message})
            else:
                form.save()
                # return redirect('success')
    form = PersonForm()
    return render(request, 'add_person.html', {'form': form})

# def success(request):
#     return render(request,'success.html')

def table(request):
    data=Person.objects.all()
    return render(request,'table.html',{'data':data})
