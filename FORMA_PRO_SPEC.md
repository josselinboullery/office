Basé sur la fiche formation FormaPro : parcours débutant Office de **6 jours / 43 h**, avec **Word 18 h, Excel 18 h et PowerPoint 7 h**. 

````markdown
# FORMA_PRO_SPEC.md

# Spécification générale — Kit de formation Office débutant FormaPro

## 1. Objectif du projet

Créer un kit complet de formation bureautique débutant pour FormaPro, destiné à l’animation d’un parcours Office comprenant :

- Word
- Excel
- PowerPoint

Le kit doit permettre au formateur d’animer la formation avec une friction minimale, tout en proposant aux stagiaires une expérience claire, moderne, progressive, interactive et engageante.

Tous les livrables principaux doivent être produits au format :

```text
HTML / CSS / JavaScript standalone
````

Chaque page HTML doit fonctionner localement, en double-cliquant sur le fichier, sans installation, sans serveur, sans CDN et sans dépendance externe obligatoire.

---

## 2. Source officielle à respecter

Le projet doit être construit à partir du PDF de formation FormaPro présent dans le dossier courant.

Titre du parcours :

```text
Parcours bureautique : maîtrise des logiciels Word, Excel et PowerPoint — Niveau débutant
```

Caractéristiques officielles :

* Public concerné : tout public débutant en bureautique
* Prérequis : aucun
* Durée : 6 jours, soit 43 heures
* Word : 18 heures
* Excel : 18 heures
* PowerPoint : 7 heures

Objectifs officiels :

À l’issue de la formation, les participants doivent être capables de :

* créer, modifier et mettre en forme des documents professionnels avec Word ;
* réaliser des tableaux simples et effectuer des calculs de base avec Excel ;
* concevoir des présentations claires et structurées avec PowerPoint ;
* utiliser les fonctionnalités essentielles des outils bureautiques dans un contexte professionnel.

Méthode pédagogique officielle :

* alternance théorie / pratique ;
* mises en situation réalistes ;
* exercices et simulations ;
* accompagnement personnalisé ;
* évaluation initiale ;
* évaluations continues ;
* exercices pratiques ;
* évaluation finale ;
* attestation de fin de formation.

---

## 3. Planning réel de la formation

La formation est organisée sur 6 journées :

| Jour   |                Date | Durée | Logiciel principal |
| ------ | ------------------: | ----: | ------------------ |
| Jour 1 |        Mardi 2 juin |   7 h | Word               |
| Jour 2 |     Mercredi 3 juin |   7 h | Word               |
| Jour 3 |     Vendredi 5 juin |   7 h | Word + Excel       |
| Jour 4 |       Jeudi 18 juin |   8 h | Excel              |
| Jour 5 |     Mardi 7 juillet |   7 h | Excel              |
| Jour 6 | Vendredi 10 juillet |   7 h | PowerPoint         |

Répartition pédagogique à respecter :

| Logiciel   | Durée officielle | Répartition recommandée        |
| ---------- | ---------------: | ------------------------------ |
| Word       |             18 h | J1 : 7 h / J2 : 7 h / J3 : 4 h |
| Excel      |             18 h | J3 : 3 h / J4 : 8 h / J5 : 7 h |
| PowerPoint |              7 h | J6 : 7 h                       |

Total : 43 h.

---

## 4. Public cible

Le public est composé de grands débutants.

Contraintes pédagogiques :

* aucun prérequis technique ;
* vocabulaire simple ;
* progression très guidée ;
* nombreuses manipulations ;
* répétition des gestes essentiels ;
* exercices courts et concrets ;
* droit à l’erreur valorisé ;
* accompagnement rassurant ;
* supports très lisibles ;
* pas de surcharge d’information ;
* pas de jargon non expliqué.

Les supports doivent partir du principe que certains stagiaires peuvent avoir des difficultés avec :

* la souris ;
* le clavier ;
* le copier-coller ;
* l’enregistrement d’un fichier ;
* la recherche d’un fichier ;
* la différence entre un fichier, un dossier et un logiciel ;
* la sélection de texte ;
* la manipulation de fenêtres ;
* l’impression ;
* l’export PDF.

---

## 5. Objectif final du kit

À la fin du travail, le dossier `FormaPro` doit contenir un kit complet permettant d’animer la formation sans avoir à improviser les supports, les exercices ou les corrections.

Le formateur doit pouvoir ouvrir :

```text
FormaPro/00_Index_general/index.html
```

Depuis cette page, il doit accéder à :

* la vue d’ensemble du parcours ;
* le guide formateur ;
* les supports stagiaires interactifs ;
* les exercices ;
* les corrigés ;
* les fichiers de départ ;
* les fiches mémo interactives ;
* les évaluations ;
* le projet fil rouge ;
* les mini-défis intersessions ;
* les cartes SOS ;
* le rapport de génération.

---

## 6. Principe de production

Ne pas tout générer en une seule fois.

Le projet doit être exécuté par phases successives :

1. Audit du dossier et création de l’arborescence
2. Création du design system
3. Création des templates HTML
4. Génération du module Word
5. Génération du module Excel
6. Génération du module PowerPoint
7. Génération du projet fil rouge
8. Génération des évaluations
9. Génération des fiches mémo et cartes SOS
10. Création de l’index général
11. Vérification finale
12. Rapport final

À chaque phase :

* ne traiter que la phase demandée ;
* ne pas modifier les fichiers originaux ;
* ne pas supprimer de fichiers ;
* mettre à jour le rapport de génération ;
* vérifier les liens créés ;
* signaler les limites ou fichiers manquants.

---

## 7. Format technique des livrables

Tous les livrables pédagogiques principaux doivent être en HTML standalone.

Chaque fichier HTML doit contenir :

* le HTML ;
* le CSS dans une balise `<style>` ;
* le JavaScript dans une balise `<script>` ;
* aucune dépendance externe obligatoire ;
* aucun CDN ;
* aucun appel à Internet ;
* aucun framework externe ;
* aucune police distante ;
* aucune image distante ;
* des SVG inline si des pictogrammes sont nécessaires ;
* une compatibilité avec un navigateur moderne ;
* un affichage responsive desktop / tablette ;
* une feuille de style d’impression avec `@media print`.

Chaque page doit pouvoir être :

* ouverte hors ligne ;
* utilisée en formation ;
* projetée au vidéoprojecteur ;
* consultée par les stagiaires ;
* imprimée ;
* exportée en PDF via le navigateur.

---

## 8. Direction artistique générale

Le design doit être :

* moderne ;
* professionnel ;
* clair ;
* rassurant ;
* engageant ;
* très lisible ;
* sobre ;
* cohérent sur tout le kit ;
* adapté à des grands débutants.

Il faut éviter :

* les interfaces trop denses ;
* les effets visuels inutiles ;
* les animations excessives ;
* les couleurs agressives ;
* les textes trop petits ;
* les blocs trop longs ;
* les consignes ambiguës.

Chaque page doit contenir une hiérarchie visuelle forte :

* titre principal clair ;
* sous-titres visibles ;
* cartes pédagogiques ;
* encadrés ;
* checklists ;
* boutons larges ;
* espaces respirants ;
* navigation simple ;
* progression visible quand c’est utile.

---

## 9. Direction artistique par logiciel

Les supports doivent s’inspirer de l’univers visuel Microsoft Office, sans utiliser les logos officiels Microsoft ni copier des éléments protégés.

### 9.1 Word

Ambiance :

* claire ;
* structurée ;
* rédactionnelle ;
* professionnelle ;
* calme.

Couleurs :

```text
Word — Bleu Office
Couleur principale : #185ABD
Couleur secondaire : #2B579A
Accent clair : #41A5EE
Fond très clair : #F3F7FF
Texte foncé : #1F2937
```

Utilisation :

* supports Word ;
* exercices Word ;
* corrigés Word ;
* fiches mémo Word ;
* sections liées à la rédaction, aux documents et à la mise en page.

---

### 9.2 Excel

Ambiance :

* organisée ;
* logique ;
* structurée ;
* orientée données ;
* rassurante.

Couleurs :

```text
Excel — Vert Office
Couleur principale : #107C41
Couleur secondaire : #217346
Accent clair : #33C481
Fond très clair : #F1FAF5
Texte foncé : #1F2937
```

Utilisation :

* supports Excel ;
* exercices Excel ;
* corrigés Excel ;
* fiches mémo Excel ;
* sections liées aux tableaux, calculs, graphiques et données.

---

### 9.3 PowerPoint

Ambiance :

* visuelle ;
* dynamique ;
* claire ;
* orientée présentation ;
* créative mais sobre.

Couleurs :

```text
PowerPoint — Rouge / orange Office
Couleur principale : #C43E1C
Couleur secondaire : #D24726
Accent clair : #F0643B
Fond très clair : #FFF4F0
Texte foncé : #1F2937
```

Utilisation :

* supports PowerPoint ;
* exercices PowerPoint ;
* corrigés PowerPoint ;
* fiches mémo PowerPoint ;
* sections liées aux diapositives, aux visuels et à la présentation orale.

---

### 9.4 Documents généraux et formateur

Ambiance :

* neutre ;
* professionnelle ;
* synthétique ;
* organisationnelle.

Couleurs :

```text
Général / Formateur
Couleur principale : #334155
Couleur secondaire : #1F2937
Accent : #64748B
Fond clair : #F8FAFC
Texte foncé : #111827
```

Utilisation :

* index général ;
* vue d’ensemble ;
* guide formateur général ;
* évaluations ;
* rapport ;
* documents transversaux.

---

## 10. Composants HTML communs

Chaque page doit utiliser une structure cohérente avec les composants suivants.

### 10.1 En-tête

Chaque page doit afficher :

* titre de la page ;
* logiciel concerné ;
* public cible ;
* durée estimée ;
* niveau ;
* bouton d’impression ;
* bouton retour à l’index quand c’est pertinent.

### 10.2 Sommaire

Chaque support long doit inclure un sommaire cliquable.

Le sommaire doit permettre de naviguer rapidement vers :

* objectifs ;
* notions ;
* exercices ;
* quiz ;
* mémo ;
* correction ;
* synthèse.

### 10.3 Cartes pédagogiques

Utiliser des cartes visuelles pour :

* les notions ;
* les étapes ;
* les erreurs fréquentes ;
* les astuces ;
* les rappels ;
* les mini-défis.

### 10.4 Encadrés

Prévoir les types d’encadrés suivants :

```text
À retenir
Erreur fréquente
Astuce
Exemple
Attention
Mini-défi
Correction
Pour aller plus loin
```

### 10.5 Checklists

Utiliser des checklists pour :

* les étapes d’exercice ;
* la préparation formateur ;
* la validation stagiaire ;
* les critères de réussite ;
* la fin de journée.

### 10.6 Boutons

Les boutons doivent être grands, lisibles et explicites.

Exemples :

```text
Afficher la correction
Masquer la correction
Afficher un indice
Je vérifie ma réponse
Tout ouvrir
Tout fermer
Imprimer / Exporter en PDF
Révision rapide
```

---

## 11. Interactivités attendues

Les interactions doivent rester simples, utiles et robustes.

Interactions à intégrer selon les besoins :

* accordéons ;
* sections repliables ;
* quiz avec correction immédiate ;
* boutons afficher / masquer ;
* checklists cochables ;
* barre de progression ;
* cartes retournables pour le lexique ;
* recherche interne dans les fiches mémo ;
* filtres par logiciel ;
* filtres par niveau ;
* mode révision ;
* boutons tout ouvrir / tout fermer ;
* corrigés masqués par défaut ;
* indices progressifs ;
* feedback simple après une réponse.

L’utilisation de `localStorage` est autorisée uniquement pour :

* mémoriser les cases cochées ;
* mémoriser la progression ;
* mémoriser les sections déjà consultées ;
* conserver l’état d’une fiche mémo.

Si `localStorage` est utilisé, le code doit rester simple et ne pas bloquer la page si le navigateur le refuse.

---

## 12. Mode impression

Chaque page HTML doit être imprimable proprement.

Prévoir une règle :

```css
@media print
```

Le mode impression doit :

* masquer les boutons inutiles ;
* masquer les éléments interactifs non nécessaires ;
* ouvrir les contenus importants ;
* conserver les titres ;
* conserver les consignes ;
* conserver les tableaux ;
* conserver les critères de réussite ;
* éviter les fonds trop chargés ;
* éviter les coupures gênantes dans les cartes ;
* afficher l’URL ou le nom du fichier si utile ;
* permettre une exportation PDF propre.

---

## 13. Arborescence cible

Créer l’arborescence suivante :

```text
FormaPro/
├── FORMA_PRO_SPEC.md
├── STYLE_GUIDE.md
├── CONTENT_PLAN.md
├── TASKS.md
├── QA_CHECKLIST.md
├── RAPPORT_GENERATION.md
├── RAPPORT_GENERATION.html
├── 00_Index_general/
│   └── index.html
├── 01_Admin_et_vue_d_ensemble/
│   └── Vue_ensemble_formation.html
├── 02_Guide_formateur_HTML/
│   ├── Guide_formateur_general.html
│   ├── Jour_1_Word.html
│   ├── Jour_2_Word.html
│   ├── Jour_3_Word_Excel.html
│   ├── Jour_4_Excel.html
│   ├── Jour_5_Excel.html
│   └── Jour_6_PowerPoint_Evaluation.html
├── 03_Supports_stagiaires_HTML/
│   ├── Support_Word_Debutant.html
│   ├── Support_Excel_Debutant.html
│   └── Support_PowerPoint_Debutant.html
├── 04_Exercices_HTML/
│   ├── Word/
│   ├── Excel/
│   └── PowerPoint/
├── 05_Corriges_HTML/
│   ├── Word/
│   ├── Excel/
│   └── PowerPoint/
├── 06_Fichiers_de_depart/
│   ├── Word/
│   ├── Excel/
│   └── PowerPoint/
├── 07_Fiches_memo_interactives/
│   ├── Fiche_memo_gestes_de_base.html
│   ├── Fiche_memo_Word.html
│   ├── Fiche_memo_Excel.html
│   ├── Fiche_memo_PowerPoint.html
│   ├── Lexique_bureautique_debutant.html
│   └── Raccourcis_clavier_utiles.html
├── 08_Evaluations_HTML/
│   ├── Evaluation_initiale.html
│   ├── Evaluations_continues.html
│   ├── Evaluation_finale.html
│   ├── Grille_observation_formateur.html
│   └── Auto_evaluation_stagiaire.html
├── 09_Projet_fil_rouge_HTML/
│   ├── Projet_fil_rouge.html
│   ├── Brief_projet.html
│   ├── Grille_correction_projet.html
│   ├── Version_simplifiee.html
│   └── Version_bonus.html
├── 10_Mini_defis_intersessions_HTML/
│   ├── Defi_apres_jour_1.html
│   ├── Defi_apres_jour_2.html
│   ├── Defi_apres_jour_3.html
│   ├── Defi_apres_jour_4.html
│   └── Defi_apres_jour_5.html
├── 11_Cartes_SOS_interactives/
│   ├── Index_Cartes_SOS.html
│   ├── SOS_J_ai_perdu_mon_fichier.html
│   ├── SOS_Je_ne_sais_plus_ou_cliquer.html
│   ├── SOS_Mon_texte_a_bouge.html
│   ├── SOS_Mon_image_ne_va_pas_ou_je_veux.html
│   ├── SOS_Mon_tableau_Excel_ne_calcule_pas.html
│   ├── SOS_Je_n_arrive_pas_a_imprimer.html
│   ├── SOS_Je_veux_annuler_une_action.html
│   └── SOS_Je_n_arrive_pas_a_selectionner.html
├── 12_Templates_HTML/
│   ├── template_support_stagiaire.html
│   ├── template_guide_formateur.html
│   ├── template_exercice.html
│   ├── template_corrige.html
│   ├── template_fiche_memo.html
│   ├── template_evaluation.html
│   └── template_carte_sos.html
└── 13_Assets_optionnels/
```

---

## 14. Index général

Créer :

```text
FormaPro/00_Index_general/index.html
```

Cette page doit servir de tableau de bord général.

Elle doit contenir :

* titre de la formation ;
* résumé du parcours ;
* planning des 6 jours ;
* répartition Word / Excel / PowerPoint ;
* accès aux documents formateur ;
* accès aux documents stagiaires ;
* accès aux exercices ;
* accès aux corrigés ;
* accès aux fichiers de départ ;
* accès aux fiches mémo ;
* accès aux évaluations ;
* accès au projet fil rouge ;
* accès aux mini-défis ;
* accès aux cartes SOS ;
* accès au rapport final ;
* indication claire des contenus destinés au formateur ;
* indication claire des contenus destinés aux stagiaires.

L’index doit aussi contenir :

* checklist de préparation avant la formation ;
* checklist de préparation avant chaque journée ;
* rappel des fichiers à imprimer ;
* rappel des fichiers à distribuer ;
* rappel des fichiers à garder côté formateur.

---

## 15. Vue d’ensemble du parcours

Créer :

```text
FormaPro/01_Admin_et_vue_d_ensemble/Vue_ensemble_formation.html
```

Cette page doit contenir :

* objectifs globaux ;
* objectifs par logiciel ;
* tableau des 6 journées ;
* progression pédagogique ;
* carte visuelle du parcours ;
* répartition horaire ;
* compétences travaillées ;
* modalités pédagogiques ;
* modalités d’évaluation ;
* synthèse du projet fil rouge ;
* points de vigilance pour grands débutants.

---

## 16. Guide formateur

Créer les fichiers suivants :

```text
FormaPro/02_Guide_formateur_HTML/Guide_formateur_general.html
FormaPro/02_Guide_formateur_HTML/Jour_1_Word.html
FormaPro/02_Guide_formateur_HTML/Jour_2_Word.html
FormaPro/02_Guide_formateur_HTML/Jour_3_Word_Excel.html
FormaPro/02_Guide_formateur_HTML/Jour_4_Excel.html
FormaPro/02_Guide_formateur_HTML/Jour_5_Excel.html
FormaPro/02_Guide_formateur_HTML/Jour_6_PowerPoint_Evaluation.html
```

Chaque journée doit contenir :

* objectifs de la journée ;
* déroulé horaire ;
* découpage par séquence ;
* durée estimée ;
* matériel nécessaire ;
* fichiers à ouvrir ;
* ce que le formateur montre ;
* ce que les stagiaires font ;
* consignes à dire simplement ;
* questions à poser au groupe ;
* erreurs fréquentes ;
* points de vigilance ;
* variante si le groupe est lent ;
* variante si le groupe avance vite ;
* activité bonus ;
* correction collective ;
* mini-évaluation ;
* synthèse de fin de journée ;
* checklist de fin de journée.

Le guide formateur doit intégrer :

* boutons “Afficher les consignes stagiaires” ;
* boutons “Afficher les réponses” ;
* boutons “Version courte si retard” ;
* boutons “Activité bonus” ;
* timeline de la journée ;
* checklist “avant de commencer” ;
* checklist “fin de journée”.

---

## 17. Supports stagiaires

Créer :

```text
FormaPro/03_Supports_stagiaires_HTML/Support_Word_Debutant.html
FormaPro/03_Supports_stagiaires_HTML/Support_Excel_Debutant.html
FormaPro/03_Supports_stagiaires_HTML/Support_PowerPoint_Debutant.html
```

Chaque support doit être :

* interactif ;
* progressif ;
* très lisible ;
* adapté aux grands débutants ;
* utilisable seul ou accompagné ;
* imprimable ;
* cohérent avec la couleur du logiciel concerné.

Chaque support doit contenir :

* introduction simple ;
* objectifs ;
* prérequis ;
* sommaire ;
* notions essentielles ;
* démonstrations guidées ;
* mini-exercices ;
* quiz rapides ;
* corrections masquées ;
* checklists ;
* erreurs fréquentes ;
* synthèse ;
* mémo final.

### 17.1 Support Word

Contenus à couvrir :

* découvrir l’interface ;
* comprendre le ruban ;
* créer un document ;
* saisir du texte ;
* corriger du texte ;
* sélectionner du texte ;
* copier, couper, coller ;
* mettre en forme les caractères ;
* mettre en forme les paragraphes ;
* utiliser des styles simples ;
* insérer une image ;
* insérer un tableau ;
* gérer les marges ;
* gérer l’orientation ;
* préparer l’impression ;
* exporter en PDF ;
* créer un courrier simple ;
* créer un CV ou une fiche de présentation simple.

### 17.2 Support Excel

Contenus à couvrir :

* comprendre un classeur ;
* comprendre une feuille ;
* comprendre une cellule ;
* comprendre les lignes et les colonnes ;
* saisir des données ;
* modifier la largeur des colonnes ;
* créer un tableau simple ;
* mettre en forme un tableau ;
* utiliser SOMME ;
* utiliser MOYENNE ;
* utiliser une formule simple ;
* comprendre les références de cellules ;
* utiliser SI de manière très simple ;
* trier des données ;
* filtrer des données ;
* créer un graphique simple ;
* mettre en page avant impression ;
* exporter en PDF ;
* utiliser Excel dans un contexte professionnel simple.

### 17.3 Support PowerPoint

Contenus à couvrir :

* comprendre la logique d’une présentation ;
* créer une présentation ;
* ajouter des diapositives ;
* choisir une mise en page ;
* structurer un message ;
* éviter les diapositives trop chargées ;
* insérer du texte ;
* insérer une image ;
* insérer un graphique ;
* harmoniser la présentation ;
* utiliser les transitions avec sobriété ;
* préparer une prise de parole simple ;
* exporter ou présenter le diaporama.

---

## 18. Exercices HTML

Créer les exercices dans :

```text
FormaPro/04_Exercices_HTML/
```

Chaque exercice doit être une page HTML standalone.

Chaque exercice doit contenir :

* titre ;
* logiciel ;
* niveau ;
* durée estimée ;
* contexte professionnel ;
* objectif ;
* fichier de départ à utiliser ;
* consignes ;
* étapes ;
* résultat attendu ;
* critères de réussite ;
* checklist ;
* bouton “Afficher un indice” ;
* bouton “Afficher le corrigé” ;
* bouton d’impression ;
* section “Pour aller plus loin”.

Prévoir trois niveaux :

```text
Niveau 1 : guidé
Niveau 2 : semi-guidé
Niveau 3 : autonomie
```

### 18.1 Exercices Word minimum

Créer au minimum :

```text
Word_01_Mettre_en_forme_un_texte_brut.html
Word_02_Creer_un_courrier_professionnel.html
Word_03_Inserer_image_et_tableau.html
Word_04_Creer_une_fiche_de_presentation.html
Word_05_Corriger_un_document_mal_presente.html
```

### 18.2 Exercices Excel minimum

Créer au minimum :

```text
Excel_01_Creer_un_tableau_de_suivi.html
Excel_02_Calculer_totaux_et_moyennes.html
Excel_03_Creer_un_budget_simple.html
Excel_04_Utiliser_SI_simple.html
Excel_05_Creer_un_graphique.html
Excel_06_Corriger_un_tableau_avec_erreurs.html
```

### 18.3 Exercices PowerPoint minimum

Créer au minimum :

```text
PowerPoint_01_Creer_une_presentation_3_diapositives.html
PowerPoint_02_Ameliorer_une_presentation_trop_chargee.html
PowerPoint_03_Inserer_images_et_graphique.html
PowerPoint_04_Creer_une_presentation_finale_5_diapositives.html
```

---

## 19. Corrigés HTML

Créer les corrigés dans :

```text
FormaPro/05_Corriges_HTML/
```

Chaque corrigé doit être une page HTML standalone.

Chaque corrigé doit contenir :

* rappel de l’exercice ;
* objectif ;
* résultat attendu ;
* étapes principales ;
* points de contrôle ;
* erreurs fréquentes ;
* variantes acceptables ;
* critères de validation ;
* section “comment corriger collectivement” ;
* bouton “Afficher tout le corrigé” ;
* bouton “Mode correction collective” ;
* bouton d’impression.

Les corrigés doivent être pensés pour le formateur.

Les corrigés peuvent être accessibles aux stagiaires uniquement si le formateur le décide.

---

## 20. Fichiers de départ

Créer les fichiers de départ dans :

```text
FormaPro/06_Fichiers_de_depart/
```

Créer des fichiers simples, réalistes et exploitables.

Formats recommandés :

* `.txt` pour les textes bruts Word ;
* `.csv` pour les données Excel ;
* `.md` pour les briefs ;
* `.html` si une ressource interactive est utile ;
* `.docx`, `.xlsx`, `.pptx` en complément uniquement si possible.

Les fichiers doivent couvrir :

* textes bruts à mettre en forme ;
* faux tableaux de données ;
* budgets simples ;
* listes de participants ;
* contenus bruts pour présentation ;
* documents volontairement mal présentés ;
* tableaux contenant des erreurs ;
* images placeholder en SVG si nécessaire.

Contextes recommandés :

* organisation d’un petit événement professionnel ;
* suivi de participants ;
* planning simple ;
* budget de fournitures ;
* présentation d’un service ;
* courrier d’information ;
* fiche de contact ;
* tableau de dépenses.

---

## 21. Fiches mémo interactives

Créer :

```text
FormaPro/07_Fiches_memo_interactives/Fiche_memo_gestes_de_base.html
FormaPro/07_Fiches_memo_interactives/Fiche_memo_Word.html
FormaPro/07_Fiches_memo_interactives/Fiche_memo_Excel.html
FormaPro/07_Fiches_memo_interactives/Fiche_memo_PowerPoint.html
FormaPro/07_Fiches_memo_interactives/Lexique_bureautique_debutant.html
FormaPro/07_Fiches_memo_interactives/Raccourcis_clavier_utiles.html
```

Les fiches doivent être :

* très synthétiques ;
* interactives ;
* imprimables ;
* utilisables en révision ;
* utilisables pendant les exercices.

Interactions attendues :

* recherche rapide ;
* cartes repliables ;
* cartes retournables ;
* boutons “Je sais faire” ;
* mini-quiz ;
* mode “révision rapide” ;
* bouton “tout ouvrir” ;
* bouton “tout fermer”.

### 21.1 Fiche gestes de base

Contenus à inclure :

* créer un fichier ;
* enregistrer ;
* enregistrer sous ;
* retrouver un fichier ;
* renommer un fichier ;
* copier ;
* couper ;
* coller ;
* annuler ;
* sélectionner ;
* imprimer ;
* exporter en PDF.

### 21.2 Lexique

Le lexique doit expliquer simplement :

* ruban ;
* onglet ;
* groupe ;
* document ;
* classeur ;
* feuille ;
* cellule ;
* ligne ;
* colonne ;
* formule ;
* graphique ;
* diapositive ;
* mise en page ;
* modèle ;
* PDF.

---

## 22. Évaluations

Créer :

```text
FormaPro/08_Evaluations_HTML/Evaluation_initiale.html
FormaPro/08_Evaluations_HTML/Evaluations_continues.html
FormaPro/08_Evaluations_HTML/Evaluation_finale.html
FormaPro/08_Evaluations_HTML/Grille_observation_formateur.html
FormaPro/08_Evaluations_HTML/Auto_evaluation_stagiaire.html
```

### 22.1 Évaluation initiale

Objectif :

* identifier le niveau de départ ;
* rassurer ;
* éviter une logique d’examen ;
* aider le formateur à adapter l’accompagnement.

Réponses recommandées :

```text
Je ne sais pas encore
Je sais un peu
Je sais faire seul
```

Ne pas utiliser de notation humiliante.

### 22.2 Évaluations continues

Prévoir :

* mini-défis de fin de demi-journée ;
* observation par le formateur ;
* critères simples ;
* checklists ;
* feedback rapide.

### 22.3 Évaluation finale

Le stagiaire doit produire :

* un document Word propre ;
* un tableau Excel avec calculs et graphique ;
* une présentation PowerPoint courte.

Critères :

* autonomie ;
* respect des consignes ;
* lisibilité ;
* mise en forme ;
* calculs corrects ;
* structuration ;
* capacité à enregistrer ;
* capacité à retrouver ses fichiers ;
* capacité à exporter en PDF.

---

## 23. Projet fil rouge

Créer dans :

```text
FormaPro/09_Projet_fil_rouge_HTML/
```

Fichiers attendus :

```text
Projet_fil_rouge.html
Brief_projet.html
Grille_correction_projet.html
Version_simplifiee.html
Version_bonus.html
```

Thème recommandé :

```text
Organiser et présenter un petit événement professionnel
```

Productions attendues :

* courrier d’invitation dans Word ;
* fiche d’information dans Word ;
* tableau de suivi des participants dans Excel ;
* budget simple dans Excel ;
* graphique simple dans Excel ;
* présentation PowerPoint de restitution.

Le projet doit être présenté comme une mission professionnelle progressive.

Il doit contenir :

* contexte ;
* consignes ;
* étapes cochables ;
* livrables attendus ;
* fichiers nécessaires ;
* critères de réussite ;
* indices ;
* corrigé masqué ;
* version simplifiée ;
* version bonus.

---

## 24. Mini-défis intersessions

Créer :

```text
FormaPro/10_Mini_defis_intersessions_HTML/Defi_apres_jour_1.html
FormaPro/10_Mini_defis_intersessions_HTML/Defi_apres_jour_2.html
FormaPro/10_Mini_defis_intersessions_HTML/Defi_apres_jour_3.html
FormaPro/10_Mini_defis_intersessions_HTML/Defi_apres_jour_4.html
FormaPro/10_Mini_defis_intersessions_HTML/Defi_apres_jour_5.html
```

Objectif :

Comme les dates de formation sont espacées, les mini-défis doivent aider les stagiaires à mémoriser les gestes essentiels entre deux journées.

Chaque défi doit :

* être court ;
* durer 10 à 20 minutes ;
* être rassurant ;
* réactiver les notions vues ;
* pouvoir être corrigé rapidement ;
* contenir une checklist ;
* proposer un indice ;
* proposer une correction masquée ;
* proposer une version bonus.

---

## 25. Cartes SOS interactives

Créer :

```text
FormaPro/11_Cartes_SOS_interactives/Index_Cartes_SOS.html
FormaPro/11_Cartes_SOS_interactives/SOS_J_ai_perdu_mon_fichier.html
FormaPro/11_Cartes_SOS_interactives/SOS_Je_ne_sais_plus_ou_cliquer.html
FormaPro/11_Cartes_SOS_interactives/SOS_Mon_texte_a_bouge.html
FormaPro/11_Cartes_SOS_interactives/SOS_Mon_image_ne_va_pas_ou_je_veux.html
FormaPro/11_Cartes_SOS_interactives/SOS_Mon_tableau_Excel_ne_calcule_pas.html
FormaPro/11_Cartes_SOS_interactives/SOS_Je_n_arrive_pas_a_imprimer.html
FormaPro/11_Cartes_SOS_interactives/SOS_Je_veux_annuler_une_action.html
FormaPro/11_Cartes_SOS_interactives/SOS_Je_n_arrive_pas_a_selectionner.html
```

Chaque carte doit contenir :

* problème ;
* cause probable ;
* solution rapide ;
* explication complète ;
* étapes ;
* astuce de prévention ;
* bouton “Voir la solution rapide” ;
* bouton “Voir l’explication complète” ;
* bouton d’impression.

L’index des cartes SOS doit permettre :

* de rechercher un problème ;
* de filtrer par logiciel ;
* de filtrer par type de problème ;
* d’accéder rapidement à la bonne fiche.

---

## 26. Templates HTML

Créer dans :

```text
FormaPro/12_Templates_HTML/
```

Fichiers attendus :

```text
template_support_stagiaire.html
template_guide_formateur.html
template_exercice.html
template_corrige.html
template_fiche_memo.html
template_evaluation.html
template_carte_sos.html
```

Les templates doivent inclure :

* structure HTML propre ;
* variables ou commentaires faciles à remplacer ;
* CSS intégré ;
* JavaScript intégré ;
* classes de couleur par logiciel ;
* composants réutilisables ;
* mode impression ;
* navigation ;
* boutons interactifs ;
* exemples de cartes pédagogiques ;
* exemple de quiz ;
* exemple de checklist ;
* exemple de correction masquée.

Les templates doivent servir de base aux livrables finaux.

---

## 27. Règles de contenu pédagogique

Le contenu doit être :

* concret ;
* professionnel ;
* progressif ;
* rassurant ;
* orienté pratique ;
* adapté aux grands débutants ;
* formulé simplement ;
* suffisamment détaillé pour être utilisé directement.

Éviter :

* le jargon ;
* les explications abstraites ;
* les longs paragraphes ;
* les consignes floues ;
* les exercices trop complexes ;
* les références trop techniques ;
* les présupposés de compétence.

Chaque notion doit idéalement suivre cette structure :

```text
1. À quoi ça sert ?
2. Où cliquer ?
3. Comment faire ?
4. Exemple simple
5. Erreur fréquente
6. Mini-exercice
7. À retenir
```

---

## 28. Règles pour les exercices

Chaque exercice doit être formulé comme une situation professionnelle simple.

Exemples de contextes :

* préparer un courrier d’information ;
* créer une liste de participants ;
* suivre un budget ;
* organiser un petit événement ;
* présenter un service ;
* corriger un document mal présenté ;
* rendre un tableau plus lisible ;
* préparer une présentation courte.

Chaque exercice doit contenir :

* une consigne claire ;
* un fichier de départ ;
* un résultat attendu ;
* des critères de réussite ;
* une durée réaliste ;
* un indice ;
* un corrigé ;
* une version bonus.

---

## 29. Règles pour les corrigés

Les corrigés doivent permettre :

* au formateur de corriger rapidement ;
* au stagiaire de comprendre ses erreurs ;
* de faire une correction collective ;
* de valider objectivement le résultat.

Chaque corrigé doit expliquer :

* ce qui était attendu ;
* les étapes importantes ;
* les erreurs possibles ;
* les variantes acceptables ;
* les points à vérifier.

Ne pas créer de corrigés trop secs.

---

## 30. Accessibilité et lisibilité

Tous les supports doivent respecter ces principes :

* taille de texte confortable ;
* contraste suffisant ;
* boutons lisibles ;
* zones cliquables assez grandes ;
* consignes explicites ;
* pas d’information uniquement portée par la couleur ;
* textes alternatifs simples si des images sont utilisées ;
* structure logique des titres ;
* navigation clavier acceptable quand c’est possible ;
* responsive sur écran moyen.

---

## 31. Nommage des fichiers

Utiliser des noms de fichiers :

* explicites ;
* sans accents ;
* sans espaces ;
* avec underscores ;
* cohérents ;
* faciles à retrouver.

Exemples :

```text
Support_Word_Debutant.html
Excel_03_Creer_un_budget_simple.html
SOS_J_ai_perdu_mon_fichier.html
Defi_apres_jour_2.html
```

Éviter :

```text
fichier final.html
support 2 version ok.html
cours.html
test.html
```

---

## 32. Liens internes

Les liens internes doivent être relatifs.

Exemple :

```html
<a href="../03_Supports_stagiaires_HTML/Support_Word_Debutant.html">Support Word</a>
```

Chaque page importante doit permettre de revenir :

* à l’index général ;
* au module concerné ;
* à la section précédente si pertinent.

Après génération, vérifier autant que possible les liens internes.

---

## 33. Rapport de génération

Maintenir deux rapports :

```text
FormaPro/RAPPORT_GENERATION.md
FormaPro/RAPPORT_GENERATION.html
```

Le rapport doit contenir :

* date de génération ;
* phases effectuées ;
* fichiers créés ;
* fichiers modifiés ;
* choix pédagogiques ;
* choix graphiques ;
* choix techniques ;
* ressources manquantes ;
* limites ;
* points à vérifier ;
* prochaines améliorations.

À chaque phase, mettre à jour le rapport.

---

## 34. Contrôle qualité final

Avant de considérer le projet terminé, vérifier :

* l’arborescence ;
* la présence de tous les fichiers attendus ;
* l’ouverture des HTML hors ligne ;
* l’absence de CDN ;
* l’absence de dépendance externe ;
* la présence des styles intégrés ;
* la présence des scripts intégrés ;
* le fonctionnement des boutons ;
* le fonctionnement des accordéons ;
* le fonctionnement des quiz ;
* l’impression ;
* les liens internes ;
* la cohérence des couleurs ;
* la cohérence pédagogique ;
* l’adaptation aux grands débutants ;
* la cohérence avec le programme officiel ;
* la présence des corrigés ;
* la présence des fichiers de départ ;
* la lisibilité générale.

---

## 35. Contraintes strictes

Respecter impérativement les contraintes suivantes :

* ne jamais supprimer les fichiers originaux ;
* ne jamais modifier le PDF source ;
* ne pas utiliser de CDN ;
* ne pas dépendre d’Internet ;
* ne pas utiliser de framework externe ;
* ne pas utiliser les logos officiels Microsoft ;
* ne pas créer de contenus trop techniques pour des grands débutants ;
* ne pas générer tous les fichiers en une seule phase si ce n’est pas demandé ;
* ne pas mélanger les couleurs des logiciels ;
* ne pas rendre visibles les corrigés par défaut dans les supports stagiaires ;
* ne pas créer de supports non imprimables ;
* ne pas créer de fichiers au nom ambigu ;
* ne pas oublier de mettre à jour le rapport.

---

## 36. Résultat attendu

Le résultat final doit être un kit complet, professionnel et utilisable immédiatement pour animer la formation Office débutant FormaPro.

Le dossier final doit permettre :

* au formateur de préparer chaque journée rapidement ;
* aux stagiaires de suivre la formation facilement ;
* de pratiquer régulièrement ;
* de corriger efficacement ;
* de réviser entre les sessions ;
* de gérer les grands débutants sans friction ;
* de rendre la formation plus vivante grâce à des supports interactifs ;
* de produire une expérience cohérente avec l’univers visuel Word, Excel et PowerPoint.

Fin de la spécification.

```
```
