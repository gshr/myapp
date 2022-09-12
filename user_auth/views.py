from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import CustomerModel,Product
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView
import json
from .serializer import ProductSerializer
from django.db.models import Count
from django.db.models.functions import ExtractMonth,ExtractYear
import logging
import traceback
logger = logging.getLogger('watchtower-logger')
import math
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django.db.models import Q

class index(ListAPIView):
   

    serializer_class = ProductSerializer
    pagination_class =PageNumberPagination

    def get_queryset(self):
        try:
            msg= "-----***************************************  Getting into index view ****** -----"
            logger.info(msg)
            print('Hello from index view')
            queryset = Product.objects.all()

            s = self.request.query_params.get('s', None)
            print(s)
            sort= self.request.query_params.get('sort', None)
            if s is not None:
                queryset = queryset.filter(Q(title__icontains=s) | Q(description__icontains=s))
            if sort == 'asc':
                queryset=queryset.order_by('price')
            else:
                queryset=queryset.order_by('-price')

            logger.info("Sending Response Successfully")


            return  queryset
        except:
            var=traceback.format_exc()
            logger.warning(var)
            logger.error(var)
            return Response({"Error": "Some Error occurred"})
        




# def get(self,request):
#     msg= "***************************************  Getting into index view ******" 
#     logger.info(msg)
#     try:
#         s = request.GET.get('s')
#         sort = request.GET.get('sort')

#         products = Product.objects.all()

#         if s:
    #             products = products.filter(Q(title__icontains=s) | Q(description__icontains=s))

    #         if sort == 'asc':
    #             products = products.order_by('price')
    #         elif sort == 'desc':
    #             products = products.order_by('-price')

           

    #         serializer_class = ProductSerializer
            
            
        
   
        
        

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
        
    
        
