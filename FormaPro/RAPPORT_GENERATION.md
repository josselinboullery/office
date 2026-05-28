# Rapport de génération - Kit Horizon Compétences Office débutant

Date de mise à jour : 27 mai 2026

## Phase effectuée

- PHASE 1 uniquement : audit du dossier courant et création de l'arborescence cible.

## Audit du dossier source

- Dossier source : `C:\Users\jboul\OneDrive\professionnel\Formations\office`
- PDF officiel présent : `49_Parcours bureautique _ Débutant.pdf`
- Spécification présente : `FORMA_PRO_SPEC.md`
- Dossiers pédagogiques source présents : `Word`, `Excel`, `Powerpoint`
- Dossier cible `FormaPro` absent avant génération.

## Fichiers créés

- `FormaPro/FORMA_PRO_SPEC.md` : copie de la spécification source, sans modification du fichier original.
- `FormaPro/RAPPORT_GENERATION.md` : présent rapport.

## Dossiers créés

- `FormaPro/00_Index_general/`
- `FormaPro/01_Admin_et_vue_d_ensemble/`
- `FormaPro/02_Guide_formateur_HTML/`
- `FormaPro/03_Supports_stagiaires_HTML/`
- `FormaPro/04_Exercices_HTML/Word/`
- `FormaPro/04_Exercices_HTML/Excel/`
- `FormaPro/04_Exercices_HTML/PowerPoint/`
- `FormaPro/05_Corriges_HTML/Word/`
- `FormaPro/05_Corriges_HTML/Excel/`
- `FormaPro/05_Corriges_HTML/PowerPoint/`
- `FormaPro/06_Fichiers_de_depart/Word/`
- `FormaPro/06_Fichiers_de_depart/Excel/`
- `FormaPro/06_Fichiers_de_depart/PowerPoint/`
- `FormaPro/07_Fiches_memo_interactives/`
- `FormaPro/08_Evaluations_HTML/`
- `FormaPro/09_Projet_fil_rouge_HTML/`
- `FormaPro/10_Mini_defis_intersessions_HTML/`
- `FormaPro/11_Cartes_SOS_interactives/`
- `FormaPro/12_Templates_HTML/`
- `FormaPro/13_Assets_optionnels/`

## Fichiers modifiés

- Aucun fichier source original modifié.
- `FormaPro/RAPPORT_GENERATION.md` créé et renseigné.

## Choix pédagogiques

- Aucun contenu pédagogique généré pendant cette phase.
- Respect strict de la limite PHASE 1 : préparation du conteneur de travail seulement.

## Choix graphiques

- Aucun design system créé pendant cette phase.
- Les choix graphiques Word / Excel / PowerPoint seront traités dans une phase ultérieure.

## Choix techniques

- Arborescence créée en dossiers locaux.
- Aucun CDN, aucune dépendance externe, aucun serveur, aucun appel Internet.
- Spécification copiée dans le dossier cible pour garder le kit autonome.

## Liens vérifiés

- Aucun lien interne créé pendant cette phase.

## Ressources manquantes ou non créées à ce stade

- `STYLE_GUIDE.md`
- `CONTENT_PLAN.md`
- `TASKS.md`
- `QA_CHECKLIST.md`
- `RAPPORT_GENERATION.html`
- Tous les HTML finaux de supports, exercices, corrigés, fiches mémo, évaluations, projet fil rouge, mini-défis, cartes SOS, templates et index général.

Ces éléments ne sont pas générés en PHASE 1 afin de respecter la consigne : exécuter uniquement la PHASE 1.

## Limites

- Le contenu du PDF officiel n'a pas été extrait ni transformé.
- Aucun fichier pédagogique final n'a été produit.
- Aucune vérification de liens HTML n'est applicable à ce stade.

## Points à vérifier avant PHASE 2

- Confirmer que l'arborescence `FormaPro` convient.
- Lancer ensuite uniquement la PHASE 2 pour créer le design system.

---

## Mise à jour - PHASE 2

Date de mise à jour : 27 mai 2026

### Phase effectuée

- PHASE 2 uniquement : création du design system.

### Fichiers créés

- `FormaPro/STYLE_GUIDE.md` : règles visuelles, ergonomiques et techniques du kit.
- `FormaPro/RAPPORT_GENERATION.html` : version HTML standalone du rapport de génération.

