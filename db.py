import sqlite3
from faker import Faker
import random

# Initialiser Faker
fake = Faker()

# Connexion à la base SQLite
DB_NAME = "./db.sql"

def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Créer la table products si elle n'existe pas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            price REAL,
            image_url TEXT
        )
    ''')
    conn.commit()
    conn.close()

def generate_random_image_url(width, height,rdm):
    return f"https://picsum.photos/{width}/{height}?random={rdm}"

def faker_products():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for _ in range(600):
        name = fake.word()
        description = fake.sentence()
        price = round(random.uniform(10, 200), 2)
        rdm = random.randint(1, 1000)
        image_url = generate_random_image_url(300, 300,rdm)
        
        cursor.execute('''
            INSERT INTO products (name, description, price, image_url)
            VALUES (?, ?, ?, ?)
        ''', (name, description, price, image_url))

    conn.commit()
    conn.close()

# Initialiser la base de données
if __name__ == "__main__":
    create_db()
    print("Base de données créée.")
    faker_products()
    print("600 produits ajoutés.")