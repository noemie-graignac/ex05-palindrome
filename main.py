#### Fonction secondaire
"""on vérifie si la fonction est un pallindrome"""
def ispalindrome(p):
    """on regarde si c'est un pallindrome"""
    # votre code ici
    a = p.lower()
    a=a.replace(" ", "")
    c=str.maketrans({"é": "e","ê": "e","è": "e","ë": "e","à": "a",
    "?":"","!":"",",": "","'": "",":": "","-": "","ç": "c","ô": "o"})
    a=a.translate(c)
    b = a[::-1]
    return a == b
#### Fonction principale
def main():
    # vos appels à la fonction secondaire ici
    """"on vérifie quelque cas pour voir s'il s'agit d'un pallindrome"""
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))
if __name__ == "__main__":
    main()
