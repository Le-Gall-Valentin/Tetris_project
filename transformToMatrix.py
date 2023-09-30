"""
T'es Trisse
Hugo Leyx-valade | Valentin Le Gall
Ce module 'transformToMatrix.py' permet l'affichage des différents menus dans durant le jeu.
"""


def transformFormsToMatrix(Path: str) -> list:
    """
    Transforme chaque piece d'un fichier donné en matrix 2D puis les range dans une liste contenant toutes les pièces transformées
    :param Path: chaine de caractère, renseigne quel fichier doit ètre utiliser (Exemple: circleForms.txt)
    :return: matrix, renvoie une liste 3D : renvoie une liste contenant toutes les pièces du fichier dans des tableaux 2D
    """
    """
    Ouvre le fichier spécifié par le paramètre form contenant les pièces en 'read'
    """
    with open(Path, "r") as file:
        content = file.readlines()
    """
    Matrix[] : Est la liste 3D retourné contenant toutes les pièces du fichier
    tab2[] : Est une liste temporaire qui contient une pièce utilisé pour remplir Matrix[] 
    """
    matrix = []
    tab2 = []
    """ 
    Lit chaque ligne du fichier  
    """
    for lines in content:
        """
        'if' : Vérifie que la ligne n'est pas vide 
        """
        if lines != '\n':
            """
            tab[] : tableau temporaire corespondant à une ligne d'une piece permetant de remplir tab2[]
            """
            tab = []
            for number in lines:
                """
                'if': vérifie que le caractère est bien un chiffre compris entre 0 et 2
                """
                if (number == '1') or (number == '0') or (number == '2'):
                    tab.append(int(number))
            tab2.append(tab)
            """
            'else' : Si lines = '\n' alors c'est que tab2[] contient une piece entière sous forme de tableau 2D donc on l'ajoute à Matrix[]
            """
        else:
            matrix.append(tab2)
            tab2 = []
    file.close()
    matrix.append(tab2)
    return matrix
