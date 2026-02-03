#--1-- Cowie & Scholz (1992) - Displacement-Length Scaling

##  Métadonnées
- **Titre complet** : Displacement-length scaling relationship for faults: data synthesis and discussion
- **Auteurs** : Patience A. Cowie, Christopher H. Scholz
- **Institution** : Lamont-Doherty Geological Observatory, Columbia University
- **Journal** : Journal of Structural Geology
- **Volume/Pages** : Vol. 14, No. 10, pp. 1149-1156
- **Année** : 1992
- **PDF** : `papers/cowie_rapport.pdf`
- **Résumé Word** : `notes/cowie_scholz_1992_resume.docx`
- **Date de lecture** : 02/02/2026 

---

##  Question de Recherche

**Question principale** : 
Quelle est la forme exacte de la relation entre le déplacement (d) et la longueur (L) d'une faille ?

**Débat existant** :
- **Linéaire** : d = γL (Cowie & Scholz, Elliott, Krantz, etc.)
- **Quadratique** : d ∝ L² (Walsh & Watterson 1988)
- **Puissance 1.5** : d ∝ L^1.5 (Marrett & Allmendinger 1991)

**Conclusion de Cowie & Scholz** : 
 **Relation LINÉAIRE privilégiée** avec γ variable selon la lithologie,La résistance de la roche,Le module de cisaillement,La friction.


---

##  Résultats Clés de Cowie & Scholz

### 1. Relation Linéaire Préférée
```
d = γL

où γ = ratio D/L (constante pour un dataset donné)
```

**Arguments** :
- Chaque dataset individuel montre linéarité
- Variance augmente avec fit non-linéaire (7/9 cas, Tableau 1)
- Base physique solide (voir Équation 2)

### 2. γ Varie Selon Lithologie & Contexte
- **Pas de loi universelle** !
- γ dépend des propriétés de la roche



##  Équations Importantes

### Équation (1) - Modèle Walsh & Watterson
```
d = L² / P

où P = variable liée aux propriétés de la roche
```
**Problème** : Pas de base physique claire

### **Équation (2) - Modèle Cowie & Scholz** 
```
d = C[(τ₀ - τf)/μ]L

où :
- τ₀ = résistance au cisaillement de la roche
- τf = contrainte de friction sur la faille  
- μ = module de cisaillement
- C = constante (rapport stress/résistance)
```

**Implication** :
```
γ = d/L = C[(τ₀ - τf)/μ]

γ dépend des propriétés mécaniques !
→ Chaque lithologie a son γ
```
**Observation** : γ varie de **0.001 à 0.1** selon contexte !

---
##  Tableau 1 (Récapitulatif)

| Dataset | Type | γ (×10⁻²) | Échelle L | Lithologie |
|---------|------|-----------|-----------|------------|
| Elliott | Inverse | 6.0 | 10-500 km | Paléozoïque |
| **Krantz**  | **Normale** | **0.7** | **0.2-5 km** | **Grès Navajo** |
| Walsh & W. | Normale | 0.6 | 0.5-5 km | Charbon |
| Peacock & S. | Normale | 0.9 | 5-30 m | Calcaire |
| Peacock | Décroch. | 1.5 | <10 m | Graywacke |
| Villemin | Normale | 2.9 | 1-30 km | Charbon |
| Muraoka | Normale | 1.2 | <1 m | Sédiments |
| Opheim | Normale | 0.12 | <3 km | Basalte |
| MacMillan | Décroch. | 17.0 | 100-2000 km | Variable 

## Application à Mon Projet

### Pour le Générateur (Mois 1)
```python
# Paramètres Krantz (1988) à utiliser
gamma_mean = 0.007  # 7×10⁻³
gamma_std = 0.002   # Pour scatter réaliste (±30%)

# Relation
d = gamma * L

# Distribution longueurs
L_min = 200  # m
L_max = 5000  # m
L_median = 1800  # m (log-normale)
```

### Calcul Position Tipline
```
Si d_centre = 10 m connu
→ L = d_centre / gamma = 10 / 0.007 = 1428 m

Tiplines :
  tipline1 = centre - L/2 = centre - 714 m
  tipline2 = centre + L/2 = centre + 714 m
```

### Scatter Réaliste (Mois 2)
- Variabilité naturelle γ : ±0.002
- Scatter multiplicatif : facteur 1.5-2.0
- Sources : lithologie, interaction, mesure

### Modèle Physique
```python
# Équation (2) de Cowie & Scholz
def calculate_gamma(tau_0, tau_f, mu, C):
    """
    Calcule γ selon propriétés roche
    """
    return C * (tau_0 - tau_f) / mu
```

---
##  Questions Ouvertes 

1. **Effet lithologie sur γ** :
   - Comment quantifier précisément ?
   - Lien avec module Young, Poisson ?

2. **Tiplines 3D** :
   - Form elliptique → γ différent selon direction ?
   - Comment modéliser en 3D ?


---

##  Notes Personnelles

### Compréhension Générale
 **Très clair** : Relation d = γL pour failles bornées
 **Compris** : γ varie selon lithologie (0.001-0.1)
 **Compris** : Scatter naturel facteur 1.5-2.0
 **À clarifier** : Détails modèle physique (Équation 2)

### Points Forts Article
- Compilation exhaustive 9 datasets
- Discussion honnête des limites
- Base physique solide (mécanique rupture)
- Tableau 1 très utile (valeurs γ)

### Points Faibles
- Figure 1(b) Krantz : pas de tableau numérique (à digitaliser !)
- Modèle Équation (2) : paramètres difficiles à estimer
- Cross-over petit/grand : pas assez de données

### Liens avec Projet
 **Mois 1** : Utiliser γ=0.007 pour générateur
 **Mois 2** : Modéliser scatter avec σ_γ=0.002
 **Mois 3** : Tiplines = zones où d→0 (incertitude max)
 **Mois 4** : Valider contre Krantz (1988) données

---
