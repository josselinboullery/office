# Style guide - Kit Horizon Compétences Office débutant

Phase : 2 - Création du design system

## Objectif

Définir les règles visuelles, ergonomiques et techniques communes aux futurs fichiers HTML standalone du kit Horizon Compétences.

Ce guide servira de base à la phase 3 pour créer les templates HTML. Il ne crée pas encore de page finale.

## Principes de design

- Interface claire, sobre et rassurante.
- Lecture confortable pour grands débutants.
- Navigation simple et visible.
- Boutons larges, explicites, faciles à cliquer.
- Contenus courts, aérés, structurés en blocs.
- Aucune information portée uniquement par la couleur.
- Pas de logo Microsoft, pas de copie d'interface protégée.
- Pas de CDN, pas de police distante, pas de dépendance externe.

## Typographie

Police recommandée :

```css
font-family: "Segoe UI", Arial, sans-serif;
```

Tailles recommandées :

```css
--text-xs: 0.82rem;
--text-sm: 0.95rem;
--text-md: 1rem;
--text-lg: 1.15rem;
--text-xl: 1.45rem;
--text-2xl: 1.85rem;
--text-3xl: 2.35rem;
```

Règles :

- Corps de texte : 16 px minimum.
- Interligne : 1.55 à 1.7.
- Titres courts et explicites.
- Paragraphes courts.
- Pas de texte justifié.

## Espacements

Échelle recommandée :

```css
--space-1: 0.25rem;
--space-2: 0.5rem;
--space-3: 0.75rem;
--space-4: 1rem;
--space-5: 1.5rem;
--space-6: 2rem;
--space-7: 3rem;
```

Règles :

- Largeur de contenu : 1100 px maximum.
- Marges latérales mobiles : 16 px minimum.
- Cartes séparées par 16 à 24 px.
- Sections longues découpées en sous-blocs.

## Rayons, ombres, bordures

```css
--radius-sm: 4px;
--radius-md: 8px;
--radius-lg: 12px;
--border-soft: 1px solid #E5E7EB;
--shadow-soft: 0 8px 24px rgba(15, 23, 42, 0.08);
```

Usage :

- Cartes : rayon 8 px.
- Boutons : rayon 8 px.
- Encadrés : bordure gauche épaisse + fond clair.
- Ombres légères seulement pour hiérarchie.

## Couleurs générales

### Général / formateur

```css
--general-primary: #334155;
--general-secondary: #1F2937;
--general-accent: #64748B;
--general-bg: #F8FAFC;
--general-text: #111827;
```

Usage :

- Index général.
- Vue d'ensemble.
- Guide formateur général.
- Évaluations.
- Rapport.
- Documents transversaux.

### Word

```css
--word-primary: #185ABD;
--word-secondary: #2B579A;
--word-accent: #41A5EE;
--word-bg: #F3F7FF;
--word-text: #1F2937;
```

Usage :

- Supports Word.
- Exercices Word.
- Corrigés Word.
- Fiches mémo Word.
- Sections rédaction, document, mise en page.

### Excel

```css
--excel-primary: #107C41;
--excel-secondary: #217346;
--excel-accent: #33C481;
--excel-bg: #F1FAF5;
--excel-text: #1F2937;
```

Usage :

- Supports Excel.
- Exercices Excel.
- Corrigés Excel.
- Fiches mémo Excel.
- Sections tableau, calcul, graphique, données.

### PowerPoint

```css
--powerpoint-primary: #C43E1C;
--powerpoint-secondary: #D24726;
--powerpoint-accent: #F0643B;
--powerpoint-bg: #FFF4F0;
--powerpoint-text: #1F2937;
```

Usage :

- Supports PowerPoint.
- Exercices PowerPoint.
- Corrigés PowerPoint.
- Fiches mémo PowerPoint.
- Sections diapositive, visuel, prise de parole.

## Variables de thème recommandées

Les futurs templates doivent utiliser des variables génériques alimentées par la classe de thème.

