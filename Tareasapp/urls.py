from django.urls import path
from Tareasapp import views

urlpatterns = [
    path('tasks/', views.tareas_api),
    path('tasks/register', views.tareas_api),
    path('tasks/update', views.tareas_api),
    path('tasks/delete/<id>',views.tareas_api)
]