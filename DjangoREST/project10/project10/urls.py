from django.contrib import admin
from django.urls import path, include
from first_app import views
from rest_framework.routers import DefaultRouter

'''this is for authentication and persmission'''
# router = DefaultRouter()

# router.register("studentapi", views.StudentViewSet, basename="student")

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", include(router.urls)),
#     path('auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

'''this is for authentication and persmission function based view api'''

from django.contrib import admin
from django.urls import path
from first_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("studentapi/", views.student_api),
    path("studentapi/<int:pk>", views.student_api),
]