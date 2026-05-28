from pathlib import Path
from html import escape
import re

from generate_phases_5_12 import BASE_CSS, BASE_JS


ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = ROOT / "09_Projet_fil_rouge_HTML"
SOURCE_DIR = ROOT / "06_Fichiers_de_depart" / "Projet_fil_rouge"

SCENARIO = {
    "titre": "Forum Découverte Métiers et Formation",
    "date": "jeudi 9 juillet 2026",
    "horaire": "14h00 à 17h00",
    "lieu": "Salle polyvalente Jean-Moulin, 12 rue des Ateliers, 59000 Lille",
    "organisateur": "Horizon Compétences, service formation",
    "contact": "Camille Bernard, coordinatrice formation, camille.bernard@example.local",
    "budget_max": "1 200,00 €",
    "budget_prevu": "1 028,55 €",
    "reste": "171,45 €",
}

PARTICIPANTS = [
    ["Alice Martin", "Demandeuse d'emploi", "Lille", "CV et candidature Word", "Oui", "Oui"],
    ["Karim Benali", "Salarié en reconversion", "Roubaix", "Budget Excel", "Oui", "Oui"],
    ["Sophie Laurent", "Assistante RH", "Tourcoing", "Présentation PowerPoint", "Oui", "Non"],
    ["Thomas Petit", "Commercial junior", "Lille", "Budget Excel", "Oui", "Oui"],
    ["Nadia Diallo", "Demandeuse d'emploi", "Villeneuve-d'Ascq", "CV et candidature Word", "À confirmer", "Oui"],
    ["Hugo Moreau", "Agent logistique", "Seclin", "Budget Excel", "Oui", "Oui"],
    ["Léa Nguyen", "Apprentie", "Lomme", "Présentation PowerPoint", "Oui", "Oui"],
    ["Samir Haddad", "Demandeur d'emploi", "Lille", "CV et candidature Word", "Oui", "Oui"],
    ["Camille Bernard", "Coordinatrice formation", "Lille", "Présentation PowerPoint", "Oui", "Non"],
    ["Julien Robert", "Technicien", "La Madeleine", "Budget Excel", "Oui", "Oui"],
    ["Inès Garcia", "Assistante administrative", "Marcq-en-Baroeul", "CV et candidature Word", "Oui", "Oui"],
    ["Mehdi Leroy", "Responsable équipe", "Wattrelos", "Budget Excel", "À confirmer", "Non"],
    ["Clara Morel", "Demandeuse d'emploi", "Lille", "CV et candidature Word", "Oui", "Oui"],
    ["Lucas Dubois", "Alternant", "Croix", "Présentation PowerPoint", "Oui", "Oui"],
    ["Amina Traoré", "Agent d'accueil", "Roubaix", "CV et candidature Word", "Oui", "Oui"],
    ["Élodie Simon", "Chargée de planning", "Lille", "Budget Excel", "Oui", "Oui"],
    ["Yanis Fontaine", "Magasinier", "Haubourdin", "Budget Excel", "Non", "Non"],
    ["Marion Lefèvre", "Assistante commerciale", "Lille", "Présentation PowerPoint", "Oui", "Oui"],
    ["Paul Richard", "Demandeur d'emploi", "Loos", "CV et candidature Word", "Oui", "Oui"],
    ["Sarah Mercier", "Responsable accueil", "Lille", "Présentation PowerPoint", "Oui", "Non"],
    ["Baptiste Roux", "Technicien support", "Wasquehal", "Budget Excel", "Oui", "Oui"],
    ["Fatou Ndiaye", "Demandeuse d'emploi", "Roubaix", "CV et candidature Word", "À confirmer", "Oui"],
    ["Romain Girard", "Assistant polyvalent", "Lille", "Budget Excel", "Oui", "Oui"],
    ["Chloé Perrin", "Apprentie RH", "Tourcoing", "Présentation PowerPoint", "Oui", "Oui"],
]

