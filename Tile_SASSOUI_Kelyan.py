#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 13:29:31 2026

@author: ksassoui
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


# affiche une suite de points reliés entre eux
def visu_point(matPoint, style):
    x = matPoint[0, :]
    y = matPoint[1, :]

    # on trace avec une grosse épaisseur pour donner un effet de trait
    plt.plot(
        x, y, style,
        linewidth=12,
        solid_capstyle='round',
        solid_joinstyle='round'
    )


# trace un segment entre deux points
def visu_segment(P1, P2, style):
    # on regroupe les deux points dans une seule matrice
    matP = np.concatenate((P1, P2), 1)
    visu_point(matP, style)


# crée une matrice de rotation
def mat_rotation(theta):
    # theta est l’angle de rotation en radians
    mat = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    return mat


# trace une courbe de Bézier cubique avec 4 points de contrôle
def visu_BezierCubique(matPointControl, style):
    n = 120  # nombre de points utilisés pour dessiner la courbe

    # t varie de 0 à 1 pour parcourir toute la courbe
    t = np.linspace(0, 1., n)

    # matrice contenant 1, t, t² et t³
    mat_t = np.ones((4, n))
    mat_t[1, :] = t
    mat_t[2, :] = t * t
    mat_t[3, :] = t * t * t

    # matrice de Bézier cubique
    matBezier4 = np.array([
        [1, 0, 0, 0],
        [-3, 3, 0, 0],
        [3, -6, 3, 0],
        [-1, 3, -3, 1]
    ])

    # calcul des coordonnées des points de la courbe
    matPointligne = (mat_t.T @ matBezier4) @ matPointControl.T
    matPoint = matPointligne.T

    visu_point(matPoint, style)


# fonction plus simple pour tracer une courbe avec 4 points
def courbe(P0, P1, P2, P3):
    # on transforme les 4 points en matrice de contrôle
    mat = np.column_stack((P0, P1, P2, P3))
    visu_BezierCubique(mat, 'k-')


# affiche un point en forme de losange
def point(x, y, taille=12):
    plt.plot(
        x, y,
        marker='D',
        color='black',
        markersize=taille
    )


# dessine le cadre carré d’une tuile
def dessiner_tuile():
    x = [-1, 11, 11, -1, -1]
    y = [-1, -1, 11, 11, -1]

    plt.plot(x, y, 'k-', linewidth=3)


# règle l’affichage de chaque tuile
def reglage_tuile():
    plt.xlim(-2, 12)
    plt.ylim(-2, 12)

    # garde les mêmes proportions et enlève les axes
    plt.axis('equal')
    plt.axis('off')


def lettre_ra():

    # grande courbe qui forme le corps du ra
    P0 = np.array([6.8, 8.6])
    P1 = np.array([8.2, 6.2])
    P2 = np.array([6.6, 3.0])
    P3 = np.array([3.2, 2.0])
    courbe(P0, P1, P2, P3)

    # petit prolongement en bas vers la gauche
    P0 = np.array([3.2, 2.0])
    P1 = np.array([2.4, 1.8])
    P2 = np.array([1.8, 2.1])
    P3 = np.array([1.2, 2.4])
    courbe(P0, P1, P2, P3)


def lettre_lam():

    # trait vertical principal de la lettre
    P0 = np.array([7.0, 9.5])
    P1 = np.array([7.1, 7.0])
    P2 = np.array([7.2, 4.5])
    P3 = np.array([7.0, 2.3])
    courbe(P0, P1, P2, P3)

    # partie arrondie du bas
    P0 = np.array([7.0, 2.3])
    P1 = np.array([6.7, 0.8])
    P2 = np.array([3.0, 0.8])
    P3 = np.array([2.2, 2.0])
    courbe(P0, P1, P2, P3)

    # remontée sur la gauche après l’arrondi
    P0 = np.array([2.2, 2.0])
    P1 = np.array([1.9, 2.6])
    P2 = np.array([2.1, 3.6])
    P3 = np.array([2.8, 4.6])
    courbe(P0, P1, P2, P3)

    # petit arrondi en haut pour éviter une fin trop pointue
    P0 = np.array([7.0, 9.5])
    P1 = np.array([6.8, 9.8])
    P2 = np.array([6.9, 10.0])
    P3 = np.array([7.1, 9.7])
    courbe(P0, P1, P2, P3)


