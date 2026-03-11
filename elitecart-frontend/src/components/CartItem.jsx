import React from 'react';
import { Trash2, Plus, Minus } from 'lucide-react';
import { useCart } from '../context/CartContext';

const CartItem = ({ item }) => {
  const { updateQuantity, removeFromCart } = useCart();

  return (
    <div className="flex gap-4 py-4 border-b border-gray-200 dark:border-gray-700">
      <img
        src={item.image_url || "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'><rect fill='%23e5e7eb' width='100%25' height='100%25'/><text x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' fill='%236b7280' font-size='12'>No Image</text></svg>"}
        alt={item.name}
        className="w-24 h-24 object-cover rounded-lg"
        onError={(e) => { try { e.target.onerror = null; e.target.src = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'><rect fill='%23e5e7eb' width='100%25' height='100%25'/><text x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' fill='%236b7280' font-size='12'>No Image</text></svg>"; } catch(err) {} }}
      />
      <div className="flex-1">
        <h3 className="font-semibold text-gray-900 dark:text-white">{item.name}</h3>
        <p className="text-gray-600 dark:text-gray-400 text-sm">${(Number(item.price) || 0).toFixed(2)}</p>
        <p className="text-gray-500 dark:text-gray-400 text-sm">{item.category}</p>
      </div>
      <div className="flex flex-col items-end justify-between">
        <div className="flex items-center space-x-2">
          <button
            onClick={() => updateQuantity(item.product_id, item.quantity - 1)}
            className="p-1 hover:bg-gray-200 dark:hover:bg-gray-700 rounded"
          >
            <Minus className="h-4 w-4" />
          </button>
          <span className="w-8 text-center font-semibold">{item.quantity}</span>
          <button
            onClick={() => updateQuantity(item.product_id, item.quantity + 1)}
            className="p-1 hover:bg-gray-200 dark:hover:bg-gray-700 rounded"
          >
            <Plus className="h-4 w-4" />
          </button>
        </div>
        <button
          onClick={() => removeFromCart(item.product_id)}
          className="text-red-500 hover:text-red-700 p-1"
        >
          <Trash2 className="h-5 w-5" />
        </button>
        <p className="font-bold text-gray-900 dark:text-white mt-2">
          ${(((Number(item.price) || 0) * (Number(item.quantity) || 0))).toFixed(2)}
        </p>
      </div>
    </div>
  );
};

export default CartItem;