BUDGET = [
    ["Location salle polyvalente", "Lieu", "1", "320,00 €", "320,00 €", "Confirmé"],
    ["Collations individuelles", "Accueil", "32", "4,50 €", "144,00 €", "Confirmé"],
    ["Café, thé, eau", "Accueil", "1", "65,00 €", "65,00 €", "Confirmé"],
    ["Badges nominatifs", "Signalétique", "35", "0,65 €", "22,75 €", "À commander"],
    ["Impression programmes A4", "Impression", "45", "0,28 €", "12,60 €", "Confirmé"],
    ["Affiches A3", "Communication", "10", "2,10 €", "21,00 €", "À valider"],
    ["Fournitures atelier", "Ateliers", "1", "85,00 €", "85,00 €", "Confirmé"],
    ["Défraiement intervenants", "Intervenants", "3", "90,00 €", "270,00 €", "Confirmé"],
    ["Transport matériel", "Logistique", "1", "45,00 €", "45,00 €", "À valider"],
    ["Kit papier participant", "Impression", "24", "1,80 €", "43,20 €", "Confirmé"],
]

PLANNING = [
    ["13h30", "Installation salle", "Camille Bernard + formateurs", "Vidéoprojecteur, badges, fichiers sources"],
    ["14h00", "Accueil participants", "Sarah Mercier", "Pointage, badges, programme papier"],
    ["14h15", "Ouverture", "Camille Bernard", "Objectif et règles pratiques"],
    ["14h35", "Atelier Word", "Julie Garnier", "CV, courrier, programme simple"],
    ["15h20", "Pause", "Tous", "Collation et questions"],
    ["15h35", "Atelier Excel", "Olivier Petit", "Budget, SOMME, graphique"],
    ["16h20", "Témoignage métier", "Manon Carpentier", "Parcours après formation"],
    ["16h40", "Questions recrutement", "Rachid Morel", "Attentes employeur"],
    ["16h55", "Clôture", "Camille Bernard", "Prochaines étapes"],
]

INTERVENANTS = [
    ["Julie Garnier", "Formatrice Word / PowerPoint", "Présenter le document d'invitation et la restitution"],
    ["Olivier Petit", "Formateur Excel", "Présenter le budget et le graphique"],
    ["Manon Carpentier", "Ancienne stagiaire", "Témoigner sur la montée en compétences"],
    ["Rachid Morel", "Responsable recrutement NordLog", "Expliquer les attentes employeur"],
    ["Sarah Mercier", "Responsable accueil", "Gérer l'accueil et le pointage"],
]

LIVRABLES = [
    ["Word", "Invitation_Forum_Metiers_NomPrenom.docx", "Invitation professionnelle d'une page avec titre, date, lieu, programme court, contact."],
    ["Word", "Invitation_Forum_Metiers_NomPrenom.pdf", "Export PDF propre, prêt à envoyer."],
    ["Word", "Programme_Forum_Metiers_NomPrenom.docx", "Programme détaillé en tableau simple avec horaires et responsables."],
    ["Excel", "Suivi_participants_forum_metiers_NomPrenom.xlsx", "Liste participants nettoyée, filtres, total inscrits, total confirmés, personnes à relancer."],
    ["Excel", "Budget_forum_metiers_NomPrenom.xlsx", "Budget avec quantités, prix unitaires, totaux, total général, reste disponible."],
    ["Excel", "Graphique_budget_forum_metiers_NomPrenom.xlsx", "Graphique clair : budget par catégorie ou participants par atelier."],
    ["PowerPoint", "Restitution_Forum_Metiers_NomPrenom.pptx", "5 diapositives maximum : contexte, participants, budget, planning, décision finale."],
    ["PowerPoint", "Restitution_Forum_Metiers_NomPrenom.pdf", "Export PDF de la présentation."],
]

