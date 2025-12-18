# EliteCart Backend Setup Guide

## Prerequisites
- Python 3.8 or higher
- MySQL Server 5.7 or higher
- pip (Python package manager)

## Installation Steps

### 1. Virtual Environment Setup

**On Windows (PowerShell):**
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate
```

**On macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. MySQL Database Setup

**Option A: Using MySQL Command Line**
```bash
mysql -u root -p < database.sql
```
(You'll be prompted for your MySQL password)

**Option B: Using MySQL Workbench/GUI**
1. Open MySQL Workbench
2. Create a new database named `elitecart`
3. Open and execute the `database.sql` file
4. Click Execute

### 4. Environment Configuration

1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

2. Edit `.env` file with your database credentials:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password_here
DB_NAME=elitecart
DB_PORT=3306
JWT_SECRET_KEY=your-secret-key-change-in-production
FLASK_ENV=development
```

**Note:** Replace `your_password_here` with your actual MySQL password

### 5. Run Backend Server

```bash
python app/main.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

✅ Backend is now running on `http://localhost:5000`

## API Endpoints Reference

### Health Check
- `GET http://localhost:5000/api/health`

### Authentication
- `POST http://localhost:5000/api/auth/signup`
- `POST http://localhost:5000/api/auth/login`

### Products
- `GET http://localhost:5000/api/products`
- `GET http://localhost:5000/api/products/{id}`
- `POST http://localhost:5000/api/products` (requires auth)
- `PUT http://localhost:5000/api/products/{id}` (requires auth)
- `DELETE http://localhost:5000/api/products/{id}` (requires auth)

### Orders
- `POST http://localhost:5000/api/orders` (requires auth)
- `GET http://localhost:5000/api/orders/user/{user_id}` (requires auth)
- `GET http://localhost:5000/api/orders/{order_id}` (requires auth)

## Testing with cURL/Postman

### Test Health Endpoint
```bash
curl http://localhost:5000/api/health
```

### Test Signup
```bash
curl -X POST http://localhost:5000/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@example.com","password":"password123"}'
```

### Test Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"john@example.com","password":"password123"}'
```

## Troubleshooting

### Issue: "Module not found" error
**Solution:** Ensure virtual environment is activated and dependencies are installed
```bash
pip install -r requirements.txt
```

### Issue: Database connection error
**Solution:** Check `.env` file credentials and MySQL is running
```bash
# Test MySQL connection
mysql -u root -p
```

### Issue: Port 5000 already in use
**Solution:** Edit `app/main.py` and change `port=5000` to another port like `5001`

### Issue: JWT errors
**Solution:** Ensure `JWT_SECRET_KEY` is set in `.env` file

## Sample Data

The database is pre-populated with:
- 1 admin user
- 8 sample products

### Admin Login Credentials
- Email: `admin@example.com`
- Password: (See database.sql for hash)

## Database Schema Details

### Users
- `user_id` - Primary Key (Auto-increment)
- `name` - VARCHAR(255)
- `email` - VARCHAR(255) UNIQUE
- `password_hash` - VARCHAR(255)
- `created_at` - TIMESTAMP

### Products
- `product_id` - Primary Key (Auto-increment)
- `name` - VARCHAR(255)
- `description` - TEXT
- `price` - DECIMAL(10, 2)
- `image_url` - TEXT
- `stock` - INT
- `category` - VARCHAR(100)
- `created_at` - TIMESTAMP

### Orders
- `order_id` - Primary Key (Auto-increment)
- `user_id` - Foreign Key (users.user_id)
- `total_amount` - DECIMAL(12, 2)
- `created_at` - TIMESTAMP

### OrderItems
- `order_item_id` - Primary Key (Auto-increment)
- `order_id` - Foreign Key (orders.order_id)
- `product_id` - Foreign Key (products.product_id)
- `quantity` - INT
- `price` - DECIMAL(10, 2)

## Production Deployment

### Before Deploying:
1. Change `JWT_SECRET_KEY` to a strong random key
2. Set `FLASK_ENV=production`
3. Use a production WSGI server (gunicorn)
4. Enable HTTPS
5. Use environment variables for sensitive data

### Deploy to Heroku:
```bash
# Install Heroku CLI and login
heroku login

# Create Procfile
echo "web: gunicorn app.main:app" > Procfile

# Deploy
git push heroku main
```

## Support

For issues or questions, please check the main README.md or create an issue.
