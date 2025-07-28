# Libyan Market Place

This is a simple web application for a Libyan marketplace, built with Flask and SQLite.

## How to Run

### Development

1. **Install dependencies:**
   ```bash
   pip install Flask
   ```

2. **Run the application:**
   ```bash
   python app/app.py
   ```

3. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```

### Production (with Gunicorn)

1. **Install dependencies:**
   ```bash
   pip install Flask gunicorn
   ```

2. **Run the application with Gunicorn:**
   ```bash
   gunicorn -w 4 'app.app:app'
   ```

3. **Open your browser and go to:**
   ```
   http://127.0.0.1:8000/
   ```
