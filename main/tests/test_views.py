from django.test import TestCase,Client
from django.urls import reverse
from main.models import Receipt 


class TestViews(TestCase):

    def test_receipt_list_GET(self):
        client = Client()
        response = client.get(reverse("receipts"))
        self.assertEquals(response.status_code,302)
        self.assertTemplateUsed("receipt/listReceipt.html")