import json
import os

"""
T'es Trisse
Hugo Leyx-valade | Valentin Le Gall
Ce module 'transformToMatrix.py' permet l'affichage des différents menus dans durant le jeu.
"""


def saveGame(gridMatrix: list, formsMatrix: list, states: dict):
    """
    Sauvegarde la partie en cours dans un fichier crée au moment de la sauvegarde sous forme .JSON
    :param 1 gridMatrix: Grille de jeu actuel (avec les piece placées)
    :param 2 formsMatrix: Matrice des formes utilisés
    :param 3 states: dictionnaire contenant l'état de la partie
    :return: Ne retourne rien car on modifie le fichier json nous n'avons donc pas besoin de retourner quelque chose
    """
    """
    Dictionnaire contenant toutes les valeurs ou matrices à sauvegarder
    """
    saveJsonForm = {"gridMatrix": gridMatrix, "formsMatrix": formsMatrix,
                    "Score": states["Score"], "Lives": states["Lives"]}
    """
    Crée et ouvre un fichier sous format json en 'write' afin d'enregistrer saveJsonForm 
    """
    with open("assets/Save.json", "w") as saveFile:
        json.dump(saveJsonForm, saveFile)
        saveFile.close()


def existSave() -> bool:
    """
    Vérifie si une sauvegarde est déjà existante
    :return: Retourne True si le fichier est déjà existant False sinon
    """
    if os.path.exists('assets/Save.json'):
        return True
    else:
        return False


def clearSave():
    """
    Supprime la sauvegarde si elle existe
    :return: Rien car l'on supprime un fichier
    """
    if existSave():
        os.remove('assets/Save.json')


def returnSavesMatrix() -> tuple:
    """
    Renvoi les informations de la sauvegarde en .json
    :return: tuple contenant les informations de la sauvegarde
    """
    with open("assets/Save.json", "r") as saveFile:
        saveDict = json.load(saveFile)
        states = {"Score": saveDict["Score"], "Lives": saveDict["Lives"], 'EndGame': False}
        saveFile.close()
        return saveDict["gridMatrix"], saveDict["formsMatrix"], states

