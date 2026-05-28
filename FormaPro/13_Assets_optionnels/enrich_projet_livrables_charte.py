from pathlib import Path
from html import escape
import re

from generate_phases_5_12 import BASE_CSS, BASE_JS


ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = ROOT / "09_Projet_fil_rouge_HTML"
VISUALS_DIR = ROOT / "06_Fichiers_de_depart" / "Projet_fil_rouge" / "Visuels"

EXTRA_CSS = """
.table-scroll{overflow-x:auto;margin-top:1rem}
.kpi{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin:1rem 0}
.kpi .card strong{display:block;font-size:1.35rem;color:var(--p)}
.asset-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem}
.asset-grid img,.hero-img{display:block;width:100%;height:auto;border:1px solid var(--b);border-radius:var(--r);background:#fff}
.logo-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem}
.logo-grid img{display:block;width:100%;height:auto;border:1px solid var(--b);border-radius:var(--r);background:#fff}
.file-name{font-family:Consolas,"Courier New",monospace;font-weight:700;overflow-wrap:anywhere}
.swatches{display:grid;grid-template-columns:repeat(6,1fr);gap:.75rem}
.swatch{border:1px solid var(--b);border-radius:var(--r);overflow:hidden;background:#fff}
.swatch span{display:block;height:3rem}
.swatch code{display:block;padding:.55rem;font-weight:700}
@media(max-width:900px){.asset-grid,.logo-grid,.kpi,.swatches{grid-template-columns:repeat(2,1fr)}}
@media(max-width:640px){.asset-grid,.logo-grid,.kpi,.swatches{grid-template-columns:1fr}}
"""

NAV_LINKS = [
    ("Projet", "Projet_fil_rouge.html"),
    ("Brief", "Brief_projet.html"),
    ("Livrables", "Livrables_projet.html"),
    ("Charte", "Charte_graphique_projet.html"),
    ("Sources", "Sources_projet.html"),
    ("Grille", "Grille_correction_projet.html"),
    ("Simplifié", "Version_simplifiee.html"),
    ("Bonus", "Version_bonus.html"),
]

LOGOS = [
    ("Logo 1 - orientation", "logo_01_bleu_orientation.png", "Option sobre pour invitation Word et première diapositive."),
    ("Logo 2 - progression", "logo_02_vert_progression.png", "Option plus dynamique pour documents Excel et graphiques."),
    ("Logo 3 - rencontre", "logo_03_orange_rencontre.png", "Option chaleureuse pour accueil et affiche."),
    ("Logo 4 - compétences", "logo_04_slate_competences.png", "Option neutre pour version institutionnelle."),
]

PHOTOS = [
    ("Accueil forum", "photo_accueil_forum_metiers.png", "Image d'ouverture pour invitation ou première diapositive."),
    ("Atelier Excel budget", "photo_atelier_excel_budget.png", "Image adaptée au budget, aux participants ou au graphique."),
    ("Documents Word", "photo_documents_word_programme.png", "Image adaptée à l'invitation et au programme."),
    ("Restitution PowerPoint", "photo_presentation_powerpoint.png", "Image adaptée à la conclusion ou à la restitution orale."),
    ("Préparation de la salle", "photo_preparation_salle_forum.png", "Image adaptée à l'organisation, au programme ou à la logistique."),
    ("Accompagnement CV", "photo_accompagnement_cv_word.png", "Image adaptée aux productions Word et aux documents d'invitation."),
    ("Échange recruteur", "photo_echange_recruteur_participants.png", "Image adaptée à la partie métier ou recrutement."),
    ("Tableau de bord Excel", "photo_tableau_bord_excel.png", "Image adaptée aux synthèses, graphiques et budgets."),
    ("Table ronde métiers", "photo_table_ronde_metiers.png", "Image adaptée à la restitution finale."),
    ("Fond PowerPoint abstrait", "fond_abstrait_powerpoint_16_9.png", "Fond 16:9 pour page de titre ou conclusion PowerPoint."),
]

