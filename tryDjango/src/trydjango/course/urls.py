from .views import CourseDetailView, CourseListView, CourseCreateView, CourseUpdateView
from django.urls import path

urlpatterns = [
    path('<int:id>', CourseDetailView.as_view(), name='course_detail_view'),
    path('create/', CourseCreateView.as_view(), name='course_create_view'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='course_update_view'),
    path('', CourseListView.as_view(), name='course_list_view'),
]