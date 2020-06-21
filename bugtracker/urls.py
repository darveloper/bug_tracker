"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from tracker.views import index, add_new_ticket, edit_ticket, ticket_detail, completed_ticket, invalid_ticket, user_page

urlpatterns = [
    path('', index, name='home'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add/', add_new_ticket),
    path('edit/<int:id>', edit_ticket),
    path('ticket/<int:id>', ticket_detail),
    path('invalid/<int:id>', invalid_ticket),
    path('admin/', admin.site.urls),
    path('completed/<int:id>', completed_ticket),
    path('userpage/<int:id>', user_page)
]