def lettre_ba():

    # courbe principale du ba
    P0 = np.array([1.8, 5.8])
    P1 = np.array([1.0, 2.8])
    P2 = np.array([7.0, 2.8])
    P3 = np.array([8.5, 5.8])
    courbe(P0, P1, P2, P3)

    # petite pointe à droite
    P0 = np.array([8.5, 5.8])
    P1 = np.array([8.8, 6.4])
    P2 = np.array([8.6, 7.0])
    P3 = np.array([8.0, 7.6])
    courbe(P0, P1, P2, P3)

    # point sous la lettre
    point(6, 1.8, 10)


def lettre_mim():

    # partie arrondie du haut
    P0 = np.array([4.0, 6.8])
    P1 = np.array([4.5, 8.5])
    P2 = np.array([6.7, 8.5])
    P3 = np.array([7.2, 6.6])
    courbe(P0, P1, P2, P3)

    # retour intérieur pour donner la forme du mim
    P0 = np.array([7.2, 6.6])
    P1 = np.array([6.0, 6.9])
    P2 = np.array([4.8, 6.6])
    P3 = np.array([4.1, 5.8])
    courbe(P0, P1, P2, P3)

    # début de la descente
    P0 = np.array([4.1, 5.8])
    P1 = np.array([3.5, 4.8])
    P2 = np.array([3.6, 3.4])
    P3 = np.array([3.9, 2.2])
    courbe(P0, P1, P2, P3)

    # fin de la descente vers le bas
    P0 = np.array([3.9, 2.2])
    P1 = np.array([4.1, 1.4])
    P2 = np.array([4.3, 0.8])
    P3 = np.array([4.5, 0.3])
    courbe(P0, P1, P2, P3)


def lettre_qaf():

    # grande base arrondie du qaf
    P0 = np.array([2.0, 5.4])
    P1 = np.array([1.2, 1.2])
    P2 = np.array([7.8, 1.0])
    P3 = np.array([8.0, 4.4])
    courbe(P0, P1, P2, P3)

    # montée vers la partie du haut
    P0 = np.array([8.0, 4.4])
    P1 = np.array([8.4, 5.8])
    P2 = np.array([8.1, 7.4])
    P3 = np.array([6.6, 7.5])
    courbe(P0, P1, P2, P3)

    # côté gauche de la tête
    P0 = np.array([6.6, 7.5])
    P1 = np.array([5.0, 7.5])
    P2 = np.array([4.8, 5.2])
    P3 = np.array([6.2, 4.8])
    courbe(P0, P1, P2, P3)

    # fermeture de la tête vers la droite
    P0 = np.array([6.2, 4.8])
    P1 = np.array([6.8, 4.6])
    P2 = np.array([7.5, 4.3])
    P3 = np.array([8.0, 4.4])
    courbe(P0, P1, P2, P3)

    # les deux points du qaf
    point(5.0, 8.5)
    point(6.3, 8.9)


def lettre_ain():

    dy = -1  # permet de descendre toute la lettre sans changer tous les points

    # tête du ain
    P0 = np.array([5.5, 8.5 + dy])
    P1 = np.array([4.0, 9.0 + dy])
    P2 = np.array([3.0, 7.5 + dy])
    P3 = np.array([4.2, 6.8 + dy])
    courbe(P0, P1, P2, P3)

    # petite branche vers la droite
    P0 = np.array([4.4, 6.6 + dy])
    P1 = np.array([4.9, 6.8 + dy])
    P2 = np.array([5.3, 7.0 + dy])
    P3 = np.array([5.7, 7.3 + dy])
    courbe(P0, P1, P2, P3)

    # liaison entre le haut et le bas
    P0 = np.array([4.2, 6.8 + dy])
    P1 = np.array([3.0, 5.5 + dy])
    P2 = np.array([2.8, 4.0 + dy])
    P3 = np.array([3.2, 2.8 + dy])
    courbe(P0, P1, P2, P3)

    # partie basse arrondie
    P0 = np.array([3.2, 2.8 + dy])
    P1 = np.array([4.0, 1.5 + dy])
    P2 = np.array([5.2, 1.4 + dy])
    P3 = np.array([6.3, 2.0 + dy])
    courbe(P0, P1, P2, P3)


