from django.urls import path
from .views import(ObtainAuthTokenView,updateuserdetails,deleteuserdetails

)



app_name = 'users'

urlpatterns = [
 	path('api_login', ObtainAuthTokenView.as_view(), name="api_login"), # this url use for api login
 	path('<slug>/update/', updateuserdetails, name="update"), # this url use for update the image and captions
 	path('<slug>/delete/', deleteuserdetails, name="delete"), # this url use for delete the image and captions

]