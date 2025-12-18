-- Create Database
CREATE DATABASE IF NOT EXISTS elitecart;
USE elitecart;

-- Create Users Table
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create Products Table
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    image_url TEXT NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    category VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create Orders Table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total_amount DECIMAL(12, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create OrderItems Table
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create Indexes
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_product_category ON products(category);
CREATE INDEX idx_order_user ON orders(user_id);
CREATE INDEX idx_order_item_order ON order_items(order_id);
CREATE INDEX idx_order_item_product ON order_items(product_id);

-- Sample Data
INSERT INTO users (name, email, password_hash) VALUES 
('Admin User', 'admin@example.com', 'scrypt$n=16384,r=8,p=1$2mHUqk5e+nLXwlGM1TGaVg$tD7/HdqKGWfaJ2cKvPhSlQhHLCBhh0BkNfaYfLTnf3I');

INSERT INTO products (name, description, price, image_url, stock, category) VALUES 
('Premium Sneaker', 'High quality running sneaker with excellent comfort', 99.99, '/images/sneaker.jpg', 50, 'Men'),
('Casual T-Shirt', 'Comfortable cotton t-shirt for everyday wear', 29.99, '/images/tshirt.jpg', 100, 'Men'),
('Elegant Dress', 'Beautiful evening dress perfect for special occasions', 149.99, '/images/dress.jpg', 30, 'Women'),
('Running Shorts', 'Breathable shorts designed for active sportspeople', 49.99, '/images/shorts.jpg', 75, 'Men'),
('Sports Bra', 'High support sports bra for intense workouts', 69.99, '/images/sportsbra.jpg', 40, 'Women'),
('Jeans', 'Classic blue jeans with perfect fit', 79.99, '/images/jeans.jpg', 60, 'Unisex'),
('Leather Jacket', 'Premium leather jacket for a sophisticated look', 199.99, '/images/jacket.jpg', 25, 'Men'),
('Yoga Pants', 'Comfortable yoga pants with high waistband', 59.99, '/images/yogapants.jpg', 45, 'Women');
