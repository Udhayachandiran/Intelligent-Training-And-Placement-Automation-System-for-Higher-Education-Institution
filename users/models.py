from django.db import models
# from django.contrib.auth.models import User,AbstractUser
from hiring_team.models import JobDetail
from students.models import Detail
# from allauth.account.models import EmailAddress
# from allauth.socialaccount.models import SocialAccount
# from django.contrib.auth import get_user_model

class StudentJob(models.Model):
    student_id = models.ForeignKey(Detail, on_delete=models.CASCADE)
    job_id = models.ForeignKey(JobDetail, on_delete=models.CASCADE)
    registered_to_job = models.CharField(max_length=30,default="not registered")


# class MyModel(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
# class CustomEmailAddress(EmailAddress):
#     custom_user = models.ForeignKey('your_app_name.CustomUser', on_delete=models.CASCADE)

# class CustomSocialAccount(SocialAccount):
#     custom_user = models.ForeignKey('your_app_name.CustomUser', on_delete=models.CASCADE)    

# class CustomUser(AbstractUser):
#     is_student = models.BooleanField(default=False)


#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.is_student = True  # set is_student flag to True for new users
#         super(User, self).save(*args, **kwargs)


# all_users = User.objects.all()
# for user in all_users:
#     user.is_student = False
#     user.save()
