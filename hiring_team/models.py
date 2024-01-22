from django.db import models
from django.db import connection

class JobDetail(models.Model):
    company_name = models.CharField(max_length=150)
    job_title = models.CharField(max_length=150)
    ctc_min = models.PositiveIntegerField()
    ctc_max = models.PositiveIntegerField()
    other_info = models.TextField(blank=True)
    comp_link = models.TextField()
    drive_strt_date = models.DateField(auto_now=False, auto_now_add=False,blank=False)
    drive_end_date = models.DateField(auto_now=False, auto_now_add=False,blank=False)
    required_skill = models.TextField(blank=True)
    job_desc = models.TextField()
    last_reg_date = models.DateField(auto_now=False, auto_now_add=False,blank=False)
    media = models.FileField(upload_to="media", null=True, blank=True)
    eligible_10th_minp = models.PositiveSmallIntegerField()
    eligible_12th_minp = models.PositiveSmallIntegerField()
    eligible_ug_minp = models.DecimalField(blank=True,max_digits=4, decimal_places=2)
    type_of_offer = models.CharField(max_length=25,default='nil')
    hist_of_arr = models.CharField(max_length=25)
    admin_approval = models.CharField(max_length=30, default='review',blank=True)
    status_of_drive = models.CharField(max_length=100,default='active',blank=True)

# class Job(models.Model):
#     name = models.CharField(max_length=255)

    # def save(self, *args, **kwargs):
    #     super(JobDetail, self).save(*args, **kwargs)
    #     with connection.schema_editor() as schema_editor:
    #         model = type(self.company_name.title(), (models.Model,), {
    #             '__module__': self.__class__.__module__,
    #             'job_id': models.ForeignKey(JobDetail,on_delete=models.CASCADE),
    #             'student_id':models.CharField(max_length=30)
    #         })
    #         schema_editor.create_model(model)

    
