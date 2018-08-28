"""ipoms URL Configuration

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



from . import views

urlpatterns = [

    url(r'^addStock$', views.add_stock, name='addStock'),
    url(r'^listStock$', views.list_stock, name='listStock'),

    url(r'^listUnderwriter$', views.list_underwriter, name='listUnderwriter'),
    url(r'^addUnderwriter$', views.add_underwriter, name='addUnderwriter'),
    url(r'^deleteUnderwriter$', views.delete_underwriter, name='deleteUnderwriter'),

    url(r'^listProduct$', views.list_product, name='listProduct'),
    url(r'^addProduct$', views.add_product, name='addProduct'),
    url(r'^saveProduct$', views.save_product, name='saveProduct'),
    url(r'^deleteProduct$', views.delete_product, name='deleteProduct'),


]