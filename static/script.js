// Handle product form submission
document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("productForm");

    // Check if form exists on page
    if (form) {

        form.addEventListener("submit", function (e) {
            e.preventDefault();

            // Get input values
            const name = document.getElementById("productName").value;
            const qty = document.getElementById("quantity").value;

            // Simple console log (can connect to backend later)
            console.log("Product Added:", name, qty);

            // Reset form after submission
            form.reset();
        });
    }

});