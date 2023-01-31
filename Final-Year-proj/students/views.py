from django.shortcuts import render
from .models import Detail
from django.contrib import messages

def home(request):
    return render(request,'students/student.html')

def studentDetails(request):
    return render(request,'students/forms.html')    

def addStudentDetails(request):
    if request.method =='POST':
        if request.POST.get('fname') and request.POST.get('email') and request.POST.get('rollno'):
            stu_record = Detail()
            stu_record.fname = request.POST.get('')
            stu_record.email = request.POST.get('')
            stu_record.rollno = request.POST.get('')
            stu_record.dob = request.POST.get('')
            stu_record.gender = request.POST.get('')
            stu_record.clg_name = request.POST.get('')
            stu_record.degree = request.POST.get('')
            stu_record.branch = request.POST.get('')
            stu_record.yrOfPass = request.POST.get('')
            stu_record.dayscholar = request.POST.get('')
            stu_record.phone_no = request.POST.get('')
            stu_record.ug_cgpa = request.POST.get('')
            stu_record.fath_name = request.POST.get('')
            stu_record.fath_phone_no = request.POST.get('')
            stu_record.fath_occu = request.POST.get('')
            stu_record.moth_name = request.POST.get('')
            stu_record.moth_phone_no = request.POST.get('')
            stu_record.moth_occu = request.POST.get('')
            stu_record.annual_inc = request.POST.get('')
            stu_record.native_place = request.POST.get('')
            stu_record.curr_addr = request.POST.get('')
            stu_record.perr_addr = request.POST.get('')
            stu_record.stan_arr = request.POST.get('')
            stu_record.hist_arr = request.POST.get('')
            stu_record.sslc_mark = request.POST.get('')
            stu_record.sslc_max_mark = request.POST.get('')
            stu_record.sslc_med = request.POST.get('')
            stu_record.sslc_sch = request.POST.get('')
            stu_record.sslc_board = request.POST.get('')
            stu_record.sslc_yop = request.POST.get('')
            stu_record.hsc_mark = request.POST.get('')
            stu_record.hsc_max_mark = request.POST.get('')
            stu_record.hsc_med = request.POST.get('')
            stu_record.hsc_sch = request.POST.get('')
            stu_record.hsc_board = request.POST.get('')
            stu_record.hsc_yop = request.POST.get('')
            stu_record.dip_mark = request.POST.get('')
            stu_record.dip_max_mark = request.POST.get('')
            stu_record.dip_univ_name = request.POST.get('')
            stu_record.dip_branch = request.POST.get('')
            stu_record.dip_yop = request.POST.get('')
            stu_record.break_in_acca = request.POST.get('')
            stu_record.certi_course = request.POST.get('')
            stu_record.intern_exp = request.POST.get('')
            stu_record.intern_comp_name = request.POST.get('')
            stu_record.intern_role = request.POST.get('')
            stu_record.inter_duration = request.POST.get('')
            stu_record.save()
            messages.success(request, stu_record.fname + "details added successfully!!")
            return render(request,'students/viewprofile.html')

    else:
        return render(request,'students/forms.html')


  

def viewUserDetails(request):
    
    context = {
        'stu_detail':Detail.objects.filter()
    }

    return render(request,'students/viewprofile.html',context)    