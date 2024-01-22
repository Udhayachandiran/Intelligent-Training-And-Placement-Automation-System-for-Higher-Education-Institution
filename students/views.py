from django.shortcuts import render,redirect,get_object_or_404
from .models import Detail
from hiring_team.models import JobDetail
from users.models import StudentJob
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json


@login_required
def stuHome(request):
    if 'student' in request.session:
        email = request.session['user_email']
        student_details = Detail.objects.filter(email=email)
        jobs = JobDetail.objects.all()
        job_dates = []
        for job in jobs:
            job_date={
                'title': job.company_name,
                'start': job.drive_strt_date.isoformat(),
                'end': job.drive_end_date.isoformat(),
                'registration': job.last_reg_date.isoformat(),
            }
            job_dates.append(job_date)
        job_dates = json.dumps(job_dates)  
        return render(request,'students/student.html',{'student': student_details,'job_dates': job_dates}) 
    else:
        return redirect('logout')
     

@login_required
def studentDetails(request):
    if 'student' in request.session:
        try:
            email = request.session['user_email']
            student_details = Detail.objects.get(email=email)
        except Detail.DoesNotExist:
            # Student details not found, display empty form
            return render(request,'students/forms.html')
        else:
            # Student details found, populate form fields with retrieved data
            return render(request, 'students/forms.html', {'student': student_details})
    else:
        return redirect('logout')
        

#--------------------------------------------------------------------------asdasd-------------------

@login_required
def addStudentDetails(request):
    if 'student' in request.session:
        if request.method == 'POST':
            if request.POST.get('fname'):
                stu_record, created = Detail.objects.update_or_create(
                    email=request.POST.get('email'),
                    defaults={
                        'fname': request.POST.get('fname'),
                        'rollno': request.POST.get('rollno'),
                        'dob': request.POST.get('dob'),
                        'gender': request.POST.get('gender'),
                        'clg_name': request.POST.get('clg_name'),
                        'degree': request.POST.get('degree'),
                        'branch': request.POST.get('branch'),
                        'yrOfPass': request.POST.get('yrOfPass'),
                        'dayscholar': request.POST.get('dayscholar'),
                        'phone_no': request.POST.get('phone_no'),
                        'ug_cgpa': request.POST.get('ug_cgpa'),
                        'fath_name': request.POST.get('fath_name'),
                        'fath_phone_no': request.POST.get('fath_phone_no'),
                        'fath_occu': request.POST.get('fath_occu'),
                        'moth_name': request.POST.get('moth_name'),
                        'moth_phone_no': request.POST.get('moth_phone_no'),
                        'moth_occu': request.POST.get('moth_occu'),
                        'annual_inc': request.POST.get('annual_inc'),
                        'native_place': request.POST.get('native_place'),
                        'curr_addr': request.POST.get('curr_addr'),
                        'perr_addr': request.POST.get('perr_addr'),
                        'stan_arr': request.POST.get('stan_arr'),
                        'hist_arr': request.POST.get('hist_arr'),
                        'sslc_mark': request.POST.get('sslc_mark'),
                        'sslc_max_mark': request.POST.get('sslc_max_mark'),
                        'sslc_med': request.POST.get('sslc_med'),
                        'sslc_sch': request.POST.get('sslc_sch'),
                        'sslc_board': request.POST.get('sslc_board'),
                        'sslc_yop': request.POST.get('sslc_yop'),
                        'hsc_mark': request.POST.get('hsc_mark'),
                        'hsc_max_mark': request.POST.get('hsc_max_mark'),
                        'hsc_med': request.POST.get('hsc_med'),
                        'hsc_sch': request.POST.get('hsc_sch'),
                        'hsc_board': request.POST.get('hsc_board'),
                        'hsc_yop': request.POST.get('hsc_yop'),
                        'dip_mark': request.POST.get('dip_mark'),
                        'dip_max_mark': request.POST.get('dip_max_mark'),
                        'dip_univ_name': request.POST.get('dip_univ_name'),
                        'dip_branch': request.POST.get('dip_branch'),
                        'dip_yop': request.POST.get('dip_yop'),
                        'break_in_acca': request.POST.get('break_in_acca'),
                        'certi_course': request.POST.get('certi_course'),
                        'intern_exp': request.POST.get('intern_exp'),
                        'intern_comp_name': request.POST.get('intern_comp_name'),
                        'intern_role': request.POST.get('intern_role'),
                        'inter_duration': request.POST.get('inter_duration'),
                    }
                )

                if created:
                    messages.success(request, stu_record.fname + " details added successfully!!")
                else:
                    messages.success(request, stu_record.fname + " details updated successfully!!")

                return redirect('viewUserDet')
            else:
                return render(request, 'students/forms.html')
        else:
            return render(request,'students/student.html')
    else:
        return redirect('logout')


