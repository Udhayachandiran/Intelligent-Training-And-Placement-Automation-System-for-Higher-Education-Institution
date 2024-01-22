from django.shortcuts import render,redirect
from hiring_team.models import JobDetail
import pickle,sklearn,numpy as np
import csv , tempfile
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

@login_required
def tpoApproval(request):
    if 'tpo' in request.session:
        comp_detail=JobDetail.objects.filter(admin_approval='review')
        return render(request,'tpo/approval.html',{ 'comp_detail':comp_detail, 'title':'TPO-Approval'})
    else:
        return redirect('logout')
    
    
@login_required
def approvedDrive(request):
    if 'tpo' in request.session:
        if request.method =='GET':
            if request.GET.get('approved'):
                comp_name = request.GET.get('approved')
                job_upt = JobDetail.objects.filter(company_name=comp_name)
                job_upt.update(admin_approval ='Accepted')
                comp_detail=JobDetail.objects.filter(admin_approval='review')
                return render(request,'tpo/approval.html',{'comp_detail':comp_detail,'title':'TPO-Approval'})
            else:
                return render(request,'tpo/approval.html',{'comp_detail':comp_detail,'title':'TPO-Approval'})
        else:
            return render(request,'students/student.html')
    else:
        return redirect('logout')
        

@login_required
def deniedDrive(request):
    if 'tpo' in request.session:
        if request.method =='GET':
            if request.GET.get('denied'):
                comp_name = request.GET.get('denied')
                job_upt = JobDetail.objects.filter(company_name=comp_name)
                job_upt.update(admin_approval ='Rejected')
                comp_detail=JobDetail.objects.filter(admin_approval='review')
                return render(request,'tpo/approval.html',{ 'comp_detail':comp_detail,'title':'TPO-Approval'})
            else:
                return render(request,'tpo/approval.html',{'comp_detail':comp_detail,'title':'TPO-Approval'})
        else:
            return render(request,'students/student.html')    
    else:
        return redirect('logout')
    

@login_required    
def spa(request):
    if 'tpo' in request.session:
        if request.method == 'POST':
            with open('dtc.pkl', 'rb') as f:
                my_model = pickle.load(f)
            # get the uploaded file from the form data
            file = request.FILES['file']
            with tempfile.NamedTemporaryFile(delete=False) as temp:
                for chunk in file.chunks():
                    temp.write(chunk)
            # initialize the counters
            placed = 0
            unplaced = 0
            
            # process the data row by row
            reader = csv.reader(open(temp.name, 'rt'))

            for row in reader:
                # normalize the row values using MinMaxScaler
                # data_list = [float(x) for x in row]
                # normalized_data = scaler.fit_transform([data_list])
                # convert the row to a list of column values
                data_list = [float(x) for x in row]
                data_array = np.array(data_list)
                reshaped_array = data_array.reshape(1, -1)

                my_prediction = my_model.predict(reshaped_array)

                if my_prediction == 1:
                    placed += 1
                else:
                    unplaced += 1
            context = {'placed': placed, 'unplaced': unplaced}
            # Render a template with the prediction result
            return render(request, 'tpo/spa.html', context)    
        
        else:
            # create an instance of the file upload form
            form = UploadFileForm()
            return render(request, 'tpo/spa.html', {'form': form})  
    else:
        return redirect('logout')





    # x=[[22,1,3,1,8,1,1]]