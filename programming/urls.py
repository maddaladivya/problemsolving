from django.conf.urls import url, include
from programming import views
from programming.views import viewsummary, detailGroup, studentsDetail, StudentView, dailyChallenges, searchDailyChallenges, home

urlpatterns = [
    url(r'^$', home.as_view(), name='home'),
    url(r'^addstudent/$', StudentView.as_view(), name='studentview'),
    url(r'^viewsummary/$', viewsummary.as_view(), name='viewsummary'),
    #url(r'^creategroup/$', addGroup.as_view(), name='addgroup'),
    url(r'^creategroup/$', views.addgroup, name='addgroup'),
    url(r'^viewgroups/$', views.viewgroups, name='viewgroups'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^deletestudents/$', views.deleteStudents, name='deleteStudents'),
    url(r'^detailgroup/(?P<slug>[\w-]+)/$', detailGroup.as_view(), name='detailgroup'),
    url(r'^profile/(?P<pk>\d+)/$', studentsDetail.as_view(), name='studentsDetail'),
    url(r'^dailychallenges/$', dailyChallenges.as_view(), name='dailyChallenges'),
    url(r'^searchdailychallenges/$', searchDailyChallenges.as_view(), name='searchDailyChallenges'),
]
