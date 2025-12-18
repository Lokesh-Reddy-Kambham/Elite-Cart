import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { ordersAPI } from '../utils/api';

const ProfilePage = () => {
  const navigate = useNavigate();
  const { user, isAuthenticated, logout } = useAuth();
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!isAuthenticated) {
      navigate('/login');
      return;
    }

    const fetchOrders = async () => {
      try {
        const response = await ordersAPI.getByUser(user.user_id);
        setOrders(response.data.orders || []);
      } catch (error) {
          console.error('Failed to fetch orders:', error);
          const status = error.response?.status;
          // If token is invalid/expired or unauthorized, log out and redirect to login
          if (status === 401 || status === 403 || status === 422) {
            // clear auth and redirect
            try {
              // use logout from context if available
              if (typeof logout === 'function') logout();
            } catch (e) {
              // ignore
            }
            navigate('/login');
          }
        } finally {
          setLoading(false);
        }
    };

    fetchOrders();
  }, [isAuthenticated, user, navigate]);

  if (!isAuthenticated) {
    return null;
  }

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white mb-8">My Profile</h1>

        {/* User Info */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 mb-8">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
            Account Information
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <p className="text-gray-600 dark:text-gray-400 text-sm">Full Name</p>
              <p className="text-gray-900 dark:text-white text-lg font-semibold">{user.name}</p>
            </div>
            <div>
              <p className="text-gray-600 dark:text-gray-400 text-sm">Email</p>
              <p className="text-gray-900 dark:text-white text-lg font-semibold">{user.email}</p>
            </div>
            <div>
              <p className="text-gray-600 dark:text-gray-400 text-sm">User ID</p>
              <p className="text-gray-900 dark:text-white text-lg font-semibold">{user.user_id}</p>
            </div>
          </div>
        </div>

        {/* Orders */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
            Order History
          </h2>

          {loading ? (
            <div className="space-y-4">
              {[...Array(3)].map((_, i) => (
                <div key={i} className="bg-gray-200 dark:bg-gray-700 h-24 rounded-lg animate-pulse"></div>
              ))}
            </div>
          ) : orders.length > 0 ? (
            <div className="space-y-4">
              {orders.map((order) => (
                <div
                  key={order.order_id}
                  className="border border-gray-200 dark:border-gray-700 rounded-lg p-4 hover:shadow-md transition-shadow"
                >
                  <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                    <div>
                      <p className="text-gray-600 dark:text-gray-400 text-sm">Order ID</p>
                      <p className="text-gray-900 dark:text-white font-semibold">#{order.order_id}</p>
                    </div>
                    <div>
                      <p className="text-gray-600 dark:text-gray-400 text-sm">Date</p>
                      <p className="text-gray-900 dark:text-white font-semibold">
                        {new Date(order.created_at).toLocaleDateString()}
                      </p>
                    </div>
                    <div>
                      <p className="text-gray-600 dark:text-gray-400 text-sm">Items</p>
                      <p className="text-gray-900 dark:text-white font-semibold">
                        {order.items?.length || 0} items
                      </p>
                    </div>
                    <div>
                      <p className="text-gray-600 dark:text-gray-400 text-sm">Total</p>
                      <p className="text-gray-900 dark:text-white font-semibold text-lg">
                        ${(Number(order.total_amount) || 0).toFixed(2)}
                      </p>
                    </div>
                  </div>

                  {/* Order Items */}
                  {order.items && order.items.length > 0 && (
                    <div className="mt-4 pt-4 border-t border-gray-200 dark:border-gray-700">
                      <div className="space-y-2 text-sm">
                        {order.items.map((item) => (
                          <div key={item.order_item_id} className="flex justify-between text-gray-700 dark:text-gray-300">
                            <span>
                              Product ID {item.product_id} × {item.quantity}
                            </span>
                            <span>${(((Number(item.price) || 0) * (Number(item.quantity) || 0))).toFixed(2)}</span>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              ))}
            </div>
          ) : (
            <div className="text-center py-8">
              <p className="text-gray-600 dark:text-gray-400 mb-4">No orders yet</p>
              <button
                onClick={() => navigate('/products')}
                className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-lg font-semibold"
              >
                Start Shopping
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ProfilePage;
