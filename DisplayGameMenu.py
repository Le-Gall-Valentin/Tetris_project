from os import system
from displayMatrix import returnDisplayGridMatrixLine, returnDisplayFormMatrixLine

"""
T'es Trisse
Hugo Leyx-valade | Valentin Le Gall
Ce module 'DisplayGameMenu.py' permet d'afficher différentes choses durant la partie.
"""


def windowLength(x: int, y: int):
    """
    Fonction permettant de modifier la taille de la fenêtre de jeu
    :param x: entier correspondant à la longueur de la fenêtre
    :param y: entier correspondant à la hauteur de la fenêtre
    :return: Aucun car il modifie la taille directement
    """
    system("mode "+str(x)+","+str(y))


def displayFormToRotate(form):
    """
    Fonction permettant d'afficher la nouvelle fenêtre avec la forme que l'on veut tourner
    :param form: Matrice de la forme que l'on désire tourner
    :return: Aucun car elle affiche seulement quelque chose
    """
    windowLength(30, 10)
    print("—" * ((len(form[0]) * 2) + 2))
    """
    Boucle qui parcours les lignes de la forme
    """
    for lines in form:
        """
        Vérification si il y a des 1 dans la ligne
        """
        if 1 in lines:
            print("|", end="")
            """
            boucle qui parcours chaque élément de la ligne
            """
            for element in lines:
                if element == 1:
                    print("■", end=' ')
                else:
                    print(' ', end=' ')
            print('|')
    print("—" * ((len(form[0]) * 2) + 2))


def displayGameMenu(gridMatrix: list, formsMatrix: list, forms: list, states: dict):
    """
    Cette fonction permet l'affichage de la grille avec les coordonnées,
    mais également le Score, Les vies et les formes possibles à placer
    param 1 gridMatrix : Matrice de la grille
    param 2 formsMatrix : Matrice de toutes les formes
    param 3 forms : liste d'entiers choisis aléatoirement correspondant aux 3 formes à afficher
    param states : Dictionnaire d'état du jeu {Score, Lives, EndGame}
    return : Rien
    """
    windowLength(46 + len(gridMatrix[0])*2, 10 + len(gridMatrix))
    print(3 * " ", end=' ')
    for i in range(97, 97 + len(gridMatrix[0]), 1):
        """
        Boucle permettant l'affichage des lettres en haut
        """
        if i > 122:
            i -= 74
        print(chr(i), end=' ')
    print(8 * " " + 12 * "=" + (8 * " " + 12 * "="))
    print(2 * " " + ((len(gridMatrix[0]) + 1) * 2 + 1) * "—", end="")
    print(8 * " " + "Score :", states["Score"], 10 * " " + "Lives :", states["Lives"])
    for i in range(65, 65 + len(gridMatrix), 1):
        """
        Boucle permettant l'affichage des lignes une par une
        """
        if i > 90:
            """
            exception permettant de mettre après le z, 1,2,3,4,5,6,7,8,9
            """
            Y_coords = chr(i-42)
        else:
            Y_coords = chr(i)
        """
        variable qui permet d'afficher seulement la grille avec la coordonnée à gauche
        """
        display = Y_coords + " |" + returnDisplayGridMatrixLine(gridMatrix, i - 65) + " |" + 5 * " "
        if i == 65:
            """
            exception permettant d'afficher display + une partie à droit dessous le score et les vies
            """
            print(display + 2 * " " + 12 * "=" + (8 * " " + 12 * "="))
        elif 66 <= i <= 70:
            """
            exception permettant d'afficher dispay + les formes à placer à droite
            """
            Form1 = returnDisplayFormMatrixLine(formsMatrix, forms[0], i - 66)
            Form2 = returnDisplayFormMatrixLine(formsMatrix, forms[1], i - 66)
            Form3 = returnDisplayFormMatrixLine(formsMatrix, forms[2], i - 66)
            print(display + Form1 + 3 * " " + Form2 + 3 * " " + Form3)
        elif i == 71:
            """
            exception permettant d'afficher display + les chiffres sous les formes pour les identifier
            """
            print(display + 4 * " " + "1" + 12 * " " + "2" + 11 * " " + "3")
        else:
            """
            afficher seulement display si il n'y à rien à mettre à droite 
            """
            print(display)
    print(2 * " " + ((len(gridMatrix[0]) + 1) * 2 + 1) * "—")
