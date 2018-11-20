"""
planches.py
---
Utilise au mieux les planches de la database pour reproduire la forme `x` souhaitée.

Inputs:
    - brep
    - origin
    - direction
    - minWasteLength : Longueur minimale acceptable pour créer une nouvelle chute
    - smallFirst : défini si on trie en priorité de courtes chutes ou des longues chutes
    - DB
    - reuse

    
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

# WIP

import rhinoscriptsyntax as rs

intersection = rs.IntersectBreps(brep, origin)
vertices = rs.PolylineVertices(intersection)

x = [i[0] for i in vertices]
y = [i[1] for i in vertices]

corner1 = [min(x), min(y), 0]
corner2 = [max(x), min(y), 0]
corner3 = [max(x), max(y), 0]
corner4 = [min(x), max(y), 0]

breps = rs.AddPolyline([corner1, corner2, corner3, corner4, corner1])