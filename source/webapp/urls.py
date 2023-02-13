from django.urls import path

from webapp.views.to_do import add_view, detail_view
from webapp.views.base import index_view

urlpatterns = [
    path("", index_view),
    path('to_do/add', add_view),
    path('to_do/', detail_view)
]