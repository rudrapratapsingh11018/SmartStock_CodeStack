# Main Flask app to connect frontend and backend

from flask import Flask, render_template, request, redirect
from database import init_db
from order_logic import create_order
from movement import add_product

app = Flask(__name__)

# Initialize database
init_db()

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Admin page
@app.route('/admin')
def admin():
    return render_template('admin.html')

# Orders page
@app.route('/orders')
def orders():
    return render_template('orders.html')

# Add product
@app.route('/add_product', methods=['POST'])
def add_product_route():
    name = request.form['name']
    quantity = request.form['quantity']
    add_product(name, quantity)
    return redirect('/admin')

# Create order
@app.route('/create_order', methods=['POST'])
def create_order_route():
    product = request.form['product']
    quantity = request.form['quantity']
    create_order(product, quantity)
    return redirect('/orders')

if __name__ == '__main__':
    app.run(debug=True)