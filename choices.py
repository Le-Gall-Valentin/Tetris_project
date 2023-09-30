"""
T'es Trisse
Hugo Leyx-valade | Valentin Le Gall
Ce module 'choice.py' permet de faire les différents choix durant le jeu.
Chaque fonction est une saisie sécurisée afin d'empêcher que le programme ne s'arrête prématurément
"""


def leave(entry: str, states: dict):
    """
    Cette fonction permet de vérifier si le terme entré dans les autres fonctions n'est pas 'exit' dans ce cas,
    elle modifie le paramètre states
    param 1 entry : chaîne de caractères correspondant à la saisie de l'utilisateur
    param 2 states : dictionnaire correspondant à l'état du jeu
    return : Rien car 'states' est modifié et est mutable.
    """
    if entry == "exit":
        states["EndGame"] = True
        print("You have decided to leave the game, finish the current round !")


def choiceRotate(states: dict) -> bool:
    """
    Saisie sécurisée pour le choix de la rotation
    param states : dictionnaire correspondant à l'état du jeu affin de lancer la fonction leave()
    return : boolean utile à la fonction appelante gameMenu()
    """
    print("Do you want to turn the form ?")
    print("Y : Yes | N : No")
    response = input("Response : ")
    leave(response, states)
    while (response != "Y") and (response != "N"):
        response = input("Response : ")
        leave(response, states)
    if response == "Y":
        return True
    else:
        return False


def choiceLengthGrid() -> int:
    """
    Saisie sécurisée afin de choisir la taille de la grille
    return : entier correspondant à la taille de la grille
    """
    response = input(14 * " " + "Choose odd grid length : ")
    while not response.isdigit():
        response = input("Choose valid odd grid length >= 7 and <= 35 : ")
    while (int(response) % 2 == 0) or (int(response) < 7) or (int(response) > 35):
        response = input("Choose valid odd grid length >= 7 and <= 35 : ")
        if not response.isdigit():
            response = 36
    return int(response)


def choiceSave() -> str:
    """
    Saisie sécurisée permettant de dire OUI ou NON
    return : chaîne de caractère Y ou N
    """
    response = input(20 * " " + "Enter your response: ")
    while (response != "Y") and (response != "N"):
        response = input(20 * " " + "Invalid response: ")
    return response


def choiceXCoords(length: int, states: dict) -> int:
    """
    Saisie sécurisée permettant à l'utilisateur d'entrer les coordonnées X
    param 1 length : longueur de la grille
    param 2 states : dictionnaire correspondant à l'état du jeu affin de lancer la fonction leave()
    return : entier correspondant à la position x dans le tableau
    """
    """
    première vérification de la taille du tableau (length) permettant de savoir 
    quelle méthode employer pour envoyer le message car les coordonnées finissent 
    par 1,2,3,4,5,6,7,8,9 si length > 26
    """
    if length <= 26:
        x_coords = input("Enter vertical coordinate like 'a' and '" + chr(96+length) + "' : ")
        lengthMax = length
        gap = 0
    else:
        x_coords = input("Enter vertical coordinate like 'a' and '" + chr(22 + length) + "' : ")
        lengthMax = 26
        gap = length - 26
    leave(x_coords, states)
    """
    Première vérification de saisie pour éviter le crash 
    à la prochaine vérification car ord() ne supporte par 2 caractères
    """
    while len(x_coords) != 1:
        x_coords = input("Invalid coordinate :")
        leave(x_coords, states)
    """
    Seconde vérification
    ((97 > ord(x_coords)) or (ord(x_coords) > 96+lengthMax)) vérifie si la saisie est bien entre a et z
    ((ord(x_coords) < 49) or (ord(x_coords) >= 49 + gap)) vérifie si la saisie est bien entre 1 et 9
    """
    while ((97 > ord(x_coords)) or (ord(x_coords) > 96+lengthMax)) and ((ord(x_coords) < 49) or (ord(x_coords) >= 49 + gap)):
        response = input("Invalid coordinate :")
        if len(response) == 1:
            x_coords = response
        leave(response, states)
    if x_coords.isdigit():
        x_coords = int(x_coords) + 25
    else:
        x_coords = ord(x_coords) - 97
    return x_coords


