from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import CustomerModel
# Create your views here.


def index(request):
    
    if request.method == 'GET':
        pass
        

def login(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        try:
            print(email)
            custObj=CustomerModel.objects.filter(email=email).first()
            print(custObj)
        except:
            return HttpResponse("error")

        print(custObj.password)
        print(request.POST['password'])
        if (custObj.password == request.POST['password']):
            return render(request, "index.html", {"context":custObj})
            #  return HttpResponse(f"msg {custObj.first_name} ")
        else:
            return HttpResponse("msg Error")
            
            
            
        
    
    return render(request, "login.html")

    
    

def register(request):
    if request.method == 'GET':
        
        context ={}
        context['form']= RegistrationForm()
        return render(request, "register.html", context)
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            reg = form.save(commit=False)
            reg.user = request.user
            reg.save()
        context ={}
        context['form']= RegistrationForm()
        return render(request, "register.html",context )
        
    
        
