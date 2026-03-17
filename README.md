# STORA - Warehouse Management System

## Project Concept
A professional inventory and sales tracking system designed for small to medium warehouses.

## Tech Stack
- **Framework:** Django 5.x / 6.x
- **Database:** PostgreSQL
- **Frontend:** Custom CSS with a focus on UX/UI and Responsive Tables.

## Key Features & Implementations
- **Dashboard:** Real-time statistics using Django ORM Aggregation (`Sum`, `Count`).
- **Advanced Sales:** Complex sales processing with `inlineformset_factory`.
- **Business Logic:** Automatic stock deduction and price calculation within `models.py`.
- **Validation:** Custom regex validators for VAT and BULSTAT numbers.
- **Custom Filters:** Custom template tags for currency formatting.
- **Error Handling:** Personalized 404 page for better user experience.

## How to Run
1. `pip install -r requirements.txt`
2. Configure DB in `settings.py`
3. `python manage.py migrate`
4. `python manage.py runserver`