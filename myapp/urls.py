from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home,name='home' ),
    path('home1/',views.Home,name='home1' ),
    path('about/',views.about,name='about' ),
    path('contact/',views.contact,name='contact' ),
    path('student_list/',views.student_list,name='student_list' ),
    path('add/',views.add_student,name='add_student' ),
    path('edit/<int:pk>/',views.edit_student,name='edit_student' ),
    path('delete/<int:pk>/',views.delete_student,name='delete_student' ),
    path('register/',views.register_view,name='register'),
    path('reshome/',views.reshome,name='reshome'),
    path('resabout/',views.resabout,name='resabout' ),
    
   
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)