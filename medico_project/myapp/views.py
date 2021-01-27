from django.shortcuts import render
from.models import *
from django.core.mail import send_mail
from random import randint
from .utils import sendmail
# Create your views here.
def register_page(request):
    return render(request,"myapp/authentication/register.html")


def add_patient(request):
    return render(request, "myapp/patients/add-patients.html")

def login_page(request):
    return render(request,"myapp/authentication/login.html")




   # doctor section


def doctors(request):
    data=Doctor.objects.all()
    return render(request, "myapp/doctor/doctors.html",{'data':data})


def drprofile(request,ck):
    did=Doctor.objects.get(user_id=ck)
    return render(request, "myapp/doctor/profile.html",{'did':did})

def addoctors(request):
    return render(request, "myapp/doctor/add-doctor.html")


def event(request):
    return render(request,"myapp/doctor/events.html")



def book_appoitment(request):
    return render(request, "myapp/appointment/book-appointment.html")

def appointment(request):
    fname=request.POST['firstname']
    lname = request.POST['lastname']
    email = request.POST['email']
    age = request.POST['age']
    role = request.POST['role']
    number = request.POST['number']
    uid=appoint.objects.create(firstname=fname,lastname=lname,email=email)
    return render(request,"myapp/dashboard/index.html")



# app

def chat(request):
    return render(request, "myapp/app/chat.html")

def compose(request):
    return render(request, "myapp/app/compose.html")

def contact_list(request):
    return render(request, "myapp/app/contact-list.html")

def inbox(request):
    return render(request, "myapp/app/inbox.html")

def single(request):
    return render(request, "myapp/app/single.html")




# authentication
def register(request):
    role=request.POST['role']
    firstname = request.POST['firstname']
    password = request.POST['password']
    email=request.POST['email']
    terms=request.POST['terms']
    try:
        if terms == "accept":
            uid = User.objects.create(email=email, role=role, password=password)
            if role =="Doctor":
                did=Doctor.objects.create(user_id=uid,firstname=firstname)
                send_mail("conformation-message", "welcome to medico expert", "dipenpatel898065@gmail.com", [email])
                s_mass = "successful registration"
                return render(request,"myapp/authentication/login.html", {'s_mass': s_mass})
            else:
                pid = Patient.objects.create(user_id=uid, firstname=firstname)
                send_mail("conformation-message", "welcome to medico expert", "dipenpatel898065@gmail.com", [email])
                s_mass = "successful registration"
                return render(request, "myapp/authentication/login.html", {'s_mass': s_mass})
        else:
            e_mass="term condition required"
            return render(request, "myapp/authentication/register.html",{'e_mass':e_mass})
    except:
        e_mass = "all field required"
        return render(request, "myapp/authentication/register.html", {'e_mass': e_mass})


def login_evalute(request):
    role=request.POST['role']
    p_assword = request.POST['password']
    email=request.POST['email']
    uid=User.objects.get(email=email)
    if uid:
        if uid.role == "Doctor":
            did=Doctor.objects.get(user_id=uid)
            request.session['firstname']=did.firstname
            request.session['email'] = uid.email
            request.session['id'] = uid.id
            print("-doctor ",did.profile_pic)
            context={
                'uid':uid,
                'did':did,
            }
            #print("----------------> context:",context.did.profile_pic.url)
            return render(request, "myapp/dashboard/index.html",{'context':context,'did':did})
        elif role == "Patient":
            pid=Patient.objects.get(user_id=uid)
            request.session['firstname'] = pid.firstname
            request.session['email'] = uid.email
            request.session['id'] = uid.id
            context = {
                'uid':uid,
                'pid':pid
            }
            return render(request, "myapp/patients/Patients-profile.html",{'context': context})
        else:
            return render(request, "myapp/authentication/login.html")

    else:
        return render(request, "myapp/authentication/login.html")

def logout(request):
    if "email" in request.session:
        del request.session['firstname']
        del request.session['email']
        del request.session['id']
        return render(request, "myapp/authentication/login.html")
    else:
        return render(request, "myapp/authentication/login.html")

def forgot_password(request):
    return render(request, "myapp/authentication/forgot-password.html")



def SEND_OTP(request):
    try:
        email=request.POST['email']
        uid=User.objects.get(email=email)
        if uid:
            otp=randint(1111,9999)
            uid.otp=otp #update otp
            uid.save()
            if uid.role=="Doctor":
                did=Doctor.objects.get(user_id=uid)
                context={
                    'did':did,
                    'otp':otp
                }

                sendmail("Forgot Password", "mail_template", email, {'context': context})
                return render(request, "myapp/authentication/reset_password.html",{'email':email})
            else:
                pass

    except:
        e_mass="user does not exit"
        return render(request, "myapp/authentication/forgot-password",{'e_mass':e_mass})

