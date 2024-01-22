from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from allauth.account.signals import user_signed_up
from users.models import Detail, JobDetail, StudentJob

from django.dispatch import receiver
from allauth.account.signals import user_signed_up



# @receiver(user_signed_up)
# def assign_default_role(sender, request, user, **kwargs):
#     # Check if user signed up using Google
#     if user.socialaccount_set.filter(provider='google').exists():
#         # Assign 'student' role to the user
#         student_group, created = Group.objects.get_or_create(name='student')
#         user.groups.add(student_group)


        
@receiver(post_save, sender=Detail)
def add_job_student(sender, instance, **kwargs):
    jobs = JobDetail.objects.all()
    for job in jobs:
        if not StudentJob.objects.filter(student_id=instance, job_id=job).exists():
            StudentJob.objects.create(student_id=instance, job_id=job)



@receiver(post_save, sender=JobDetail)
def create_student_jobs(sender, instance, created, **kwargs):
    if created:
        students = Detail.objects.all()
        for student in students:
            if not StudentJob.objects.filter(student_id=student, job_id=instance).exists():
                student_job = StudentJob.objects.create(student_id=student, job_id=instance)
                student_job.save()
