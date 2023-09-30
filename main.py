from Menus import *
from save import existSave, clearSave, returnSavesMatrix, saveGame
"""
T'es Trisse
Hugo Leyx-valade | Valentin Le Gall
Ce module 'main.py' permet d'enclencher le programme
Il va donc vérifier si il y a une sauvegarde, lancer la procédure de récupération, puis
lancer les procédures de créations des grilles et des formes, et pour finir lance le jeu.
C'est également elle qui s'occupe d'arrêter le jeu par manque de vie ou par demande d'arrêt
"""
startMenu()
exist = existSave()
if (exist and not saveMenu()) or (not exist):
    gridMatrix, formsMatrix = setGridMatrixAndForms()
    states = {"Score": 0, "Lives": 3, "EndGame": False}
else:
    gridMatrix, formsMatrix, states = returnSavesMatrix()
clearSave()
while (states["Lives"] > 0) and (not states["EndGame"]):
    gameMenu(gridMatrix, formsMatrix, states)
if states["Lives"] <= 0:
    looseMenu()
elif states["EndGame"]:
    if endSaveMenu():
        saveGame(gridMatrix, formsMatrix, states)
endMenu()
