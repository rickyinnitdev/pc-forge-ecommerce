# PC Forge Store - Full Stack E-Commerce (FastAPI + Vue 3 + MySQL)

This project is a complete full stack e-commerce website for selling gaming PCs and PC components.

## Tech Stack

- Backend: FastAPI (Python)
- Frontend: Vue.js 3 (Composition API) + Tailwind CSS
- Database: MySQL
- Containerization: Docker + Docker Compose

## Features

### Client Side
- Home page with hero banner and featured products
- Product listing page with search and filters (category + price)
- Product detail page with image gallery
- Shopping cart (add/remove/update quantity)
- Checkout form page
- Order confirmation page

### Admin Side
- Admin JWT login
- Dashboard with metrics and chart
- Product CRUD (add/edit/delete with image URL)
- Order management and status updates
- Inventory tracking (low stock highlights)

### API
- REST API with FastAPI
- JWT authentication for admin routes
- CORS enabled
- Swagger docs at `/docs`

## Important Image Rule Applied

All product images are real online URLs from `images.unsplash.com`.
No local image files are used.

## Default Admin Credentials

- Email: `admin@pcforge.com`
- Password: `Admin@12345`

## Project Structure

```text
Ecommerce/
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── auth.py
│   │   │   ├── cart.py
│   │   │   ├── orders.py
│   │   │   └── products.py
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── seed.py
│   ├── .env.example
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── AdminNav.vue
│   │   │   ├── ProductCard.vue
│   │   │   └── SiteHeader.vue
│   │   ├── router/
│   │   │   └── index.js
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── stores/
│   │   │   ├── admin.js
│   │   │   └── cart.js
│   │   ├── views/
│   │   │   ├── admin/
│   │   │   │   ├── AdminDashboardView.vue
│   │   │   │   ├── AdminInventoryView.vue
│   │   │   │   ├── AdminLoginView.vue
│   │   │   │   ├── AdminOrdersView.vue
│   │   │   │   └── AdminProductsView.vue
│   │   │   ├── CartView.vue
│   │   │   ├── CheckoutView.vue
│   │   │   ├── HomeView.vue
│   │   │   ├── OrderConfirmationView.vue
│   │   │   ├── ProductDetailView.vue
│   │   │   └── ProductsView.vue
│   │   ├── App.vue
│   │   ├── main.js
│   │   └── style.css
│   ├── .env.example
│   ├── Dockerfile
│   ├── index.html
│   ├── package.json
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   └── vite.config.js
├── .env.example
├── docker-compose.yml
└── README.md
```

## 12 Pre-Filled Sample Products

Database is seeded automatically with:
- Gaming PCs: 4 products
- Office PCs: 3 products
- Components: 3 products
- Accessories: 2 products

Each includes:
- Name
- Category
- Price (USD)
- Description
- Unsplash image URL
- Stock quantity

## Step-by-Step Setup (Beginner Friendly)

### 1) Install prerequisites

Make sure you have:
- Docker
- Docker Compose (v2)

### 2) Open terminal in project root

Project root is the folder containing `docker-compose.yml`.

### 3) Copy environment file

```bash
cp .env.example .env
```

### 4) Build and start all services

```bash
docker compose up --build
```

This starts:
- MySQL database
- FastAPI backend
- Vue frontend

### 5) Access the app

- Frontend Store: `http://localhost:5173`
- Backend API Root: `http://localhost:8000`
- Swagger Docs: `http://localhost:8000/docs`

## How To Add New Products As Admin

1. Open `http://localhost:5173/admin/login`
2. Login with:
   - `admin@pcforge.com`
   - `Admin@12345`
3. Go to **Products** page in admin panel
4. Click **Add Product**
5. Fill all fields:
   - Name
   - Category
   - Price
   - Description
   - Image URL (must be a working Unsplash URL)
   - Stock quantity
6. Click **Save**

The product appears instantly in both admin and shop listings.

## Useful Commands

Start:
```bash
docker compose up --build
```

Stop:
```bash
docker compose down
```

Stop and remove DB data:
```bash
docker compose down -v
```

## Small Sample Products (ready to copy)

If you want a quick small list before running, use:
- `sample_products_small.json`

It contains 6 products with real online `images.unsplash.com` URLs and includes:
- name
- category
- price
- description
- image_url
- stock_quantity