SOURCES = [
    ["participants_forum_metiers.xlsx", "../06_Fichiers_de_depart/Projet_fil_rouge/participants_forum_metiers.xlsx", "Liste nominative fictive de 24 participants, statuts, villes, ateliers, présence, collation."],
    ["budget_forum_metiers.xlsx", "../06_Fichiers_de_depart/Projet_fil_rouge/budget_forum_metiers.xlsx", "Budget détaillé : postes, catégories, quantités, prix, total, budget maximum."],
    ["donnees_restitution_forum_metiers.xlsx", "../06_Fichiers_de_depart/Projet_fil_rouge/donnees_restitution_forum_metiers.xlsx", "Indicateurs prêts à réutiliser dans le PowerPoint : participants, budget, planning, ateliers."],
    ["programme_forum_metiers.txt", "../06_Fichiers_de_depart/Projet_fil_rouge/programme_forum_metiers.txt", "Programme horaire à reprendre dans Word et PowerPoint."],
    ["brief_intervenants_forum_metiers.txt", "../06_Fichiers_de_depart/Projet_fil_rouge/brief_intervenants_forum_metiers.txt", "Rôles des intervenants, messages clés, contraintes de prise de parole."],
    ["notes_organisation_forum_metiers.txt", "../06_Fichiers_de_depart/Projet_fil_rouge/notes_organisation_forum_metiers.txt", "Contraintes logistiques, nommage, délais et critères de réussite."],
]

EXTRA_CSS = """
.table-scroll{overflow-x:auto;margin-top:1rem}
.source-list{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem}
.source-list .card{display:flex;flex-direction:column;gap:.35rem}
.kpi{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin:1rem 0}
.kpi .card strong{display:block;font-size:1.45rem;color:var(--p)}
.file-name{font-family:Consolas,"Courier New",monospace;font-weight:700;overflow-wrap:anywhere}
.small{font-size:.92rem}
@media(max-width:900px){.source-list,.kpi{grid-template-columns:1fr 1fr}}
@media(max-width:640px){.source-list,.kpi{grid-template-columns:1fr}}
"""


def write(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def panel(title, content, ident=None):
    attr = f' id="{ident}"' if ident else ""
    return f'<section class="panel"{attr}><h2>{escape(title)}</h2>{content}</section>'


def table(headers, rows):
    head = "".join(f"<th>{escape(str(h))}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{escape(str(cell))}</td>" for cell in row) + "</tr>" for row in rows)
    return f'<div class="table-scroll"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def checklist(items, cid):
    return f'<ul class="checklist" data-checklist-id="{escape(cid)}">' + "".join(f'<li><input type="checkbox"><span>{item}</span></li>' for item in items) + "</ul>"


def steps(items):
    return '<ol class="steps">' + "".join(f"<li><span>{item}</span></li>" for item in items) + "</ol>"


def accordion(label, content):
    return f'<div class="accordion"><button type="button" aria-expanded="false">{escape(label)}</button><div class="content">{content}</div></div>'


def nav():
    links = [
        ("Projet", "Projet_fil_rouge.html"),
        ("Brief", "Brief_projet.html"),
        ("Sources", "Sources_projet.html"),
        ("Grille", "Grille_correction_projet.html"),
        ("Simplifié", "Version_simplifiee.html"),
        ("Bonus", "Version_bonus.html"),
    ]
    return '<nav class="toc"><ul>' + "".join(f'<li><a href="{href}">{label}</a></li>' for label, href in links) + "</ul></nav>"


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
      <div class="meta"><span class="badge">Projet fil rouge concret</span><span class="badge">Word + Excel + PowerPoint</span></div>
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


def source_cards():
    return '<section class="source-list">' + "".join(
        f'<article class="card"><h3>{escape(name)}</h3><p>{escape(desc)}</p><p><a href="{href}">Ouvrir la source</a></p></article>'
        for name, href, desc in SOURCES
    ) + "</section>"


def kpis():
    items = [
        ("24", "participants inscrits"),
        ("20", "présences confirmées"),
        (SCENARIO["budget_prevu"], "budget prévu"),
        (SCENARIO["reste"], "marge restante"),
    ]
    return '<section class="kpi">' + "".join(f'<article class="card"><strong>{v}</strong><span>{escape(label)}</span></article>' for v, label in items) + "</section>"


