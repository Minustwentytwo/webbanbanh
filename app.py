from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Dữ liệu sản phẩm mẫu với hình ảnh
products = [
    {'name': 'Bánh Mì', 'price': 10000, 'image': 'banh_mi.jpg'},
    {'name': 'Bánh Bao', 'price': 15000, 'image': 'banh_bao.jpg'},
    {'name': 'Bánh Xèo', 'price': 20000, 'image': 'banh_xeo.jpg'},
    {'name': 'Bánh Chưng', 'price': 25000, 'image': 'banh_chung.jpg'},
    {'name': 'Bánh Cuốn', 'price': 30000, 'image': 'banh_cuon.jpg'},
    {'name': 'Bánh Khọt', 'price': 35000, 'image': 'banh_khot.jpg'}
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/login')
def login():
    return "Đăng nhập"

@app.route('/register')
def register():
    return "Đăng ký"

if __name__ == '__main__':
    app.run(debug=True)
