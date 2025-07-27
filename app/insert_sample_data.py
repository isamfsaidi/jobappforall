import sqlite3

DATABASE = 'libyan_market.db'

def insert_sample_data():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Sample cities
    cursor.execute("INSERT INTO cities (name_ar, population) VALUES (?, ?)", ('طرابلس', 2000000))
    cursor.execute("INSERT INTO cities (name_ar, population) VALUES (?, ?)", ('بنغازي', 1500000))

    # Sample services
    cursor.execute("INSERT INTO services (city_id, service_name_ar, description_ar, contact_info) VALUES (?, ?, ?, ?)",
                   (1, 'خدمات توصيل', 'توصيل سريع وآمن داخل طرابلس', '091-xxxxxxx'))

    # Sample job seekers
    cursor.execute("INSERT INTO job_seekers (city_id, name_ar, skills_ar, contact_info) VALUES (?, ?, ?, ?)",
                   (1, 'أحمد', 'مطور مواقع ويب', 'ahmed@email.com'))

    # Sample job vacancies
    cursor.execute("INSERT INTO job_vacancies (city_id, title_ar, description_ar, contact_info) VALUES (?, ?, ?, ?)",
                   (2, 'محاسب', 'مطلوب محاسب للعمل في شركة ببنغازي', '092-xxxxxxx'))

    # Sample products
    cursor.execute("INSERT INTO products (city_id, product_name_ar, description_ar, price, contact_info) VALUES (?, ?, ?, ?, ?)",
                   (1, 'لابتوب مستعمل', 'لابتوب بحالة ممتازة للبيع', 1500, '091-yyyyyyy'))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    insert_sample_data()
