# **MarketLink (Backend)**

MarketLink is a multi-vendor marketplace platform that connects vehicle owners with local repair shops.This backend is built using **Django REST Framework** and supports vendors, customers, services with variants, orders, and online payments.

## **Features**

-   Custom User model with roles (**Customer, Vendor, Admin**)
-   Vendor profile management
-   Vendor services with multiple price variants
-   Stock-based service booking (concurrency safe)
-   Order management
-   SSLCommerz payment gateway integration
-   JWT Authentication

## **Tech Stack**

-   Django
-   Django REST Framework
-   JWT (SimpleJWT)
-   PostgreSQL
-   SSLCommerz (Sandbox)

## **Authentication**

JWT based authentication is used.

After login, use the token in all protected requests:

```
Authorization: Bearer <access_token>
```

## **API Endpoints**

| Action         | Endpoint                                    |
| -------------- | ------------------------------------------- |
| Register       | `POST /api/auth/register/`                  |
| Login          | `POST /api/auth/login/`                     |
| Create Vendor  | `POST /api/vendors/`                        |
| Get Vendors    | `GET /api/vendors/`                         |
| Create Service | `POST /api/services/`                       |
| Get Services   | `GET /api/services/`                        |
| Create Variant | `POST /api/services/{service_id}/variants/` |
| Place Order    | `POST /api/orders/`                         |
| My Orders      | `GET /api/orders/`                          |

## **API Request Examples**

### **Register**

`POST /api/auth/register/`

```json
{
    "email": "demo@mail.com",
    "first_name": "Rahim",
    "last_name": "Khan",
    "password": "password@123",
    "password_2": "password@123"
}
```

### **Login**

`POST /api/auth/login/`

```json
{
    "email": "demo@mail.com",
    "password": "password@123"
}
```

### **Become a Vendor**

`POST /api/vendors/`

```json
{
    "business_name": "ABC Motors",
    "address": "Dhaka"
}
```

### **Create Service**

`POST /api/services/`

```json
{
    "service_name": "Car Wash",
    "description": "Complete car cleaning service"
}
```

### **Create Service Variant**

`POST /api/services/{service_id}/variants/`

```json
{
    "variant_name": "Express",
    "price": 1200,
    "estimated_minutes": 30,
    "stock": 2
}
```

### **Place Order**

`POST /api/orders/`

```json
{
    "variant": 2
}
```

Response:

```json
{
    "order_id": "a8f2c3...",
    "payment_url": "https://sandbox.sslcommerz.com/..."
}
```

The frontend redirects the user to `payment_url` to complete payment.

### **My Orders**

`GET /api/orders/`

Returns all orders for the logged-in customer.

## **Business Logic Overview**

-   Users register as **customers by default**
-   A user becomes a **vendor** by creating a vendor profile
-   Vendors create services and variants
-   Customers place orders on variants
-   Stock is reduced using database-level locking to prevent over-booking
-   Payments are processed via **SSLCommerz**

## **Order Status Flow**

```
pending → paid → processing → completed
            ↘
           failed / cancelled
```

Kawsar Matubbor
