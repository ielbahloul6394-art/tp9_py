
from models import Produit, Client
from sqlite_dao import SQLiteDAO


def afficher_menu():
    print("\n========== GESTION BOUTIQUE ==========")
    print("1. Ajouter un produit")
    print("2. Lister les produits")
    print("3. Ajouter un client")
    print("4. Lister les clients")
    print("5. Rechercher un client par email")
    print("6. Modifier le prix d'un produit")
    print("0. Quitter")
    print("======================================")


def main():
    dao = SQLiteDAO()

    print("Connexion SQLite reussie.")

    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        try:
            if choix == "1":
                nom = input("Nom du produit : ")
                prix = float(input("Prix du produit : "))

                if not nom.strip() or prix < 0:
                    print("Donnees invalides.")
                    continue

                produit = Produit(None, nom, prix)
                dao.ajouter_produit(produit)

            elif choix == "2":
                produits = dao.lister_produits()
                print("\nListe des produits :")

                if produits:
                    for produit in produits:
                        print(produit)
                else:
                    print("Aucun produit.")

            elif choix == "3":
                nom = input("Nom du client : ")
                email = input("Email du client : ")

                if not nom.strip() or not email.strip():
                    print("Informations invalides.")
                    continue

                client = Client(None, nom, email)
                dao.ajouter_client(client)

            elif choix == "4":
                clients = dao.lister_clients()
                print("\nListe des clients :")

                if clients:
                    for client in clients:
                        print(client)
                else:
                    print("Aucun client.")

            elif choix == "5":
                email = input("Email a rechercher : ")
                client = dao.rechercher_client(email)

                if client:
                    print("Client trouve :")
                    print(client)
                else:
                    print("Client introuvable.")

            elif choix == "6":
                id_produit = int(input("ID du produit : "))
                nouveau_prix = float(input("Nouveau prix : "))

                if nouveau_prix < 0:
                    print("Prix invalide.")
                    continue

                dao.modifier_prix(id_produit, nouveau_prix)

            elif choix == "0":
                print("Fermeture du programme.")
                break

            else:
                print("Choix invalide.")

        except ValueError:
            print("Veuillez entrer une valeur correcte.")

        except Exception as erreur:
            print("Erreur :", erreur)

    dao.fermer()


if __name__ == "__main__":
    main()
