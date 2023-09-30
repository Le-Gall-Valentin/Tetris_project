from json import load
"""
T'es Trisse
Hugo Leyx-valade | Valentin Le Gall
Ce module 'jsonManage.py' contient une fonction lié aux fichiers .json
"""


def returnJsonPath(key: str) -> str:
    """
    Permet de renvoyer le chemin d'accès qui est stocké dans un fichier json
    :param key: Clé du dictionnaire dans le chier json
    :return: le chemin d'accès dans le fichier json
    """
    with open("assets/Paths.json", "r") as testJsonFile:
        data = load(testJsonFile)
        testJsonFile.close()
        return data[key]
