from django.shortcuts import render,get_object_or_404
from .models import Myworks
def all_myworks(request):
    myworks=Myworks.objects.all()
    return render(request,'myworks/all_myworks.html',{'myworks':myworks})
def detail(request, myworks_id):
    myworks=get_object_or_404(Myworks, pk=myworks_id)
    return render(request,'myworks/detail.html',{'myworks':myworks})
