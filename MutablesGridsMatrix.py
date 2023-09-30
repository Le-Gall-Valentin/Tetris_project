from math import sqrt
"""
T'es Trisse
Hugo Leyx-valade | Valentin Le Gall
Ce module 'MutableGridsMatrix.py' permet l'affichage des différents menus dans durant le jeu.
"""


def createCircleGridMatrix(long: int) -> list:
    """
    Crée une grille en forme de cercle de taille (long) grace au théorème de Pythagore
    :param long: entier, c'est la taille en longueur et largeur de la grille
    :return: liste, renvoie une liste 2D représentant la grille Cercle
    """
    rayon = long//2+1
    gridMatrix = []
    for i in range(-(rayon-1), rayon, 1):
        temp = []
        for j in range(-(rayon-1), rayon, 1):
            if sqrt((i**2) + j**2) <= rayon:
                temp.append(1)
            else:
                temp.append(0)
        gridMatrix.append(temp)
    return gridMatrix


def createDiamondGridMatrix(long: int) -> list:
    """
    Crée une grille en forme de losange de taille (long)
    :param long: entier, C'est la taille en longueur et largeur de la grille
    :return: liste, Renvoie une liste 2D représentant la grille diamant
    """
    gridMatrix = list()
    pas = 0
    for i in range(long):
        gridMatrix.append([1]*long)
        for j in range(0, long//2 - pas, 1):
            gridMatrix[i][-j-1] = 0
            gridMatrix[i][j] = 0
        if i < (long//2):
            pas += 1
        else:
            pas -= 1
    return gridMatrix


def createTriangleGridMatrix(long: int) -> list:
    """
    Crée une grille en forme de triangle de taille (long)
    :param long: entier, C'est la taille en longueur et largeur de la grille
    :return: liste, Renvoie une liste 2D représentant la grille triangle
    """
    gridMatrix = []
    for i in range((long//2) + 1):
        gridMatrix.append([1]*long)
        for j in range((long//2) - i):
            gridMatrix[i][-j-1] = 0
            gridMatrix[i][j] = 0
    return gridMatrix


