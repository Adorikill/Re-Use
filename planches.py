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

import rhinoscriptsyntax as rs # Permet d'importer des fonctions depuis rhino; pour Dynamo, trouver le SDK

intersection = rs.IntersectBreps(brep, origin) # Avec 'brep' = la forme à créer et 'origin' = la database de planches 
vertices = rs.PolylineVertices(intersection)

x = [i[0] for i in vertices]
y = [i[1] for i in vertices]

corner1 = [min(x), min(y), 0]
corner2 = [max(x), min(y), 0]
corner3 = [max(x), max(y), 0]
corner4 = [min(x), max(y), 0] # Pb avec le positionement de la planche; si on la place à partir de l'origine (point) du brep à observer, on rate une intersection 
                              # (x max) dans le cas ou on aurait à observer un quadrilatère sans angle droit ni parallèles (ou juste si l'un des cotés du quadrilatère 
                              # n'est pas parallèle au vecteur x de l'origine)
                              # RESOLUTION : TOURNER LA FORME ? 

# Verifier si le vecteur résultant de 'corner3 = [max(x), max(y), 0]' et corner2 = [max(x), min(y), 0]' a deux intersections (avec le brep à observer);
# Si = true, alors on passe à l'étape d'après
# Si = false, alors on doit prolonger le vecteur jusqu'à une intersection avec le brep (en corner2 [max(x), min(y), 0]) et créer une nouvelle surface à remplir

# Comparer la surface obtenue qui fait [corners1, corner2, corner3, corner 4] avec la database pour vérifier si y'a un recoupement avec le max(y) et la planche qu'on veut utiliser

# Check si on peut la couper et créer une chute selon les parmaètres en minWasteLength;
# Si = true, alors on la coupe et stocke provisoirement la chute créée 'C'
# Si = false, on essaye avec la prochaine planche de la liste jusqu'à ce que ce soit =true

# On répète l'opération pour remplir le brep

           # PB: que se passe-t-il quand on arrive au bout du brep et qu'il reste un angle contenu dans une poutre ? 
           # 
           
breps = rs.AddPolyline([corner1, corner2, corner3, corner4, corner1])

