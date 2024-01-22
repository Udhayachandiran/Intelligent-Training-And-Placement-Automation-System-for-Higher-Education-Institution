from django.urls import path
from . import views

urlpatterns = [
    path('company/',views.companyDetails, name='company'),
    path('addCompanyDetails/',views.addCompanyDetails, name='addCompDet'),
    path('home/',views.hiringHome, name='hiringHome'),
    path('appliedStu/',views.students_applied_to_company, name='appliedStu'),
    path('viewStuD/',views.viewIndividualStudent, name='viewStuD'),
]