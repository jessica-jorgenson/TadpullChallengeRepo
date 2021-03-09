from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    ItemDetailView,
    HomeView,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    ]
