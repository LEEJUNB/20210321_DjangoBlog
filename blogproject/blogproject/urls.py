from django.contrib import admin
from django.urls import path
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),

    # html form 이용한 블로그 객체
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # django form 이용한 블로그 객체생성
    path('djangocreate/', views.djangocreate, name='djangocreate'),
]