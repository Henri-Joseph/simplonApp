from django.urls import include, path
from visiteCandidats import views

urlpatterns = [
    path('', views.show),
    path('cdt', views.cdt),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]