"""
T'es Trisse
Hugo Leyx-valade | Valentin Le Gall
Ce module 'displayMatrix.py' permet de renvoyer l'affichage des lignes
des formes et de la grille pour les envoyer à la fonction displayGameMenu.
"""


def returnDisplayFormMatrixLine(content: list, form: int, line: int) -> str:
    """
    Cette fonction permet de renvoyer l'affichage d'une ligne d'une forme
    :param content: liste correspondant ici à la matrice des formes
    :param form: entier correspondant à la forme dans la matrice
    :param line: ligne que l'on veut récupérer
    :return: chaine de caractères correspondant à l'affichage de la ligne d'une forme.
    """
    display = ''
    if len(content[form]) > line:
        for number in content[form][line]:
            if number == 1:
                display += "■" + " "
            else:
                display += "  "
    else:
        display += " " * (len(content[form][0])*2)
    display += " " * (5 - len(content[form][0]))
    return display


def returnDisplayGridMatrixLine(content: list, line: int) -> str:
    """
    Fonction permettant de renvoyer l'affichage d'une ligne dans la grille
    :param content: liste correspondant ici à la Matrice de la grille
    :param line: Ligne que l'on veut récupérer
    :return: chaine de caractères correspondant à l'affichage de la ligne de la grille.
    """
    display = ''
    for number in content[line]:
        if number == 1:
            display += " ."
        elif number == 0:
            display += "  "
        else:
            display += ' ' + "■"
    return display
