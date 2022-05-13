from django.urls import path, re_path
from register.views import logout, register,login, forgot_password, change_password ,activate
from .views import UserProfileView
from django.contrib.auth import views as auth_views

from . import views
app_name = 'register'

urlpatterns = [
    path('', register, name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
            activate, name='activate'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('edit-profile/<int:pk>', UserProfileView.as_view(), name='edit-profile'),
    path('login/reset-password', forgot_password, name='forgot_password'),
    path('login/change-password/', change_password, name='change_password'),
    path('login/reset-password/', auth_views.PasswordResetView.as_view(), name='reset-password'),
    path('login/reset-password-sent', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('login/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('login/reset-password-complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #path('myaccounts/', user_profile, name='user-profile'),

]