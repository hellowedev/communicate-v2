"""
URL configuration for communicate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = 'share'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.share_create, name='share_create') ,
    path('<int:share_id>/edit/', views.share_edit, name='share_edit') ,
    path('<int:share_id>/delete/', views.share_delete, name='share_delete') ,
]
