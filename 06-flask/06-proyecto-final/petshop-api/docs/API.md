# API Documentation

This document describes the available endpoints for the PetShop E-Commerce API.

Base URL:

```text
http://localhost:5000
```

Protected endpoints require a JWT access token:

```http
Authorization: Bearer <access_token>
```

---

## Authentication

### Register User

```http
POST /auth/register
```

Access: Public

Request body:

```json
{
  "name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "password": "password123"
}
```

Successful response:

```json
{
  "message": "User registered successfully.",
  "access_token": "<jwt_token>"
}
```

Status:

```text
201 Created
```

Possible errors:

- `400 Bad Request` - Missing request body.
- `400 Bad Request` - Missing required fields.
- `400 Bad Request` - Email already registered.

---

### Login

```http
POST /auth/login
```

Access: Public

Request body:

```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

Successful response:

```json
{
  "message": "Login successful.",
  "access_token": "<jwt_token>"
}
```

Status:

```text
200 OK
```

Possible errors:

- `400 Bad Request` - Missing request body.
- `400 Bad Request` - Email or password missing.
- `401 Unauthorized` - Invalid email or password.

---

### Get Current User

```http
GET /auth/me
```

Access: Authenticated user

Successful response:

```json
{
  "user": {
    "id": 1,
    "role": "CLIENT"
  }
}
```

Status:

```text
200 OK
```

---

# Products

## Get All Products

```http
GET /products
```

Access: Authenticated user

Description:

Returns all products. The endpoint uses Redis caching with the key:

```text
products:all
```

Status:

```text
200 OK
```

---

## Get Product by ID

```http
GET /products/<product_id>
```

Access: Authenticated user

Example:

```http
GET /products/1
```

Redis cache key:

```text
product:<product_id>
```

Possible responses:

- `200 OK`
- `404 Not Found`

---

## Create Product

```http
POST /products
```

Access: ADMIN

Request body:

```json
{
  "name": "Premium Dog Food",
  "price": 29.99,
  "stock": 50
}
```

Required fields:

- `name`
- `price`
- `stock`

Status:

```text
201 Created
```

Possible errors:

- `400 Bad Request`
- `401 Unauthorized`
- `403 Forbidden`

The `products:all` cache entry is invalidated after creation.

---

## Update Product

```http
PUT /products/<product_id>
```

Access: ADMIN

Example request:

```json
{
  "price": 34.99,
  "stock": 75
}
```

Fields can be updated partially.

Status:

```text
200 OK
```

Possible errors:

- `400 Bad Request`
- `404 Not Found`
- `401 Unauthorized`
- `403 Forbidden`

The following Redis keys are invalidated:

```text
product:<product_id>
products:all
```

---

## Delete Product

```http
DELETE /products/<product_id>
```

Access: ADMIN

Description:

Disables the product through the application's product deletion logic.

Successful status:

```text
204 No Content
```

Possible errors:

- `404 Not Found`
- `401 Unauthorized`
- `403 Forbidden`

The product cache and product list cache are invalidated.

---

# Billing Addresses

## Get Billing Addresses

```http
GET /billing-addresses
```

Access: Authenticated user

Description:

Returns all billing addresses belonging to the authenticated user.

Status:

```text
200 OK
```

---

## Get Billing Address

```http
GET /billing-addresses/<address_id>
```

Access: Authenticated user

The authenticated user can only access their own billing addresses.

Possible responses:

- `200 OK`
- `403 Forbidden`
- `404 Not Found`

---

## Create Billing Address

```http
POST /billing-addresses
```

Access: Authenticated user

Request body:

```json
{
  "address": "123 Main Street",
  "city": "Heredia",
  "province": "Heredia",
  "postal_code": 40101,
  "country": "Costa Rica"
}
```

Required fields:

- `address`
- `city`
- `province`
- `postal_code`
- `country`

Status:

```text
201 Created
```

Possible errors:

- `400 Bad Request`
- `401 Unauthorized`

---

## Update Billing Address

```http
PUT /billing-addresses/<address_id>
```

Access: Authenticated user

Example:

```json
{
  "address": "456 New Street",
  "city": "San Rafael"
}
```

Possible responses:

- `200 OK`
- `400 Bad Request`
- `403 Forbidden`
- `404 Not Found`

---

## Delete Billing Address

```http
DELETE /billing-addresses/<address_id>
```

Access: Authenticated user

Successful status:

```text
204 No Content
```

Possible errors:

- `403 Forbidden`
- `404 Not Found`

---

# Shopping Carts

## Get Active Cart

```http
GET /carts/active
```

Access: Authenticated user

Description:

Returns the user's active cart. If no active cart exists, the service creates one.

Status:

```text
200 OK
```

---

## Get User Carts

```http
GET /carts
```

Access: Authenticated user

Description:

Returns the authenticated user's carts, including previous carts.

Status:

```text
200 OK
```

---

## Get Cart

```http
GET /carts/<cart_id>
```

Access: Authenticated user

Users can only access their own carts.

Possible responses:

- `200 OK`
- `403 Forbidden`
- `404 Not Found`

---

## Add Product to Cart

```http
POST /carts/<cart_id>/items
```

Access: Authenticated user

Request body:

```json
{
  "product_id": 1,
  "quantity": 2
}
```

Required fields:

- `product_id`
- `quantity`

Status:

```text
200 OK
```

Possible errors:

- `400 Bad Request`
- `403 Forbidden`
- `404 Not Found`

---

## Update Product Quantity

```http
PUT /carts/<cart_id>/items/<product_id>
```

Access: Authenticated user

Request body:

```json
{
  "quantity": 3
}
```

Status:

```text
200 OK
```

Possible errors:

- `400 Bad Request`
- `403 Forbidden`
- `404 Not Found`

---

## Remove Product from Cart

```http
DELETE /carts/<cart_id>/items/<product_id>
```

Access: Authenticated user

Status:

```text
200 OK
```

Possible errors:

- `400 Bad Request`
- `403 Forbidden`
- `404 Not Found`

---

## Abandon Cart

```http
DELETE /carts/<cart_id>
```

Access: Authenticated user

Description:

Marks the selected active cart as abandoned according to the cart service logic.

Status:

```text
200 OK
```

Possible errors:

- `400 Bad Request`
- `403 Forbidden`
- `404 Not Found`

---

# Checkout

## Complete Checkout

```http
POST /carts/<cart_id>/checkout
```

Access: Authenticated user

Request body:

```json
{
  "billing_address_id": 1,
  "payment_method": "SINPE",
  "payment_reference": "SINPE-123456"
}
```

Required fields:

- `billing_address_id`
- `payment_method`
- `payment_reference`

Successful response:

```json
{
  "message": "Checkout completed successfully.",
  "invoice_number": "INV-ABC123456789",
  "total": 59.98
}
```

Status:

```text
201 Created
```

The checkout process:

1. Validates the cart.
2. Validates cart ownership.
3. Validates the billing address.
4. Validates product availability and stock.
5. Calculates the purchase total.
6. Creates an invoice.
7. Creates invoice product records.
8. Creates a payment.
9. Reduces product stock.
10. Marks the cart as completed.
11. Invalidates the affected product cache entries.

Possible errors:

- `400 Bad Request`
- `403 Forbidden`
- `404 Not Found`

---

# Invoices

## Get Invoices

```http
GET /invoices
```

Access: Authenticated user

Behavior:

- `CLIENT` users receive only their own invoices.
- `ADMIN` users receive all invoices.

Status:

```text
200 OK
```

---

## Get Invoice by Number

```http
GET /invoices/<invoice_number>
```

Access: Authenticated user

Example:

```http
GET /invoices/INV-ABC123456789
```

Behavior:

- Clients can access only their own invoices.
- Administrators can access any invoice.

Possible responses:

- `200 OK`
- `403 Forbidden`
- `404 Not Found`

---

# Returns

## Create Return Request

```http
POST /returns/invoice/<invoice_number>
```

Access: Authenticated user

Example:

```http
POST /returns/invoice/INV-ABC123456789
```

Request body:

```json
{
  "reason": "Product arrived damaged",
  "products": [
    {
      "invoice_product_id": 1,
      "quantity": 1
    }
  ]
}
```

Required fields:

- `reason`
- `products`

Status:

```text
201 Created
```

Possible errors:

- `400 Bad Request`
- `403 Forbidden`
- `404 Not Found`

The user must own the invoice associated with the return.

---

## Update Return Status

```http
PUT /returns/<return_id>/status
```

Access: ADMIN

Request body:

```json
{
  "status": "APPROVED"
}
```

Supported return statuses:

```text
REQUESTED
APPROVED
REJECTED
COMPLETED
```

Status:

```text
200 OK
```

Possible errors:

- `400 Bad Request`
- `404 Not Found`
- `401 Unauthorized`
- `403 Forbidden`

When a return reaches `COMPLETED`, the application restores the returned product stock and recalculates the invoice status.

---

# HTTP Status Codes

| Status | Meaning |
|---|---|
| `200` | Request completed successfully |
| `201` | Resource created successfully |
| `204` | Request completed without a response body |
| `400` | Invalid request or business rule violation |
| `401` | Authentication failed or token is missing/invalid |
| `403` | User does not have permission to access the resource |
| `404` | Requested resource was not found |

---

# Authentication Header

For all protected endpoints, include:

```http
Authorization: Bearer <access_token>
```

Example:

```bash
curl \
  -H "Authorization: Bearer <access_token>" \
  http://localhost:5000/products
```