from django.urls import path
from . import views

urlpatterns = [
    path('set_session_item/', views.set_item),
    path('get_session_item/', views.get_item, name='get-item'),
    path('del_session_item/', views.del_item),
    path('session_methods/', views.session_methods),

    # page count pr0ject link
    path('page_count/', views.page_count)

]
