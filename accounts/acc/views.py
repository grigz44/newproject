from django.shortcuts import render

# Create your views here.
from acc.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *



class usereg(APIView):

    def post(self,req, *args, **kwarg):

        print(req.data)
        serializer = userregserializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
        


class usercreate(APIView):
    

    def get(self, request):
        
        data = user.objects.all()
        serializer = usercreateserializer(data, many=True)
        return Response(serializer.data)
    

    def post(self,req, *args, **kwarg):
        
        
        Login={'owner':req.data['Phone_number']}

        print(req.data)
        serializer = usercreateserializer(data=req.data)
        logserial=usercartserializer(data=Login)
        if serializer.is_valid():
            serializer.save()
            
            if logserial.is_valid():
                logserial.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        

class createproduct(APIView):
    
    def get(self, request):
        ls=[]
        data = product.objects.all()
        d=product.objects.all().count()
        print("#############################")
        print(d)
        serializer = productserializer(data, many=True)
        for i in range(0,d):
            tc=serializer.data[i]['Unique_id']
            print(tc)
            
            img=product_image.objects.filter(product=tc)
            serializer1=productimgserializer(img,many=True)
            ls.append(serializer.data[0])
            ls.append(serializer1.data)
        return Response(ls)

    

    def post(self,req, *args, **kwarg):

        print(req.data)
        serializer = productserializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
  
        
        

class productimg(APIView):



    def get(self, request):
        
        data = product_image.objects.all()
        serializer = productimgserializer(data, many=True)
        return Response(serializer.data)
    
    def post(self,req, *args, **kwarg):

        print(req.data)
        serializer = productimgserializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
        
        

class addproduct(APIView):
    

    def get(self, request):
        
        data = UserCartProduct.objects.all()
        serializer = usercartproductserializer(data, many=True)
        return Response(serializer.data)
    
    

    def post(self,req, *args, **kwarg):

        print(req.data)
        serializer = usercartproductserializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
        
class cart(APIView):
    

    def get(self, request):
        
        data = UserCart.objects.all()
        serializer = usercartserializer(data, many=True)
        return Response(serializer.data)