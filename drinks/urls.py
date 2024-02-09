from django.urls import path
from drinks import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "drinks"

urlpatterns = [
    # path('', views.drink_list, name='drinks'),
    # path('<int:id>', views.drink_detail, name='drinks'),
    path('', views.Currency_list, name='drinks'),
    path('<int:id>', views.Currency_detail, name='drinks'),
]

urlpatterns = format_suffix_patterns(urlpatterns)