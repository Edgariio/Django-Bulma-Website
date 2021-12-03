from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.summary, name='summary'),
    path('summary', views.summary, name='summary'),
    path('installation', views.installation, name='installation'),
    path('tutorial', views.tutorial, name='tutorial'),
    path('page4', views.page4, name='page4'),
    path('conclusions', views.conclusions, name='conclusions'),
    path('credits', views.credits, name='credits'),
    path('delete/<int:post_id>', views.delete, name='delete'),
    path('edit/<int:post_id>', views.edit, name="edit"),
]
