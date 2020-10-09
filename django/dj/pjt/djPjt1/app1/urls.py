from django.urls import path
from . import views
app_name = 'app1'
urlpatterns = [
        path('login/', views.loginApp, name='login'), 
        path('register/', views.registerApp, name='register'),
        path('store/<str:img_name>/<str:leftRight>/<str:openClose>/', views.storeImageApp, name='storeImage'),
        path('getImage/', views.getImageApp, name='getImage'),
]
