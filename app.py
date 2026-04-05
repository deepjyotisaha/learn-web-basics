"""
app.py  —  Web Fundamentals Learning Lab
==========================================
Run:   python app.py
Open:  http://localhost:5000
"""

import os, json, time, datetime
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template, request, jsonify, Response

app = Flask(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# IN-MEMORY PRODUCT CATALOG  (used by Steps 8 & 9)
# ─────────────────────────────────────────────────────────────────────────────
PRODUCTS = [
    {"id": 1, "name": "Wireless Mouse",      "price": 599,  "category": "electronics", "stock": 34},
    {"id": 2, "name": "USB-C Hub",            "price": 1299, "category": "electronics", "stock": 12},
    {"id": 3, "name": "Notebook (200 pages)", "price": 120,  "category": "stationery",  "stock": 85},
    {"id": 4, "name": "Gel Pen Set (5 pack)", "price": 75,   "category": "stationery",  "stock": 200},
    {"id": 5, "name": "Laptop Stand",         "price": 1899, "category": "electronics", "stock": 8},
    {"id": 6, "name": "Desk Lamp (LED)",      "price": 749,  "category": "home",        "stock": 22},
]

CART = []          # simple in-memory cart
ORDER_COUNTER = 0  # auto-increment order id


# ─────────────────────────────────────────────────────────────────────────────
# PAGES
# ─────────────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


# ─────────────────────────────────────────────────────────────────────────────
# STEP 1  —  RESTAURANT MENU  (realistic GET example)
# ─────────────────────────────────────────────────────────────────────────────
MENU = [
    {"dish": "Paneer Tikka",       "price": 220, "type": "starter",  "veg": True},
    {"dish": "Masala Dosa",        "price": 120, "type": "main",     "veg": True},
    {"dish": "Chicken Biryani",    "price": 280, "type": "main",     "veg": False},
    {"dish": "Dal Makhani",        "price": 180, "type": "main",     "veg": True},
    {"dish": "Gulab Jamun",        "price": 90,  "type": "dessert",  "veg": True},
]

@app.route("/menu", methods=["GET"])
def get_menu():
    """Simulates a restaurant menu — the simplest realistic GET request."""
    dish_type = request.args.get("type")
    items = [d for d in MENU if not dish_type or d["type"] == dish_type]
    return jsonify({
        "restaurant": "The Curry House",
        "menu": items,
        "count": len(items),
    })

@app.route("/order", methods=["POST"])
def place_order():
    """Simulates placing an order — a realistic POST request."""
    data = request.get_json(force=True)
    dish = data.get("dish", "Unknown")
    qty = data.get("qty", 1)
    item = next((d for d in MENU if d["dish"].lower() == dish.lower()), None)
    if not item:
        return jsonify({"error": f"'{dish}' is not on the menu"}), 404
    return jsonify({
        "status": "confirmed",
        "order": {"dish": item["dish"], "qty": qty,
                  "total": item["price"] * qty},
        "message": f"Your {qty}x {item['dish']} will be ready in 15 minutes!"
    }), 201

@app.route("/order/<int:oid>", methods=["PUT"])
def update_order(oid):
    """Simulates updating an order — a realistic PUT request."""
    data = request.get_json(force=True)
    dish = data.get("dish", "Paneer Tikka")
    qty = data.get("qty", 1)
    item = next((d for d in MENU if d["dish"].lower() == dish.lower()), None)
    price = item["price"] if item else 220
    return jsonify({
        "status": "updated",
        "order_id": oid,
        "order": {"dish": dish, "qty": qty, "total": price * qty},
        "message": f"Order #{oid} updated to {qty}x {dish}."
    })

@app.route("/order/<int:oid>", methods=["DELETE"])
def cancel_order(oid):
    """Simulates cancelling an order — a realistic DELETE request."""
    return jsonify({
        "status": "cancelled",
        "order_id": oid,
        "message": f"Order #{oid} has been cancelled. No charge."
    })


# ─────────────────────────────────────────────────────────────────────────────
# STEP 1 & 2  —  HTTP ECHO  (shows raw request details)
# ─────────────────────────────────────────────────────────────────────────────
@app.route("/api/echo", methods=["GET", "POST", "PUT", "DELETE"])
def echo():
    """Returns a JSON mirror of whatever HTTP request was received."""
    body = None
    if request.data:
        try:
            body = json.loads(request.data)
        except Exception:
            body = request.data.decode("utf-8", errors="replace")

    return jsonify({
        "request": {
            "method":  request.method,
            "path":    request.path,
            "query":   dict(request.args),
            "headers": {
                "Host":         request.headers.get("Host"),
                "Content-Type": request.headers.get("Content-Type"),
                "User-Agent":   request.headers.get("User-Agent", "")[:80],
            },
            "body": body,
        },
        "response": {
            "status":    200,
            "message":   f"{request.method} request received successfully!",
            "timestamp": datetime.datetime.now().isoformat(),
        }
    })


# ─────────────────────────────────────────────────────────────────────────────
# STEP 8  —  REST API  (Product catalog CRUD)
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/api/products", methods=["GET"])
def list_products():
    """GET /api/products — list all products, optional ?category= filter."""
    cat = request.args.get("category")
    items = [p for p in PRODUCTS if not cat or p["category"] == cat]
    return jsonify({"products": items, "count": len(items)})


@app.route("/api/products/<int:pid>", methods=["GET"])
def get_product(pid):
    """GET /api/products/:id — get one product."""
    p = next((p for p in PRODUCTS if p["id"] == pid), None)
    if not p:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(p)


# ─────────────────────────────────────────────────────────────────────────────
# STEP 9  —  CART & CHECKOUT  (e-commerce flow)
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/api/cart", methods=["GET"])
def view_cart():
    total = sum(item["price"] * item["qty"] for item in CART)
    return jsonify({"items": CART, "total": total})


@app.route("/api/cart", methods=["POST"])
def add_to_cart():
    global CART
    data = request.get_json(force=True)
    pid = data.get("product_id")
    qty = data.get("qty", 1)
    product = next((p for p in PRODUCTS if p["id"] == pid), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    # check if already in cart
    existing = next((c for c in CART if c["product_id"] == pid), None)
    if existing:
        existing["qty"] += qty
    else:
        CART.append({"product_id": pid, "name": product["name"],
                     "price": product["price"], "qty": qty})

    total = sum(item["price"] * item["qty"] for item in CART)
    return jsonify({"message": f"Added {product['name']} x{qty} to cart",
                    "cart": CART, "total": total}), 201


@app.route("/api/cart", methods=["DELETE"])
def clear_cart():
    global CART
    CART = []
    return jsonify({"message": "Cart cleared", "cart": [], "total": 0})


@app.route("/api/checkout", methods=["POST"])
def checkout():
    global CART, ORDER_COUNTER
    if not CART:
        return jsonify({"error": "Cart is empty"}), 400
    ORDER_COUNTER += 1
    total = sum(item["price"] * item["qty"] for item in CART)
    order = {
        "order_id":   f"ORD-{ORDER_COUNTER:04d}",
        "items":      list(CART),
        "total":      total,
        "status":     "confirmed",
        "placed_at":  datetime.datetime.now().isoformat(),
    }
    CART = []
    return jsonify(order), 201


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n  Web Fundamentals Lab")
    print("  Open http://localhost:5000 in your browser\n")
    app.run(debug=False, threaded=True, port=5000)
