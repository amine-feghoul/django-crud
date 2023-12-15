from django.urls import path,include
from .views import *
urlpatterns = [
    path("",listView, name="receipts"),
    path("receipts/",listView, name="receipts"),
    path("receipts/<int:pk>/",detailView, name="receipt-details"),
    path("signup/",signup, name="sign-up"),
    path("add-receipt/",addRecipt, name="add-receipt"),
    path("edit-receipt/<int:pk>/",edit_recipt, name="receipt-edit"),
]
