from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login_request, name="login"),
    path('', views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("counting", views.counting, name="count"),
    path("review_count", views.review_count, name="review_count"),
    path("create_custom_category", views.create_custom_category, name="create_custom_category"),
    path('updatecount', views.updatecount, name="updatecount"),
    path('getcheckdata', views.getcheckdata, name="getcheckdata"),
    path('getcontactdata', views.getcontactdata, name="getcontactdata"),
    path('savenewparishioner', views.savenewparishioner, name="savenewparishioner"),
    path('donation_note', views.donation_note, name="donation_note"),
    path('submit_count', views.submit_count, name="submit_count"),
    path('autosave_checks', views.autosave_checks, name="autosave_checks"),
    path('count_report_redirect', views.count_report_redirect, name="count_report_redirect"),
    path('count_report', views.count_report, name="count_report"),
    path('remove_count_session', views.remove_count_session, name="remove_count_session"),
    path('autosave_count', views.autosave_count, name="autosave_count"),
]