### Fichiers modifiés

- `FormaPro/RAPPORT_GENERATION.md` : ajout du suivi de PHASE 2.

### Choix pédagogiques

- Design orienté grands débutants : lisibilité, hiérarchie forte, consignes courtes, droit à l'erreur.
- Composants prévus pour supports progressifs : cartes, encadrés, checklists, accordéons, quiz simples.
- Corrigés masqués par défaut côté stagiaire dans les futurs templates.

### Choix graphiques

- Conservation stricte des palettes définies par la spécification :
  - Word : bleu Office.
  - Excel : vert Office.
  - PowerPoint : rouge / orange Office.
  - Général / formateur : gris neutre.
- Design sobre, professionnel, sans logo Microsoft.
- Rayons modérés, ombres légères, espaces respirants.

### Choix techniques

- Design system documenté en Markdown pour servir de base à la phase 3.
- Variables CSS recommandées pour thèmes `.theme-general`, `.theme-word`, `.theme-excel`, `.theme-powerpoint`.
- Règles HTML standalone préparées : CSS intégré, JS intégré, pas de CDN, pas de dépendance externe.
- Modèle `localStorage` non bloquant documenté.
- Règles `@media print` documentées.

### Liens vérifiés

- Aucun lien interne HTML de navigation créé pendant cette phase.
- `RAPPORT_GENERATION.html` est autonome et ne dépend d'aucune ressource externe.

### Ressources manquantes ou non créées à ce stade

- `CONTENT_PLAN.md`
- `TASKS.md`
- `QA_CHECKLIST.md`
- Tous les templates HTML de `12_Templates_HTML/`
- Tous les supports, exercices, corrigés, fichiers de départ, fiches mémo, évaluations, projet fil rouge, mini-défis, cartes SOS et index général.

Ces éléments ne sont pas générés en PHASE 2 afin de respecter la consigne : exécuter uniquement la phase demandée.

### Limites

- Aucun template HTML final créé.
- Aucun contenu pédagogique module Word, Excel ou PowerPoint généré.
- Aucun lien pédagogique à vérifier à ce stade.

### Points à vérifier avant PHASE 3

- Valider que `STYLE_GUIDE.md` est suffisant pour produire les templates.
- Lancer ensuite uniquement la PHASE 3 pour créer les templates HTML standalone.

---

## Mise à jour - PHASE 3

Date de mise à jour : 27 mai 2026

### Phase effectuée

- PHASE 3 uniquement : création des templates HTML standalone.

### Fichiers créés

- `FormaPro/12_Templates_HTML/template_support_stagiaire.html`
- `FormaPro/12_Templates_HTML/template_guide_formateur.html`
- `FormaPro/12_Templates_HTML/template_exercice.html`
- `FormaPro/12_Templates_HTML/template_corrige.html`
- `FormaPro/12_Templates_HTML/template_fiche_memo.html`
- `FormaPro/12_Templates_HTML/template_evaluation.html`
- `FormaPro/12_Templates_HTML/template_carte_sos.html`

### Fichiers modifiés

- `FormaPro/RAPPORT_GENERATION.md` : ajout du suivi de PHASE 3.
- `FormaPro/RAPPORT_GENERATION.html` : ajout du suivi de PHASE 3.

### Choix pédagogiques

- Templates pensés pour grands débutants : titres explicites, étapes courtes, checklists, feedback rassurant.
- Corrigés et indices masqués par défaut dans les templates stagiaires et exercices.
- Guide formateur structuré avec préparation, timeline, consignes stagiaires, réponses, variantes et synthèse.
- Évaluation sans notation humiliante, avec réponses : `Je ne sais pas encore`, `Je sais un peu`, `Je sais faire seul`.

### Choix graphiques

- Application des thèmes définis en PHASE 2 : général, Word, Excel, PowerPoint.
- Boutons larges, cartes pédagogiques, encadrés, badges, grilles responsive.
- Hiérarchie visuelle sobre et cohérente.

### Choix techniques

- Chaque template contient son CSS dans une balise `<style>`.
- Chaque template contient son JavaScript dans une balise `<script>`.
- Chaque template contient une règle `@media print`.
- Aucun CDN, aucune dépendance externe, aucun framework, aucun appel Internet.
- Interactions intégrées : accordéons, afficher/masquer, checklists, quiz, recherche locale, filtres simples ou progression selon le template.
- `localStorage` utilisé uniquement dans les templates qui mémorisent des checklists, avec fonctions non bloquantes.

