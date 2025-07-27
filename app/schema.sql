-- Database Schema for Libyan Market Place

-- Table to store cities and their populations
CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ar TEXT NOT NULL,
    population INTEGER NOT NULL
);

-- Table for businesses to advertise their services
CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER,
    service_name_ar TEXT NOT NULL,
    description_ar TEXT NOT NULL,
    contact_info TEXT NOT NULL,
    posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities (id)
);

-- Table for job seekers to post their skills
CREATE TABLE job_seekers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER,
    name_ar TEXT NOT NULL,
    skills_ar TEXT NOT NULL,
    contact_info TEXT NOT NULL,
    posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities (id)
);

-- Table for employers to post job vacancies
CREATE TABLE job_vacancies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER,
    title_ar TEXT NOT NULL,
    description_ar TEXT NOT NULL,
    contact_info TEXT NOT NULL,
    posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities (id)
);

-- Table for users to sell or buy products
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER,
    product_name_ar TEXT NOT NULL,
    description_ar TEXT NOT NULL,
    price REAL NOT NULL,
    contact_info TEXT NOT NULL,
    is_for_sale BOOLEAN DEFAULT TRUE, -- TRUE for selling, FALSE for buying
    posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities (id)
);