#-------------------------------------view User Details--------------------------------  
@login_required
def viewUserDetails(request):
    if 'student' in request.session:
        email = request.session['user_email']
        stu_detail=Detail.objects.filter(email=email)
        if stu_detail:
            return render(request,'students/viewprofile.html',{ 'stu_detail':stu_detail , 'student': stu_detail})
        else:
            messages.error(request,"Add Details to View!")
            return render(request,'students/forms.html')
    else:
        return redirect('logout')
        

#------------------------------------viewJOBS--------------------------------------------
@login_required
def jobs(request):
    if 'student' in request.session:
        try:    
            email = request.session['user_email']
            student=Detail.objects.get(email=email)
        except Detail.DoesNotExist:
            messages.error(request,"Add Details first to view jobs!!")
            return render(request,'students/forms.html')
        else:
            stu_id= student.id
            applied_jobs = JobDetail.objects.filter(studentjob__registered_to_job='registered', studentjob__student_id_id=stu_id)
            # job_ids = StudentJob.objects.filter(student_id=stu_id).values_list('job_id_id', flat=True)
            # job_ids = list(job_ids)
            # jobs = JobDetail.objects.filter(id__in=job_ids)
            comp_detail=JobDetail.objects.filter(studentjob__student_id_id=stu_id ,studentjob__registered_to_job='not registered' ,status_of_drive='active', admin_approval='Accepted').order_by('last_reg_date')
            return render(request,'students/jobs.html',{ 'comp_detail':comp_detail ,'student': student,'applied_jobs':applied_jobs})
    else:
        return redirect('logout')
    

#------------------------------------view Job's Full details--------------------------------
@login_required
def viewJobDetails(request):
    if 'student' in request.session: 
        if request.method =='GET':
            if request.GET.get('jobs'):
                email = request.session['user_email']
                stu_detail=Detail.objects.filter(email=email)
                comp_name = request.GET.get('jobs')
                job_detail = JobDetail.objects.filter(company_name=comp_name)
                return render(request,'students/viewJobDetails.html',{ 'job_detail':job_detail[0] ,'student': stu_detail})
            else:
                return render(request,'students/jobs.html')
        else:
            return render(request,'students/student.html')
    else:
        return redirect('logout')
    
#================================================ApplyToJob=============================================    
@login_required
def applyToJob(request):
    if 'student' in request.session:
        if request.method =='GET':
            if request.GET.get('applyjob'):
                comp_name = request.GET.get('applyjob')
                email = request.session['user_email']
                student=Detail.objects.get(email=email)
                stu_id= student.id
                # StudentJob.objects.filter(job_id_id__company_name=comp_name).update(registered_to_job='registered')
                # student_job = StudentJob.objects.get(job_id_id__company_name=comp_name,job_id_id=stu_id)
                # student_job.registered_to_job = 'registered'
                # student_job.save()
                job = get_object_or_404(JobDetail, company_name=comp_name)
                StudentJob.objects.filter(job_id_id=job.id, student_id_id=stu_id).update(registered_to_job='registered')
                messages.success(request,"Applied to job")
                return redirect("jobs")
            else:
                return redirect("viewJD")    
        else:
            return render(request,'students/student.html')
    else:
        return redirect('logout')        

#---------------------------------------------------------------resumeBuilder-----------------------------------------------

@login_required
def resumeBuilder(request):
    if 'student' in request.session:
        email = request.session['user_email']
        stu_details=Detail.objects.filter(email=email)
        if stu_details:
            return render(request,'students/resume.html',{'students': stu_details[0]})
        else:
            messages.error(request,"Add Details to BuildResume!")
            return render(request,'students/forms.html')
    else:
        return redirect('logout')