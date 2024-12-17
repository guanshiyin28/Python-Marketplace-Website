from app import app
from flask import render_template
import requests as req
from app.models.product import Product 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/kategori')
def kategori():
    return render_template("kategori.html")

@app.route('/produk')
def produk():
    products=[]
    r=req.get('https://fakestoreapi.com/products')
    for product in r.json():
        products.append(
            Product(
                id=product['id'],
                title=product['title'],
                price=product['price'],
                description=product['description'],
                category=product['category'],
                image=product['image']
            )
        )
    return render_template("produk.html", products=products)

@app.route('/contact')
def contact():
    return render_template("kontak.html")

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):

    r=req.get(f'https://fakestoreapi.com/products/{product_id}')
    product=r.json()
    return render_template('detail_produk.html',product=product)
