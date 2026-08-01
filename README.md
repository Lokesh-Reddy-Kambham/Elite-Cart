# EliteCart - Modern E-commerce Application

A complete, full-stack e-commerce application built with React, Django, and MySQL.

## Live Demo

- https://elitecart-frontend.vercel.app

## 📋 Features

### Frontend
- ✅ Responsive design (mobile-first)
- ✅ Dark/Light mode toggle
- ✅ Product listing with advanced filters (category, price, stock)
- ✅ Shopping cart with persistent storage
- ✅ User authentication (Login/Signup)
- ✅ Checkout page with order summary
- ✅ User profile with order history
- ✅ Admin panel to manage products
- ✅ Modern UI with Tailwind CSS

### Backend
- ✅ Django REST Framework
- ✅ JWT authentication
- ✅ MySQL database
- ✅ Product management (CRUD)
- ✅ Order management
- ✅ User authentication & authorization
- ✅ CORS enabled for frontend integration

## 🛠️ Tech Stack

### Frontend
- React 18
- React Router v6
- Tailwind CSS
- Lucide React (icons)
- Axios

### Backend
- Django 4.2
- Django REST Framework
- djangorestframework-simplejwt
- django-cors-headers
- MySQL Connector
- Pydantic

### Database
- MySQL

## 📦 Project Structure

```
Elite-Cart/
├── elitecart-frontend/
│   ├── public/
│   │   ├── index.html
│   │   └── manifest.json
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.js
│   │   │   ├── ProductCard.js
│   │   │   ├── Filter.js
│   │   │   ├── CartItem.js
│   │   │   └── Footer.js
│   │   ├── pages/
│   │   │   ├── Home.js
│   │   │   ├── ProductList.js
│   │   │   ├── CartPage.js
│   │   │   ├── CheckoutPage.js
│   │   │   ├── LoginPage.js
│   │   │   ├── SignupPage.js
│   │   │   ├── ProfilePage.js
│   │   │   └── AdminPage.js
│   │   ├── context/
│   │   │   ├── AuthContext.js
│   │   │   ├── CartContext.js
│   │   │   └── ThemeContext.js
│   │   ├── utils/
│   │   │   └── api.js
│   │   ├── assets/
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── index.css
│   │   └── README.md
│   ├── package.json
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── .gitignore
│
├── elitecart-backend/
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── apps/
│   │   ├── users/
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   └── serializers.py
│   │   ├── products/
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   └── serializers.py
│   │   └── orders/
│   │       ├── models.py
│   │       ├── views.py
│   │       ├── urls.py
│   │       └── serializers.py
│   ├── requirements.txt
│   ├── database.sql
│   ├── .env.example
│   ├── manage.py
│   └── README.md
│
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Node.js (v14 or higher)
- Python (v3.8 or higher)
- MySQL Server (v5.7 or higher)

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd elitecart-backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup MySQL Database**
   - Open MySQL and create database:
     ```bash 
     mysql -u root -p < database.sql
     ```
   - Or manually import `database.sql` file using MySQL Workbench/phpMyAdmin

5. **Configure environment**
   - Copy `.env.example` to `.env`
   - Update `.env` with your MySQL credentials:
     ```
     DB_HOST=localhost
     DB_USER=root
     DB_PASSWORD=your_password
     DB_NAME=elitecart
     DB_PORT=3306
     SECRET_KEY=your-secret-key-change-in-production
     DEBUG=True
     ```

6. **Run migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run backend server**
   ```bash
   python manage.py runserver
   ```
   Server will run on `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd elitecart-frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Create .env file** (optional)
   ```
   REACT_APP_API_URL=http://localhost:8000/api
   ```

4. **Start development server**
   ```bash
   npm start
   ```
   App will open at `http://localhost:3000`

## 📚 API Endpoints

### Authentication
- `POST /api/auth/signup` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/token/` - Get JWT token
- `POST /api/auth/token/refresh/` - Refresh JWT token

### Products
- `GET /api/products` - Get all products with filters
- `GET /api/products/{id}` - Get single product
- `POST /api/products` - Create product (requires auth)
- `PUT /api/products/{id}` - Update product (requires auth)
- `DELETE /api/products/{id}` - Delete product (requires auth)

### Orders
- `POST /api/orders` - Create order (requires auth)
- `GET /api/orders/user/{user_id}` - Get user's orders (requires auth)
- `GET /api/orders/{order_id}` - Get order details (requires auth)

### Health
- `GET /api/health` - Check API status

## 📝 Database Schema

### Users Table
```sql
CREATE TABLE users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Products Table
```sql
CREATE TABLE products (
  product_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  image_url TEXT NOT NULL,
  stock INT NOT NULL DEFAULT 0,
  category VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Orders Table
```sql
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  total_amount DECIMAL(12, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

### OrderItems Table
```sql
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT PRIMARY KEY,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

## 🔐 Authentication

The application uses JWT (JSON Web Tokens) for authentication:

1. User signs up or logs in
2. Backend generates JWT token
3. Token stored in localStorage
4. Token sent with API requests in Authorization header
5. Backend validates token and processes request

## 🎨 Customization

### Change Theme Colors
Edit `elitecart-frontend/tailwind.config.js`:
```javascript
colors: {
  primary: '#1e40af',  // Change primary color
  secondary: '#ea580c',  // Change secondary color
}
```

### Add More Products
- Use Admin panel in browser
- Or add directly via API using Postman/cURL
- Or insert via MySQL directly

## 🐛 Troubleshooting

### Backend Issues
- **Port 8000 already in use**: Run on different port with `python manage.py runserver 8001`
- **Database connection error**: Check `.env` file MySQL credentials
- **JWT errors**: Ensure `SECRET_KEY` is set in `.env`
- **Migrations error**: Run `python manage.py makemigrations` then `python manage.py migrate`

### Frontend Issues
- **API not responding**: Ensure backend is running on port 8000
- **CORS errors**: Check Django CORS configuration in `config/settings.py`
- **Dark mode not working**: Clear browser localStorage and refresh

## 📱 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## 🚀 Deployment

### Frontend (Vercel)
```bash
npm run build
# Deploy the 'build' folder to Vercel
```

### Backend (Heroku/PythonAnywhere)
1. Create `Procfile` with `web: gunicorn config.wsgi`
2. Update database credentials for production
3. Deploy using git or platform's dashboard

## 📄 License

This project is open source and available under the MIT License.

## 👥 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📞 Support

For issues, questions, or suggestions, please create an issue in the repository.

---

**Built by Lokesh Reddy Kambham**
