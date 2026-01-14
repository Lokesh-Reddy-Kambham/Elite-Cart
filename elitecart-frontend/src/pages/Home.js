import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { ShoppingBag, TrendingUp, Zap, Award } from 'lucide-react';
import { productsAPI } from '../utils/api';

const Home = () => {
  const navigate = useNavigate();
  const [featured, setFeatured] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchFeatured = async () => {
      try {
        const response = await productsAPI.getAll({ limit: 6 });
        setFeatured(response.data.products.slice(0, 6));
      } catch (error) {
        console.error('Failed to fetch products:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchFeatured();
  }, []);

  return (
    <div className="min-h-screen bg-white dark:bg-gray-900">
      {/* Hero Section */}
      <section className="relative h-96 md:h-[500px] bg-gradient-to-r from-blue-600 to-blue-800 dark:from-blue-800 dark:to-blue-950 flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0 opacity-20">
          <div className="absolute top-0 right-0 w-96 h-96 bg-white rounded-full blur-3xl"></div>
          <div className="absolute bottom-0 left-0 w-96 h-96 bg-blue-400 rounded-full blur-3xl"></div>
        </div>
        
        <div className="relative z-10 text-center text-white px-4">
          <h1 className="text-4xl md:text-6xl font-bold mb-4">Welcome to EliteCart</h1>
          <p className="text-lg md:text-2xl mb-8 text-blue-100">Discover Premium Fashion & Lifestyle Products</p>
          <button
            onClick={() => navigate('/products')}
            className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-blue-50 transition-colors"
          >
            Shop Now
          </button>
        </div>
      </section>

      {/* Features Section */}
      <section className="max-w-7xl mx-auto px-4 py-16">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md text-center">
            <ShoppingBag className="h-12 w-12 mx-auto mb-4 text-blue-600" />
            <h3 className="font-semibold text-gray-900 dark:text-white mb-2">Easy Shopping</h3>
            <p className="text-gray-600 dark:text-gray-400 text-sm">Browse our collection with ease</p>
          </div>
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md text-center">
            <TrendingUp className="h-12 w-12 mx-auto mb-4 text-orange-600" />
            <h3 className="font-semibold text-gray-900 dark:text-white mb-2">Trending Items</h3>
            <p className="text-gray-600 dark:text-gray-400 text-sm">Latest fashion trends available</p>
          </div>
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md text-center">
            <Zap className="h-12 w-12 mx-auto mb-4 text-yellow-600" />
            <h3 className="font-semibold text-gray-900 dark:text-white mb-2">Fast Delivery</h3>
            <p className="text-gray-600 dark:text-gray-400 text-sm">Quick and reliable shipping</p>
          </div>
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md text-center">
            <Award className="h-12 w-12 mx-auto mb-4 text-green-600" />
            <h3 className="font-semibold text-gray-900 dark:text-white mb-2">Quality Assured</h3>
            <p className="text-gray-600 dark:text-gray-400 text-sm">Premium products guaranteed</p>
          </div>
        </div>
      </section>

      {/* Featured Products */}
      <section className="max-w-7xl mx-auto px-4 py-16">
        <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-8">Featured Products</h2>
        {loading ? (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {[...Array(6)].map((_, i) => (
              <div key={i} className="bg-gray-200 dark:bg-gray-700 h-96 rounded-lg animate-pulse"></div>
            ))}
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {featured.map((product) => (
              <div
                key={product.product_id}
                onClick={() => navigate(`/products?id=${product.product_id}`)}
                className="bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-lg transition-shadow cursor-pointer overflow-hidden"
              >
                <div className="w-full h-48 bg-gray-200 dark:bg-gray-700">
                  <img
                    src={product.image_url || "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='200'><rect fill='%23e5e7eb' width='100%25' height='100%25'/><text x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' fill='%236b7280' font-size='20'>No Image</text></svg>"}
                    alt={product.name}
                    className="w-full h-full object-cover hover:scale-110 transition-transform"
                    onError={(e) => { try { e.target.onerror = null; e.target.src = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='200'><rect fill='%23e5e7eb' width='100%25' height='100%25'/><text x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' fill='%236b7280' font-size='20'>No Image</text></svg>"; } catch(err) {} }}
                  />
                </div>
                <div className="p-4">
                  <h3 className="font-semibold text-gray-900 dark:text-white mb-2">{product.name}</h3>
                  <p className="text-2xl font-bold text-blue-600 dark:text-blue-400 mb-2">
                    ₹{ (Number(product.price) || 0).toFixed(2) }
                  </p>
                  <p className="text-sm text-gray-600 dark:text-gray-400">
                    {product.stock} in stock
                  </p>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>

      {/* CTA Section */}
      <section className="bg-blue-600 dark:bg-blue-800 text-white py-16 my-16">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold mb-4">Ready to Shop?</h2>
          <p className="text-lg mb-8">Explore our complete collection of premium products</p>
          <button
            onClick={() => navigate('/products')}
            className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-blue-50 transition-colors"
          >
            Browse All Products
          </button>
        </div>
      </section>
    </div>
  );
};

export default Home;
