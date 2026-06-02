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

Le workflow `.github/workflows/pages.yml` publie uniquement :

- `index.html`
- `.nojekyll`
- `FormaPro/`

Les dossiers sources `Word/`, `Excel/`, `Powerpoint/` et les scripts restent dans le repo, hors site publie.

Si Pages n'est pas encore active dans GitHub :

1. Ouvrir `Settings > Pages`.
2. Choisir `GitHub Actions` comme source.
3. Relancer `Deploy course supports` dans l'onglet Actions si besoin.
