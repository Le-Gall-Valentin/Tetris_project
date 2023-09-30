import time
from DisplayGameMenu import displayGameMenu
"""
T'es Trisse
Hugo Leyx-valade | Valentin Le Gall
Ce module 'placePiece.py' contient toutes les fonction nécessaire au placement des pièces
mais également la suite comme la suppression des lignes pleines
"""


def rotatePiece(form: list):
    """
    Cette fonction permet la rotation de la piece à la position initiale
    :param form: Une liste contenant la forme que l'on veut tourner
    :return: Aucun car form est une liste et donc mutable
    """
    tempForm = []
    tempForm2 = []
    """
    supprime les lignes vides dans form pour éviter les problèmes au moment de la rotation
    """
    while ([0] * len(form[0])) in form:
        form.remove([0] * len(form[0]))
    """
    Boucles permettant la rotation de la piece form dans la liste tempForm
    tempForm2 est ici une liste temporaire 
    """
    for columns in range(len(form[0])):
        for raws in range(len(form)):
            tempForm2.append(form[len(form) - 1 - raws][columns])
        tempForm.append(tempForm2)
        tempForm2 = []
    """
    supprime les lignes vides dans tempForm qui pourraient se trouver à la fin de la matrice
    """
    while ([0] * len(tempForm[0])) in tempForm:
        tempForm.remove([0] * len(tempForm[0]))
    """
    Ajoute des lignes vides en haut de tempForm afin de la remettre aux dimensions initiales.
    """
    while len(tempForm) < len(form[0]):
        tempForm.insert(0, [0] * len(tempForm[0]))
    """
    Ajoute des 0 à la fin de chaques lignes afin de la remettre aux dimensions initiales.
    """
    for raws in tempForm:
        while len(raws) < len(form[0]):
            raws.append(0)
    """
    transfert tempForm dans form
    """
    form.clear()
    for raws in tempForm:
        form.append(raws)


def placePiece(gridMatrix: list, formsMatrix: list, form: list, x_coords: int, y_coords: int, forms: list, states: dict) -> bool:
    """
    Fonction directrice du module permettant de prendre en charge la totalité du placement de la piece.
    Appellant la vérification de la position, la pose de la piece, la suppression des lignes
    param gridMatrix : Matrice de la grille
    param formsMatrix : Matrice des pieces
    param form : Matrice de la piece à placer
    param x_coords : entier, coordonnées X
    param y_coords : entier, coordonnées Y
    param forms : liste d'entiers correspondant aux pieces proposés
    param states : dictionnaire contenant l'état de la partie
    return : Boolean disant si oui ou non la pièce à été placée
    """
    if verificationPiece(form, gridMatrix, x_coords, y_coords):
        placePieceInGridMatrix(gridMatrix, form, y_coords, x_coords)
        removeCompleteHorizontalLines(gridMatrix, formsMatrix, forms, states)
        removeCompleteVerticalLines(gridMatrix, states)
    else:
        states["Lives"] -= 1
        print("You can't place this piece here ! Lives : ", states["Lives"])
        return False


def removeCompleteVerticalLines(gridMatrix: list, states: dict):
    """
    Permet de créer une liste contenant les colonnes pour la fonction clearFullVerticalLine(gridMatrix, column, states, i)
    :param gridMatrix: Matrice de la grille
    :param states: dictionnaire contenant l'état de la partie
    :return: rien, car clearFullVerticalLine(gridMatrix, column, states, i) s'occupe du reste
    """
    column = []
    for col in range(0, len(gridMatrix[0])):
        for lines in range(0, len(gridMatrix)):
            column.append(gridMatrix[lines][col])
        clearFullVerticalLine(gridMatrix, column, states, col)
        column = []


def clearFullVerticalLine(gridMatrix: list, column: list, states: dict, col: int):
    """
    Permet la suppression de toutes les cases pleines dans une colonne
    :param gridMatrix: Matrice de la grille
    :param column: liste contenant une colonne de la grille à vérifier
    :param states: dictionnaire contenant l'état de la partie
    :param col: entier correspondant à la colonne que l'on vérifi
    :return: Rien car les listes et les dictionnaires modifiés sont mutables
    """
    if 1 not in column:
        for line in range(0, len(gridMatrix)):
            if gridMatrix[line][col] == 2:
                gridMatrix[line][col] = 1
                states["Score"] += 1


