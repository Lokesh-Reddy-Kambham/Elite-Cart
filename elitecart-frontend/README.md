# EliteCart Frontend Setup Guide

## Prerequisites
- Node.js 14+ (includes npm)
- Code editor (VS Code recommended)

## Installation Steps

### 1. Install Node.js

**Option A: Direct Download**
- Visit https://nodejs.org
- Download LTS version
- Follow installation wizard

**Option B: Using Package Manager**

**Windows (Chocolatey):**
```powershell
choco install nodejs
```

**macOS (Homebrew):**
```bash
brew install node
```

**Linux (apt):**
```bash
sudo apt-get install nodejs npm
```

### 2. Verify Installation
```bash
node --version
npm --version
```

### 3. Install Dependencies
Navigate to the frontend folder and install:
```bash
cd elitecart-frontend
npm install
```

This will install all required packages:
- react, react-dom
- react-router-dom (routing)
- axios (API calls)
- tailwindcss (styling)
- lucide-react (icons)

### 4. Environment Configuration

1. Create `.env` file in `elitecart-frontend` folder:
```bash
cp .env.example .env
```

2. Edit `.env` (optional - defaults to localhost:5000):
```
REACT_APP_API_URL=http://localhost:5000/api
```

**For Production:**
```
REACT_APP_API_URL=https://your-api-url.com/api
```

### 5. Start Development Server

```bash
npm start
```

The app will automatically open at `http://localhost:3000`

You should see:
```
Compiled successfully!

You can now view elitecart-frontend in the browser.
```

## Available Scripts

### Development
```bash
npm start
```
Runs the app in development mode with hot reload.

### Build for Production
```bash
npm run build
```
Creates optimized production build in `build/` folder.

### Run Tests
```bash
npm test
```
Launches test runner in interactive mode.

## Folder Structure

```
src/
├── components/          # Reusable components
│   ├── Navbar.js
│   ├── ProductCard.js
│   ├── Filter.js
│   ├── CartItem.js
│   └── Footer.js
├── pages/              # Page components
│   ├── Home.js
│   ├── ProductList.js
│   ├── CartPage.js
│   ├── CheckoutPage.js
│   ├── LoginPage.js
│   ├── SignupPage.js
│   ├── ProfilePage.js
│   └── AdminPage.js
├── context/            # Context API
│   ├── AuthContext.js
│   ├── CartContext.js
│   └── ThemeContext.js
├── utils/              # Utilities
│   └── api.js
├── assets/             # Images, fonts, etc
├── App.js
├── index.js
└── index.css
```

## Features Overview

### 🏠 Home Page
- Hero section
- Feature highlights
- Featured products showcase
- CTA button to shop

### 🛍️ Product Listing
- Grid layout
- Advanced filters (category, price, stock)
- Product cards with details
- Add to cart button
- Responsive design

### 🛒 Shopping Cart
- Persistent cart (localStorage)
- Update quantities
- Remove items
- Order summary
- Proceed to checkout

### 💳 Checkout
- Shipping information form
- Payment information form
- Order summary with items
- Order placement
- Success confirmation

### 👤 Authentication
- Sign up form with validation
- Login form
- JWT token management
- Protected routes

### 👥 User Profile
- Account information display
- Order history
- Order details with items
- Date formatting

### ⚙️ Admin Panel
- Product management (CRUD)
- Add/Edit/Delete products
- Product list table
- Form validation

### 🌙 Dark/Light Mode
- Toggle button in navbar
- Persistent theme preference
- Full dark mode support
- Smooth transitions

## Styling with Tailwind CSS

The project uses Tailwind CSS for styling.

### Customize Colors
Edit `tailwind.config.js`:
```javascript
theme: {
  extend: {
    colors: {
      primary: '#1e40af',      // Blue
      secondary: '#ea580c',    // Orange
    }
  },
}
```

### Common Utility Classes
```html
<!-- Spacing -->
<div className="p-4 m-2">Padding and Margin</div>

<!-- Colors -->
<div className="bg-blue-600 text-white">Background and Text</div>

<!-- Dark Mode -->
<div className="bg-white dark:bg-gray-800">Light/Dark</div>

<!-- Responsive -->
<div className="md:w-1/2 lg:w-1/3">Responsive Width</div>
```

## API Integration

The `src/utils/api.js` file handles all API calls:

```javascript
import { productsAPI, authAPI, ordersAPI } from './utils/api';

// Get products
const response = await productsAPI.getAll({ category: 'Men' });

// Create order
const response = await ordersAPI.create(orderData);
```

### Authentication Headers
JWT tokens are automatically added to requests via axios interceptor:
```javascript
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
```

## Context API Usage

### AuthContext
```javascript
import { useAuth } from './context/AuthContext';

const { user, isAuthenticated, login, logout } = useAuth();
```

### CartContext
```javascript
import { useCart } from './context/CartContext';

const { 
  cartItems, 
  addToCart, 
  removeFromCart, 
  getTotalPrice 
} = useCart();
```

### ThemeContext
```javascript
import { useTheme } from './context/ThemeContext';

const { isDark, toggleTheme } = useTheme();
```

## Routing Structure

```
/                  → Home
/products          → Product Listing
/cart              → Shopping Cart
/checkout          → Checkout Page
/login             → Login Page
/signup            → Sign Up Page
/profile           → User Profile (protected)
/admin             → Admin Panel (protected)
```

## Browser DevTools

### React Developer Tools
Install React DevTools extension for Chrome/Firefox to inspect components and state.

### Redux DevTools
While we use Context API, you can still use browser DevTools for network debugging.

## Common Issues

### Issue: "Cannot find module" errors
**Solution:**
```bash
rm -rf node_modules
npm install
```

### Issue: Port 3000 already in use
**Solution:** The app will prompt to use another port (usually 3001)

### Issue: API connection errors
**Solution:** Ensure backend is running on `http://localhost:5000` and update REACT_APP_API_URL in `.env`

### Issue: Dark mode not working
**Solution:** Clear localStorage:
```javascript
localStorage.clear();
// Then refresh the page
```

### Issue: Cart not persisting
**Solution:** Check browser's localStorage is enabled and browser settings

## Performance Optimization

### Code Splitting
Routes are automatically code-split by React Router.

### Image Optimization
Consider using Next.js Image component or CDN for production.

### Bundle Size
Run this to check bundle size:
```bash
npm run build
```

## Building for Production

```bash
npm run build
```

This creates an optimized production build in the `build/` folder.

### Deploy to Vercel (Recommended)
```bash
npm install -g vercel
vercel
```

### Deploy to Netlify
1. Connect your GitHub repository
2. Set build command: `npm run build`
3. Set publish directory: `build`

### Deploy to GitHub Pages
1. Add to `package.json`:
```json
"homepage": "https://username.github.io/Elite-Cart",
```

2. Build and deploy:
```bash
npm run build
npm install gh-pages --save-dev
npm run deploy
```

## Environment Variables Reference

```
# API Configuration
REACT_APP_API_URL=http://localhost:5000/api

# Optional: Analytics, etc
REACT_APP_ANALYTICS_ID=your_id
```

## Support

For issues or questions, check the main README.md or create an issue.
