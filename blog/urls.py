from django.urls import path
from .views import computers,contact,index,mans_clothers,womans_clothers, detail,cdetail,comdetail,mdetail,wdetail,ComputersUpdateView,ComputersDeleteView,ComputersCreateView

urlpatterns = [
    path('computers',computers, name='computers'),
    path('contact',contact, name='contact'),
    path('', index, name='index'),
    path('mans_clothers',mans_clothers, name='mans_clothers'),
    path('womans_clothers',womans_clothers, name='womans_clothers'),
    path('detail/<int:id>/',detail, name='detail'),
    path('cdetail/<int:id>/',cdetail, name='cdetail'),
    path('comdetail/<int:id>/',comdetail, name='comdetail'),
    path('mdetail/<int:id>/',mdetail, name='mdetail'),
    path('wdetail/<int:id>/',wdetail, name='wdetail'),
    path('computers/edit/<slug>/', ComputersUpdateView.as_view(), name='computersUpdate'),
    path('computers/delete/<slug>/',ComputersDeleteView.as_view(),name='computersDelete'),
    path('computers/create',ComputersCreateView.as_view(), name='computersCreate')


]


