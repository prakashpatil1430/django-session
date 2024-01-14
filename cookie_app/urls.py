from django.urls import path
from . import views

urlpatterns = [
    path('test_cookie/', views.test_cookies),
    path('set/', views.set_cokkies, name='ck-set'),
    path('get/', views.get_cookie, name='ck-get'),
    path('update/', views.update_cookie, name='ck-update'),
    path('delete/', views.delete_cookie, name='ck-delete'),


]
