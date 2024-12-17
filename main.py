import os
from db import create_db, faker_products
import serveur

if not os.path.exists("db.sql"):
    print("Base de données non existante, création en cours...")
    create_db()
    faker_products()
    print("Base de données et produits fictifs créés.")

print("Démarrage du serveur...")
serveur.app.run(debug=True, port=8080)