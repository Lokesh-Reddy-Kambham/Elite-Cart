import React from 'react';
import { ChevronDown, X } from 'lucide-react';

const Filter = ({ onFilterChange, isOpen, onClose }) => {
  const [category, setCategory] = React.useState('');
  const [minPrice, setMinPrice] = React.useState('');
  const [maxPrice, setMaxPrice] = React.useState('');
  const [inStock, setInStock] = React.useState(false);

  const handleFilterChange = () => {
    onFilterChange({
      category: category || undefined,
      min_price: minPrice ? parseFloat(minPrice) : undefined,
      max_price: maxPrice ? parseFloat(maxPrice) : undefined,
      in_stock: inStock || undefined,
    });
  };

  React.useEffect(() => {
    handleFilterChange();
  }, [category, minPrice, maxPrice, inStock]);

  const categories = ['Men', 'Women', 'Unisex'];

  return (
    <>
      {/* Mobile Filter Overlay */}
      {isOpen && (
        <div className="fixed inset-0 bg-black bg-opacity-50 z-40 md:hidden" onClick={onClose} />
      )}

      {/* Filter Panel */}
      <div
        className={`fixed md:relative md:w-64 w-full h-screen md:h-auto bg-white dark:bg-gray-800 transform md:transform-none transition-transform z-50 ${
          isOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'
        }`}
      >
        <div className="p-6 h-full overflow-y-auto">
          {/* Close Button (Mobile) */}
          <div className="flex justify-between items-center md:hidden mb-6">
            <h2 className="text-xl font-bold text-gray-900 dark:text-white">Filters</h2>
            <button onClick={onClose} className="text-gray-500 hover:text-gray-700">
              <X className="h-6 w-6" />
            </button>
          </div>

          {/* Category Filter */}
          <div className="mb-6">
            <h3 className="font-semibold text-gray-900 dark:text-white mb-3 flex items-center space-x-2">
              <span>Category</span>
              <ChevronDown className="h-4 w-4" />
            </h3>
            <div className="space-y-2">
                <label className="flex items-center space-x-2 cursor-pointer">
                  <input
                    id="cat-all"
                    type="radio"
                    name="category"
                    value=""
                    checked={category === ''}
                    onChange={(e) => setCategory(e.target.value)}
                    className="w-4 h-4"
                  />
                  <span className="text-gray-700 dark:text-gray-300">All</span>
                </label>
                {categories.map((cat) => (
                  <label key={cat} htmlFor={`cat-${cat}`} className="flex items-center space-x-2 cursor-pointer">
                    <input
                      id={`cat-${cat}`}
                      type="radio"
                      name="category"
                      value={cat}
                      checked={category === cat}
                      onChange={(e) => setCategory(e.target.value)}
                      className="w-4 h-4"
                    />
                    <span className="text-gray-700 dark:text-gray-300">{cat}</span>
                  </label>
                ))}
            </div>
          </div>

          {/* Price Filter */}
          <div className="mb-6">
            <h3 className="font-semibold text-gray-900 dark:text-white mb-3 flex items-center space-x-2">
              <span>Price</span>
              <ChevronDown className="h-4 w-4" />
            </h3>
            <div className="space-y-3">
              <div>
                <label htmlFor="minPrice" className="text-sm text-gray-600 dark:text-gray-400">Min Price</label>
                <input
                  id="minPrice"
                  name="minPrice"
                  type="number"
                  value={minPrice}
                  onChange={(e) => setMinPrice(e.target.value)}
                  placeholder="$0"
                  className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                />
              </div>
              <div>
                <label htmlFor="maxPrice" className="text-sm text-gray-600 dark:text-gray-400">Max Price</label>
                <input
                  id="maxPrice"
                  name="maxPrice"
                  type="number"
                  value={maxPrice}
                  onChange={(e) => setMaxPrice(e.target.value)}
                  placeholder="$500"
                  className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                />
              </div>
            </div>
          </div>

          {/* Stock Filter */}
          <div className="mb-6">
            <h3 className="font-semibold text-gray-900 dark:text-white mb-3">Availability</h3>
            <label htmlFor="inStock" className="flex items-center space-x-2 cursor-pointer">
              <input
                id="inStock"
                name="inStock"
                type="checkbox"
                checked={inStock}
                onChange={(e) => setInStock(e.target.checked)}
                className="w-4 h-4"
              />
              <span className="text-gray-700 dark:text-gray-300">In Stock Only</span>
            </label>
          </div>
        </div>
      </div>
    </>
  );
};

export default Filter;