```css
:root {
  --color-primary: #334155;
  --color-secondary: #1F2937;
  --color-accent: #64748B;
  --color-bg-soft: #F8FAFC;
  --color-text: #111827;
  --color-card: #FFFFFF;
  --color-border: #E5E7EB;
  --color-success: #15803D;
  --color-warning: #B45309;
  --color-danger: #B91C1C;
  --color-info: #1D4ED8;
}

.theme-general {
  --color-primary: #334155;
  --color-secondary: #1F2937;
  --color-accent: #64748B;
  --color-bg-soft: #F8FAFC;
  --color-text: #111827;
}

.theme-word {
  --color-primary: #185ABD;
  --color-secondary: #2B579A;
  --color-accent: #41A5EE;
  --color-bg-soft: #F3F7FF;
  --color-text: #1F2937;
}

.theme-excel {
  --color-primary: #107C41;
  --color-secondary: #217346;
  --color-accent: #33C481;
  --color-bg-soft: #F1FAF5;
  --color-text: #1F2937;
}

.theme-powerpoint {
  --color-primary: #C43E1C;
  --color-secondary: #D24726;
  --color-accent: #F0643B;
  --color-bg-soft: #FFF4F0;
  --color-text: #1F2937;
}
```

## Structure de page

Chaque futur HTML doit suivre cette hiérarchie :

1. En-tête de page.
2. Métadonnées : logiciel, public, durée, niveau.
3. Actions : imprimer, retour index, afficher/masquer si utile.
4. Sommaire cliquable pour les pages longues.
5. Sections pédagogiques.
6. Exercices ou activités.
7. Quiz ou validation.
8. Synthèse / mémo.

## Composants communs

### En-tête

Contenu obligatoire :

- Titre clair.
- Badge logiciel.
- Public cible.
- Durée estimée.
- Niveau.
- Bouton impression.
- Lien retour index quand pertinent.

Style :

- Fond clair du thème.
- Bordure basse légère.
- Titre très lisible.
- Métadonnées en badges simples.

### Sommaire

Style :

- Carte claire.
- Liens internes visibles.
- Colonnes responsives.
- Libellés courts : Objectifs, Notions, Exercices, Quiz, Mémo, Correction, Synthèse.

### Carte pédagogique

Usage :

- Notion.
- Étape.
- Astuce.
- Rappel.
- Erreur fréquente.
- Mini-défi.

Structure :

- Titre court.
- Texte bref.
- Liste d'actions si nécessaire.
- Icône SVG inline facultative.

### Encadrés

Types :

- À retenir.
- Erreur fréquente.
- Astuce.
- Exemple.
- Attention.
- Mini-défi.
- Correction.
- Pour aller plus loin.

Style :

- Fond clair.
- Bordure gauche 5 px.
- Titre court.
- Une intention par encadré.

Couleurs fonctionnelles :

```css
.callout.remember { border-color: #15803D; }
.callout.warning { border-color: #B45309; }
.callout.error { border-color: #B91C1C; }
.callout.tip { border-color: var(--color-accent); }
.callout.correction { border-color: var(--color-primary); }
```

### Boutons

Règles :

- Hauteur minimale : 44 px.
- Texte explicite.
- Focus clavier visible.
- Pas de bouton seulement coloré sans texte ou icône claire.

États :

- Principal : fond `--color-primary`, texte blanc.
- Secondaire : fond blanc, bordure `--color-primary`, texte `--color-primary`.
- Neutre : fond gris clair, texte foncé.

Libellés recommandés :

- Imprimer / Exporter en PDF
- Afficher la correction
- Masquer la correction
- Afficher un indice
- Je vérifie ma réponse
- Tout ouvrir
- Tout fermer
- Révision rapide

### Checklists

Usage :

- Préparation formateur.
- Étapes d'exercice.
- Validation stagiaire.
- Critères de réussite.
- Fin de journée.

Règles :

- Cases larges.
- Libellés simples.
- Persistance `localStorage` autorisée uniquement si non bloquante.

### Accordéons

Usage :

- Corrections masquées.
- Indices progressifs.
- Questions fréquentes.
- Variantes formateur.

Règles :

- Fermés par défaut pour corrigés.
- Ouverts en impression si contenu important.
- Bouton avec `aria-expanded`.

