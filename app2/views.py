from django.shortcuts import render
from app2.forms import inputform
def home(request):
    qty = None
    n1 = None
    size=None
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input")
            
            qty=data.get("qty")
            import random as rd
            size=n1
    
            list1=[]
            for i in range (0,qty,1):
                rd2=rd.randint(10**(size-1),(10**size)-1)
                list1.append(rd2)

            
            return render(request,"app2/index.html",{'param1':list1, 'param2':n1, 'form':form1})
    else:
        form1=inputform()  
    return render(request,"app2/index.html",{ 'form':form1})
