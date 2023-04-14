from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('members/',views.members,name='members'),
    path('members/all/',views.all_members,name='all_members'),
    path('members/details/<slug:slug>/',views.details,name='details'),
    path('fruits/',views.fruits,name='fruits'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
