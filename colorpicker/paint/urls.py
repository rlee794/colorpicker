from django.urls import path

from paint.views import ColorPickerView

urlpatterns = [
    path('', ColorPickerView.as_view(), name='paint'),
]