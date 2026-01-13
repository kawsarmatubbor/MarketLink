import requests
from django.conf import settings

def create_sslcommerz_session(order):
    url = "https://sandbox.sslcommerz.com/gwprocess/v4/api.php"

    payload = {
        "store_id": settings.SSLCOMMERZ_STORE_ID,
        "store_passwd": settings.SSLCOMMERZ_STORE_PASS,

        "total_amount": str(order.variant.price),
        "currency": "BDT",
        "tran_id": str(order.order_id),

        "success_url": f"{settings.BASE_URL}/api/payment/success/{order.order_id}/",
        "fail_url": f"{settings.BASE_URL}/api/payment/fail/{order.order_id}/",
        "cancel_url": f"{settings.BASE_URL}/api/payment/cancel/{order.order_id}/",
        "ipn_url": f"{settings.BASE_URL}/api/payment/ipn/",

        "cus_name": order.customer.first_name or "Customer",
        "cus_email": order.customer.email,
        "cus_phone": "01700000000",
        "cus_add1": "Dhaka",
        "cus_city": "Dhaka",
        "cus_country": "Bangladesh",

        "shipping_method": "NO",
        "num_of_item": 1,

        "product_name": order.variant.service.service_name,
        "product_category": "Service",
        "product_profile": "general",
    }

    response = requests.post(url, data=payload)
    return response.json()
