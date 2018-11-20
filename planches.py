"""
planches.py
---
Utilise au mieux les planches de la database pour reproduire la forme `x` souhaitée.

Inputs:
    - brep
    - origin
    - direction
    - DB
    
Outputs:
    - breps
    - DB
"""

# On filtre les planches disponibles

planchesDispo = [planche for planche in db if planche[4] == True]

# On trie les planches disponibles

if smallFirst:
    planchesDispo.sort(key = lambda planche: planche[0])
else:
    planchesDispo.sort(key = lambda planche: planche[0], reversed=True)

# planches de longueur au moins y : [p for p in planchesDispo if p[0] >= y]
# récupérer la première planche :  p = planchesDispo[0]
# largeur d'une planche p : p[1]