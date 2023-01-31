from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='stuHome'),
    path('addStudentDetails/',views.addStudentDetails, name='addUserDet'),
    path('viewStudentDetails/',views.viewUserDetails, name='viewUserDet'),
    path('studentDetails/',views.studentDetails, name='stuDet'),
]

