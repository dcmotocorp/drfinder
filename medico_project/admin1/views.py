from django.shortcuts import render
from myapp.models import  Patient,Doctor
# Create your views here.
def dashboard(request):
    return render(request,"admin1/examples/dashboard.html")
def icons(request):
    return render(request,"admin1/examples/icons.html")
def rtl(request):
    return render(request,"admin1/admin1/examples/rtl.html")

def tables(request):
    p_data=Patient.objects.all()
    d_data = Doctor.objects.all()
    return render(request,"admin1/examples/tables.html",{'p_data':p_data,'d_data':d_data})

def map(request):
    return render(request,"admin1/examples/map.html")
def maps(request):
    return render(request,"admin1/examples/maps.html")
def notifications(request):
    return render(request,"admin1/examples/rtl.html")
def typography(request):
    return render(request,"admin1/examples/typography.html")
def upgrade(request):
    return render(request,"admin1/examples/upgrade.html")
def user(request):
    return render(request,"admin1/examples/user.html")
def template(request):
    return render(request,"admin1/template.html")