def lettre_sin():

    # grande courbe basse de la lettre
    P0 = np.array([1.2, 5.0])
    P1 = np.array([0.8, 1.2])
    P2 = np.array([5.6, 1.2])
    P3 = np.array([6.3, 4.0])
    courbe(P0, P1, P2, P3)

    # transition vers les dents du sin
    P0 = np.array([6.3, 4.0])
    P1 = np.array([6.6, 5.2])
    P2 = np.array([6.2, 6.2])
    P3 = np.array([5.8, 6.8])
    courbe(P0, P1, P2, P3)

    # dent du milieu
    P0 = np.array([5.8, 6.8])
    P1 = np.array([6.4, 5.0])
    P2 = np.array([7.4, 5.0])
    P3 = np.array([7.9, 6.7])
    courbe(P0, P1, P2, P3)

    # dent de droite
    P0 = np.array([7.9, 6.7])
    P1 = np.array([8.0, 5.2])
    P2 = np.array([8.9, 5.0])
    P3 = np.array([9.2, 6.5])
    courbe(P0, P1, P2, P3)


def lettre_taa():

    dy = -1  # décale la lettre vers le bas

    # première partie de la boucle
    P0 = np.array([4.8, 3.4 + dy])
    P1 = np.array([6.0, 5.4 + dy])
    P2 = np.array([8.2, 6.6 + dy])
    P3 = np.array([8.0, 4.5 + dy])
    courbe(P0, P1, P2, P3)

    # prolongement de la boucle vers la gauche
    P0 = np.array([8.0, 4.5 + dy])
    P1 = np.array([7.8, 3.0 + dy])
    P2 = np.array([5.0, 2.6 + dy])
    P3 = np.array([2.5, 3.5 + dy])
    courbe(P0, P1, P2, P3)

    # petite fin de trait à gauche
    P0 = np.array([2.5, 3.5 + dy])
    P1 = np.array([2.8, 3.2 + dy])
    P2 = np.array([3.2, 3.1 + dy])
    P3 = np.array([3.8, 3.2 + dy])
    courbe(P0, P1, P2, P3)

    # tige verticale dessinée avec un segment simple
    A = np.array([[4.8], [3.4 + dy]])
    B = np.array([[4.7], [8.8 + dy]])
    visu_segment(A, B, 'k-')

    # petit arrondi en haut de la tige
    P0 = np.array([4.6, 8.8 + dy])
    P1 = np.array([4.9, 9.3 + dy])
    P2 = np.array([5.1, 8.8 + dy])
    P3 = np.array([4.8, 8.4 + dy])
    courbe(P0, P1, P2, P3)


def lettre_ya():

    # grande courbe basse du ya
    P0 = np.array([1.6, 5.6])
    P1 = np.array([0.8, 1.0])
    P2 = np.array([7.0, 0.8])
    P3 = np.array([8.4, 3.5])
    courbe(P0, P1, P2, P3)

    # remontée sur la droite
    P0 = np.array([8.4, 3.5])
    P1 = np.array([9.2, 5.0])
    P2 = np.array([6.6, 5.1])
    P3 = np.array([6.0, 6.4])
    courbe(P0, P1, P2, P3)

    # partie haute de la lettre
    P0 = np.array([6.0, 6.4])
    P1 = np.array([6.8, 8.5])
    P2 = np.array([9.0, 8.8])
    P3 = np.array([8.8, 7.0])
    courbe(P0, P1, P2, P3)

    # les deux points sous le ya
    point(4.2, 0.2, 10)
    point(5.6, 0.2, 10)


# liste des lettres à afficher avec leur nom
lettres = [
    (lettre_ra, "ra"),
    (lettre_lam, "lam"),
    (lettre_ba, "ba"),
    (lettre_mim, "mim"),
    (lettre_qaf, "qaf"),
    (lettre_ain, "ain"),
    (lettre_sin, "sin"),
    (lettre_taa, "taa"),
    (lettre_ya, "ya")
]


# création de la fenêtre d’affichage
plt.figure(figsize=(16, 16))


# on parcourt toutes les lettres pour les afficher dans une grille
for i in range(len(lettres)):

    fonction, titre = lettres[i]

    # grille de 3 lignes et 3 colonnes
    plt.subplot(3, 3, i + 1)

    dessiner_tuile()

    # appel de la fonction qui dessine la lettre
    fonction()

    reglage_tuile()

    # affiche le nom de la lettre dans la tuile
    plt.text(
        5,
        10,
        titre,
        ha='center',
        va='center',
        fontsize=14,
        fontweight='bold'
    )


# espace entre les tuiles
plt.subplots_adjust(
    left=0.05,
    right=0.95,
    bottom=0.05,
    top=0.95,
    wspace=0.35,
    hspace=0.35
)

plt.show()