from django.contrib import admin
from django.urls import path, include
from first_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("studentapi", views.StudentViewSet, basename="student")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
