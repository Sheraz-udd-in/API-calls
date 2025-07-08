# Django REST API for Products - Steps and Explanation

---

## 1. Project Setup

- A Django project and app were created:
  - **Project name**: `products`
  - **App name**: `api`
- The app was added to `INSTALLED_APPS` in `settings.py`.

---

## 2. Model Creation

A model named `Product` was created with the fields:
- `name` (string)
- `des` (description - string)
- `price` (integer or float)

**Migrations:**
```bash
python manage.py makemigrations
python manage.py migrate

3. View Creation (views.py)
Required modules were imported:

python
Copy
Edit
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
A function-based view products(request) was created to handle:

a. POST Request
Accepts JSON data from the request body.

Deserializes JSON using json.loads(request.body).

Creates and saves a new Product object.

Returns:

json
Copy
Edit
{"message": "success"}
b. GET Request
Fetches all Product objects.

Converts each to a dictionary with keys: name, des, price.

Returns:

json
Copy
Edit
{
  "data": [
    {"name": "LG", "des": "5 star", "price": 20000}
  ]
}
Note: @csrf_exempt was added to allow testing via Postman.

4. App URL Configuration (api/urls.py)
python
Copy
Edit
from django.urls import path
from .views import products

urlpatterns = [
    path('product', products),
]
Accessible at:
/api/product

5. Project-Level URL Configuration (products/urls.py)
python
Copy
Edit
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
]
Full route becomes:
http://127.0.0.2:9000/api/product

6. Allowed Hosts Fix
To fix the error:

DisallowedHost: '127.0.0.2'

Solution in settings.py:

python
Copy
Edit
ALLOWED_HOSTS = ['127.0.0.1', '127.0.0.2', 'localhost']
7. Testing with Postman
a. POST Request
Endpoint: http://127.0.0.2:9000/api/product

Body (raw JSON):

json
Copy
Edit
{
  "name": "LG",
  "des": "5 star",
  "price": 20000
}
Response:

json
Copy
Edit
{"message": "success"}
b. GET Request
Endpoint: http://127.0.0.2:9000/api/product

Response:

json
Copy
Edit
{
  "data": [
    {"name": "LG", "des": "5 star", "price": 20000}
  ]
}
8. Server Logs
Each request prints a log in the terminal:

arduino
Copy
Edit
"GET /api/product HTTP/1.1" 200 OK
"POST /api/product HTTP/1.1" 200 OK
Conclusion ✅
API is functional for both POST and GET methods.

Data is correctly stored and retrieved from the database.

URL routing is working via /api/product.

Postman communicates successfully with the backend.

Server runs at 127.0.0.2:9000 without issues.

