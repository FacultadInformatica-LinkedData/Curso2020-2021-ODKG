"""RDFapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from oscar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name="home"),
    path('contract/notice/<str:contractId>/', views.ContractNotice.as_view(), name="contract-notice-one"),
    path('contract/body/<str:contractId>/', views.ContractBody.as_view(), name="contract-body-one"),
    path('contracts', views.ContractNoticeList.as_view(), name="contracts-list"),
    path('caes', views.ContractBodyList.as_view(), name="cae-list"),
    path('country/<str:countryName>', views.Country.as_view(), name="country-one"),
    path('town/<str:townName>', views.Town.as_view(), name="country-one")
]
