from django.shortcuts import render,redirect
from .models import JobDetail
from students.models import Detail 
from django.contrib import messages
from django.db import connection
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required

@login_required
def companyDetails(request):
    if 'hiring' in request.session:
        try:
            company_name = request.session['uname']
            company_name = company_name.capitalize()
            comp_details = JobDetail.objects.get(company_name=company_name)
        except Detail.DoesNotExist:
            # Company details not found, display empty form
            return render(request,'hiring_team/jobcreation.html')
        else:
            # Company details found, populate form fields with retrieved data
            return render(request,'hiring_team/jobcreation.html', {'student': comp_details})
    else:
        return redirect('logout')


@login_required
def hiringHome(request):
    if 'hiring' in request.session:
        return render(request,'hiring_team/index.html')
    else:
        return redirect('logout')
    

@login_required
def addCompanyDetails(request):
    if 'hiring' in request.session:
        if request.method =='POST':
            company_name = request.session['uname']
            company_name = company_name.capitalize()
            job_detail = JobDetail.objects.get(company_name=company_name)
            if request.POST.get('jc-comp-name') and request.POST.get('jc-job-title'):
                comp_d, created = JobDetail.objects.update_or_create(
                    id= job_detail.id,
                    defaults={
                        'company_name': request.POST.get('jc-comp-name'),
                        'job_title': request.POST.get('jc-job-title'),
                        'ctc_min': request.POST.get('jc-min-ctc'),
                        'ctc_max': request.POST.get('jc-max-ctc'),
                        'other_info': request.POST.get('jc-other-info'),
                        'comp_link': request.POST.get('jc-comp-link'),
                        'drive_strt_date': request.POST.get('jc-drive-date-start'),
                        'drive_end_date': request.POST.get('jc-drive-date-end'),
                        'required_skill': request.POST.get('jc-skills'),
                        'job_desc': request.POST.get('jc-job-desc'),
                        'last_reg_date': request.POST.get('jc-deadline'),
                        'media': request.POST.get('jc-documents'),
                        'eligible_10th_minp': request.POST.get('ec-10'),
                        'eligible_12th_minp': request.POST.get('ec-12'),
                        'eligible_ug_minp': request.POST.get('ec-ug'),
                        'hist_of_arr': request.POST.get('jc-backlog'),
                        'type_of_offer': request.POST.get('jc-package'),
                    }
                )
                if created:
                    messages.success(request, comp_d.company_name + " details added successfully!!")
                else:
                    messages.success(request, comp_d.company_name + " details updated successfully!!")
                request.session['drive'] = True
                return render(request,'hiring_team/index.html')
            else:
                return render(request,'hiring_team/jobcreation.html')
        else:
            return render(request,'hiring_team/jobcreation.html')
    else:
        return redirect('logout')

# @login_required
# def addCompanyDetails(request):
#     if 'hiring' in request.session:
#         if request.method =='POST':
#             if request.POST.get('jc-comp-name') and request.POST.get('jc-job-title'):
#                 comp_d = JobDetail()
#                 comp_d.company_name = request.POST.get('jc-comp-name')
#                 comp_d.job_title = request.POST.get('jc-job-title')
#                 comp_d.ctc_min = request.POST.get('jc-min-ctc')
#                 comp_d.ctc_max = request.POST.get('jc-max-ctc')
#                 comp_d.other_info = request.POST.get('jc-other-info')
#                 comp_d.comp_link = request.POST.get('jc-comp-link')
#                 comp_d.drive_strt_date = request.POST.get('jc-drive-date-start')
#                 comp_d.drive_end_date = request.POST.get('jc-drive-date-end')
#                 comp_d.required_skill = request.POST.get('jc-skills')
#                 comp_d.job_desc = request.POST.get('jc-job-desc')
#                 comp_d.last_reg_date = request.POST.get('jc-deadline')
#                 comp_d.media = request.POST.get('jc-documents')
#                 comp_d.eligible_10th_minp = request.POST.get('ec-10')
#                 comp_d.eligible_12th_minp = request.POST.get('ec-12')
#                 comp_d.eligible_ug_minp = request.POST.get('ec-ug')
#                 comp_d.hist_of_arr = request.POST.get('jc-backlog')
#                 comp_d.type_of_offer = request.POST.get('jc-package')
#                 comp_d.save()
#                 messages.success(request, comp_d.company_name + "details added successfully!!")
#                 request.session['drive'] = True
#                 return render(request,'hiring_team/jobcreation.html')
#             else:
#                 return render(request,'hiring_team/jobcreation.html')
#         else:
#             return render(request,'hiring_team/jobcreation.html')
#     else:
#         return redirect('logout')
    
#-------------------------------------view Applied Students --------------------------------  
@login_required
def students_applied_to_company(request):
    if 'hiring' in request.session:
        # if 'drive' in request.session:
            company_name = request.session['uname']
            company_name = company_name.capitalize()
            # job = JobDetail.objects.filter(company_name=company_name).first()
            #if job:
            # job_id = job.id
            # applied_students = Detail.objects.filter(studentjob__registered_to_job='registered', studentjob__job_id_id=job_id)
            applied_students = Detail.objects.filter(studentjob__job_id_id__company_name=company_name,studentjob__registered_to_job='registered')
            # else:
                
            if applied_students:
                return render(request,'hiring_team/studentlist.html',{ 'stu_detail':applied_students })
            else:
                messages.error(request,"No students applied to job")
                return render(request,'hiring_team/index.html')
        # else:
        #     messages.error(request,"Create Drive to view applied students")
        #     return redirect('company')     
    else:
        return redirect('logout')

#-------------------------------------view Applied Students Details--------------------------------  
@login_required
def viewIndividualStudent(request):
    if 'hiring' in request.session:
        # if 'drive' in request.session:
            if request.method =='GET':
                if request.GET.get('indvstu'):
                    stu_email = request.GET.get('indvstu')
                    company_name = request.session['uname']
                    indv_student = Detail.objects.filter(email=stu_email)
                    applied_students = Detail.objects.filter(studentjob__job_id_id__company_name='Prodapt',studentjob__registered_to_job='registered')
                    if indv_student and applied_students:
                        return render(request,'hiring_team/studentlist.html',{ 'stu_detail':applied_students ,'student_detail':indv_student  })
                    else:
                        messages.error(request,"Student Detail does not exist")
                        return render(request,'hiring_team/index.html')
            else:
                messages.error(request,"No students applied to job")
                return render(request,'hiring_team/index.html')
        # else:
        #     messages.error(request,"Create Drive to view applied students")
        #     return redirect('company') 
    else:
        return redirect('logout')    
    