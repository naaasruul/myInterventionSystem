from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),

    # main page for each roles
    path("student/<str:studentId>", views.studentPage, name="studentPage"),
    path("lecturer/<str:mentorId>", views.lecturerPage, name="lecturerPage"),
    path("admin/<str:adminId>", views.adminPage, name="adminPage"),

    # lecturer make report about student behavior
    path("lecturer/lectReport/<str:mentorId>", views.viewsReport, name="lectReport"),
    path("lecturer/lectReport/report/<str:mentorId>", views.lectReport, name="lectReport"),
    path("lecturer/lectReport/report/updateReport/<str:repId>", views.viewUpdateReport, name="lectReport"),
    path("lecturer/lectReport/report/updateReport/update/<str:repId>", views.submitUpdateReport, name="lectReport"),

    # lecturer find student and mentee
    path("lecturer/myStudent/<str:mentorId>", views.displayStudent, name="myStudent"),
    path("lecturer/myStudent/findMyMentee/<str:mentorId>", views.findMyMentee, name="findMyMentee"),

    # lecturer make appointment
    path("lecturer/myAppointment/<str:mentorId>", views.makeAppointment, name="makeAppointment"),
    path("lecturer/myAppointment/submitAppointment/<str:mentorId>", views.submitAppointment, name="makeAppointment"),
    path("lecturer/myAppointment/submitAppointment/updateViewsAppointment/<str:appId>", views.updateAppointment, name="makeAppointment"),
    path("lecturer/myAppointment/submitAppointment/updateAppointment/<str:appId>", views.updateAppointment, name="makeAppointment"),
    path("lecturer/myAppointment/submitAppointment/updateAppointment/update/<str:appId>", views.submitUpdateAppointment, name="makeAppointment"),

    # path("about", views.about, name="about"),
    # path("contact", views.contact, name="contact"),
    # path("newMentor", views.newMentor, name="newMentor"),
    # path("update/<str:mentorId>", views.update, name="update"),
    # path("update/updatedata/<str:mentorId>", views.updateData, name="update"),
    # path("viewdelete/<str:mentorId>", views.viewDelete, name="viewdelete"),
    # path("viewdelete/deletedata/<str:mentorId>", views.delete, name="delete"),
    # path("searchpage", views.searchpage, name="searchpage"),
]