### Liens vérifiés

- Tous les templates contiennent un lien relatif de retour vers `../00_Index_general/index.html`.
- Cible non présente à ce stade, car l'index général doit être créé en PHASE 10.
- Aucun autre lien interne de navigation créé pendant cette phase.

### Vérifications effectuées

- Les 7 templates attendus sont présents.
- Présence vérifiée de `<style>`, `<script>` et `@media print` dans chaque template.
- Recherche effectuée sur dépendances externes : aucun `http://`, `https://`, CDN, `@import`, script externe ou feuille externe détecté.

### Ressources manquantes ou non créées à ce stade

- `CONTENT_PLAN.md`
- `TASKS.md`
- `QA_CHECKLIST.md`
- Tous les supports finaux Word, Excel et PowerPoint.
- Tous les exercices finaux, corrigés finaux, fichiers de départ, fiches mémo finales, évaluations finales, projet fil rouge, mini-défis, cartes SOS finales et index général.

Ces éléments ne sont pas générés en PHASE 3 afin de respecter la consigne : exécuter uniquement la phase demandée.

### Limites

- Les templates contiennent des placeholders `{{...}}` à remplacer lors des phases de génération de contenu.
- Le lien retour index est volontairement non résolu tant que la PHASE 10 n'a pas créé `00_Index_general/index.html`.
- Aperçu navigateur intégré tenté sur `template_support_stagiaire.html`, mais bloqué par l'absence de l'extension Playwright dans Chrome.
- Vérifications structurelles effectuées par inspection locale des fichiers.

### Points à vérifier avant PHASE 4

- Valider les templates comme base commune.
- Lancer ensuite uniquement la PHASE 4 pour générer le module Word.

---

## Mise à jour - PHASE 4

Date de mise à jour : 27 mai 2026

### Phase effectuée

- PHASE 4 uniquement : génération du module Word.

### Fichiers créés

Guides formateur Word :

- `FormaPro/02_Guide_formateur_HTML/Jour_1_Word.html`
- `FormaPro/02_Guide_formateur_HTML/Jour_2_Word.html`
- `FormaPro/02_Guide_formateur_HTML/Jour_3_Word_Excel.html`

Support stagiaire Word :

- `FormaPro/03_Supports_stagiaires_HTML/Support_Word_Debutant.html`

Exercices Word :

- `FormaPro/04_Exercices_HTML/Word/Word_01_Mettre_en_forme_un_texte_brut.html`
- `FormaPro/04_Exercices_HTML/Word/Word_02_Creer_un_courrier_professionnel.html`
- `FormaPro/04_Exercices_HTML/Word/Word_03_Inserer_image_et_tableau.html`
- `FormaPro/04_Exercices_HTML/Word/Word_04_Creer_une_fiche_de_presentation.html`
- `FormaPro/04_Exercices_HTML/Word/Word_05_Corriger_un_document_mal_presente.html`

Corrigés Word :

- `FormaPro/05_Corriges_HTML/Word/Corrige_Word_01_Mettre_en_forme_un_texte_brut.html`
- `FormaPro/05_Corriges_HTML/Word/Corrige_Word_02_Creer_un_courrier_professionnel.html`
- `FormaPro/05_Corriges_HTML/Word/Corrige_Word_03_Inserer_image_et_tableau.html`
- `FormaPro/05_Corriges_HTML/Word/Corrige_Word_04_Creer_une_fiche_de_presentation.html`
- `FormaPro/05_Corriges_HTML/Word/Corrige_Word_05_Corriger_un_document_mal_presente.html`

Fichiers de départ Word :

- `FormaPro/06_Fichiers_de_depart/Word/Word_01_Texte_brut_evenement.txt`
- `FormaPro/06_Fichiers_de_depart/Word/Word_02_Courrier_professionnel_brut.txt`
- `FormaPro/06_Fichiers_de_depart/Word/Word_03_Contenu_image_tableau.txt`
- `FormaPro/06_Fichiers_de_depart/Word/Word_04_Fiche_presentation_brut.txt`
- `FormaPro/06_Fichiers_de_depart/Word/Word_05_Document_mal_presente.txt`
- `FormaPro/06_Fichiers_de_depart/Word/image_placeholder_accueil.svg`

