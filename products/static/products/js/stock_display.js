
function updateStockDisplay() {
    const selectedSize = document.getElementById('id_product_size').value;
    const stockList = document.querySelectorAll('#stock-list li');
    const stockDisplay = document.getElementById('stock-display');
    const addToBagButton = document.querySelector('input[type="submit"]');

    let stockAmount = 0;
    stockList.forEach(item => {
        const size = item.getAttribute('data-size');
        const stock = item.getAttribute('data-stock');

        if (size === selectedSize) {
            stockAmount = parseInt(stock, 10);
            if (stockAmount > 0) {
                stockDisplay.innerHTML = `<span class="text-success">In Stock: ${stockAmount}</span>`;
                addToBagButton.disabled = false;  // Enable the button
                addToBagButton.classList.remove("btn-not-allowed");
                addToBagButton.classList.add("btn-cordovan");  // Change button color to cordovan
            } else {
                stockDisplay.innerHTML = `<span class="text-danger">Out of Stock</span>`;
                addToBagButton.disabled = true;   // Disable the button
                addToBagButton.classList.remove("btn-cordovan");
                addToBagButton.classList.add("btn-not-allowed");  // Revert button color to disabled state
            }
        }
    });
}
