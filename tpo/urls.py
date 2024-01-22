from django.urls import path
from . import views

urlpatterns = [
    path('tpoApproval',views.tpoApproval, name='tpoA'),
    path('tpoApproval/Approved/',views.approvedDrive, name='approvD'),
    path('tpoApproval/Denied/',views.deniedDrive, name='deniedD'),
    path('spa/',views.spa, name='spa'),
]