### Fichiers modifiés

- `FormaPro/RAPPORT_GENERATION.md` : ajout du suivi de PHASE 4.
- `FormaPro/RAPPORT_GENERATION.html` : ajout du suivi de PHASE 4.

### Choix pédagogiques

- Module Word réparti sur 18 h : Jour 1 = 7 h, Jour 2 = 7 h, Jour 3 = 4 h Word.
- Progression grands débutants : ouvrir, enregistrer, saisir, sélectionner, mettre en forme, structurer, insérer image/tableau, imprimer/exporter.
- Exercices formulés comme situations professionnelles simples : réunion, courrier, accueil participants, fiche de présentation, compte rendu.
- Corrigés pensés pour correction formateur et correction collective.
- `Jour_3_Word_Excel.html` contient uniquement la partie Word ; la partie Excel est explicitement réservée à la PHASE 5.

### Choix graphiques

- Palette Word respectée : `#185ABD`, `#2B579A`, `#41A5EE`, `#F3F7FF`.
- Présentation claire : badges, cartes, encadrés, checklists, accordéons.
- Corrigés masqués par défaut dans les exercices et accessibles via bouton.

### Choix techniques

- Tous les HTML Word créés sont standalone.
- Chaque HTML contient CSS intégré dans `<style>`.
- Chaque HTML contient JavaScript intégré dans `<script>`.
- Chaque HTML contient `@media print`.
- Aucun CDN, aucune dépendance externe, aucun framework, aucun appel Internet.
- Fichiers de départ créés en `.txt` et `.svg` local.

### Liens vérifiés

- Liens entre support Word, exercices Word, corrigés Word et fichiers de départ Word vérifiés.
- Liens relatifs non résolus uniquement vers `../00_Index_general/index.html`, attendu car l'index général sera créé en PHASE 10.

### Vérifications effectuées

- Présence des fichiers Word attendus vérifiée.
- Recherche effectuée sur dépendances externes : aucun `http://`, `https://`, CDN, `@import`, script externe ou feuille externe détecté.
- Présence de `<style>`, `<script>` et `@media print` vérifiée sur les HTML Word.

### Ressources manquantes ou non créées à ce stade

- Module Excel.
- Module PowerPoint.
- Projet fil rouge.
- Évaluations.
- Fiches mémo interactives.
- Cartes SOS.
- Index général.
- Vue d'ensemble générale.
- Guide formateur général.
- Mini-défis intersessions.

Ces éléments ne sont pas générés en PHASE 4 afin de respecter la consigne : exécuter uniquement la phase demandée.

### Limites

- Le PDF officiel n'a pas été extrait automatiquement ; le contenu Word est construit à partir de la spécification et du programme officiel.
- `Jour_3_Word_Excel.html` devra être complété côté Excel en PHASE 5.
- Les liens retour vers l'index resteront non résolus jusqu'à la PHASE 10.
- Aperçu navigateur intégré non relancé, car l'extension Playwright était absente lors de la PHASE 3.

### Points à vérifier avant PHASE 5

- Valider le module Word.
- Lancer ensuite uniquement la PHASE 5 pour générer le module Excel et compléter la partie Excel du Jour 3.

---

## Mise à jour - PHASES 5 à 12

Date de mise à jour : 27 mai 2026

### Phases effectuées

- PHASE 5 : module Excel généré et vérifié.
- PHASE 6 : module PowerPoint généré et vérifié.
- PHASE 7 : projet fil rouge généré et vérifié.
- PHASE 8 : évaluations générées et vérifiées.
- PHASE 9 : fiches mémo et cartes SOS générées et vérifiées.
- PHASE 10 : index général, vue d'ensemble, guide général et mini-défis générés et vérifiés.
- PHASE 11 : vérification finale effectuée.
- PHASE 12 : rapport final, plan de contenu, tâches et checklist QA mis à jour.

### Inventaire créé ou complété

