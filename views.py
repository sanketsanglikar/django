from django.shortcuts import render,HttpResponseRedirect
from .models import Signup
import datetime


from django.http import HttpResponse
# Create your views here.
def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request, 'login.html')


def createaccount(request):
    if request.method == 'POST':

        print('in post request')
        # signup = Signup()
        #
        FullName = request.POST.get('full_name')
        Password = request.POST.get('password')
        Birthday = request.POST.get('birthday')
        Birthday = datetime.datetime.strptime("{}".format(Birthday), "%d/%m/%Y").strftime("%Y-%m-%d")
        Gender = request.POST.get('gender')
        Email = request.POST.get('email')
        PhoneNumber = request.POST.get('phone')
        Designation = request.POST.get('Designation')

        # return render(request, 'login.html')
        data = Signup(
            FullName = FullName,
            Password = Password,
            Birthday = Birthday,
            Gender = Gender,
            Email= Email,
            PhoneNumber = PhoneNumber,
            Designation =Designation
        )
        data.save()
        data1 = Signup.objects.all()

        print(data1[4].Password)
        return render(request, 'login.html')
    else:
        print("Nhi Hora")
        return render(request, 'signup.html')


def home(request):
    if request.method == 'POST':
        data = Signup.objects.all()
        print(len(data))
        for i in range(len(data)):
            print(data[i].Email, data[i].Password)
        print(request.POST.get('email'),request.POST.get('your_pass'))
    else:
        print("Nhi jamra")
        return render(request, 'login.html')
        # if str(data[i].Email) == str(request.POST.get('email')) and str(data[i].Password) == str(request.POST.get('password')):
        #     return render(request, 'home.html')
        # else:
        #     print('Nhi jara aage')
        #     return render(request, 'login.html')
