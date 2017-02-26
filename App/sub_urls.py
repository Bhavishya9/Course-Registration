from django.conf.urls import url

import classviews
from . import views
from CR import settings

urlpatterns=[
                url(r'^testview', views.testview),
                url(r'^admin/$', views.adminview),
                url(r'^createStudent/$',views.adduser),
                url(r'^createProfessor/$',views.adduser),
                url(r'^addstudent/(?P<new_user>[a-zA-Z0-9]+)$',views.addstudent),
                url(r'^addprofessor/(?P<new_user>[a-zA-Z0-9]+)$',views.addprofessor),
                url(r'^successful/$',views.confirm),
                url(r'^studentpage/$',views.studentview),
                url(r'^professorpage/$',views.professorview),
                url(r'^showcatelogue/$',classviews.catelogueListView.as_view(),name="cats_list"),
                url(r'^catelogue/(?P<pk>[0-9]+)/$',classviews.catelogueDetailView.as_view(),name="courses_list"),
                url(r'^catelogue/new/$',views.newCat,name="new_cat"),
                url(r'catelogue/course/(?P<pk>[0-9]+)/new/$',views.courseCreate,name="new_course"),

]