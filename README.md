# Formation Office en ligne

Supports statiques pour GitHub Pages.

URL publique prevue :

https://josselinboullery.github.io/office/

## Parcours en ligne

- `index.html` : portail public racine.
- `FormaPro/00_Index_general/index.html` : index complet de formation.
- `FormaPro/03_Supports_stagiaires_HTML/` : supports Word, Excel, PowerPoint.
- `FormaPro/04_Exercices_HTML/` : exercices.
- `FormaPro/05_Corriges_HTML/` : corriges.
- `FormaPro/07_Fiches_memo_interactives/` : fiches memo.
- `FormaPro/08_Evaluations_HTML/` : evaluations.
- `FormaPro/11_Cartes_SOS_interactives/` : aide rapide.

## Publication

Le workflow `.github/workflows/pages.yml` publie ces fichiers dans la branche `gh-pages` :

- `index.html`
- `.nojekyll`
- `FormaPro/00_Index_general/` a `FormaPro/12_Templates_HTML/`
- `FormaPro/assets/`

Les dossiers sources `Word/`, `Excel/`, `Powerpoint/` et les scripts restent sur `main`, hors site publie.

Si Pages n'est pas encore active dans GitHub :

1. Ouvrir `Settings > Pages`.
2. Choisir `Deploy from a branch`.
3. Choisir `gh-pages` et `/ (root)`.
4. Enregistrer.