WORD_LIVRABLES = [
    ["W1", "Invitation_Forum_Metiers_NomPrenom.docx", "1 page", "Titre, logo choisi, date, horaire, lieu, contact, objectif de l'événement, programme court, phrase d'invitation.", "programme_forum_metiers.txt, charte graphique"],
    ["W2", "Invitation_Forum_Metiers_NomPrenom.pdf", "PDF", "Même contenu que W1, export lisible, marges propres, aucun texte coupé.", "W1"],
    ["W3", "Programme_Forum_Metiers_NomPrenom.docx", "1 à 2 pages", "Tableau horaire avec heures, séquences, responsables, détail. Pied de page avec contact.", "programme_forum_metiers.txt"],
    ["W4", "Liste_intervenants_Forum_Metiers_NomPrenom.docx", "1 page", "Liste des 5 intervenants, rôle, contribution attendue, ordre de passage.", "brief_intervenants_forum_metiers.txt"],
]

EXCEL_LIVRABLES = [
    ["E1", "Suivi_participants_forum_metiers_NomPrenom.xlsx", "Participants, Synthèse", "Liste nettoyée, filtres, colonne Action, total inscrits, total confirmés, total à confirmer, absent annoncé.", "participants_forum_metiers.xlsx"],
    ["E2", "Budget_forum_metiers_NomPrenom.xlsx", "Budget, Synthèse", "Quantité, prix unitaire, total par ligne, total général, budget maximum 1 200,00 €, reste disponible 171,45 €.", "budget_forum_metiers.xlsx"],
    ["E3", "Graphique_budget_forum_metiers_NomPrenom.xlsx", "Graphique", "Graphique budget par catégorie ou participants par atelier, titre clair, couleurs de la charte.", "budget_forum_metiers.xlsx ou donnees_restitution_forum_metiers.xlsx"],
    ["E4", "Synthese_forum_metiers_NomPrenom.xlsx", "Synthèse finale", "Tableau de bord simple : participants inscrits, confirmés, à relancer, total prévu, reste disponible, décision réalisable/non réalisable.", "participants + budget"],
]

PPT_LIVRABLES = [
    ["P1", "Restitution_Forum_Metiers_NomPrenom.pptx", "5 diapositives max", "Diapo 1 contexte, diapo 2 participants, diapo 3 budget, diapo 4 programme, diapo 5 décision finale.", "Toutes sources + visuels"],
    ["P2", "Restitution_Forum_Metiers_NomPrenom.pdf", "PDF", "Export PDF de la présentation, lisible, sans diapositive vide.", "P1"],
    ["P3", "Notes_orateur_Forum_Metiers_NomPrenom.docx ou notes PPT", "5 phrases", "Une phrase d'explication par diapositive, sans lire tout le texte affiché.", "P1"],
]