def build_project_page():
    body = (
        panel("Scénario", f"""
        <p>Vous travaillez pour <strong>{SCENARIO['organisateur']}</strong>. Votre responsable vous demande de préparer les documents d'un événement réel et complet : le <strong>{SCENARIO['titre']}</strong>.</p>
        <p>L'événement aura lieu le <strong>{SCENARIO['date']}</strong>, de <strong>{SCENARIO['horaire']}</strong>, à <strong>{SCENARIO['lieu']}</strong>.</p>
        <p>Contact projet : <strong>{SCENARIO['contact']}</strong>.</p>
        """, "scenario")
        + kpis()
        + panel("Fichiers à réaliser", table(["Logiciel", "Fichier attendu", "Contenu concret attendu"], LIVRABLES), "livrables")
        + panel("Sources fournies", "<p>Utilisez ces fichiers comme point de départ. Les noms, chiffres, horaires et rôles sont déjà fournis pour éviter toute invention pendant l'exercice.</p>" + source_cards(), "sources")
        + panel("Données rapides à reprendre", table(["Nom", "Statut", "Ville", "Atelier", "Présence", "Collation"], PARTICIPANTS[:8]) + table(["Poste", "Catégorie", "Qté", "PU HT", "Total HT", "Statut"], BUDGET), "donnees")
        + panel("Méthode conseillée", steps([
            "Ouvrir les sources et lire le scénario avant de créer les fichiers.",
            "Créer le document Word d'invitation avec date, lieu, contact et programme court.",
            "Créer ou compléter le suivi Excel participants : filtres, totaux, personnes à relancer.",
            "Créer le budget Excel : quantités, prix unitaires, totaux, total général, marge restante.",
            "Créer un graphique simple utilisable dans PowerPoint.",
            "Créer la présentation de restitution en 5 diapositives maximum.",
            "Exporter les documents demandés en PDF et vérifier les noms de fichiers.",
        ]), "methode")
        + panel("Checklist finale", checklist([
            "Tous les fichiers attendus existent avec le bon nom.",
            "Les noms, dates, lieux et montants viennent des sources fournies.",
            "Le budget total est calculé par formule, pas saisi à la main.",
            "Le graphique a un titre clair.",
            "La présentation PowerPoint contient 5 diapositives maximum.",
            "Les exports PDF sont lisibles.",
        ], "projet-fil-rouge-concret"))
    )
    write("09_Projet_fil_rouge_HTML/Projet_fil_rouge.html", page("Projet fil rouge", "Organiser un forum métiers réaliste avec sources, budget, participants et livrables précis.", body))


def build_brief_page():
    body = (
        panel("Mission", f"""
        <p>Votre responsable vous donne une mission opérationnelle : préparer les supports du <strong>{SCENARIO['titre']}</strong> sans repartir d'une page vide.</p>
        <p>Le public est débutant ou en reconversion. Les documents doivent être simples, lisibles et utilisables par une personne qui découvre l'événement.</p>
        """)
        + panel("Contraintes non négociables", table(["Contrainte", "Détail"], [
            ["Date", SCENARIO["date"]],
            ["Horaire", SCENARIO["horaire"]],
            ["Lieu", SCENARIO["lieu"]],
            ["Budget maximum", SCENARIO["budget_max"]],
            ["Participants", "24 inscrits, dont 20 confirmés, 3 à confirmer, 1 absent annoncé"],
            ["Présentation", "5 diapositives maximum, une idée principale par diapositive"],
            ["Nommage", "Toujours finir le nom du fichier par NomPrenom"],
        ]))
        + panel("Travail Word", steps([
            "Créer l'invitation à partir du programme fourni.",
            "Insérer un titre clair : Forum Découverte Métiers et Formation.",
            "Ajouter la date, le lieu, l'horaire, le contact et les informations pratiques.",
            "Mettre le programme court sous forme de liste ou de tableau.",
            "Exporter l'invitation en PDF.",
        ]))
        + panel("Travail Excel", steps([
            "Ouvrir participants_forum_metiers.xlsx.",
            "Filtrer les personnes à confirmer et préparer une colonne Action.",
            "Calculer le nombre d'inscrits, confirmés, à confirmer et absents.",
            "Ouvrir budget_forum_metiers.xlsx.",
            "Vérifier les formules de total par ligne, total général et reste disponible.",
            "Créer un graphique lisible à partir du budget ou des ateliers.",
        ]))
        + panel("Travail PowerPoint", steps([
            "Créer 5 diapositives maximum.",
            "Diapositive 1 : contexte et objectif.",
            "Diapositive 2 : participants et ateliers.",
            "Diapositive 3 : budget et marge restante.",
            "Diapositive 4 : planning du jour.",
            "Diapositive 5 : décision finale et prochaines actions.",
        ]))
        + panel("Sources à citer dans vos fichiers", source_cards())
    )
    write("09_Projet_fil_rouge_HTML/Brief_projet.html", page("Brief projet", "Consignes détaillées pour produire les fichiers du projet sans inventer les données.", body))


