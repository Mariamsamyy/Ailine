let cartItems = [];

function addToCart(flightId, price) {
    const existingItem = cartItems.find(item => item.id === flightId);

    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cartItems.push({ id: flightId, price: price, quantity: 1 });
    }

    updateCartDisplay();
}

function removeFromCart(flightId) {
    cartItems = cartItems.filter(item => item.id !== flightId);
    updateCartDisplay();
}

function updateCartDisplay() {
    const cartItemDiv = document.getElementById("cartItem");
    const totalDiv = document.getElementById("total");

    if (cartItems.length === 0) {
        cartItemDiv.innerHTML = "Your cart is empty";
        totalDiv.textContent = "Total: EGP 0.00";
    } else {
        let cartHTML = "";
        let total = 0;

        cartItems.forEach(item => {
            cartHTML += `<div>${item.id} - ${item.price} EGP <button onclick="removeFromCart('${item.id}')">Remove</button></div>`;
            total += item.price * item.quantity;
        });

        cartItemDiv.innerHTML = cartHTML;
        totalDiv.textContent = `Total: EGP ${total.toFixed(2)}`;
    }
}

function initializeCart() {
    updateCartDisplay();
}

window.onload = initializeCart;