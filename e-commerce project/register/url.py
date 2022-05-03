from django.urls import path, re_path
from register.views import logout, register,login, forgot_password ,activate
from .views import edit_profile

app_name = 'register'

urlpatterns = [
    path('', register, name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
            activate, name='activate'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('login/reset-password', forgot_password, name='forgot-password'),
    path('edit-profile/', edit_profile, name='edit-profile'),
    #path('myaccounts/', user_profile, name='user-profile'),

]