from django.test import SimpleTestCase
from django.urls import resolve,reverse

from main.views import listView,detailView,addRecipt,edit_recipt
class TestUrls(SimpleTestCase):    
    def test_receipts_url(self):
        url = reverse("receipts")
        self.assertEquals(resolve(url).func,listView)

    def test_add_receipt_url(self):
        url = reverse("add-receipt")
        self.assertEquals(resolve(url).func,addRecipt)
    
    def test_edit_receipt_url(self):
        url = reverse("receipt-edit",kwargs={'pk': 1})
        self.assertEquals(resolve(url).func,edit_recipt)

    def test_detail_receipt_url(self):
        url = reverse("receipt-details",kwargs={'pk': 1})
        self.assertEquals(resolve(url).func,detailView)