"""tutor_prt URL Configuration

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
from.import views

urlpatterns = [
path('', views.home,name="home"),
path('reg', views.reg,name="reg"),
path('log', views.log,name="log"),
path('logtr', views.logtr,name="logtr"),
path('logins', views.logins,name="logins"),
path('ttr', views.ttr,name="ttr"),
path('trreg', views.trreg,name="trreg"),
path('tcomp', views.tcomp, name="tcomp"),

path('stformlog', views.stformlog, name="stformlog"),
path('trformlog', views.trformlog, name="trformlog"),
path('ad',views.ad,name="ad"),
path('tt',views.tt,name="tt"),
path('order',views.order,name="order"),
path('approve',views.approve,name="approve"),
path('approved',views.approved,name="approved"),
path('see',views.see,name="see"),
path('book',views.book,name="book"),
path('check',views.check,name="check"),
path('check1',views.check1,name="check1"),
path('tutorview',views.tutorview,name="tutorview"),
path('book1',views.book1,name="book1"),
path('ordered',views.ordered,name="ordered"),





    ]


