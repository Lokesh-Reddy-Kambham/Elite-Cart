import React, { useState, useEffect } from 'react';
import { Filter as FilterIcon } from 'lucide-react';
import ProductCard from '../components/ProductCard';
import Filter from '../components/Filter';
import { productsAPI } from '../utils/api';

const ProductList = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filterOpen, setFilterOpen] = useState(false);
  const [filters, setFilters] = useState({});
  const [successMessage, setSuccessMessage] = useState('');

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        setLoading(true);
        const response = await productsAPI.getAll(filters);
        setProducts(response.data.products || []);
      } catch (error) {
        console.error('Failed to fetch products:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, [filters]);

  const handleFilterChange = (newFilters) => {
    setFilters(newFilters);
  };

  const handleAddToCart = () => {
    setSuccessMessage('Product added to cart!');
    setTimeout(() => setSuccessMessage(''), 3000);
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 py-8">
        {/* Success Message */}
        {successMessage && (
          <div className="mb-4 p-4 bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-100 rounded-lg">
            {successMessage}
          </div>
        )}

        {/* Header */}
        <div className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-3xl font-bold text-gray-900 dark:text-white">Products</h1>
            <p className="text-gray-600 dark:text-gray-400">
              {products.length} products found
            </p>
          </div>
          <button
            onClick={() => setFilterOpen(!filterOpen)}
            className="md:hidden flex items-center space-x-2 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
          >
            <FilterIcon className="h-5 w-5" />
            <span>Filter</span>
          </button>
        </div>

        {/* Main Content */}
        <div className="flex gap-6">
          {/* Filter — single instance used for desktop sidebar and mobile overlay */}
          <div className="w-64">
            <Filter onFilterChange={handleFilterChange} isOpen={filterOpen} onClose={() => setFilterOpen(false)} />
          </div>

          {/* Products Grid */}
          <div className="flex-1">
            {loading ? (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {[...Array(6)].map((_, i) => (
                  <div key={i} className="bg-gray-200 dark:bg-gray-700 h-96 rounded-lg animate-pulse"></div>
                ))}
              </div>
            ) : products.length > 0 ? (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {products.map((product) => (
                  <ProductCard
                    key={product.product_id}
                    product={product}
                    onAddToCart={handleAddToCart}
                  />
                ))}
              </div>
            ) : (
              <div className="text-center py-16">
                <p className="text-2xl font-semibold text-gray-600 dark:text-gray-400">
                  No products found
                </p>
                <p className="text-gray-500 dark:text-gray-400 mt-2">
                  Try adjusting your filters
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductList;
