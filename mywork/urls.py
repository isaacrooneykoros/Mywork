
from django.contrib import admin
from django.urls import path

from adminapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inner/', views.iconremix,name='iconremix'),
    path('login/', views.iconboxicons,name='iconboxicons'),
    path('register/', views.iconbootstrap,name='iconbootstrap'),
    path('details/', views.formsvalidation,name='formvalidation'),
    path('adminhome/', views.formslayouts,name='formlayouts'),
    path('uploadimage/', views.formselements, name='formselements'),
    path('formeditors/', views.formseditors, name='formseditors'),
    path('componentstooltips/', views.componentstooltips, name='componentstooltips'),
    path('componentstabs/', views.componentstabs, name='componentstabs'),
    path('componentsspinners/', views.componentsspinners, name='componentspinners'),
    path('componentsprogress/', views.componentsprogress, name='componentsprogress'),
    path('componentspagination/', views.componentspagination, name='componentspagination'),
    path('componentstabs/', views.componentstabs, name='componentstabs'),
    path('componentsmodal/', views.componentsmodal, name='componentsmodal'),
    path('componentslistgroup/', views.componentslistgroup, name='componentslistgroup'),
    path('componentscarousel/', views.componentscarousel, name='componentscarousel'),
    path('componentscards/', views.componentscards, name='componentscards'),
    path('componentsbutton/', views.componentsbutton, name='componentsbutton'),
    path('componentsbreadcrumbs/', views.componentsbreadcrumbs, name='componentsbreadcrumbs'),
    path('componentsbadges/', views.componentsbadges, name='componentsbadges'),
    path('componentsalerts/', views.componentsalerts, name='componentsalerts'),
    path('componentsacordion/', views.componentsaccordion, name='componentsaccordion'),
    path('chartsecharts/', views.chartsecharts, name='chartecharts'),
    path('chartschartjs/', views.chartschartjs, name='chartschartsjs'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('tablesgeneral/', views.tablesgeneral, name='tablesgeneral'),
    path('tablesdata/', views.tablesdata, name='tablesdata'),
    path('pageslogin/', views.pageslogin, name='pageslogin'),
    path('pagesfaq/', views.pagesfaq, name='pagesfaq'),
    path('pageserror/', views.pageserror, name='pageserror'),
    path('pagescontact/', views.pagescontact, name='pagescontact'),
    path('pagesblanks/', views.pagesblank, name='pagesblank'),




]

