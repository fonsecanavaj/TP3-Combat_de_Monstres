# Julieta María Fonseca Nava
# 01/10/23
# TP3 - Combat de Monstres

# Importer la librairie et définir les variables
import random

niveau_vie = 20
force_adversaire = random.randint(1, 10)
numero_adversaire = 0
numero_combat = 0
score_dé1 = random.randint(1, 6)
score_dé2 = random.randint(1, 6)
nombre_victoires = 0
nombre_defaites = 0
victoires_consecutives = 0
start = 1

# Définir le dictionnaire pour les options du jeu de l'utilisateur
menu = { "1-": "Combattre cet adversaire",
         "2-": "Contourner cet adversaire et aller ouvrir une autre porte",
         "3-": "Afficher les règles du jeu",
         "4-": "Quitter la partie"
         }


# L'ordinateur affiche les instructions du jeu (output)
def rules():
    print("""\nPour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l'adversaire. 
Dans ce cas, le niveau de vie de l'usager est augmenté de la force de l'adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l'usager est inférieure ou égale à la force de l'adversaire. 
Dans ce cas, le niveau de vie de l'usager est diminué de la force de l'adversaire.""")
    print("""\nLa partie se termine lorsque les points de vie de l'usager tombent sous 0.
\nL'usager peut combattre ou éviter chaque adversaire, dans le cas de l'évitement, il y a une pénalité de 1 point de vie.\n""")

# L'ordinateur affiche les informations du joueur à chaque tour
# Output = # adversaire, force de l'adversaire, niveau de vie actuel et ratio victoire-défaite
def status():
    print(f"""\nAdversaire: {numero_adversaire}
Force de l'adversaire: {force_adversaire}
Niveau de vie de l'usager: {niveau_vie}
Combat {numero_combat}: Victoires: {nombre_victoires} vs Défaites: {nombre_defaites}""")

# Après une victoire, les informations s'actualisent
# Output = Niveau de vie actuel et Nbr de victoires consécutives
def new_status():
    print(f"""\nNiveau de vie de l'usager: {niveau_vie}
Nombre de victoires consécutives: {victoires_consecutives}""")

# Le code s'arrête
# Output = L'ordinateur affiche des politesses
def exit_game():
    print("\nMerci et au revoir...")
    exit()


# Le jeu s'execute en continu, sauf si exit_game() est appelée
while start == 1:
    print(f"\nVous tombez face à face avec un adversaire de difficulté {force_adversaire}.\n")
    for k,v in menu.items():
        print(k,v)
    choix = int(input("Que voulez vous faire? "))  # L'utilisateur choisit une des 4 options

    # Si le choix est de combattre le monstre, on ajuste les informations
    if choix == 1:
        numero_adversaire += 1
        numero_combat += 1
        status()
        print(f"Lancer du dé #1: {score_dé1}")    
        print(f"Lancer du dé #2: {score_dé2}")
        score_total = score_dé1 + score_dé2
        print(f"Score total: {score_total}")  # On calcule le lancer des 2 dés

        # Si l'utilisateur gagne, on ajuste le nbr de victoires
        if score_total > force_adversaire:
            combat_status = "Victoire"
            print(f"Dernier combat: {combat_status}")
            niveau_vie += force_adversaire
            victoires_consecutives +=1
            nombre_victoires +=1
            new_status()

        # Si l'utilisateur perd, on ajuste le nbr de défaites
        else:
            combat_status = "Défaite"
            print(f"Dernier combat: {combat_status}")
            niveau_vie -= force_adversaire
            victoires_consecutives = 0
            nombre_defaites +=1

            # Le niveau de vie ne va pas dans les négatifs (min = 0)
            if niveau_vie < 0:
                print(f"Niveau de vie: 0")
            else:
                print(f"Niveau de vie: {niveau_vie}")

            # Si l'utilisateur meurt, on recommence la partie avec un nouveau adversaire
            if niveau_vie <= 0:
                print(f"""La partie est terminée.
Vous avez vaincu {nombre_victoires} monstre(s).""")
                niveau_vie = 20
                numero_adversaire = 0
                numero_combat = 0   
                nombre_defaites = 0
                nombre_victoires = 0
                print("""\nNouvelle partie:
Niveau de vie: 20""")

        # À chaque tour, les dés sont relancés
        score_dé1 = random.randint(1, 6)
        score_dé2 = random.randint(1, 6)
        # Si l'utilisateur a plus de 3 victoires, le monstre est plus fort
        if nombre_victoires < 3:
            force_adversaire = random.randint(1, 6)
        else:
            force_adversaire = random.randint(6, 12)


    # Si le choix est de contourner, le niveau de vie diminue de 1
    elif choix == 2:
        print("\nVous avez reçu une penalité de 1 point")
        niveau_vie -=1
        print(f"Niveau de vie: {niveau_vie}")

    # Si le choix est de voir les règles, elles s'affichent
    elif choix == 3:
        rules()

    # Si le choix est 4, le jeu s'arrête
    else:
        exit_game()

    start = 1
