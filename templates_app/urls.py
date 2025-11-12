from django.urls import path
from . import views 

urlpatterns = [
    path('all/', views.template_list, name='template-list'), 
    path('category/<str:category>/', views.template_list_by_category, name='template-by-category'),
    path('paid/<str:is_paid>/', views.template_list_free_paid, name='free-and-paid-templates')
]
