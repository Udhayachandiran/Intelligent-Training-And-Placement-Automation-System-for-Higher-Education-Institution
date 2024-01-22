from django.contrib.auth import get_user_model
from django.db import models
from allauth.account.models import EmailAddress 

class User_detail(models.Model):
    email =models.EmailField(max_length=70,primary_key=True)
    password = models.CharField(max_length=50)

class Detail(models.Model): 
    # user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True,
    #     default=None)
    # email_address = models.ForeignKey(EmailAddress, on_delete=models.CASCADE,null=True,
    #     default=None)
    fname = models.CharField(max_length=30)
    # email = models.ForeignKey(User_detail,on_delete=models.CASCADE)
    email = models.EmailField(max_length=70)
    rollno =models.PositiveIntegerField()
    dob = models.DateField()
    gender =models.CharField(max_length=8)
    clg_name = models.CharField(max_length= 4)
    degree = models.CharField(max_length=8)
    branch = models.CharField(max_length=6)
    yrOfPass = models.PositiveSmallIntegerField()
    dayscholar = models.CharField(max_length=15)
    phone_no = models.PositiveBigIntegerField()
    ug_cgpa = models.CharField(max_length=6)
    fath_name = models.CharField(max_length=30)
    fath_phone_no = models.PositiveBigIntegerField()
    fath_occu = models.CharField(max_length=25)
    moth_name = models.CharField(max_length=30)
    moth_phone_no = models.PositiveBigIntegerField()
    moth_occu = models.CharField(max_length=25)
    annual_inc= models.PositiveIntegerField()
    native_place = models.CharField(max_length=30)
    curr_addr = models.TextField()
    perr_addr = models.TextField()
    stan_arr = models.PositiveSmallIntegerField()
    hist_arr = models.PositiveSmallIntegerField()
    sslc_mark = models.DecimalField(max_digits=6,decimal_places=2)
    sslc_max_mark = models.DecimalField(max_digits=6,decimal_places=2)
    sslc_med = models.CharField(max_length=10)
    sslc_sch = models.CharField(max_length=30)
    sslc_board = models.CharField(max_length=12)
    sslc_yop = models.PositiveSmallIntegerField()
    hsc_mark = models.DecimalField(max_digits=6,decimal_places=2)
    hsc_max_mark = models.DecimalField(max_digits=6,decimal_places=2)
    hsc_med = models.CharField(max_length=10)
    hsc_sch = models.CharField(max_length=30)
    hsc_board = models.CharField(max_length=12)
    hsc_yop = models.PositiveSmallIntegerField()
    dip_mark = models.DecimalField(max_digits=6,decimal_places=2)
    dip_max_mark = models.DecimalField(max_digits=6,decimal_places=2)
    dip_univ_name = models.CharField(max_length=30)
    dip_branch = models.CharField(max_length=30)
    dip_yop = models.PositiveSmallIntegerField()
    break_in_acca = models.CharField(max_length=30)
    certi_course = models.TextField()
    intern_exp = models.TextField()
    intern_comp_name = models.CharField(max_length=30)
    intern_role = models.CharField(max_length=30)
    inter_duration = models.CharField(max_length=15)

    


 