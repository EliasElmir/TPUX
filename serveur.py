from flask import Flask, jsonify
import sqlite3
from models import Product

app = Flask(__name__)

@app.route("/products", methods=["GET"])
def get_products():
    conn = sqlite3.connect("db.sql")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()

    products = [
        Product(id=row[0], name=row[1], description=row[2], price=row[3], image_url=row[4]).to_dict()
        for row in rows
    ]

    return jsonify({"products": products})

if __name__ == "__main__":
    app.run(debug=True, port=8080)