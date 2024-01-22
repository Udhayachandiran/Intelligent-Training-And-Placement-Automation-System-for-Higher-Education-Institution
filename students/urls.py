from django.urls import path
from . import views

urlpatterns = [
    path('stuHome/',views.stuHome, name='stuHome'),
    path('addStudentDetails/',views.addStudentDetails, name='addUserDet'),
    path('viewStudentDetails/',views.viewUserDetails, name='viewUserDet'),
    path('studentDetails/',views.studentDetails, name='stuDet'),
    path('jobs/',views.jobs, name='jobs'),
    path('viewJobDetails/',views.viewJobDetails, name='viewJD'),
    path('applyToJob/',views.applyToJob, name='applyToJob'),
    path('resumeBuilder/',views.resumeBuilder, name='resumeBuilder'),
]

