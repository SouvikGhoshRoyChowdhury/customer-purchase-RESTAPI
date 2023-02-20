## customer-purchase API
The assignment is to implement customer purchases api using django/django rest framework. This api is used to create/update and remove customer purchases, the purchases should contain an identification number, a name and the quantity that the customer selected. A customer has an identification number a full name and an address. 

The API includes 
1. Customer Model For Creating and Handling Users
2. Product Model With Category create/update and remove customer purchases
3. Cart System Responsible For 
4. JWT Authentication 
5. Interactive Swagger documentation Over Django Rest Framework Default User Interface


### Usage
Clone the repository using the git command
```
git clone https://github.com/SouvikGhoshRoyChowdhury/customer-purchase-RESTAPI
```

Enter into the project's root directory
```
cd customer-PurchaseAPI
```

Create a virtual environment and activate it:
```
python -m venv <name_of_your_virtual_environment>
```

To Activate virtual environment (For Windows)
```
./venv/Scripts/activate.bat
```

To Activate virtual environment (For Linux)
source ./venv/Scripts/activate
```
Create .env file in project's root directory and add below
```
SECRET_KEY=SECRETTEST
DB_NAME=SQLite
```
Run makemigrations and migrate
```
python manage.py makemigrations customers products
python3 manage.py migrate
```

Run the tests
```
python manage.py test
```
Run the development server
```
python3 manage.py runserver
```

### Docs 
The documentation for the API and all endpoints are available at:

```
http://localhost:8000/api/v1/swagger/
```
### Schema 

```
http://localhost:8000/api/v1/openapi/
```
### API Endpoints 
The various endpoints for the API.
Assuming the local server is running at http://localhost:8000

#### Authentication and Customers
Create a customer account
```
POST http://localhost:8000/api/v1/customers/

```

Login into customer account
```
POST http://localhost:8000/api/v1/api-auth/login/

```

Retrieve access token (jwt) for customer
```
POST http://localhost:8000/api/v1/api-auth/token/


Refresh access token (jwt) for user
```
POST http://localhost:8000/api/v1/api-auth/token/refresh/
```

#### Products 
Retrieve all products
```
GET http://localhost:8000/api/v1/products/

```

Retrieve a single product
```
GET http://localhost:8000/api/v1/products/{id}
```

Add a product with Id to cart
```
POST http://localhost:8000/api/v1/products/{Id}/

```

Remove a product from cart 
```
DELETE http://localhost:8000/api/v1/products/{Id}/
```


#### Cart 
Retrieve cart
```
GET http://localhost:8000/api/v1/cart/
```

Update an item in cart
```
PUT http://localhost:8000/api/v1/cart/

Request body 
{
    "<product_name>": <5> (new quantity)
}
```

Remove an item from cart
```
DELETE http://localhost:8000/api/v1/cart/

Request body 
{
    "<product_name>": "<>"
}
if request body is empty, cart will be cleared.
```
## Docker
Sample docker file and docker compose yml provided to mimic containrized solution using postgres database
as local machine do not have docker installed need more ram to install docker

## Improvements
Add more functionality on Product and Cart Model,involve more tests at views and serializers label
which would be done if large time frame given to complete the assignment.

#### Presently this simple api is built on monday at office with love and from kpn working experience cosuming around 4 hours out of 8 hours regular time
