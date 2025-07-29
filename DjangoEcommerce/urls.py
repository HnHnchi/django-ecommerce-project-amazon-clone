from django.contrib import admin
from django.urls import path
from DjangoEcommerceApp import views
from DjangoEcommerceApp import AdminViews
from django.conf.urls.static import static
from django.urls import include
from DjangoEcommerce import settings

urlpatterns = [
    path('', views.home, name='home'),  # ✅ Add this line
    path('admindashboard/', include("DjangoEcommerceApp.adminurls")),
        path("create/", views.createAccount, name="create_account"),
    path("login/", views.adminLogin, name="admin_login"),
    path("login_process/", views.adminLoginProcess, name="admin_login_process"),
    path("logout/", views.adminLogoutProcess, name="admin_logout"),
    path("admin_home/", views.demoPage, name="admin_home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
