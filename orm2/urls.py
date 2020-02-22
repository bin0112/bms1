"""orm2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add/', views.addrecode),
    url(r'^query/', views.query),
    url(r'^query2/', views.query2),
    url(r'^books/$', views.book_view),
    url(r'^$', views.book_view),
    url(r'^books/add/$', views.book_add),
    url(r'^books/edit/(?P<edit_book_id>\d+)$', views.book_edit),
    url(r'^books/delete/(?P<del_book_id>\d+)$', views.book_del),
    url(r'^books/ajax_delete/(?P<del_book_id>\d+)/$', views.book_ajax_del),

]
