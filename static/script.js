// Handle order form
const orderForm = document.getElementById("orderForm");

if (orderForm) {

    orderForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const product = document.getElementById("orderProduct").value;
        const qty = document.getElementById("orderQty").value;

        // Create new table row
        const table = document.getElementById("ordersTable");
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${Date.now()}</td>
            <td>${product}</td>
            <td>${qty}</td>
        `;

        table.appendChild(row);

        orderForm.reset();
    });
}