### Quiz

Format :

- Question courte.
- 2 à 4 réponses.
- Feedback immédiat.
- Ton rassurant.
- Pas de score humiliant.

Réponses d'auto-positionnement :

- Je ne sais pas encore.
- Je sais un peu.
- Je sais faire seul.

### Tableaux

Règles :

- En-têtes visibles.
- Zébrage léger possible.
- Pas de tableau trop large sans conteneur responsive.
- Alignement numérique à droite.
- Légende ou contexte simple.

### Barres de progression

Usage :

- Parcours de journée.
- Checklist longue.
- Projet fil rouge.

Règles :

- Indication textuelle en plus de la couleur.
- Simple, sans animation obligatoire.

## Responsive

Points de rupture recommandés :

```css
@media (max-width: 900px) { }
@media (max-width: 640px) { }
```

Règles :

- Grilles passent en une colonne sous 640 px.
- Boutons peuvent prendre toute la largeur sur mobile.
- Sommaire en une colonne sur mobile.
- Pas de texte trop petit.
- Pas de débordement horizontal.

## Mode impression

Chaque HTML final devra inclure :

```css
@media print {
  .no-print,
  .page-actions,
  button {
    display: none !important;
  }

  body {
    background: #FFFFFF;
    color: #111827;
  }

  .card,
  .callout,
  table {
    break-inside: avoid;
  }

  a {
    color: #111827;
    text-decoration: none;
  }

  .print-open {
    display: block !important;
  }
}
```

Règles :

- Masquer les boutons inutiles.
- Conserver titres, consignes, tableaux, critères.
- Ouvrir corrections importantes seulement dans corrigés formateur.
- Éviter fonds chargés.
- Éviter coupures dans cartes et tableaux.

## Accessibilité

Règles minimales :

- Contraste suffisant.
- Boutons et liens utilisables au clavier.
- Focus visible.
- Titres hiérarchiques dans l'ordre.
- Champs et quiz avec libellés.
- SVG décoratifs masqués avec `aria-hidden="true"`.
- Textes alternatifs simples pour images utiles.
- Ne jamais dépendre uniquement de la couleur.

## Interactivité

Interactions autorisées :

- Accordéons.
- Afficher / masquer.
- Quiz simples.
- Checklists cochables.
- Recherche locale.
- Filtres locaux.
- Barres de progression.

Règles techniques :

- JavaScript intégré dans chaque HTML.
- Pas de framework.
- Pas d'appel Internet.
- Code robuste si `localStorage` est indisponible.
- Corrigés masqués par défaut dans les supports stagiaires.

Modèle `localStorage` recommandé :

```javascript
function safeStorageGet(key) {
  try {
    return localStorage.getItem(key);
  } catch (error) {
    return null;
  }
}

function safeStorageSet(key, value) {
  try {
    localStorage.setItem(key, value);
  } catch (error) {
    return false;
  }
  return true;
}
```

## Icônes

Règles :

- SVG inline uniquement.
- Icônes simples, monochromes.
- Pas de dépendance externe.
- Icône toujours accompagnée d'un libellé ou d'un `aria-label`.

## Ton éditorial visuel

Règles :

- Consignes directes.
- Mots simples.
- Une action par phrase quand possible.
- Messages d'erreur rassurants.
- Feedback orienté progression.

Exemples :

- Correct : "Sélectionnez le titre, puis cliquez sur Gras."
- À éviter : "Appliquez une emphase typographique via le ruban."

## À éviter

- Interfaces trop denses.
- Couleurs agressives.
- Animations décoratives.
- Gradients lourds.
- Logos officiels Microsoft.
- Textes longs sans découpage.
- Boutons petits.
- Corrigés visibles par défaut côté stagiaire.
- Dépendances externes.

## Préparation phase 3

La phase 3 devra transformer ce guide en templates HTML standalone dans `FormaPro/12_Templates_HTML/`.

Les templates devront intégrer :

- CSS dans `<style>`.
- JavaScript dans `<script>`.
- Classes de thème.
- Composants ci-dessus.
- Mode impression.
- Exemples de quiz, checklist, correction masquée.