def choiceYCoords(height: int, states: dict) -> int:
    """
    Saisie sécurisée permettant à l'utilisateur d'entrer les coordonnées Y
    param 1 height : hauteur de la grille
    param 2 states : dictionnaire correspondant à l'état du jeu affin de lancer la fonction leave()
    return : entier correspondant à la position Y dans le tableau
    """
    """
    première vérification de la taille du tableau (height) permettant de savoir 
    quelle méthode employer pour envoyer le message car les coordonnées finissent 
    par 1,2,3,4,5,6,7,8,9 si length > 26
    """
    if height <= 26:
        y_coords = input("Enter horizontal coordinate like 'A' and '" + chr(64+height) + "' : ")
        heightMax = height
        gap = 0
    else:
        y_coords = input("Enter horizontal coordinate like 'A' and '" + chr(22 + height) + "' : ")
        heightMax = 26
        gap = height - 26
    leave(y_coords, states)
    """
        Première vérification de saisie pour éviter le crash 
        à la prochaine vérification car ord() ne supporte par 2 caractères
    """
    while len(y_coords) != 1:
        y_coords = input("Invalid coordinate :")
        leave(y_coords, states)
    """
        Seconde vérification
        ((65 > ord(y_coords)) or (ord(y_coords) > 64+heightMax)) vérifie si la saisie est bien entre A et Z
        ((ord(x_coords) < 49) or (ord(x_coords) >= 49 + gap)) vérifie si la saisie est bien entre 1 et 9
    """
    while ((65 > ord(y_coords)) or (ord(y_coords) > 64+heightMax)) and ((ord(y_coords) < 49) or (ord(y_coords) >= 49 + gap)):
        response = input("Invalid coordinate :")
        if len(response) == 1:
            y_coords = response
        leave(y_coords, states)
    if y_coords.isdigit():
        y_coords = int(y_coords) + 25
    else:
        y_coords = ord(y_coords) - 65
    return y_coords


def choiceCoord(length: int, height: int, states: dict) -> tuple:
    """
    Cette fonction permet d'appeler les fonctions permettant les saisies sécurisées des coordonnées x et y
    param 1 length : longueur de la grille
    param 2 height : hauteur de la grille
    param 3 states : dictionnaire correspondant à l'état du jeu affin de lancer la fonction leave()
    return : tuple d'entiers correspondant aux coordonnées x et y
    """
    x_coords = choiceXCoords(length, states)
    y_coords = choiceYCoords(height, states)
    return x_coords, y_coords


def choiceFormInMatrix(forms: list, formsMatrix: list, states: dict) -> list:
    """
    Permet de faire le choix de la forme entre 1, 2, 3
    :param forms: tableau d'entier correspondant aux 3 formes déterminé aléatoirement
    :param formsMatrix: Matrice contenant toutes les formes utilisés
    :param states: dictionnaire correspondant à l'état du jeu affin de lancer la fonction leave()
    :return: Matrice de la forme sélectionnée
    """
    choiceForm = 0
    while choiceForm != '1' and choiceForm != '2' and choiceForm != '3':
        choiceForm = input("Choose a form between 1 and 3 : ")
        leave(choiceForm, states)
    return formsMatrix[forms[int(choiceForm)-1]]


def choiceGrid() -> int:
    """
    Saisie sécurisée permettant de faire le choix de la grille
    :return: entier correspondant à la forme choisie 1 : diamond | 2 : triangle | 3 : circle
    """
    response = 0
    while response != '1' and response != '2' and response != '3':
        response = input(22 * " " + "Enter a number : ")
    return int(response)


def choiceRules():
    """
    Cette fonction permet de faire le choix entre play et rules
    :return: boolean correspondant à oui ou non
    """
    response = ""
    while response != "P" and response != "R":
        response = input(18 * " " + "Enter your choice : ")
    if response == "R":
        return True
    return False


def choiceLanguagesRules():
    """
    Cette fonction permet de faire le choix du langage pour les règles F : French | E : English
    :return: chaine de caractères F ou E
    """
    response = ""
    while response != "F" and response != "E":
        response = input(16 * " " + "Enter your choice languages : ")
    return response
