from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from custom.views import home_page, user_signup, user_login, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),  # this url use for admin site
    path('home/', home_page, name='home'),  # this url use for dashboard page
    path('', user_signup, name='signup'),  # this url use for signup page
    path('login/', user_login, name='login'),  # this url use for login page
    path('logout/', user_logout, name='logout'),  # this url use for logout page
    path('api/users/', include('custom.api.urls', 'users_api')),  # this url use for API
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)