import sqlite3
from flask import Flask, jsonify, request, g, send_from_directory, render_template

app = Flask(__name__)
DATABASE = 'libyan_market.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# API endpoints
@app.route('/api/cities', methods=['GET'])
def get_cities():
    db = get_db()
    cursor = db.execute('SELECT * FROM cities')
    cities = cursor.fetchall()
    return jsonify([{'id': row[0], 'name_ar': row[1], 'population': row[2]} for row in cities])

# API for services
@app.route('/api/services', methods=['GET', 'POST'])
def handle_services():
    db = get_db()
    if request.method == 'POST':
        data = request.json
        db.execute('INSERT INTO services (city_id, service_name_ar, description_ar, contact_info) VALUES (?, ?, ?, ?)',
                   [data['city_id'], data['service_name_ar'], data['description_ar'], data['contact_info']])
        db.commit()
        return jsonify({'message': 'Service added successfully'})
    else:
        cursor = db.execute('SELECT * FROM services')
        services = cursor.fetchall()
        return jsonify([{'id': row[0], 'city_id': row[1], 'service_name_ar': row[2], 'description_ar': row[3], 'contact_info': row[4]} for row in services])

# API for job seekers
@app.route('/api/job_seekers', methods=['GET', 'POST'])
def handle_job_seekers():
    db = get_db()
    if request.method == 'POST':
        data = request.json
        db.execute('INSERT INTO job_seekers (city_id, name_ar, skills_ar, contact_info) VALUES (?, ?, ?, ?)',
                   [data['city_id'], data['name_ar'], data['skills_ar'], data['contact_info']])
        db.commit()
        return jsonify({'message': 'Job seeker added successfully'})
    else:
        cursor = db.execute('SELECT * FROM job_seekers')
        seekers = cursor.fetchall()
        return jsonify([{'id': row[0], 'city_id': row[1], 'name_ar': row[2], 'skills_ar': row[3], 'contact_info': row[4]} for row in seekers])

# API for job vacancies
@app.route('/api/job_vacancies', methods=['GET', 'POST'])
def handle_job_vacancies():
    db = get_db()
    if request.method == 'POST':
        data = request.json
        db.execute('INSERT INTO job_vacancies (city_id, title_ar, description_ar, contact_info) VALUES (?, ?, ?, ?)',
                   [data['city_id'], data['title_ar'], data['description_ar'], data['contact_info']])
        db.commit()
        return jsonify({'message': 'Job vacancy added successfully'})
    else:
        cursor = db.execute('SELECT * FROM job_vacancies')
        vacancies = cursor.fetchall()
        return jsonify([{'id': row[0], 'city_id': row[1], 'title_ar': row[2], 'description_ar': row[3], 'contact_info': row[4]} for row in vacancies])

# API for products
@app.route('/api/products', methods=['GET', 'POST'])
def handle_products():
    db = get_db()
    if request.method == 'POST':
        data = request.json
        db.execute('INSERT INTO products (city_id, product_name_ar, description_ar, price, contact_info, is_for_sale) VALUES (?, ?, ?, ?, ?, ?)',
                   [data['city_id'], data['product_name_ar'], data['description_ar'], data['price'], data['contact_info'], data.get('is_for_sale', True)])
        db.commit()
        return jsonify({'message': 'Product added successfully'})
    else:
        cursor = db.execute('SELECT * FROM products')
        products = cursor.fetchall()
        return jsonify([{'id': row[0], 'city_id': row[1], 'product_name_ar': row[2], 'description_ar': row[3], 'price': row[4], 'contact_info': row[5], 'is_for_sale': row[6]} for row in products])

def insert_sample_data():
    with app.app_context():
        db = get_db()
        # Sample cities
        db.execute("INSERT INTO cities (name_ar, population) VALUES (?, ?)", ('طرابلس', 2000000))
        db.execute("INSERT INTO cities (name_ar, population) VALUES (?, ?)", ('بنغازي', 1500000))

        # Sample services
        db.execute("INSERT INTO services (city_id, service_name_ar, description_ar, contact_info) VALUES (?, ?, ?, ?)",
                       (1, 'خدمات توصيل', 'توصيل سريع وآمن داخل طرابلس', '091-xxxxxxx'))

        # Sample job seekers
        db.execute("INSERT INTO job_seekers (city_id, name_ar, skills_ar, contact_info) VALUES (?, ?, ?, ?)",
                       (1, 'أحمد', 'مطور مواقع ويب', 'ahmed@email.com'))

        # Sample job vacancies
        db.execute("INSERT INTO job_vacancies (city_id, title_ar, description_ar, contact_info) VALUES (?, ?, ?, ?)",
                       (2, 'محاسب', 'مطلوب محاسب للعمل في شركة ببنغازي', '092-xxxxxxx'))

        # Sample products
        db.execute("INSERT INTO products (city_id, product_name_ar, description_ar, price, contact_info) VALUES (?, ?, ?, ?, ?)",
                       (1, 'لابتوب مستعمل', 'لابتوب بحالة ممتازة للبيع', 1500, '091-yyyyyyy'))
        db.commit()

def setup_database():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        insert_sample_data()

if __name__ == '__main__':
    import os
    if not os.path.exists(DATABASE):
        setup_database()
    app.run(debug=True)