def removeCompleteHorizontalLines(gridMatrix: list, formsMatrix: list, forms: list, states: dict):
    """
    Cette fonction permet de vider une lignes pleine
    :param gridMatrix: Matrice de la grille
    :param formsMatrix: Matrice des formes nécessaire à la fonction
    displayGameMenuIfModifications(gridMatrix, formsMatrix, forms, states)
    :param forms: liste contenant des entiers correspondant aux 3 formes en cours d'utilisation nécessaire
    à la fonction displayGameMenuIfModifications(gridMatrix, formsMatrix, forms, states)
    :param states: dictionnaire contenant l'état de la partie
    :return: Rien car les tableaux modifiés sont mutables
    """
    for lines in range(len(gridMatrix)):
        if 1 not in gridMatrix[lines]:
            for col in range(0, len(gridMatrix[lines])):
                if gridMatrix[lines][col] == 2:
                    gridMatrix[lines][col] = 1
                    states["Score"] += 1
                    moveNumbersInMatrix(gridMatrix, lines, col)
            displayGameMenuIfModifications(gridMatrix, formsMatrix, forms, states)


def moveNumbersInMatrix(gridMatrix: list, lines: int, col: int):
    """
    Fonction qui permet si une ligne est vidée de faire tomber toutes les lignes au dessus
    :param gridMatrix: Matrice de la grille
    :param lines: Entier correspondant à la ligne à partir de laquelle elle fait tomber celles du dessus
    :param col: Entier correspondant à la colonne que l'on fait tomber
    :return: Aucun car les tableaux sont mutables
    """
    for line in range(lines, 0, -1):
        if gridMatrix[line - 1][col] == 2:
            gridMatrix[line][col] = gridMatrix[line - 1][col]
            gridMatrix[line - 1][col] = 1


def displayGameMenuIfModifications(gridMatrix: list, formsMatrix: list, forms: list, states: dict):
    """
    Fonction permettant d'afficher le menu mais également de rappeler la fonction
    removeCompleteHorizontalLines(gridMatrix, formsMatrix, forms, states)
    afin de faire une boucle tant qu'il y a des lignes pleines
    :param gridMatrix: Matrice de la grille
    :param formsMatrix: Matrice des formes
    :param forms: Liste contenant les formes que l'on utilise
    :param states: dictionnaire contenant l'état de la partie
    :return: Aucun, car elle lance seulement d'autres fonctions
    """
    displayGameMenu(gridMatrix, formsMatrix, forms, states)
    time.sleep(0.40)
    removeCompleteHorizontalLines(gridMatrix, formsMatrix, forms, states)


def placePieceInGridMatrix(gridMatrix: list, form: list, x_coords: int, y_coords: int):
    """
    Fonction qui permet de placer les piece dans la grille
    :param gridMatrix: Matrice de la grille
    :param form: Matrice de la forme que l'on veut placer
    :param x_coords: Entier correspondant aux coordonnées x
    :param y_coords: Entier correspondant aux coordonnées Y
    :return: Rien car les tableaux son mutables
    """
    for lines in range(len(form)-1, -1, -1):
        for col in range(0, len(form), 1):
            if form[len(form)-1 - lines][col] == 1:
                gridMatrix[x_coords - lines][y_coords + col] += form[len(form) - 1 - lines][col]


def verificationPiece(form: list, gridMatrix: list, x_coords: int, y_coords: int) -> bool:
    """
    Fonction qui vérifi si la piece peut-être placée ici
    :param form: Matrice de la form que l'on veut placer
    :param gridMatrix: Matrice de la grille
    :param x_coords: Entier correspondant aux coordonnées x
    :param y_coords: Entier correspondant aux coordonnées Y
    :return: Boolean True si elle est plaçable et false sinon
    """
    for lines in range(len(form) - 1, -1, -1):
        for col in range(0, len(form), 1):
            if form[len(form) - 1 - lines][col] == 1:
                if ((y_coords - lines) >= 0) and (x_coords + col) < len(gridMatrix[0]):
                    indexInGridMatrix = gridMatrix[y_coords - lines][x_coords + col]
                    if (indexInGridMatrix == 0) or (indexInGridMatrix == 2):
                        return False
                else:
                    return False
    return True
