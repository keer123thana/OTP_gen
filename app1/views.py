from django.shortcuts import render
def home(request):
    import random as rd
    size=4
    qty=10
    list1=[]
    for i in range (0,qty,1):
        rd2=rd.randint(10**(size-1),(10**size)-1)
        list1.append(rd2)
    return render(request,'app1/index.html',{'param1':list1})