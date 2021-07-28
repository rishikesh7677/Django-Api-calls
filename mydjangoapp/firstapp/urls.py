from django.urls import path
from django.urls.resolvers import URLPattern
from .import views,productviews

urlpatterns=[
    path("fir",views.index),
    path("cancel/<int:ordid>/<int:prodid>",views.cancel),
    path("addproduct",productviews.addproduct),
    path("addorder",views.addorder),
    path("update/<int:ordid>/<int:prodid>",views.updatestatus)
]