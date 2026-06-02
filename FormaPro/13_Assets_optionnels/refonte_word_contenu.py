from pathlib import Path
import re
import unicodedata

from generate_phases_5_12 import BASE_CSS, BASE_JS


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parent
SOURCE = PROJECT / "contenuFormationWord.md"

EXTRA_CSS = """
.source-note{font-size:.92rem;color:#64748B;margin-top:.75rem}
.table-scroll{overflow-x:auto;margin-top:1rem}.table-scroll table{min-width:760px}
.lesson{background:#fff;border:1px solid var(--b);border-radius:var(--r);padding:1.15rem;margin-bottom:1rem}
.lesson h3{margin-top:0}.compact-list li{margin-bottom:.35rem}
.split{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem}
.flow{display:grid;grid-template-columns:repeat(5,1fr);gap:.75rem;margin:1rem 0}
.flow .card{min-height:100%;border-top:4px solid var(--p)}
.badge.soft{background:var(--bg);color:var(--s)}
.day-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:1rem}
.memo-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
.search-item .content ol{margin-top:.25rem}
header .wrap,main.wrap>*{animation:none!important}
@media(max-width:900px){.split,.day-grid,.memo-grid{grid-template-columns:1fr}.flow{grid-template-columns:repeat(2,1fr)}.table-scroll table{min-width:640px}}
@media(max-width:640px){.flow{grid-template-columns:1fr}}
"""

SOURCE_CHECKS = [
    "un bon document Word est un document structuré avant d’être décoré",
    "Les caractères invisibles",
    "sauts de page et sauts de section",
    "Publipostage",
    "Accessibilité",
]


def ensure_source():
    text = SOURCE.read_text(encoding="utf-8")
    missing = [phrase for phrase in SOURCE_CHECKS if phrase.lower() not in text.lower()]
    if missing:
        raise RuntimeError("Source Word incomplète : " + ", ".join(missing))
    return text


