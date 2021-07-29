from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

import debug_toolbar

from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('artistMarket.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', user_views.register, name='register'),
    path('__debug__/', include(debug_toolbar.urls)),
]
