from django.urls import path, re_path
from register.views import register,login, forgot_password ,activate

app_name = 'accounts'

urlpatterns = [
    path('', register, name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
            activate, name='activate'),
    path('login', login, name='login'),
    path('login/reset-password', forgot_password, name='forgot-password'),

]