def build_sources_page():
    body = (
        panel("Fichiers sources", "<p>Toutes les données sont fictives et fournies pour l'exercice. Les adresses en <span class='file-name'>example.local</span> évitent d'utiliser de vraies données personnelles.</p>" + source_cards())
        + panel("Participants", table(["Nom", "Statut", "Ville", "Atelier prioritaire", "Présence", "Collation"], PARTICIPANTS), "participants")
        + panel("Budget", table(["Poste", "Catégorie", "Qté", "Prix unitaire HT", "Total HT", "Statut"], BUDGET), "budget")
        + panel("Programme", table(["Heure", "Séquence", "Responsable", "Détail"], PLANNING), "programme")
        + panel("Intervenants", table(["Nom", "Rôle", "Contribution attendue"], INTERVENANTS), "intervenants")
    )
    write("09_Projet_fil_rouge_HTML/Sources_projet.html", page("Sources projet", "Données concrètes à utiliser dans Word, Excel et PowerPoint.", body))


def build_grille_page():
    rows = [
        ["Word - invitation", "20 pts", "Informations obligatoires présentes : titre, date, lieu, horaire, contact, programme court, mise en page propre."],
        ["Word - programme", "10 pts", "Tableau ou liste horaire lisible, sans faute de structure, exportable en PDF."],
        ["Excel - participants", "20 pts", "Liste propre, filtres utilisables, totaux inscrits/confirmés/à relancer, données non inventées."],
        ["Excel - budget", "20 pts", "Formules correctes, total général 1 028,55 €, budget max 1 200,00 €, reste 171,45 €."],
        ["Graphique", "10 pts", "Titre clair, données correctes, graphique lisible dans Excel ou PowerPoint."],
        ["PowerPoint", "15 pts", "5 diapositives maximum, messages courts, chiffres cohérents, présentation exportée en PDF."],
        ["Organisation fichiers", "5 pts", "Noms de fichiers respectés, fichiers rangés, aucune source originale écrasée."],
    ]
    body = (
        panel("Barème concret", table(["Partie", "Points", "Validation attendue"], rows))
        + panel("Seuils", table(["Résultat", "Interprétation"], [
            ["90 à 100 pts", "Autonomie solide : le stagiaire peut refaire une mission similaire."],
            ["75 à 89 pts", "Objectif atteint avec quelques points à corriger."],
            ["60 à 74 pts", "Bases présentes, mais reprise nécessaire sur les calculs ou la structure."],
            ["Moins de 60 pts", "Accompagnement nécessaire avant validation."],
        ]))
        + panel("Contrôle rapide formateur", checklist([
            "Le stagiaire sait expliquer d'où viennent les noms et les chiffres.",
            "Le budget utilise des formules.",
            "Les exports PDF s'ouvrent correctement.",
            "La présentation ne dépasse pas 5 diapositives.",
            "Les corrections demandées sont appliquées.",
        ], "grille-projet-concret"))
    )
    write("09_Projet_fil_rouge_HTML/Grille_correction_projet.html", page("Grille correction projet", "Critères observables pour corriger le projet fil rouge.", body))