def reset_password(request):
    email=request.POST['email']
    otp = request.POST['OTP']
    newpassword = request.POST['new-password']
    repassword = request.POST['re-password']
    uid=User.objects.get(email=email)
    if str(uid.otp)==otp and newpassword==repassword:
        uid.password=newpassword
        uid.save()
        s_mass="succesful save"
        return render(request, "myapp/authentication/login.html",{'s_mass':s_mass})
    else:
        e_mass = "unsuccesful save"
        return render(request, "myapp/authentication/forgot-password",{'e_mass':e_mass},{'email':email})


def page404(request):
    return render(request, "myapp/authentication/page404.html")

def page500(request):
    return render(request, "myapp/authentication/page500.html")

def page_offline(request):
    return render(request, "myapp/authentication/page-offline.html")



# blog

def dashboard(request):
    return render(request, "myapp/blog/dashboard.html")
def detail(request):
    return render(request, "myapp/blog/detail.html")
def grid(request):
    return render(request, "myapp/blog/grid.html")
def list(request):
    return render(request, "myapp/blog/list.html")
def new_post(request):
    return render(request, "myapp/blog/new-post.html")

# dashboard

def index_page(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        did=Doctor.objects.get(user_id=uid)
        context = {
            'uid': uid,
            'did': did
        }
        return render(request, "myapp/dashboard/index.html", {'context': context})
    else:
        return render(request,"myapp/authentication/login.html")



# department

def add_department(request):
    return render(request, "myapp/departments/add-department.html")
def all_department(request):
    return render(request, "myapp/departments/all-departments.html")
def more_department(request):
    return render(request, "myapp/departments/more-departments.html")


#doctors

#file-manager
def dashboard(request):
    return render(request, "myapp/file-manager/dashboard.html")
def document(request):
    return render(request, "myapp/file-manager/documents.html")
def image(request):
    return render(request, "myapp/file-manager/image.html")
def media(request):
    return render(request, "myapp/file-manager/media.html")

#page

def blank_pages(request):
    return render(request, "myapp/pages/blank-page.html")
def image_gallery(request):
    return render(request, "myapp/pages/image-gallery.html")
# def invoice(request):
#     return render(request, "myapp/patient/invoice.html")
def profile(request):
    return render(request, "myapp/pages/profile.html")
def rtl(request):
    return render(request, "myapp/pages/rtl.html")
def search_result(request):
    return render(request, "myapp/pages/search-result.html")
def timeline(request):
    return render(request, "myapp/pages/timeline.html")

# patients


def patient_profile(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Patient.objects.get(user_id=uid)
        context = {
            'uid': uid,
            'pid': pid
        }
        return render(request, "myapp/patients/patients-profile.html", {'context': context})

    return render(request, "myapp/patients/Patients-profile.html")

def all_patients(request):
    data=Patient.objects.all()
    return render(request, "myapp/patients/all-patients.html",{'data':data})

def invoice(request):
    return render(request, "myapp/patients/invoice.html")
#payment

def add_payment(request):
    return render(request, "myapp/payment/add-payment.html")

def all_payment(request):
    return render(request, "myapp/payment/all-payment.html")
#ui

def alerts(request):
    return render(request, "myapp/ui/alerts.html")

def collapse(request):
    return render(request, "myapp/ui/collapse.html")
def colors(request):
    return render(request, "myapp/ui/colors.html")

def dialogs(request):
    return render(request, "myapp/ui/dialogs.html")
def icons(request):
    return render(request, "myapp/ui/icons.html")

def list_group(request):
    return render(request, "myapp/ui/list-group.html")
def media_objects(request):
    return render(request, "myapp/ui/media-objects.html")

def models(request):
    return render(request, "myapp/ui/models.html")

def notifications(request):
    return render(request, "myapp/ui/notifications.html")

def progressbar(request):
    return render(request, "myapp/ui/progressbar.html")

def range_slider(request):
    return render(request, "myapp/ui/range-slider.html")

def sortable_nestable(request):
    return render(request, "myapp/ui/sortable-nestable.html")

def tabs(request):
    return render(request, "myapp/ui/tabs.html")

def ui_ki(request):
    return render(request, "myapp/ui/ui-ki.html")
def waves(request):
    return render(request, "myapp/ui/waves.html")

# widgets
def apps(request):
    return render(request, "myapp/widgets/apps.html")

def data(request):
    return render(request, "myapp/widgets/data.html")

# edit - patient -detail

def edit_patient(request):
    return render(request, "myapp/patients/edit_patient_detail.html")

def edit_patient_detail(request):

    firstname=request.POST['firstname']
    lastname = request.POST['lastname']
    contactno = request.POST['contactno']
    age = request.POST['age']
    occupations = request.POST['occupations']
    address = request.POST['address']
    email = request.POST['email']
    password = request.POST['password']
    uid=User.objects.get(email=email)
    print("<_________________> ",uid)
    if uid:
       pid= Patient.objects.get(user_id=uid)
       pid.firstname=firstname
       pid.lastname=lastname
       pid.contactno = contactno
       pid.age = age
       pid.occupations = occupations
       pid.address = address
       pid.password = password
       pid.save()

       return render(request, "myapp/authentication/login.html",)
    else:
        return render(request, "myapp/patients/edit_patient_detail.html")