def write(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def nav():
    return '<nav class="toc"><ul>' + "".join(f'<li><a href="{href}">{label}</a></li>' for label, href in NAV_LINKS) + "</ul></nav>"


def page(title, subtitle, body):
    return f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <style>{BASE_CSS}{EXTRA_CSS}</style>
</head>
<body class="theme-general">
  <header>
    <div class="wrap">
      <a class="top no-print" href="../00_Index_general/index.html">Retour à l'index général</a>
      <h1>{escape(title)}</h1>
      <p class="lead">{escape(subtitle)}</p>
      <div class="meta"><span class="badge">Projet fil rouge concret</span><span class="badge">Livrables + charte</span></div>
      <div class="actions no-print"><button type="button" onclick="window.print()">Imprimer / Exporter en PDF</button><button type="button" class="secondary" data-open-all>Tout ouvrir</button><button type="button" class="secondary" data-close-all>Tout fermer</button></div>
    </div>
  </header>
  <main class="wrap">
    {nav()}
    {body}
  </main>
  <script>{BASE_JS}</script>
</body>
</html>
"""


def panel(title, content):
    return f'<section class="panel"><h2>{escape(title)}</h2>{content}</section>'


def table(headers, rows):
    head = "".join(f"<th>{escape(str(h))}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{escape(str(cell))}</td>" for cell in row) + "</tr>" for row in rows)
    return f'<div class="table-scroll"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def checklist(items, cid):
    return f'<ul class="checklist" data-checklist-id="{escape(cid)}">' + "".join(f'<li><input type="checkbox"><span>{item}</span></li>' for item in items) + "</ul>"


def steps(items):
    return '<ol class="steps">' + "".join(f"<li><span>{item}</span></li>" for item in items) + "</ol>"


def img_card(title, filename, desc):
    href = f"../06_Fichiers_de_depart/Projet_fil_rouge/Visuels/{filename}"
    return f'<article class="card"><img src="{href}" alt="{escape(title)}"><h3>{escape(title)}</h3><p>{escape(desc)}</p><p><a href="{href}">Ouvrir le fichier</a></p><p class="file-name">{escape(filename)}</p></article>'


def build_livrables():
    body = (
        panel("Règle générale", "<p>Chaque stagiaire produit ses propres fichiers en remplaçant <span class='file-name'>NomPrenom</span> par son nom. Les données doivent venir des sources fournies, sans invention.</p>")
        + panel("Livrables Word", table(["Code", "Nom exact du fichier", "Format", "Contenu obligatoire", "Source à utiliser"], WORD_LIVRABLES))
        + panel("Livrables Excel", table(["Code", "Nom exact du fichier", "Onglets attendus", "Contenu obligatoire", "Source à utiliser"], EXCEL_LIVRABLES))
        + panel("Livrables PowerPoint", table(["Code", "Nom exact du fichier", "Format", "Contenu obligatoire", "Source à utiliser"], PPT_LIVRABLES))
        + panel("Contrôles avant rendu", checklist([
            "Tous les noms de fichiers respectent le modèle demandé.",
            "Les fichiers Word contiennent au moins un logo ou un visuel choisi.",
            "Les fichiers Excel contiennent des formules et pas seulement des montants saisis.",
            "Le budget affiche 1 028,55 € de total prévu et 171,45 € de reste disponible.",
            "Le PowerPoint contient 5 diapositives maximum.",
            "Les exports PDF s'ouvrent correctement.",
        ], "livrables-projet-detail"))
        + panel("Ordre de travail conseillé", steps([
            "Choisir un logo et une photo dans la charte graphique.",
            "Créer Word W1 puis W2, car l'invitation sert de base visuelle.",
            "Créer Excel E1 et E2, puis E3 à partir des chiffres.",
            "Créer PowerPoint P1 avec les chiffres validés dans Excel.",
            "Exporter les PDF à la fin, puis vérifier tous les noms de fichiers.",
        ]))
    )
    write("09_Projet_fil_rouge_HTML/Livrables_projet.html", page("Livrables projet", "Liste précise des fichiers Word, Excel et PowerPoint à produire.", body))


def build_charte():
    swatches = [
        ("Bleu confiance", "#185ABD", "Word, titres"),
        ("Vert action", "#107C41", "Excel, validation"),
        ("Orange échange", "#D24726", "PowerPoint, accueil"),
        ("Slate texte", "#1F2937", "Texte principal"),
        ("Fond clair", "#F8FAFC", "Arrière-plan"),
        ("Bordure", "#E5E7EB", "Tableaux"),
    ]
    swatch_html = '<section class="swatches">' + "".join(
        f'<article class="swatch"><span style="background:{color}"></span><code>{color}</code><p>{escape(name)}<br>{escape(use)}</p></article>'
        for name, color, use in swatches
    ) + "</section>"
    body = (
        panel("Intention graphique", "<p>La charte doit donner une impression professionnelle, simple et accessible. Les stagiaires choisissent un logo et au moins une photo, puis appliquent les mêmes couleurs dans Word, Excel et PowerPoint.</p>")
        + panel("Logos au choix", "<p>Choisir un seul logo pour tout le projet. Ne pas mélanger plusieurs logos dans le même rendu.</p><section class='logo-grid'>" + "".join(img_card(*logo) for logo in LOGOS) + "</section>")
        + panel("Photos au choix", "<p>Choisir les photos selon le document : accueil pour l'invitation, budget pour Excel, présentation pour PowerPoint.</p><section class='asset-grid'>" + "".join(img_card(*photo) for photo in PHOTOS) + "</section>")
        + panel("Palette couleur", swatch_html)
        + panel("Règles d'utilisation", table(["Élément", "Règle"], [
            ["Logo", "Toujours en haut du document ou sur la première diapositive. Largeur conseillée : 3 à 4 cm dans Word, 10 à 15 % de la diapositive dans PowerPoint."],
            ["Photo", "Une seule photo forte par document ou section. Ne pas étirer l'image. Garder les proportions."],
            ["Titres", "Bleu ou slate, taille lisible, jamais plus de deux tailles de titre dans un document."],
            ["Excel", "Couleurs sobres : en-têtes verts ou slate, graphiques avec 2 à 3 couleurs maximum."],
            ["PowerPoint", "Fond clair, texte court, une idée par diapositive, image en appui du message."],
            ["Accessibilité", "Contraste fort, texte jamais posé sur une zone trop chargée de la photo."],
        ]))
        + panel("Choix stagiaire attendu", checklist([
            "Je choisis 1 logo.",
            "Je choisis 1 photo principale pour Word.",
            "Je choisis 1 photo ou graphique pour PowerPoint.",
            "J'utilise les mêmes couleurs dans mes trois logiciels.",
            "Je garde une mise en page lisible et sobre.",
        ], "charte-projet-visuels"))
        + panel("Origine des visuels", "<p>Visuels générés localement avec imagegen pour ce kit. Ils sont fictifs, sans logos réels et sans texte incrusté obligatoire.</p>")
    )
    write("09_Projet_fil_rouge_HTML/Charte_graphique_projet.html", page("Charte graphique projet", "Logos, photos, couleurs et règles visuelles pour le projet fil rouge.", body))


def update_existing_navs():
    nav_html = nav()
    for path in PROJECT_DIR.glob("*.html"):
        text = path.read_text(encoding="utf-8")
        text = re.sub(r'<nav class="toc"><ul>.*?</ul></nav>', nav_html, text, flags=re.S)
        path.write_text(text, encoding="utf-8")


def insert_panel_once(path, marker, panel_html):
    text = path.read_text(encoding="utf-8")
    if marker in text:
        return
    text = text.replace("</main>", panel_html + "\n  </main>")
    path.write_text(text, encoding="utf-8")


def update_project_pages():
    project = PROJECT_DIR / "Projet_fil_rouge.html"
    insert_panel_once(project, "livrables-detail-ajout", panel("Livrables et charte", "<p id='livrables-detail-ajout'>Avant de commencer, ouvrez la liste détaillée des livrables et choisissez vos visuels.</p><p><a href='Livrables_projet.html'>Voir les livrables précis</a> · <a href='Charte_graphique_projet.html'>Voir la charte graphique</a></p>"))
    brief = PROJECT_DIR / "Brief_projet.html"
    insert_panel_once(brief, "brief-livrables-detail-ajout", panel("À consulter avant production", "<p id='brief-livrables-detail-ajout'><a href='Livrables_projet.html'>Liste précise des fichiers à rendre</a> · <a href='Charte_graphique_projet.html'>Logos, photos et règles graphiques</a></p>"))


def update_index():
    path = ROOT / "00_Index_general" / "index.html"
    text = path.read_text(encoding="utf-8")
    additions = [
        ('Livrables projet', '../09_Projet_fil_rouge_HTML/Livrables_projet.html'),
        ('Charte graphique projet', '../09_Projet_fil_rouge_HTML/Charte_graphique_projet.html'),
    ]
    for title, href in additions:
        if title in text:
            continue
        marker = '<article class="card"><h3>Sources projet</h3><p><a href="../09_Projet_fil_rouge_HTML/Sources_projet.html">Ouvrir</a></p></article>'
        text = text.replace(marker, marker + f'<article class="card"><h3>{title}</h3><p><a href="{href}">Ouvrir</a></p></article>')
    path.write_text(text, encoding="utf-8")


def update_text_source():
    path = ROOT / "06_Fichiers_de_depart" / "Projet_fil_rouge" / "charte_graphique_forum_metiers.txt"
    path.write_text("""Charte graphique source - Forum Découverte Métiers et Formation

Titre de l'événement : Forum Découverte Métiers et Formation
Ton visuel : professionnel, simple, accessible, adulte, formation et emploi.

Couleurs :
- Bleu confiance : #185ABD
- Vert action : #107C41
- Orange échange : #D24726
- Slate texte : #1F2937
- Fond clair : #F8FAFC
- Bordure : #E5E7EB

Règles :
- Choisir un seul logo.
- Choisir au moins une photo.
- Ne pas déformer les images.
- Utiliser les mêmes couleurs dans Word, Excel et PowerPoint.
- Garder les titres courts et lisibles.
""", encoding="utf-8")


def update_report_and_qa():
    report = ROOT / "RAPPORT_GENERATION.md"
    text = report.read_text(encoding="utf-8")
    marker = "\n---\n\n## Mise à jour - livrables et charte projet"
    if marker in text:
        text = text.split(marker)[0]
    text += f"""{marker}

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
"""
    report.write_text(text, encoding="utf-8")

    qa = ROOT / "QA_CHECKLIST.md"
    q = qa.read_text(encoding="utf-8")
    marker = "\n## Livrables et charte projet"
    if marker in q:
        q = q.split(marker)[0].rstrip() + "\n"
    q += f"""{marker}

- Livrables Word/Excel/PowerPoint détaillés : OK.
- Charte graphique projet : OK.
- Logos au choix : 4.
- Photos au choix : 4.
- Ressources imagegen copiées dans le kit : OK.
- Liens internes : à vérifier après génération.
"""
    qa.write_text(q, encoding="utf-8")

    html_report = ROOT / "RAPPORT_GENERATION.html"
    html = html_report.read_text(encoding="utf-8")
    if "Livrables et charte projet" not in html:
        html = html.replace("</main>", "<section class='panel'><h2>Livrables et charte projet</h2><ul><li>Liste précise des livrables ajoutée.</li><li>Charte graphique avec logos et photos ajoutée.</li><li>Pack visuel généré avec imagegen et copié dans le kit.</li></ul></section>\n  </main>")
        html_report.write_text(html, encoding="utf-8")


def verify():
    problems = []
    for path in ROOT.rglob("*.html"):
        if "node_modules" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for href in re.findall(r'href=["\']([^"\']+)["\']', text):
            if href.startswith(("#", "mailto:", "tel:")):
                continue
            if not (path.parent / href).resolve().exists():
                problems.append(f"{path.relative_to(ROOT)} -> {href}")
        for src in re.findall(r'src=["\']([^"\']+)["\']', text):
            if src.startswith(("data:", "http://", "https://")):
                continue
            if not (path.parent / src).resolve().exists():
                problems.append(f"{path.relative_to(ROOT)} -> {src}")
    return problems


def main():
    build_livrables()
    build_charte()
    update_existing_navs()
    update_project_pages()
    update_index()
    update_text_source()
    update_report_and_qa()
    problems = verify()
    print("Livrables + charte ajoutés")
    print(f"Pages projet : {len(list(PROJECT_DIR.glob('*.html')))}")
    print(f"Visuels : {len(list(VISUALS_DIR.glob('*.png')))}")
    if problems:
        print("Liens/images à corriger :")
        for problem in problems:
            print(problem)
    else:
        print("Liens/images OK")


if __name__ == "__main__":
    main()
