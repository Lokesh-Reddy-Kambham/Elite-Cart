import React from 'react';
import { Star, ShoppingCart } from 'lucide-react';
import { useCart } from '../context/CartContext';

const ProductCard = ({ product, onAddToCart }) => {
  const { addToCart } = useCart();
  const [quantity, setQuantity] = React.useState(1);

  const handleAddToCart = () => {
    addToCart(product, quantity);
    setQuantity(1);
    if (onAddToCart) {
      onAddToCart();
    }
  };

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-lg transition-shadow overflow-hidden">
      {/* Image */}
      <div className="relative w-full h-48 bg-gray-200 dark:bg-gray-700 overflow-hidden">
        <img
          src={product.image_url || "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='200'><rect fill='%23e5e7eb' width='100%25' height='100%25'/><text x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' fill='%236b7280' font-size='20'>No Image</text></svg>"}
          alt={product.name}
          className="w-full h-full object-cover hover:scale-110 transition-transform"
          onError={(e) => { try { e.target.onerror = null; e.target.src = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='200'><rect fill='%23e5e7eb' width='100%25' height='100%25'/><text x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' fill='%236b7280' font-size='20'>No Image</text></svg>"; } catch(err) {} }}
        />
        {product.stock === 0 && (
          <div className="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center">
            <span className="text-white font-bold text-lg">Out of Stock</span>
          </div>
        )}
      </div>

      {/* Content */}
      <div className="p-4">
        <div className="flex justify-between items-start mb-2">
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white line-clamp-2">
            {product.name}
          </h3>
          <span className="text-xs bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-100 px-2 py-1 rounded">
            {product.category}
          </span>
        </div>

        <p className="text-gray-600 dark:text-gray-400 text-sm line-clamp-2 mb-3">
          {product.description}
        </p>

        {/* Rating */}
        <div className="flex items-center space-x-1 mb-3">
          {[...Array(5)].map((_, i) => (
            <Star key={i} className="h-4 w-4 fill-yellow-400 text-yellow-400" />
          ))}
          <span className="text-sm text-gray-600 dark:text-gray-400">(32)</span>
        </div>

        {/* Price and Stock */}
        <div className="flex justify-between items-center mb-4">
          <div>
            <p className="text-2xl font-bold text-gray-900 dark:text-white">
              ${ (Number(product.price) || 0).toFixed(2) }
            </p>
            <p className="text-xs text-gray-500 dark:text-gray-400">
              {product.stock} in stock
            </p>
          </div>
        </div>

        {/* Add to Cart Button */}
        {product.stock > 0 ? (
          <div className="flex items-center space-x-2">
            <select
              id={`quantity-${product.product_id}`}
              name="quantity"
              value={quantity}
              onChange={(e) => setQuantity(parseInt(e.target.value))}
              className="flex-1 px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white text-sm"
            >
              {[...Array(Math.min(product.stock, 10))].map((_, i) => (
                <option key={i + 1} value={i + 1}>
                  {i + 1}
                </option>
              ))}
            </select>
            <button
              onClick={handleAddToCart}
              className="flex-1 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg flex items-center justify-center space-x-2 transition-colors"
            >
              <ShoppingCart className="h-4 w-4" />
              <span>Add</span>
            </button>
          </div>
        ) : (
          <button disabled className="w-full bg-gray-300 dark:bg-gray-600 text-gray-500 dark:text-gray-400 px-4 py-2 rounded-lg">
            Out of Stock
          </button>
        )}
      </div>
    </div>
  );
};

export default ProductCard;
