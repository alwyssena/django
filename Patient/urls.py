from django.contrib import admin
from django.urls import path
from Patient import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.signup),
    path('login/',views.login)
]
