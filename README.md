#  Modélisation de l'incertitude des Tiplines de Failles

# Présentation du Projet
Ce projet développe une méthodologie statistique pour detecter,quantifier et visualiser l'incertitude géométrique des failles, en se focalisant sur les **tiplines** (lignes de terminaison). 

L'approche combine :
- Les **lois d'échelle physiques** (d = \gamma L) basées sur Cowie & Scholz (1992).
- Des simulations stochastiques de **Monte Carlo** pour générer des populations de failles.
- La **Théorie de l'Information (Entropie de Shannon)** pour piloter un remaillage adaptatif 3D des zones de forte incertitude.

##  Planning du Stage (4 Mois)
1. **Mois 1 : Fondations & Générateur** - Développement du `FaultGenerator` et validation statistique (Krantz, 1988).
2. **Mois 2 : Modélisation Incertitude (MCUE)** - Implémentation Monte Carlo et calcul de l'entropie.
3. **Mois 3 : Remaillage ** - Algorithmes de raffinement de maillage avec PyVista.
4. **Mois 4 : Validation & Rédaction** - Application sur cas d'étude réel et rapport final.

##  Structure du Projet
```text
.
├── code/                # Scripts Python (Générateur, MCUE, Meshing)
├── data/                # Données brutes (raw) et traitées (processed)
├── docs/                # Méthodologie et documentation technique
├── papers_notes/        # Fiches de lecture (Cowie & Scholz, Krajnovich)
└── results/             # Figures 3D et rapports de validation

## Références Clés
Cowie & Scholz (1992) : Relation Déplacement-Longueur.

Krajnovich et al. (2020) : MCUE pour les failles géologiques.

Pakyuz-Charrier et al. (2018) : Entropie de Shannon appliquée à la géologie.