- Module Excel : support stagiaire, exercices, corrigés, fichiers de départ XLSX, guides jours 3, 4 et 5.
- Module PowerPoint : support stagiaire, 4 exercices, 4 corrigés, fichiers de départ locaux, guide jour 6.
- Projet fil rouge : 5 pages HTML.
- Évaluations : 5 pages HTML.
- Fiches mémo : 6 pages HTML.
- Cartes SOS : index + 8 cartes HTML.
- Mini-défis intersessions : 5 pages HTML.
- Administration : index général, vue d'ensemble, guide formateur général.
- Documents de pilotage : `CONTENT_PLAN.md`, `TASKS.md`, `QA_CHECKLIST.md`.
- Asset optionnel : `FormaPro/13_Assets_optionnels/generate_phases_5_12.py`, générateur local utilisé pour produire les phases 5 à 12.

### Résultat d'inventaire final

- HTML présents : 80.
- Fichiers attendus contrôlés : aucun manquant.
- Liens HTML relatifs : tous résolus.
- HTML avec `<style>`, `<script>` et `@media print` : OK.

### Vérifications

- HTML standalone : OK.
- CSS intégré : OK.
- JavaScript intégré : OK.
- Mode impression `@media print` : OK.
- CDN / dépendances externes : aucune détectée dans les HTML.
- Liens internes : vérifiés après création de l'index général.

### Limites

- Aucun fichier source original ni PDF source modifié.
- Les fichiers de départ Excel sont désormais générés en `.xlsx`. Les fichiers natifs Word et PowerPoint ne sont pas générés.
- Aperçu navigateur intégré non utilisé car l'extension Playwright était absente.
---

## Mise à jour - enrichissement Excel INI

Date de mise à jour : 28 mai 2026

Sources utilisées :

- `C:\Users\jboul\OneDrive\professionnel\Formations\office\Excel\Excel Ini\PLAN COMPLET Excel INI.docx`
- `C:\Users\jboul\OneDrive\professionnel\Formations\office\Excel\Excel Ini\Plan concis Excel Ini.docx`
- `C:\Users\jboul\OneDrive\professionnel\Formations\office\Excel\Excel Ini\opérateurs de calcul.docx`

### Contenu enrichi

- Support stagiaire Excel remplacé par une version restructurée issue des plans Excel INI.
- Plan de cours séquencé ajouté : démarrage, feuilles, saisie, mise en forme, fonctions, opérateurs, séries, impression, graphiques, MFC.
- Section opérateurs de calcul ajoutée : arithmétiques, comparaison, texte, références et ordre de priorité.
- Guides formateur jours 3, 4 et 5 enrichis : démarrage, saisie, formats, fonctions, séries, impression, références absolues, graphiques, notes, mise en forme conditionnelle et interaction Word.
- Exercices Excel portés à 10 cas pratiques.
- Corrigés Excel portés à 10 pages formateur.
- Fichiers de départ Excel convertis en `.xlsx` : participants, budget, erreurs, frais vacances, séries/recopie, commissions, graphique + mise en forme conditionnelle.

### Vérifications ciblées

- HTML Excel standalone : OK après génération.
- Liens internes Excel : OK.
- Fichier source DOCX original : non modifié.
- HTML présents après enrichissement : 88.

---

## Mise à jour - refonte supports autonomes

Date de mise à jour : 28 mai 2026

### Supports refondus

- `Support_Word_Debutant.html` : parcours pas-à-pas, gestes de base, mise en forme, page, images/tableaux, contrôle final.
- `Support_Excel_Debutant.html` : démarrage, saisie, tableaux, formules, références, impression, graphiques, contrôle final.
- `Support_PowerPoint_Debutant.html` : structure, diapositives, visuels, graphiques, oral, contrôle final.

### Choix de refonte

- Les exercices HTML/CSS existants sont conservés.
- Les supports contiennent des procédures concrètes, erreurs fréquentes, solutions de dépannage, mini-entraînements et checklists.
- Source de génération ajoutée : `FormaPro/13_Assets_optionnels/refonte_supports_autonomie.py`.
- Enrichissement Word depuis `C:\Users\jboul\OneDrive\professionnel\Formations\office\Word\support.md` : interface, sauvegarde, raccourcis, styles, table des matières, QuickParts, numérotation, CV/candidature.

---

## Mise à jour - projet fil rouge concret

Date de mise à jour : 28 mai 2026

### Contenu refondu

- Projet fil rouge remplacé par un scénario réaliste : `Forum Découverte Métiers et Formation`, le jeudi 9 juillet 2026 à Lille.
- Liste précise des livrables Word, Excel, PowerPoint et PDF à réaliser.
- Sources concrètes ajoutées : participants, budget, programme, intervenants, notes organisation.
- Version simplifiée, version bonus et grille de correction alignées sur le même scénario.

