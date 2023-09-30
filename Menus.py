import time
from os import system
from random import randint
from DisplayGameMenu import windowLength, displayGameMenu, displayFormToRotate
from MutablesGridsMatrix import createDiamondGridMatrix, createTriangleGridMatrix, createCircleGridMatrix
from choices import choiceSave, choiceCoord, choiceFormInMatrix, choiceGrid, choiceLengthGrid, choiceRotate, \
    choiceRules, choiceLanguagesRules
from jsonManage import returnJsonPath
from placePiece import placePiece, rotatePiece
from transformToMatrix import *
"""
T'es Trisse
Hugo Leyx-valade | Valentin Le Gall
Ce module 'Menus.py' permet l'affichage des différents menus dans durant le jeu.
"""


def saveMenu() -> bool:
    """
    Cette fonction affiche le menu de récupération de la sauvegarde.
    :return: boolean nécessaire au main.py
    """
    windowLength(60, 10)
    print(20 * ' ' + 20 * '-')
    print(24 * ' ' + "Resume Game ?")
    print(20 * ' ' + 20 * '-')
    print(20 * " " + "Yes : Y" + 5 * ' ' + "No : N")
    print()
    response = choiceSave()
    if response == "Y":
        return True
    else:
        return False


def endSaveMenu() -> bool:
    """
    Cette fonction affiche le menu de demande de sauvegarde
    :return: boolean nécessaire au main.py
    """
    windowLength(60, 10)
    print(5 * ' ' + 46 * '-')
    print(5 * ' ' + "You have left the game ! Do you want to save ?")
    print(5 * ' ' + 46 * '-')
    print(20 * " " + "Yes : Y" + 5 * ' ' + "No : N")
    print()
    response = choiceSave()
    if response == "Y":
        return True


def endMenu():
    """
    Afficher le message de fin
    :return: Aucun car rien ne le succède
    """
    windowLength(60, 4)
    print(20 * ' ' + 20 * '-')
    print(25 * ' ' + "GoodBye !")
    print(20 * ' ' + 20 * '-')
    time.sleep(3)


def startMenu():
    """
    Afficher le menu de départ avec les choix play et rules
    :return: Aucun
    """
    windowLength(60, 10)
    print(20 * ' ' + 20 * '-')
    print(18 * ' ' + " Welcome in t'es trisse !")
    print(20 * ' ' + 20 * '-')
    print()
    print(18 * " " + "P : Play    |    R : Rules")
    print()
    if choiceRules():
        rulesMenu()


def rulesMenu():
    """
    Affiche le menu de choix entre les langues pour les règles
    :return: Aucun elle ne s'occupe que d'afficher
    """
    windowLength(60, 10)
    question = "In which language do you want to read?"
    print(12 * ' ' + len(question) * '-')
    print(12 * ' ' + question)
    print(12 * ' ' + len(question) * '-')
    print()
    print(16 * " " + "F : French    |    E : English")
    print()
    lang = choiceLanguagesRules()
    if lang == "F":
        pathRules = returnJsonPath("frenchRules")
    else:
        pathRules = returnJsonPath("englishRules")
    windowLength(60, 31)
    displayRules(pathRules)
    system("@pause")


def displayRules(path: str):
    """
    Cette fonction permet d'afficher les règles
    :param path: chemin d'accès des règles
    :return: Aucun, elle ne s'occupe que d'afficher
    """
    with open(path, "r", encoding="utf-8") as ruleFile:
        rules = ruleFile.readlines()
        for i in rules:
            if '\n' in i:
                i = i[:-1]
            print(i)
        ruleFile.close()


def choiceMenu():
    """
    Afficher le menu pour le choix de la grille
    :return: Aucun il ne s'occupe que de l'affichage
    """
    print(20 * ' ' + 20 * '-')
    print(22 * ' ' + "Choose your grid")
    print(20 * ' ' + 20 * '-')
    print()
    print(10 * " " + "Diamond : 1" + 5 * ' ' + "Triangle : 2" + 5 * ' ' + "Circle : 3")
    print()


def setGridMatrixAndForms() -> tuple:
    """
    Cette fonction permet de créer les matrices de la grille et des formes
    :return: un tuple constitué de la matrice de la grille et de la matrice des formes
    """
    windowLength(60, 8)
    choiceMenu()
    numberGrid = choiceGrid()
    length = choiceLengthGrid()
    grid = {1: 'diamondForms', 2: 'triangleForms', 3: 'circleForms'}
    if numberGrid == 1:
        gridMatrix = createDiamondGridMatrix(length)
    elif numberGrid == 2:
        gridMatrix = createTriangleGridMatrix(length)
    else:
        gridMatrix = createCircleGridMatrix(length)
    formsMatrix = transformFormsToMatrix(returnJsonPath(grid[numberGrid]))
    formsMatrix += transformFormsToMatrix(returnJsonPath("commonForms"))
    return gridMatrix, formsMatrix


def gameMenu(gridMatrix: list, formsMatrix: list, states: dict):
    """
    C'est cette fonction qui gère la manche en cours et va lancer toutes les fonctions nécéssaires au jeu
    :param gridMatrix: Matrice de la grille
    :param formsMatrix: Matrice des formes
    :param states: dictionnaire correspondant à l'état du jeu
    :return: Ne renvoi rien
    """
    forms = defineRandomForm(formsMatrix)
    displayGameMenu(gridMatrix, formsMatrix, forms, states)
    choiceForm = choiceFormInMatrix(forms, formsMatrix, states)
    displayFormToRotate(choiceForm)
    while choiceRotate(states):
        rotatePiece(choiceForm)
        displayFormToRotate(choiceForm)
    displayGameMenu(gridMatrix, formsMatrix, forms, states)
    x_coords, y_coords = choiceCoord(len(gridMatrix[0]), len(gridMatrix), states)
    while (placePiece(gridMatrix, formsMatrix, choiceForm, x_coords,
                      y_coords, forms, states) is False) and (states["Lives"] > 0):
        x_coords, y_coords = choiceCoord(len(gridMatrix[0]), len(gridMatrix), states)


def defineRandomForm(formsMatrix):
    """
    Définit 3 fomres aléatoires parmis la Matrice des formes
    :param formsMatrix: Matrice des formes
    :return: un tuple contenant l'indice des 3 formes dans la matrice de formes
    """
    forms = [None] * 3
    for i in range(0, len(forms)):
        form = randint(0, len(formsMatrix) - 1)
        while form in forms:
            form = randint(0, len(formsMatrix) - 1)
        forms[i] = form
    return forms


def looseMenu():
    """
    Afficher le menu de défaite
    :return: Rien elle ne s'occupe que de l'affichage
    """
    windowLength(60, 4)
    print(20 * ' ' + 20 * '-')
    print(22 * ' ' + " You Loose !")
    print(20 * ' ' + 20 * '-')
    time.sleep(5)
