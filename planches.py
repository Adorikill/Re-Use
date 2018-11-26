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

# On créé une BoundingBox autour du Brep en input; ca permet de definir une origine absolue pour n'importe quelle forme et de construire les planches imaginaires à recouper avec la DB

for brep

brep = brep #On récupère l'input brep
if brep:
    box = rs.boundingBox(brep)
        if box:
        for point[0] in enumerate(box)
        breps = rs.AddBox(point[]) #(C'est pas bon mais l'idée c'est de pouvoir avoir la bounding box construite pour la voir sur l'output 'breps')

#TROUVER LE CODE POUR : 

# PREMIERE PARTIE :
#STOCKER QQ PART L'AIRE DE LA BOUNDING BOX
#TESTER UN ROTATE DU BREP POUR VOIR SI ON PEUT AVOIR UNE PLUS PETITE BOUNDING BOX
#SI OUI, ON RESTOCKE QQ PART LA NOUVELLE DONNEE, ET ON LA COMPARE POUR UN ENSEMBLE DE ROTATE SUR 360° (loop sur l'ensemble des 360° pour trouver la meilleure orientation)
#ON CONSERVE LA PLUS PETITE BOUNDING BOX =>>> ALGO DE TRI OU ON GARDE LA PLUS PETITE DATA ? 

# DEUXIEME PARTIE : 
#ON UTILISE LA LARGEUR DE LA PREMIERE PLANCHE TRIEE DANS L'ALGO POUR EN CREER UNE ARRTIFICIELLE SUR ymax (boundingBox); ON TESTE LES INTERSECTIONS AVEC LE BREP D'ORIGINE
#ON COMPARE LES DIMENSIONS DU RECTANGLE OBTENU AVEC LES INTERSECTIONS AVEC LA PREMIERE PLANCHE DE LA DB; SI ELLE EST ASSEZ LONGUE, ON LA GARDE, SINON ON ESSAYE AVEC UNE AUTRE PLANCHE
#  


for surface 

import rhinoscriptsyntax as rs # Permet d'importer des fonctions depuis rhino

intersection = rs.IntersectBreps(brep, origin) # Avec ['brep' = la forme à créer] et ['origin' = la database de planches] 
vertices = rs.PolylineVertices(intersection)

x = [i[0] for i in vertices]
y = [i[1] for i in vertices]

corner1 = [min(x), min(y), 0]
corner2 = [max(x), min(y), 0]
corner3 = [max(x), max(y), 0]
corner4 = [min(x), max(y), 0] 
           
breps = rs.AddPolyline([corner1, corner2, corner3, corner4, corner1])