### Fichiers créés ou modifiés

- `FormaPro/09_Projet_fil_rouge_HTML/Projet_fil_rouge.html`
- `FormaPro/09_Projet_fil_rouge_HTML/Brief_projet.html`
- `FormaPro/09_Projet_fil_rouge_HTML/Sources_projet.html`
- `FormaPro/09_Projet_fil_rouge_HTML/Grille_correction_projet.html`
- `FormaPro/09_Projet_fil_rouge_HTML/Version_simplifiee.html`
- `FormaPro/09_Projet_fil_rouge_HTML/Version_bonus.html`
- `FormaPro/06_Fichiers_de_depart/Projet_fil_rouge/participants_forum_metiers.xlsx`
- `FormaPro/06_Fichiers_de_depart/Projet_fil_rouge/budget_forum_metiers.xlsx`
- `FormaPro/06_Fichiers_de_depart/Projet_fil_rouge/donnees_restitution_forum_metiers.xlsx`
- `FormaPro/06_Fichiers_de_depart/Projet_fil_rouge/programme_forum_metiers.txt`
- `FormaPro/06_Fichiers_de_depart/Projet_fil_rouge/brief_intervenants_forum_metiers.txt`
- `FormaPro/06_Fichiers_de_depart/Projet_fil_rouge/notes_organisation_forum_metiers.txt`

### Données concrètes intégrées

- 24 participants fictifs nommés.
- Budget maximum : 1 200,00 €.
- Budget prévu : 1 028,55 €.
- Reste disponible : 171,45 €.
- Planning horaire de 13h30 à 16h55.
- 5 intervenants avec rôles et contributions.

### Vérifications

- HTML présents après refonte : 89.
- Liens HTML relatifs : OK.
- HTML standalone (`<style>`, `<script>`, `@media print`) : OK.
- Dépendances externes dans les HTML : aucune détectée.
- Fichiers `.xlsx` sources : ouvrables, formules sans erreur détectée.

---

## Mise à jour - livrables et charte projet

Date de mise à jour : 28 mai 2026

### Ajouts

- Page `Livrables_projet.html` : liste précise des fichiers Word, Excel, PowerPoint et PDF à produire.
- Page `Charte_graphique_projet.html` : logos, photos, palette, règles d'utilisation et choix stagiaire.
- Pack visuel généré avec imagegen puis copié dans `FormaPro/06_Fichiers_de_depart/Projet_fil_rouge/Visuels/`.
- 4 options de logo, 9 photos d'ambiance et 1 fond abstrait PowerPoint disponibles.

### Ressources visuelles

- `logo_01_bleu_orientation.png`
- `logo_02_vert_progression.png`
- `logo_03_orange_rencontre.png`
- `logo_04_slate_competences.png`
- `photo_accueil_forum_metiers.png`
- `photo_atelier_excel_budget.png`
- `photo_documents_word_programme.png`
- `photo_presentation_powerpoint.png`
- `photo_preparation_salle_forum.png`
- `photo_accompagnement_cv_word.png`
- `photo_echange_recruteur_participants.png`
- `photo_tableau_bord_excel.png`
- `photo_table_ronde_metiers.png`
- `fond_abstrait_powerpoint_16_9.png`

### Vérifications

- HTML présents après ajout : 91.
- Liens HTML et images locales : OK.
- HTML standalone (`<style>`, `<script>`, `@media print`) : OK.
- Dépendances externes dans les HTML : aucune détectée.

---

## Mise à jour - images complémentaires

Date de mise à jour : 28 mai 2026

- 6 nouvelles images générées avec imagegen et copiées dans `FormaPro/06_Fichiers_de_depart/Projet_fil_rouge/Visuels/`.
- Total du pack visuel projet : 15 fichiers PNG.
- Charte graphique mise à jour pour proposer plus de choix aux stagiaires.

Nouvelles ressources :

- `photo_preparation_salle_forum.png`
- `photo_accompagnement_cv_word.png`
- `photo_echange_recruteur_participants.png`
- `photo_tableau_bord_excel.png`
- `photo_table_ronde_metiers.png`
- `fond_abstrait_powerpoint_16_9.png`