def build_simplifiee_page():
    body = (
        panel("Objectif réduit", "<p>Utiliser le même scénario, mais réduire le nombre de livrables pour un groupe plus lent.</p>")
        + panel("Périmètre", table(["À faire", "Réduction"], [
            ["Participants", "Utiliser seulement les 12 premiers noms."],
            ["Budget", "Utiliser seulement 5 lignes : salle, collations, badges, impressions, intervenants."],
            ["Word", "Créer seulement l'invitation d'une page."],
            ["Excel", "Créer un seul classeur avec participants + budget."],
            ["PowerPoint", "Créer 3 diapositives : contexte, chiffres, décision finale."],
        ]))
        + panel("Fichiers attendus", table(["Logiciel", "Fichier"], [
            ["Word", "Invitation_Forum_Metiers_NomPrenom.docx"],
            ["Excel", "Projet_simplifie_forum_metiers_NomPrenom.xlsx"],
            ["PowerPoint", "Restitution_simplifiee_forum_metiers_NomPrenom.pptx"],
        ]))
        + panel("Validation minimum", checklist([
            "Invitation lisible avec date, lieu, horaire et contact.",
            "Excel contient au moins 12 participants.",
            "Budget simplifié calculé par formule.",
            "PowerPoint contient 3 diapositives lisibles.",
        ], "projet-simplifie-concret"))
    )
    write("09_Projet_fil_rouge_HTML/Version_simplifiee.html", page("Version simplifiée", "Même scénario, livrables réduits pour sécuriser les bases.", body))


def build_bonus_page():
    body = (
        panel("Défis bonus", "<p>Pour les stagiaires rapides : conserver le scénario complet et ajouter des améliorations utiles, sans compliquer inutilement les fichiers.</p>")
        + panel("Options Word", steps([
            "Créer une version courrier + une version programme.",
            "Ajouter un pied de page avec contact et date.",
            "Utiliser les styles Titre 1 et Titre 2.",
            "Préparer une version PDF prête à envoyer.",
        ]))
        + panel("Options Excel", steps([
            "Ajouter une colonne Action dans le suivi participants.",
            "Utiliser SI pour afficher À relancer quand la présence vaut À confirmer.",
            "Créer un graphique participants par atelier.",
            "Créer une mise en forme conditionnelle sur les postes budgétaires supérieurs à 100 €.",
            "Ajouter un onglet Synthèse avec budget maximum, total prévu et reste disponible.",
        ]))
        + panel("Options PowerPoint", steps([
            "Insérer le graphique Excel.",
            "Ajouter des notes orateur courtes.",
            "Créer une conclusion avec décision : événement réalisable ou non.",
            "Limiter chaque diapositive à 3 messages visibles.",
        ]))
        + panel("Critères bonus", checklist([
            "Les formules restent compréhensibles.",
            "Le design reste sobre.",
            "Les chiffres restent cohérents avec les sources.",
            "Le stagiaire sait expliquer ses choix.",
        ], "projet-bonus-concret"))
    )
    write("09_Projet_fil_rouge_HTML/Version_bonus.html", page("Version bonus", "Défis supplémentaires pour enrichir le projet sans changer le scénario.", body))


def build_text_sources():
    write("06_Fichiers_de_depart/Projet_fil_rouge/programme_forum_metiers.txt", "\n".join([
        "Programme source - Forum Découverte Métiers et Formation",
        f"Date : {SCENARIO['date']}",
        f"Horaire : {SCENARIO['horaire']}",
        f"Lieu : {SCENARIO['lieu']}",
        "",
        *[f"{h} - {seq} - {resp} - {detail}" for h, seq, resp, detail in PLANNING],
    ]) + "\n")
    write("06_Fichiers_de_depart/Projet_fil_rouge/brief_intervenants_forum_metiers.txt", "\n".join([
        "Brief intervenants - données fictives pédagogiques",
        "",
        *[f"{nom} | {role} | {contribution}" for nom, role, contribution in INTERVENANTS],
        "",
        "Messages clés :",
        "- La bureautique sert à produire des documents utiles, pas seulement à connaître des boutons.",
        "- Word : invitation et programme clairs.",
        "- Excel : suivi participants et budget fiable.",
        "- PowerPoint : restitution courte et lisible.",
    ]) + "\n")
    write("06_Fichiers_de_depart/Projet_fil_rouge/notes_organisation_forum_metiers.txt", "\n".join([
        "Notes organisation - Forum Découverte Métiers et Formation",
        "",
        f"Budget maximum : {SCENARIO['budget_max']}",
        f"Budget prévu : {SCENARIO['budget_prevu']}",
        f"Reste disponible : {SCENARIO['reste']}",
        "Participants : 24 inscrits, 20 confirmés, 3 à confirmer, 1 absent annoncé.",
        "Collations à prévoir : 20 personnes confirmées + intervenants + marge logistique.",
        "",
        "Règles de nommage :",
        "- Invitation_Forum_Metiers_NomPrenom.docx",
        "- Suivi_participants_forum_metiers_NomPrenom.xlsx",
        "- Budget_forum_metiers_NomPrenom.xlsx",
        "- Restitution_Forum_Metiers_NomPrenom.pptx",
        "",
        "Tous les noms, chiffres et horaires doivent venir des sources fournies.",
    ]) + "\n")


