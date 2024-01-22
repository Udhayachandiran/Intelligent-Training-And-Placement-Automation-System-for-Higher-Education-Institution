from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login 
from django.contrib.auth.models import User
from django.contrib import messages
from students.models import User_detail
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        if request.user.username == 'admin':
            return redirect('spa')
        else:
            return redirect('logout')
    my_variables = request.session.items()
    context = {'my_variables': my_variables}
    return render(request,'users/home.html',context)

def login_pg(request):
    user_type = request.GET.get('user_type', None)
    return render(request,'account/login.html',{'user_type':user_type})

def login_redirect_view(request):
    if request.user.is_authenticated:
        request.session['user_email'] = request.user.email
        request.session['student'] = True
        
        # messages.success(request, f'You have been logged in successfully!!')
        return redirect('stuHome')
    else:
        messages.warning(request, f'There was an error logging you in.')
        return redirect('/')
    

def login_ht_tpo(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        password = request.POST.get('password')
    
        try:
            user = User.objects.get(username=uname)
            
        except:
            messages.error(request, 'User does not exist')
            return redirect('login') 

        user = authenticate(request,username=uname,password=password)
        if user is not None:
            login(request, user)
            if uname!='admin':
                request.session['uname'] = uname
                request.session['hiring'] = True
                return redirect('hiringHome')
            else:
                request.session['tpo'] = True
                return redirect('spa')
        else:
             messages.error(request, 'Invalid Credentials!')
             return redirect('/')           
    return redirect('/')
        
            
def logout_view(request):
    logout(request)
    return redirect('/')

def create_user(username, email, password):
    user = User.objects.create_user(username=username, email=email, password=password)
    return user
