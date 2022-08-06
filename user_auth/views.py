from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import CustomerModel
# Create your views here.
from django.views import View

# class index(View):
    
#     def get(self,request):
#         pass
        
        

def login(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        try:
             custObj=CustomerModel.objects.filter(email=email).first()
        except:
            return HttpResponse("error")

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
        
    
        