def update_index():
    path = ROOT / "00_Index_general" / "index.html"
    text = path.read_text(encoding="utf-8")
    if "Sources projet" in text:
        return
    marker = '<article class="card"><h3>Projet fil rouge</h3><p><a href="../09_Projet_fil_rouge_HTML/Projet_fil_rouge.html">Ouvrir</a></p></article>'
    replacement = marker + '<article class="card"><h3>Sources projet</h3><p><a href="../09_Projet_fil_rouge_HTML/Sources_projet.html">Ouvrir</a></p></article>'
    text = text.replace(marker, replacement)
    path.write_text(text, encoding="utf-8")


def update_report():
    marker = "\n---\n\n## Mise à jour - projet fil rouge concret"
    report = ROOT / "RAPPORT_GENERATION.md"
    text = report.read_text(encoding="utf-8")
    if marker in text:
        text = text.split(marker)[0]
    section = f"""{marker}

Date de mise à jour : 28 mai 2026

### Contenu refondu

- Projet fil rouge remplacé par un scénario réaliste : `{SCENARIO['titre']}`, le {SCENARIO['date']} à Lille.
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
- Budget maximum : {SCENARIO['budget_max']}.
- Budget prévu : {SCENARIO['budget_prevu']}.
- Reste disponible : {SCENARIO['reste']}.
- Planning horaire de 13h30 à 16h55.
- 5 intervenants avec rôles et contributions.
"""
    report.write_text(text + section, encoding="utf-8")

    html_report = ROOT / "RAPPORT_GENERATION.html"
    html = html_report.read_text(encoding="utf-8")
    block = """<section class="panel"><h2>Projet fil rouge concret</h2><ul><li>Scénario réaliste ajouté : Forum Découverte Métiers et Formation.</li><li>Sources `.xlsx` et `.txt` ajoutées.</li><li>Pages projet, brief, sources, grille, simplifiée et bonus refondues.</li></ul></section>"""
    if "Projet fil rouge concret" not in html:
        html = html.replace("</main>", f"{block}\n  </main>")
        html_report.write_text(html, encoding="utf-8")


def update_qa():
    path = ROOT / "QA_CHECKLIST.md"
    text = path.read_text(encoding="utf-8")
    marker = "\n## Projet fil rouge concret"
    if marker in text:
        text = text.split(marker)[0].rstrip() + "\n"
    text += f"""{marker}

- Scénario réaliste : ajouté.
- Pages projet fil rouge : 6 pages HTML.
- Sources projet : 3 fichiers `.xlsx`, 3 fichiers `.txt`.
- Participants nommés : 24.
- Budget concret : {SCENARIO['budget_prevu']} sur {SCENARIO['budget_max']}.
- Liens internes : à vérifier après génération.
"""
    path.write_text(text, encoding="utf-8")


def verify_project_links():
    problems = []
    for path in PROJECT_DIR.glob("*.html"):
        text = path.read_text(encoding="utf-8")
        for href in re.findall(r'href="([^"]+)"', text):
            if href.startswith(("#", "mailto:", "tel:")):
                continue
            target = (path.parent / href).resolve()
            if not target.exists():
                problems.append(f"{path.name} -> {href}")
    return problems


def main():
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    build_text_sources()
    build_project_page()
    build_brief_page()
    build_sources_page()
    build_grille_page()
    build_simplifiee_page()
    build_bonus_page()
    update_index()
    update_report()
    update_qa()
    problems = verify_project_links()
    print("Projet fil rouge refondu")
    print(f"Pages HTML projet : {len(list(PROJECT_DIR.glob('*.html')))}")
    if problems:
        print("Liens à corriger :")
        for problem in problems:
            print(f"- {problem}")
    else:
        print("Liens projet OK")


if __name__ == "__main__":
    main()
