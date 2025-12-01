# code/simplelms/core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create-user/', views.create_test_user, name='create_test_user'),
    path('create-course/', views.create_course_from_query, name='create_course_from_query'),
    path('all-course/', views.allCourse, name='api_all_courses'),
    path('user-courses/', views.userCourses, name='api_user_courses'),
    path('stats-courses/', views.courseStat, name='api_course_stats'),
    path('stats-members/', views.courseMemberStat, name='api_member_stats'),
    path('course-detail/<int:course_id>/', views.courseDetail, name='api_course_detail'),
]