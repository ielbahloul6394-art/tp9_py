
import sqlite3
from models import Produit, Client


class SQLiteDAO:

    def __init__(self):
        self.conn = sqlite3.connect("boutique.db")
        self.creer_tables()

    def creer_tables(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prix REAL NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)

        self.conn.commit()

    def ajouter_produit(self, produit):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO produits (nom, prix) VALUES (?, ?)",
            (produit.nom, produit.prix)
        )
        self.conn.commit()
        print("Produit ajoute avec succes.")

    def lister_produits(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM produits")
        lignes = cursor.fetchall()

        return [
            Produit(id, nom, prix)
            for id, nom, prix in lignes
        ]

    def ajouter_client(self, client):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO clients (nom, email) VALUES (?, ?)",
            (client.nom, client.email)
        )
        self.conn.commit()
        print("Client ajoute avec succes.")

    def lister_clients(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM clients")
        lignes = cursor.fetchall()

        return [
            Client(id, nom, email)
            for id, nom, email in lignes
        ]

    def rechercher_client(self, email):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM clients WHERE email = ?",
            (email,)
        )

        ligne = cursor.fetchone()

        if ligne:
            return Client(ligne[0], ligne[1], ligne[2])

        return None

    def modifier_prix(self, id_produit, nouveau_prix):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE produits SET prix = ? WHERE id = ?",
            (nouveau_prix, id_produit)
        )
        self.conn.commit()

        if cursor.rowcount > 0:
            print("Prix modifie avec succes.")
        else:
            print("Produit introuvable.")

    def fermer(self):
        self.conn.close()