def slug(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value[:48] or "word"


def write_formapro(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def nav(prefix):
    return f"""
  <nav class="site-nav no-print">
    <a class="site-nav-logo" href="{prefix}/00_Index_general/index.html">
      <span class="site-nav-logo-icon">
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><rect x="2" y="2" width="10" height="2" rx="1" fill="white"/><rect x="2" y="6" width="7" height="2" rx="1" fill="white"/><rect x="2" y="10" width="5" height="2" rx="1" fill="white"/></svg>
      </span>
      Formation Office
    </a>
    <div class="site-nav-tabs">
      <a href="{prefix}/03_Supports_stagiaires_HTML/Support_Word_Debutant.html" class="word-active">Word</a>
      <a href="{prefix}/03_Supports_stagiaires_HTML/Support_Excel_Debutant.html">Excel</a>
      <a href="{prefix}/03_Supports_stagiaires_HTML/Support_PowerPoint_Debutant.html">PowerPoint</a>
    </div>
  </nav>
"""


def page(title, subtitle, prefix, body, badges, label):
    badge_html = "".join(f'<span class="badge">{badge}</span>' for badge in badges)
    return f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>{BASE_CSS}{EXTRA_CSS}</style>
  <link rel="stylesheet" href="{prefix}/assets/formapro-design.css">
</head>
<body class="theme-word">
{nav(prefix)}
  <header>
    <div class="wrap">
      <a class="top no-print" href="{prefix}/00_Index_general/index.html">Retour à l'index général</a>
      <p class="section-label">{label}</p>
      <h1>{title}</h1>
      <p class="lead">{subtitle}</p>
      <div class="meta">{badge_html}<span class="badge soft">Source : contenuFormationWord.md</span></div>
      <div class="actions no-print"><button type="button" onclick="window.print()">Imprimer / Exporter en PDF</button><button type="button" class="secondary" data-open-all>Tout ouvrir</button><button type="button" class="secondary" data-close-all>Tout fermer</button></div>
    </div>
  </header>
  <main class="wrap">
    {body}
  </main>
  <script>{BASE_JS}</script>
</body>
</html>
"""


def panel(title, content, ident=None):
    attr = f' id="{ident}"' if ident else ""
    return f'<section class="panel"{attr}><h2>{title}</h2>{content}</section>'


def lesson(title, content):
    return f'<article class="lesson"><h3>{title}</h3>{content}</article>'


def cards(items, klass="grid"):
    return f'<section class="{klass}">' + "".join(f'<article class="card"><h3>{title}</h3>{content}</article>' for title, content in items) + "</section>"


def ul(items, klass="compact-list"):
    return f'<ul class="{klass}">' + "".join(f"<li>{item}</li>" for item in items) + "</ul>"


def steps(items):
    return '<ol class="steps">' + "".join(f"<li><span>{item}</span></li>" for item in items) + "</ol>"


def checklist(items, cid):
    return f'<ul class="checklist" data-checklist-id="{slug(cid)}">' + "".join(f'<li><input type="checkbox"><span>{item}</span></li>' for item in items) + "</ul>"


def accordion(label, content):
    return f'<div class="accordion"><button type="button" aria-expanded="false">{label}</button><div class="content">{content}</div></div>'


def table(headers, rows):
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>" for row in rows)
    return f'<div class="table-scroll"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def toc(items):
    return '<nav class="toc"><ul>' + "".join(f'<li><a href="#{ident}">{label}</a></li>' for ident, label in items) + "</ul></nav>"


def quiz(question, answers, good):
    buttons = "".join(f'<button type="button" data-choice="{key}">{label}</button>' for key, label in answers)
    return f'<section class="panel"><h2>Quiz rapide</h2><p><strong>{question}</strong></p><div class="quiz-options" data-answer="{good}">{buttons}</div><p class="feedback" aria-live="polite"></p></section>'


def word_support():
    body = toc([
        ("logique", "Logique Word"),
        ("depart", "Départ"),
        ("texte", "Texte"),
        ("structure", "Styles"),
        ("page", "Page"),
        ("objets", "Objets"),
        ("avance", "Fonctions avancées"),
        ("finaliser", "Finaliser"),
        ("exercices", "Exercices"),
    ])
    body += panel(
        "La règle de travail : structurer avant de décorer",
        '<p>Un bon document Word est un document structuré avant d’être décoré. On rédige le contenu, on indique sa structure, puis seulement on règle l’apparence.</p>'
        + '<section class="flow">'
        + ''.join([
            '<article class="card"><h3>1. Rédiger</h3><p>Écrire le contenu sans chercher la mise en forme parfaite.</p></article>',
            '<article class="card"><h3>2. Organiser</h3><p>Découper en paragraphes, listes et parties.</p></article>',
            '<article class="card"><h3>3. Structurer</h3><p>Appliquer Normal, Titre 1, Titre 2.</p></article>',
            '<article class="card"><h3>4. Présenter</h3><p>Régler police, espacements, marges, tableaux et images.</p></article>',
            '<article class="card"><h3>5. Finaliser</h3><p>Relire, vérifier l’accessibilité, exporter en PDF.</p></article>',
        ])
        + '</section>'
        + table(["Niveau Word", "Ce que cela contrôle", "Erreur classique"], [
            ["Caractère", "Un mot ou quelques lettres : police, gras, couleur.", "Mettre chaque titre en forme à la main."],
            ["Paragraphe", "Alignement, retrait, interligne, espace avant/après.", "Appuyer plusieurs fois sur Entrée pour aérer."],
            ["Page", "Marges, orientation, taille du papier.", "Découvrir le problème seulement à l’impression."],
            ["Section", "Une partie avec sa propre mise en page.", "Supprimer un saut de section sans comprendre son rôle."],
            ["Document", "Structure globale, styles, champs, export.", "Envoyer sans relecture ni PDF."],
        ]),
        "logique",
    )
    body += panel(
        "Créer, enregistrer, retrouver",
        lesson("Premier réflexe", steps([
            "Ouvrir Word, créer un document vierge.",
            "Enregistrer sous avant de travailler longtemps.",
            "Choisir un dossier connu et un nom clair : <code>Courrier_relance_NomPrenom.docx</code>.",
            "Utiliser <span class=\"kbd\">Ctrl</span> + <span class=\"kbd\">S</span> après chaque étape importante.",
            "Exporter en PDF seulement quand le document est relu et stabilisé.",
        ]))
        + lesson("Interface utile", table(["Onglet", "Usage prioritaire"], [
            ["Fichier", "Nouveau, ouvrir, enregistrer, imprimer, exporter."],
            ["Accueil", "Police, paragraphes, listes, styles, rechercher/remplacer."],
            ["Insertion", "Pages, tableaux, images, formes, en-tête, pied, numéro de page."],
            ["Disposition / Mise en page", "Marges, orientation, sauts de page, sauts de section."],
            ["Références", "Table des matières, notes, légendes, renvois."],
            ["Révision", "Orthographe, commentaires, suivi des modifications."],
            ["Affichage", "Règle, volet de navigation, zoom, modes d’affichage."],
        ])),
        "depart",
    )
    body += panel(
        "Saisir, sélectionner, corriger",
        '<section class="split">'
        + lesson("Saisie propre", ul([
            "Ne pas appuyer sur Entrée à la fin de chaque ligne : Word revient à la ligne seul.",
            "Entrée crée un nouveau paragraphe.",
            "Maj+Entrée crée un retour à la ligne dans le même paragraphe.",
            "Tabulation sert à se déplacer dans une structure, pas à aligner un texte à coups d’espaces.",
        ]))
        + lesson("Sélection efficace", ul([
            "Double-clic : sélectionner un mot.",
            "Triple-clic : sélectionner un paragraphe.",
            "Ctrl+A : tout sélectionner.",
            "Ctrl+Z : annuler immédiatement une mauvaise manipulation.",
        ]))
        + '</section>'
        + lesson("Caractères invisibles", '<p>Afficher ¶ permet de voir les espaces, tabulations, retours, sauts de page et sauts de section. C’est le premier outil de diagnostic quand un document bouge.</p>')
        + table(["Symbole", "Signification", "Action utile"], [
            ["·", "Espace", "Supprimer les espaces multiples."],
            ["→", "Tabulation", "Remplacer les alignements bricolés."],
            ["¶", "Fin de paragraphe", "Éviter les lignes vides répétées."],
            ["Saut de page", "Nouvelle page forcée", "Garder si le changement de page est voulu."],
            ["Saut de section", "Nouvelle zone de mise en page", "Vérifier avant suppression."],
        ]),
        "texte",
    )
    body += panel(
        "Styles, titres, listes et table des matières",
        lesson("Styles", '<p>Un style applique plusieurs réglages et donne une identité au texte. Un titre en gras n’est pas un vrai titre pour Word. Un texte en <strong>Titre 1</strong> ou <strong>Titre 2</strong> devient exploitable dans le volet de navigation et la table des matières.</p>')
        + table(["Besoin", "Commande Word", "Résultat"], [
            ["Titre principal", "Accueil > Styles > Titre 1", "Structure reconnue."],
            ["Sous-partie", "Accueil > Styles > Titre 2", "Hiérarchie claire."],
            ["Texte courant", "Normal", "Document homogène."],
            ["Table des matières", "Références > Table des matières automatique", "Sommaire généré depuis les styles."],
        ])
        + lesson("Listes", ul([
            "Puces : éléments sans ordre.",
            "Numéros : étapes à suivre dans l’ordre.",
            "Multiniveau : plan, clauses, grandes parties.",
            "Si la numérotation recommence mal, utiliser les options de liste plutôt que taper les numéros à la main.",
        ])),
        "structure",
    )
    body += panel(
        "Mise en page, sections, en-têtes et numérotation",
        lesson("Mise en page", steps([
            "Régler les marges avant de finaliser.",
            "Choisir Portrait pour courrier ou fiche ; Paysage seulement pour un tableau large.",
            "Utiliser un saut de page pour commencer une nouvelle page.",
            "Utiliser un saut de section pour changer orientation, marges, colonnes, en-tête ou numérotation sur une partie.",
        ]))
        + lesson("En-têtes et pieds de page", ul([
            "En-tête : informations répétées en haut : logo, titre, service.",
            "Pied de page : date, contact, numéro de page, mention courte.",
            "Première page différente : utile pour une page de garde non numérotée.",
            "Lier au précédent : à vérifier quand plusieurs sections existent.",
        ])),
        "page",
    )
    body += panel(
        "Tableaux, images, légendes",
        '<section class="split">'
        + lesson("Tableaux Word", ul([
            "À utiliser pour des données courtes, lisibles dans le document.",
            "Ajouter une ligne d’en-tête claire.",
            "Répéter la ligne d’en-tête si le tableau passe sur plusieurs pages.",
            "Pour calculs lourds, préparer dans Excel puis copier proprement.",
        ]))
        + lesson("Images et objets", ul([
            "Redimensionner depuis un coin pour ne pas déformer.",
            "Choisir un habillage : aligné sur le texte pour débuter, carré si le texte doit entourer.",
            "Ajouter un texte alternatif si l’image porte une information.",
            "Ajouter une légende quand l’image ou le tableau doit être référencé.",
        ]))
        + '</section>',
        "objets",
    )
    body += panel(
        "Fonctions avancées à connaître",
        cards([
            ("Documents longs", "<p>Styles, table des matières, légendes, renvois, notes de bas de page et volet de navigation deviennent indispensables.</p>"),
            ("Modèles", "<p>Un modèle évite de repartir de zéro : courrier, compte rendu, attestation, procédure, fiche client.</p>"),
            ("Révision", "<p>Commentaires et suivi des modifications permettent de corriger sans perdre l’historique.</p>"),
            ("Publipostage", "<p>Document principal + base de données + champs de fusion pour produire courriers, étiquettes ou convocations.</p>"),
            ("Formulaires", "<p>Contrôles de contenu, listes déroulantes, cases à cocher et protection du formulaire.</p>"),
            ("Champs", "<p>Date, numéro de page, table des matières et renvois doivent être mis à jour avant export.</p>"),
        ]),
        "avance",
    )
    body += panel(
        "Contrôle final avant envoi",
        checklist([
            "Le fichier est enregistré au bon endroit avec un nom explicite.",
            "Les caractères invisibles ne montrent pas d’espaces ou paragraphes vides inutiles.",
            "Les titres utilisent les styles Word.",
            "Les listes sont de vraies listes, pas des tirets tapés à la main.",
            "Marges, orientation, en-têtes, pieds et numéros sont vérifiés en aperçu avant impression.",
            "Images et tableaux restent lisibles et ne coupent pas le texte.",
            "Orthographe, grammaire et accessibilité sont vérifiées.",
            "La version PDF a été ouverte pour contrôle.",
        ], "controle-final-word"),
        "finaliser",
    )
    body += panel(
        "Exercices guidés",
        checklist([
            '<a href="../04_Exercices_HTML/Word/Word_01_Mettre_en_forme_un_texte_brut.html">Word 01 - Structurer un texte brut</a> : sélection, paragraphes, caractères invisibles, styles simples.',
            '<a href="../04_Exercices_HTML/Word/Word_02_Creer_un_courrier_professionnel.html">Word 02 - Courrier professionnel</a> : mise en page, objet, formule, PDF.',
            '<a href="../04_Exercices_HTML/Word/Word_03_Inserer_image_et_tableau.html">Word 03 - Image et tableau</a> : habillage, tableau lisible, texte alternatif.',
            '<a href="../04_Exercices_HTML/Word/Word_04_Creer_une_fiche_de_presentation.html">Word 04 - Fiche structurée</a> : titres, styles, listes, modèle réutilisable.',
            '<a href="../04_Exercices_HTML/Word/Word_05_Corriger_un_document_mal_presente.html">Word 05 - Diagnostic</a> : réparer espaces, paragraphes, numérotation, pages et export.',
        ], "support-word-exercices")
        + quiz("Pourquoi utiliser un style Titre 1 plutôt qu’un titre mis en gras à la main ?", [
            ("A", "Pour que Word reconnaisse la structure du document."),
            ("B", "Pour changer seulement la couleur du titre."),
            ("C", "Pour empêcher l’impression."),
        ], "A"),
        "exercices",
    )
    return page(
        "Word : créer des documents professionnels structurés",
        "Support stagiaire refondu depuis le parcours complet Word : logique du document, gestes de base, styles, mise en page, objets, finalisation.",
        "..",
        body,
        ["Word", "Support stagiaire", "Débutant à autonome", "18 h"],
        "Support stagiaire",
    )


def guide_day_1():
    body = panel(
        "Objectifs de la journée",
        '<p>Installer les réflexes de base : enregistrer, saisir sans casser les lignes, sélectionner, afficher ¶, mettre en forme sobrement.</p>'
        + checklist([
            "Chaque stagiaire sait créer et retrouver son fichier.",
            "Chaque stagiaire sait expliquer : je sélectionne d’abord, j’applique ensuite.",
            "Chaque stagiaire sait afficher les caractères invisibles.",
            "Chaque stagiaire produit un texte propre exportable en PDF.",
        ], "jour-1-objectifs")
        + '<p class="source-note">Modules source : comprendre Word, interface, saisie, caractères invisibles, mise en forme.</p>',
    )
    body += panel(
        "Déroulé horaire",
        table(["Heure", "Séquence", "Message formateur"], [
            ["09:00", "Accueil et cadre", "Droit à l’erreur, lenteur utile, sauvegarde fréquente."],
            ["09:30", "Créer et enregistrer", "Fichier > Enregistrer sous ; nom clair ; dossier visible."],
            ["10:15", "Interface Word", "Fichier, Accueil, Insertion, Disposition, Révision, Affichage."],
            ["11:00", "Saisie propre", "Entrée = paragraphe ; Word gère les retours à la ligne."],
            ["13:30", "Sélection et correction", "Mot, ligne, paragraphe, tout le document ; Ctrl+Z."],
            ["14:30", "Caractères invisibles", "Diagnostiquer espaces, tabulations, paragraphes vides."],
            ["15:15", "Mise en forme caractères et paragraphes", "Hiérarchiser sans décorer partout."],
            ["16:15", "Exercice Word 01", "Transformer le texte brut en fiche lisible."],
        ]),
    )
    body += panel(
        "Démonstration clé",
        '<section class="day-grid">'
        + lesson("Le formateur montre", steps([
            "Créer un document et l’enregistrer sous un nom explicite.",
            "Saisir un titre et trois paragraphes sans retours de ligne inutiles.",
            "Afficher ¶ et expliquer les marques visibles.",
            "Sélectionner le titre, appliquer un style ou une mise en forme simple.",
            "Exporter en PDF et ouvrir le PDF pour vérifier.",
        ]))
        + lesson("Les stagiaires reformulent", ul([
            "Où est enregistré mon fichier ?",
            "Qu’est-ce qu’un paragraphe ?",
            "Quel symbole montre une fin de paragraphe ?",
            "Pourquoi sélectionner avant de cliquer ?",
        ]))
        + '</section>',
    )
    body += panel(
        "Vigilance formateur",
        cards([
            ("Espaces pour aligner", "<p>Montrer ¶, supprimer les espaces multiples, utiliser alignement ou tabulation.</p>"),
            ("Entrée répétée", "<p>Remplacer par espace avant/après paragraphe.</p>"),
            ("Tout le texte modifié", "<p>Ctrl+Z, sélectionner seulement la zone voulue, refaire lentement.</p>"),
        ], "grid"),
    )
    body += panel(
        "Fichiers et fin de séance",
        ul([
            '<a href="../03_Supports_stagiaires_HTML/Support_Word_Debutant.html">Support Word stagiaire</a>',
            '<a href="../04_Exercices_HTML/Word/Word_01_Mettre_en_forme_un_texte_brut.html">Exercice Word 01</a>',
            '<a href="../07_Fiches_memo_interactives/Fiche_memo_Word.html">Fiche mémo Word</a>',
        ])
        + checklist([
            "Tous les fichiers sont enregistrés.",
            "Exercice 01 corrigé collectivement.",
            "Chaque stagiaire sait retrouver le PDF exporté.",
        ], "jour-1-fin"),
    )
    return page("Jour 1 - Word : premiers réflexes professionnels", "Créer un document propre, comprendre l’interface, saisir, sélectionner, corriger et formater sans bricolage.", "..", body, ["Word", "Guide formateur", "7 h", "Mardi 2 juin"], "Guide formateur")


def guide_day_2():
    body = panel(
        "Objectifs de la journée",
        '<p>Passer du texte propre au document structuré : styles, listes, mise en page, en-têtes, pieds, tableaux et images.</p>'
        + checklist([
            "Les stagiaires distinguent mise en forme manuelle et styles.",
            "Les titres peuvent alimenter une table des matières.",
            "Les sauts de page et de section sont identifiés.",
            "Un tableau et une image sont insérés sans casser la page.",
        ], "jour-2-objectifs")
        + '<p class="source-note">Modules source : styles, listes, mise en page, en-têtes/pieds, tableaux, images.</p>',
    )
    body += panel(
        "Déroulé horaire",
        table(["Heure", "Séquence", "Message formateur"], [
            ["09:00", "Réactivation J1", "Afficher ¶, retrouver le fichier, sélectionner proprement."],
            ["09:30", "Styles", "Un style donne une structure, pas seulement une apparence."],
            ["10:30", "Titres et table des matières", "Titre 1 / Titre 2 > Références > Table automatique."],
            ["11:15", "Listes", "Puces pour éléments ; numéros pour procédure ; éviter les numéros tapés."],
            ["13:30", "Mise en page", "Marges, orientation, sauts de page, sauts de section."],
            ["14:30", "En-tête, pied, numéros", "Première page différente ; lien au précédent."],
            ["15:15", "Tableaux et images", "Ligne d’en-tête, habillage, redimensionnement, texte alternatif."],
            ["16:15", "Exercices 02 à 04", "Courrier, image/tableau, fiche de présentation."],
        ]),
    )
    body += panel(
        "Ateliers conseillés",
        cards([
            ("Atelier courrier", '<p><a href="../04_Exercices_HTML/Word/Word_02_Creer_un_courrier_professionnel.html">Word 02</a> : objet, paragraphes, formule, PDF.</p>'),
            ("Atelier objets", '<p><a href="../04_Exercices_HTML/Word/Word_03_Inserer_image_et_tableau.html">Word 03</a> : image, habillage, tableau accessible.</p>'),
            ("Atelier fiche", '<p><a href="../04_Exercices_HTML/Word/Word_04_Creer_une_fiche_de_presentation.html">Word 04</a> : titres, styles, listes, modèle réutilisable.</p>'),
        ]),
    )
    body += panel(
        "Vigilance formateur",
        '<section class="split">'
        + lesson("À faire verbaliser", ul([
            "Mon titre est-il un vrai style ?",
            "Ai-je créé une page vide avec Entrée ou un vrai saut de page ?",
            "Mon image est-elle informative ? Si oui, ai-je prévu un texte alternatif ?",
        ]))
        + lesson("Corrections rapides", ul([
            "Titre absent du sommaire : appliquer Titre 1 ou Titre 2.",
            "Page vide : afficher ¶ puis supprimer paragraphes vides ou saut en trop.",
            "Image instable : choisir l’habillage et vérifier l’ancrage.",
        ]))
        + '</section>',
    )
    return page("Jour 2 - Word : structurer et mettre en page", "Styles, listes, marges, sections, en-têtes, tableaux et images pour produire des documents lisibles.", "..", body, ["Word", "Guide formateur", "7 h", "Mercredi 3 juin"], "Guide formateur")


def guide_day_3():
    body = panel(
        "Objectifs Word du matin",
        '<p>Consolider l’autonomie : document long, modèle simple, révision, accessibilité, PDF et diagnostic des problèmes fréquents.</p>'
        + checklist([
            "Les stagiaires savent diagnostiquer un document mal présenté.",
            "Les styles et champs sont mis à jour avant export.",
            "Le PDF est contrôlé après génération.",
            "Le passage vers Excel est préparé sans confusion d’outil.",
        ], "jour-3-objectifs")
        + '<p class="source-note">Modules source : documents longs, modèles, révision, accessibilité, champs, export, diagnostic.</p>',
    )
    body += panel(
        "Déroulé horaire",
        table(["Heure", "Séquence", "Message formateur"], [
            ["09:00", "Diagnostic Word", "Afficher ¶, repérer styles absents, espaces, sauts et pages vides."],
            ["09:45", "Documents longs", "Volet de navigation, table des matières, légendes, renvois, champs à mettre à jour."],
            ["10:30", "Modèle et révision", "Créer une base réutilisable ; commenter sans écraser le texte."],
            ["11:00", "Accessibilité et export", "Titres structurés, texte alternatif, tableaux simples, PDF vérifié."],
            ["11:30", "Exercice Word 05", "Corriger un document mal présenté avec méthode."],
            ["13:30", "Démarrage Excel", "Classeur, feuille, cellule active, saisie et formats."],
            ["15:15", "Premiers tableaux Excel", "Largeurs, bordures, premières formules simples."],
            ["16:15", "Bilan", "Différence Word / Excel : document rédigé vs données calculées."],
        ]),
    )
    body += panel(
        "Pont Word vers Excel",
        table(["Besoin", "Bon outil", "Raison"], [
            ["Rédiger un courrier, une procédure, un compte rendu", "Word", "Texte structuré, mise en page, PDF."],
            ["Calculer un budget, totaliser, filtrer", "Excel", "Cellules, formules, tableaux de données."],
            ["Insérer un petit tableau dans un document", "Word", "Lecture intégrée au document."],
            ["Analyser beaucoup de lignes", "Excel", "Tri, filtre, formule, graphique."],
        ]),
    )
    body += panel(
        "Correction collective Word 05",
        steps([
            "Lire sans modifier.",
            "Afficher les marques ¶.",
            "Supprimer les espaces et paragraphes vides inutiles.",
            "Appliquer les styles de titres.",
            "Transformer décisions ou actions en liste.",
            "Vérifier aperçu, accessibilité et PDF.",
        ])
        + '<p><a href="../04_Exercices_HTML/Word/Word_05_Corriger_un_document_mal_presente.html">Ouvrir Word 05</a></p>',
    )
    return page("Jour 3 - Word + Excel : finaliser puis changer d’outil", "Matin : autonomie Word et diagnostic. Après-midi : passage vers Excel avec la bonne frontière d’usage.", "..", body, ["Word + Excel", "Guide formateur", "7 h", "Vendredi 5 juin"], "Guide formateur")


EXERCISES = [
    {
        "num": "01",
        "file": "Word_01_Mettre_en_forme_un_texte_brut.html",
        "corrige": "Corrige_Word_01_Mettre_en_forme_un_texte_brut.html",
        "title": "Word 01 - Structurer un texte brut",
        "h1": "Structurer un texte brut avant de le décorer",
        "duration": "45 min",
        "level": "Niveau 1",
        "start": "Word_01_Texte_brut_evenement.txt",
        "context": "Vous recevez un texte non mis en forme. Votre mission : en faire une fiche lisible sans ajouter de contenu inutile.",
        "objective": "Travailler dans l’ordre : lire, découper, afficher ¶, sélectionner, appliquer titres, paragraphes et listes.",
        "criteria": ["Titre principal visible", "Paragraphes séparés par espacements propres", "Liste à puces réelle", "Aucun alignement par espaces", "Nom de fichier clair"],
        "steps": [
            "Ouvrir le fichier de départ et copier le texte dans Word.",
            "Enregistrer sous <code>Fiche_evenement_NomPrenom.docx</code>.",
            "Afficher les caractères invisibles ¶.",
            "Repérer titre, informations clés et liste.",
            "Appliquer un style Titre ou une mise en forme sobre au titre.",
            "Régler les espacements de paragraphes au lieu d’ajouter des lignes vides.",
            "Créer une vraie liste à puces.",
            "Relire, corriger, exporter en PDF si demandé.",
        ],
        "hint": "Si le document paraît impossible à ranger, affichez ¶ : les espaces multiples et retours inutiles deviennent visibles.",
        "correction": "La fiche doit montrer une structure nette : titre, blocs courts, liste propre, aucun bricolage d’espaces.",
        "bonus": "Appliquer un style Titre 1 au titre puis modifier ce style pour changer toute la présentation en une fois.",
    },
    {
        "num": "02",
        "file": "Word_02_Creer_un_courrier_professionnel.html",
        "corrige": "Corrige_Word_02_Creer_un_courrier_professionnel.html",
        "title": "Word 02 - Créer un courrier professionnel",
        "h1": "Créer un courrier professionnel prêt à envoyer",
        "duration": "55 min",
        "level": "Niveau 2",
        "start": "Word_02_Courrier_professionnel_brut.txt",
        "context": "Vous préparez un courrier de relance ou d’invitation. Le destinataire doit comprendre l’objet en quelques secondes.",
        "objective": "Construire un courrier avec coordonnées, date, objet, corps structuré, formule de politesse, signature et PDF.",
        "criteria": ["Coordonnées lisibles", "Date et objet présents", "Paragraphes courts", "Formule et signature correctes", "PDF contrôlé"],
        "steps": [
            "Créer un nouveau document et l’enregistrer sous un nom explicite.",
            "Placer expéditeur, destinataire, date et objet.",
            "Structurer le corps en paragraphes courts.",
            "Utiliser alignements et espaces de paragraphe, pas des lignes vides répétées.",
            "Ajouter formule de politesse et signature.",
            "Vérifier marges, aperçu avant impression et orthographe.",
            "Exporter en PDF et ouvrir le PDF.",
        ],
        "hint": "L’objet doit dire le motif du courrier. Un bon objet évite un long premier paragraphe.",
        "correction": "Le courrier doit tenir sur une page, avec objet clair, blocs lisibles, formule complète et PDF fidèle.",
        "bonus": "Ajouter un pied de page discret avec téléphone ou adresse email.",
    },
    {
        "num": "03",
        "file": "Word_03_Inserer_image_et_tableau.html",
        "corrige": "Corrige_Word_03_Inserer_image_et_tableau.html",
        "title": "Word 03 - Insérer image et tableau",
        "h1": "Insérer une image et un tableau sans casser la mise en page",
        "duration": "60 min",
        "level": "Niveau 2",
        "start": "Word_03_Contenu_image_tableau.txt",
        "context": "Vous préparez une note d’information avec un visuel et un petit tableau. Le document doit rester lisible à l’écran et en PDF.",
        "objective": "Insérer un tableau simple, une image, choisir l’habillage, ajouter une légende ou un texte alternatif si utile.",
        "criteria": ["Tableau avec en-têtes", "Image non déformée", "Habillage maîtrisé", "Texte alternatif ou légende prévu", "Aperçu avant impression propre"],
        "steps": [
            "Créer le document et coller le contenu de départ.",
            "Créer le tableau avec une information par cellule.",
            "Mettre la première ligne en en-tête.",
            "Insérer l’image au bon endroit.",
            "Redimensionner depuis un coin.",
            "Choisir Aligné sur le texte ou Carré selon le besoin.",
            "Ajouter texte alternatif ou légende si l’image apporte une information.",
            "Contrôler en aperçu avant impression.",
        ],
        "hint": "Si l’image bouge, commencez avec Aligné sur le texte. C’est moins libre, mais plus stable.",
        "correction": "Le tableau doit être lisible, l’image proportionnée, et aucun élément ne doit couper le texte.",
        "bonus": "Ajouter une légende sous l’image puis vérifier qu’elle reste avec l’image.",
    },
    {
        "num": "04",
        "file": "Word_04_Creer_une_fiche_de_presentation.html",
        "corrige": "Corrige_Word_04_Creer_une_fiche_de_presentation.html",
        "title": "Word 04 - Créer une fiche de présentation",
        "h1": "Créer une fiche structurée et réutilisable",
        "duration": "60 min",
        "level": "Niveau 2",
        "start": "Word_04_Fiche_presentation_brut.txt",
        "context": "Vous devez produire une fiche claire pour présenter un service, une action ou un événement.",
        "objective": "Utiliser titres, styles, listes, encadré d’information et contrôle final pour obtenir une fiche professionnelle.",
        "criteria": ["Titre 1 utilisé", "Sous-titres cohérents", "Listes propres", "Information importante mise en valeur", "Version réutilisable possible"],
        "steps": [
            "Lire le contenu brut et repérer les grandes parties.",
            "Appliquer Titre 1 au titre principal.",
            "Appliquer Titre 2 aux sous-parties.",
            "Transformer les informations répétées en listes.",
            "Ajouter un encadré discret pour l’information prioritaire.",
            "Harmoniser police, espacements et marges.",
            "Enregistrer une version propre ; exporter en PDF si demandé.",
        ],
        "hint": "Une fiche réussie se parcourt rapidement : titres visibles, sections courtes, information prioritaire isolée.",
        "correction": "La fiche doit utiliser une hiérarchie de titres réelle et une présentation sobre, sans mise en forme différente à chaque ligne.",
        "bonus": "Enregistrer la fiche comme base réutilisable pour créer un modèle simple.",
    },
    {
        "num": "05",
        "file": "Word_05_Corriger_un_document_mal_presente.html",
        "corrige": "Corrige_Word_05_Corriger_un_document_mal_presente.html",
        "title": "Word 05 - Corriger un document mal présenté",
        "h1": "Diagnostiquer et réparer un document Word",
        "duration": "55 min",
        "level": "Niveau 3",
        "start": "Word_05_Document_mal_presente.txt",
        "context": "Vous reprenez un compte rendu écrit trop vite : espaces partout, titres non structurés, listes bricolées, page instable.",
        "objective": "Diagnostiquer avant de modifier, puis corriger structure, paragraphes, listes, pages et PDF.",
        "criteria": ["Diagnostic avec ¶", "Espaces et lignes vides corrigés", "Titres en styles", "Listes et décisions lisibles", "PDF final vérifié"],
        "steps": [
            "Lire le document complet sans modifier.",
            "Afficher les caractères invisibles ¶.",
            "Repérer espaces multiples, tabulations, paragraphes vides et sauts inutiles.",
            "Recréer la structure : titre, date, participants, décisions, prochaines étapes.",
            "Appliquer les styles aux titres.",
            "Transformer les décisions en vraie liste.",
            "Vérifier page, orthographe, accessibilité simple et export PDF.",
        ],
        "hint": "Ne corrigez pas ligne par ligne au hasard. Travaillez par familles de problèmes : espaces, paragraphes, titres, listes, page.",
        "correction": "Le compte rendu doit devenir lisible en une minute : sujet, présents, décisions et actions sautent aux yeux.",
        "bonus": "Ajouter un tableau Action / Responsable / Échéance pour transformer le compte rendu en outil de suivi.",
    },
]


def exercise_page(data):
    prefix = "../.."
    start = f"{prefix}/06_Fichiers_de_depart/Word/{data['start']}"
    corrige = f"{prefix}/05_Corriges_HTML/Word/{data['corrige']}"
    body = f"""
    <div class="exercise-layout">
      <nav class="exercise-sidebar no-print">
        <a href="#objectif" class="active">Objectif</a>
        <a href="#consignes">Consignes</a>
        <a href="#ressources">Ressources</a>
        <a href="#validation">Validation</a>
      </nav>
      <div>
        {panel("Contexte professionnel", f"<p>{data['context']}</p><div class='callout ok'><h3>Résultat attendu</h3><p>{data['objective']}</p></div>", "objectif")}
        {panel("Consignes pas à pas", steps(data["steps"]) + accordion("Indice", f"<p>{data['hint']}</p>") + accordion("Corrigé résumé", f"<p>{data['correction']}</p>"), "consignes")}
        {panel("Ressources", ul([f'<a href="{start}">Fichier de départ</a>', f'<a href="{corrige}">Corrigé formateur</a>', '<a href="../../07_Fiches_memo_interactives/Fiche_memo_Word.html">Fiche mémo Word</a>']), "ressources")}
        {panel("Checklist de réussite", checklist(data["criteria"], data["title"]), "validation")}
        {panel("Pour aller plus loin", f"<p>{data['bonus']}</p>")}
      </div>
    </div>
    """
    return page(data["h1"], data["context"], prefix, body, ["Word", data["level"], data["duration"], f"Module {data['num']}"], "Exercice stagiaire")


def corrige_page(data):
    prefix = "../.."
    exercise = f"{prefix}/04_Exercices_HTML/Word/{data['file']}"
    checks = data["criteria"]
    repair = {
        "01": "Le corrigé valorise la structure : vrai titre, paragraphes courts, puces réelles et espacements propres.",
        "02": "Le corrigé doit rester sobre : coordonnées, date, objet, corps, formule, signature, aperçu et PDF.",
        "03": "Le corrigé vérifie surtout la stabilité : tableau lisible, image proportionnée, habillage maîtrisé.",
        "04": "Le corrigé montre une fiche hiérarchisée par styles, prête à servir de base réutilisable.",
        "05": "Le corrigé suit une méthode de diagnostic : marques ¶, nettoyage, styles, listes, contrôle PDF.",
    }[data["num"]]
    errors = {
        "01": "Titre simplement grossi sans style, lignes vides répétées, puces tapées au clavier, fichier non enregistré.",
        "02": "Objet absent, paragraphes trop longs, formule incomplète, marges non vérifiées, document envoyé en DOCX sans PDF.",
        "03": "Image déformée, tableau sans en-têtes, habillage choisi au hasard, image informative sans texte alternatif.",
        "04": "Sous-titres tous différents, couleurs trop nombreuses, liste non structurée, aucune version réutilisable.",
        "05": "Correction au hasard, suppression d’un saut de section utile, numéros tapés à la main, PDF non contrôlé.",
    }[data["num"]]
    body = f"""
    <p><a href="{exercise}">Retour à l’exercice</a></p>
    <section class="split">
      <article class="panel"><h2>Résultat attendu</h2><p>{repair}</p></article>
      <article class="panel"><h2>Erreurs à repérer</h2><p>{errors}</p></article>
    </section>
    {panel("Étapes de correction", steps(data["steps"]))}
    {panel("Points de contrôle", checklist(checks, "corrige-" + data["title"]))}
    {panel("Correction collective", "<p>Faire expliquer les choix : pourquoi ce titre est un style, pourquoi ce paragraphe est aéré, pourquoi le PDF est fidèle. La qualité attendue est une méthode reproductible, pas seulement une belle page.</p>")}
    """
    return page("Corrigé - " + data["title"], "Corrigé formateur aligné sur la méthode Word : diagnostiquer, structurer, présenter, vérifier.", prefix, body, ["Word", "Corrigé formateur", f"Module {data['num']}"], "Corrigé formateur")


def memo_page():
    items = [
        ("Créer et enregistrer", "Fichier > Enregistrer sous, nom clair, dossier connu, Ctrl+S régulier.", ["Choisir le dossier.", "Nommer le fichier.", "Vérifier le chemin."]),
        ("Afficher ¶", "Premier réflexe dès qu’un document bouge ou contient des espaces étranges.", ["Accueil > ¶.", "Repérer espaces, tabulations, paragraphes.", "Corriger une famille de problème à la fois."]),
        ("Sélectionner", "On sélectionne d’abord, on applique ensuite.", ["Mot : double-clic.", "Paragraphe : triple-clic.", "Tout : Ctrl+A."]),
        ("Paragraphes", "Aérer avec les espacements, pas avec des lignes vides répétées.", ["Sélectionner le paragraphe.", "Accueil > Paragraphe.", "Régler espace avant/après."]),
        ("Styles", "Un style donne une structure exploitable par Word.", ["Cliquer dans le titre.", "Accueil > Styles.", "Choisir Titre 1 ou Titre 2."]),
        ("Table des matières", "Elle fonctionne si les titres utilisent de vrais styles.", ["Appliquer les styles.", "Références > Table des matières.", "Mettre à jour avant PDF."]),
        ("Saut de page", "Nouvelle page volontaire.", ["Placer le curseur.", "Insertion ou Disposition > Saut de page.", "Éviter les Entrée répétées."]),
        ("Saut de section", "Changer la mise en page d’une partie seulement.", ["Afficher ¶.", "Identifier la section.", "Ne pas supprimer sans vérifier."]),
        ("Image stable", "Aligné sur le texte pour débuter ; carré si besoin d’habillage.", ["Insérer l’image.", "Redimensionner par un coin.", "Choisir Options de disposition."]),
        ("Tableau lisible", "Un tableau Word sert à présenter, pas à faire de gros calculs.", ["Créer les en-têtes.", "Une info par cellule.", "Vérifier largeur et répétition d’en-tête."]),
        ("Révision", "Commentaires et suivi servent à collaborer sans écraser.", ["Révision > Nouveau commentaire.", "Activer suivi si demandé.", "Accepter/refuser à la fin."]),
        ("PDF final", "Le PDF est la version d’envoi quand la mise en page doit rester fixe.", ["Fichier > Exporter PDF.", "Ouvrir le PDF.", "Comparer rapidement avec Word."]),
    ]
    cards_html = '<section class="memo-grid">' + "".join(
        f'<article class="card search-item"><h3>{title}</h3><p>{desc}</p>{accordion("Voir les étapes", "<ol>" + "".join(f"<li>{step}</li>" for step in steps_) + "</ol>")}</article>'
        for title, desc, steps_ in items
    ) + "</section>"
    body = '<div class="filters no-print"><label for="search">Recherche</label><input id="search" type="search" data-search placeholder="Rechercher un réflexe Word"></div>'
    body += panel("Les 3 réflexes à retenir", '<section class="flow"><article class="card"><h3>1. Voir</h3><p>Afficher ¶ pour comprendre le document.</p></article><article class="card"><h3>2. Structurer</h3><p>Styles, listes, tableaux propres.</p></article><article class="card"><h3>3. Vérifier</h3><p>Aperçu, accessibilité simple, PDF.</p></article></section>')
    body += cards_html
    body += quiz("Un titre mis en gras suffit-il pour une table des matières automatique ?", [("A", "Non, il faut un style de titre."), ("B", "Oui, Word devine toujours."), ("C", "Seulement si le titre est bleu.")], "A")
    return page("Fiche mémo Word : réflexes professionnels", "Mémo interactif pour diagnostiquer, structurer, mettre en page et finaliser un document Word.", "..", body, ["Word", "Fiche mémo", "Imprimable"], "Fiche mémo")


def write_all():
    source_text = ensure_source()
    (PROJECT / "Word" / "support.md").write_text(source_text, encoding="utf-8")
    write_formapro("03_Supports_stagiaires_HTML/Support_Word_Debutant.html", word_support())
    write_formapro("02_Guide_formateur_HTML/Jour_1_Word.html", guide_day_1())
    write_formapro("02_Guide_formateur_HTML/Jour_2_Word.html", guide_day_2())
    write_formapro("02_Guide_formateur_HTML/Jour_3_Word_Excel.html", guide_day_3())
    for data in EXERCISES:
        write_formapro(f"04_Exercices_HTML/Word/{data['file']}", exercise_page(data))
        write_formapro(f"05_Corriges_HTML/Word/{data['corrige']}", corrige_page(data))
    write_formapro("07_Fiches_memo_interactives/Fiche_memo_Word.html", memo_page())
    print("Refonte Word écrite : Word/support.md + 15 HTML")


if __name__ == "__main__":
    write_all()
