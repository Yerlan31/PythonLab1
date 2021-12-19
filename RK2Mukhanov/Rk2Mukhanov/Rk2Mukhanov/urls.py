from django.contrib import admin
from django.urls import path, include
from labr import views
# import sys
# sys.path.insert(0, './labrk2/')
# import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('', views.output, name='output')
]
