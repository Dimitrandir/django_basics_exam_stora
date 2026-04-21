# STORA - Warehouse Management System

STORA is a Django-based warehouse and sales management system designed for small and medium-sized businesses. It provides tools for managing products, categories, suppliers, sales, deliveries, employee accounts, reports, and background processing with Celery.

---

## Project Overview

The system is built around a modular Django architecture with separate apps for accounts, products, sales, deliveries, reports, and core functionality. It includes:

- a custom user model
- user registration and authentication
- product, category, and supplier management
- sales and delivery operations with inline formsets
- dashboard and report pages
- REST API endpoints
- Celery background processing
- responsive templates using Bootstrap

---

## Tech Stack

- **Backend:** Django
- **Database:** PostgreSQL
- **REST API:** Django REST Framework
- **Background Tasks:** Celery + Redis
- **Frontend:** Django Templates + Bootstrap + Custom JavaScript
- **Static Assets:** Custom CSS and image icons

---

## Main Features

### Accounts
- user registration
- login and logout
- extended custom user model
- employee management
- automatic creation of default user groups and permissions

### Products
- product CRUD
- categories CRUD
- suppliers CRUD
- product details
- barcode support

### Sales
- sales creation with inline formsets
- sales list
- sales details
- sales deletion confirmation
- draft save and restore support

### Deliveries
- delivery creation with inline formsets
- deliveries list
- delivery details
- delivery deletion confirmation
- draft save and restore support

### Reports
- dashboard report
- sales report
- deliveries report
- date range filtering
- stock overview

### Async Processing
- Celery background task triggered after successful sale completion

### API Endpoints
- products API
- deliveries API

---

## Project Structure

The project consists of the following Django apps:

- `accounts`
- `core`
- `deliveries`
- `products`
- `reports`
- `sales`

Each app is responsible for a specific part of the system, keeping the codebase organized and maintainable.

---

## Database Models

The application includes several related models such as:

- custom user model
- products
- categories
- suppliers
- barcodes
- sales
- sale items
- deliveries
- delivery items

The database design includes:
- many-to-one relationships
- many-to-many relationships
- one-to-many relationships
- custom user model extension

---

## REST API

The project exposes the following protected REST endpoints:

- `/products/api/products/`
- `/deliveries/api/`

---

## Asynchronous Processing

STORA uses **Celery** for background task processing.  
A background task is triggered after a successful sale is completed so that the main request-response cycle remains fast.

---

## User Groups and Permissions

The application creates the following groups automatically:

- **Managers**
- **Cashiers**
- **Warehouse**

Each group receives different permissions based on its role.

---

## Security Notes

The project uses:

- authentication-protected private views
- CSRF protection
- permission checks on API endpoints
- custom user model
- Django form validation

Sensitive settings such as:
- secret key
- database credentials
- Redis/Celery configuration

should be stored in environment variables in production.

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd STORA
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

---

## Celery / Redis Setup

To run background tasks locally, start Redis and then run the Celery worker:

```bash
celery -A STORA worker -l info
```

Make sure Redis is running before starting the worker.

---

## Environment Variables

Example `.env` file:

```env
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com,127.0.0.1

DB_NAME=stora_db
DB_USER=stora_usr
DB_PASSWORD=your-password
DB_HOST=127.0.0.1
DB_PORT=5432

CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

---

## Testing

The project includes tests for:

- authentication pages
- API endpoints
- sales views
- deliveries views
- form validation
- index page
- template rendering
- custom logic

### Run tests

```bash
python manage.py test
```

---

## Deployment Notes

Before deployment, make sure to:

- set production environment variables
- run migrations
- collect static files
- configure PostgreSQL
- configure Redis if Celery is used
- disable debug mode
- set allowed hosts properly

---

## UI Notes

The frontend uses:

- Django template inheritance
- reusable base layout
- Custom JavaScript
- Bootstrap styling
- custom CSS
- image icons for actions
- responsive tables and cards

---

## Custom Pages

The application includes:

- custom 404 page
- dashboard
- reports pages
- detail pages
- list pages
- create/edit/delete confirmation pages

---

## License

This project is created for educational purposes as part of the Django Advanced retake exam requirements.
```