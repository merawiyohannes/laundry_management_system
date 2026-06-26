# 🧺 Kokeb Laundry ERP

A simple but powerful Laundry Management System built with Django.

Developed for real-world laundry business operations including:
- Order management
- Customer tracking
- Payment handling
- Business analytics dashboard
- Worker and owner role system

---

## 🚀 Features

### 📦 Orders
- Create unlimited laundry orders
- Add multiple services per order
- Track order status (Received → Washing → Drying → Ironing → Ready → Collected)

### 👤 Customers
- Store customer details
- Phone-based tracking system

### 💳 Payments
- Record payments per order
- Automatic balance calculation
- Payment history tracking

### 📊 Dashboard (Owner)
- Daily orders overview
- Revenue tracking (daily & weekly)
- Active & completed orders
- Business analytics (customers, workers, payments)

### 👥 User Roles
- Superuser (Owner)
- Worker accounts
- Role-based dashboard access

---

## 🛠 Tech Stack

- Python
- Django
- PostgreSQL (Neon DB)
- TailwindCSS (CDN)
- Gunicorn (deployment)
- Whitenoise (static files)

---

## ⚙️ Setup (Local)

```bash
git clone https://github.com/merawiyohannes/laundry_management_system.git
cd kokeb-laundry

python -m venv env
source env/bin/activate  # or env\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver