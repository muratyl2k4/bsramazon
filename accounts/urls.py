from django.urls import path
import accounts.views as views 
urlpatterns = [
    path('test' , views.test , name='loginpage')
]