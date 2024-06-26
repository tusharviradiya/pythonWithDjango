from django.contrib import admin
from django.urls import path, include
from first_app import views
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from first_app.auth import CustomAuthToken

router = DefaultRouter()

router.register("studentapi", views.StudentViewSet, basename="student")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("gettoken/", CustomAuthToken.as_view()),
]