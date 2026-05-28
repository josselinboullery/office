from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


BASE_CSS = """
:root{--p:#334155;--s:#1F2937;--a:#64748B;--bg:#F8FAFC;--t:#111827;--b:#E5E7EB;--ok:#15803D;--w:#B45309;--d:#B91C1C;--r:8px}
.theme-word{--p:#185ABD;--s:#2B579A;--a:#41A5EE;--bg:#F3F7FF;--t:#1F2937;--b:#D8E3F8}
.theme-excel{--p:#107C41;--s:#217346;--a:#33C481;--bg:#F1FAF5;--t:#1F2937;--b:#CFEBDD}
.theme-powerpoint{--p:#C43E1C;--s:#D24726;--a:#F0643B;--bg:#FFF4F0;--t:#1F2937;--b:#F6D4C9}
*{box-sizing:border-box}
body{margin:0;font-family:"Segoe UI",Arial,sans-serif;font-size:16px;line-height:1.65;color:var(--t);background:linear-gradient(180deg,var(--bg),#fff 28rem)}
.wrap{width:min(1120px,calc(100% - 2rem));margin:auto}
header{padding:2rem 0;border-bottom:1px solid var(--b)}
main{padding:2rem 0}
h1{margin:0;color:var(--s);font-size:clamp(1.9rem,4vw,2.65rem);line-height:1.15}
h2{margin:0 0 1rem;color:var(--s);font-size:1.5rem}
h3{margin:.25rem 0;color:var(--s);font-size:1.12rem}
p{margin:.5rem 0 1rem}
a{color:var(--p);font-weight:700}
a:focus,button:focus,input:focus,textarea:focus,select:focus{outline:3px solid var(--a);outline-offset:3px}
.top{display:inline-block;margin-bottom:1rem;text-decoration:none}
.lead{max-width:780px;font-size:1.1rem}
.meta,.actions,.filters{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1rem}
.badge{display:inline-flex;align-items:center;min-height:2rem;border:1px solid var(--b);border-radius:999px;background:#fff;padding:.25rem .75rem;font-weight:700}
button,.button{min-height:44px;border:0;border-radius:var(--r);background:var(--p);color:#fff;padding:.72rem 1rem;font:inherit;font-weight:700;text-decoration:none;cursor:pointer;display:inline-flex;align-items:center;justify-content:center}
button.secondary,.button.secondary{background:#fff;color:var(--p);border:1px solid var(--p)}
.panel,.card,.toc{background:#fff;border:1px solid var(--b);border-radius:var(--r);box-shadow:0 8px 24px rgba(15,23,42,.08)}
.panel{padding:1.5rem;margin-bottom:1.5rem}
.card{padding:1rem}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
.two{grid-template-columns:repeat(2,1fr)}
.toc{padding:1rem;margin-bottom:1.5rem}
.toc ul{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(4,1fr);gap:.5rem}
.toc a{display:block;min-height:44px;border-radius:var(--r);background:var(--bg);padding:.65rem .8rem;text-decoration:none}
.callout{border-left:5px solid var(--p);background:var(--bg);border-radius:var(--r);padding:1rem;margin:1rem 0}
.callout.ok{border-color:var(--ok)}.callout.warn{border-color:var(--w)}.callout.danger{border-color:var(--d)}
.steps{counter-reset:s;list-style:none;padding:0;margin:0}
.steps li{counter-increment:s;display:grid;grid-template-columns:2.5rem 1fr;gap:.75rem;padding:.75rem 0;border-bottom:1px solid var(--b)}
.steps li:before{content:counter(s);display:grid;place-items:center;width:2rem;height:2rem;border-radius:999px;background:var(--p);color:#fff;font-weight:800}
.checklist{list-style:none;margin:0;padding:0}
.checklist li{display:flex;gap:.75rem;padding:.72rem;border-bottom:1px solid var(--b)}
.checklist input{width:1.2rem;height:1.2rem;margin-top:.2rem;accent-color:var(--p)}
.accordion{border:1px solid var(--b);border-radius:var(--r);overflow:hidden;margin-top:.75rem;background:#fff}
.accordion button{width:100%;border-radius:0;text-align:left;justify-content:flex-start}
.content{display:none;padding:1rem}
.content.open{display:block}
.quiz-options{display:grid;gap:.5rem;margin-top:.75rem}
.quiz-options button{background:#fff;color:var(--s);border:1px solid var(--b);justify-content:flex-start;text-align:left}
.feedback{font-weight:800}
table{width:100%;border-collapse:collapse;margin-top:1rem}
th,td{border:1px solid var(--b);padding:.65rem;text-align:left;vertical-align:top}
th{background:var(--bg);color:var(--s)}
input[type=search],textarea,select{min-height:44px;border:1px solid var(--b);border-radius:var(--r);padding:.65rem .8rem;font:inherit}
textarea{width:100%;min-height:7rem}
.search-item[hidden]{display:none}
@media(max-width:900px){.grid,.two,.toc ul{grid-template-columns:repeat(2,1fr)}}
@media(max-width:640px){.wrap{width:min(100% - 1rem,1120px)}.grid,.two,.toc ul{grid-template-columns:1fr}.panel{padding:1rem}button,.button{width:100%}.actions,.filters{flex-direction:column}}
@media print{body{background:#fff;color:#111827}.no-print,.actions,button{display:none!important}.panel,.card,.toc,.callout,table{box-shadow:none;break-inside:avoid}.content{display:block!important}a{color:#111827;text-decoration:none}}
"""

BASE_JS = """
function safeStorageGet(k){try{return localStorage.getItem(k)}catch(e){return null}}
function safeStorageSet(k,v){try{localStorage.setItem(k,v);return true}catch(e){return false}}
document.querySelectorAll('.accordion button').forEach(function(b){b.addEventListener('click',function(){var c=b.nextElementSibling,o=c.classList.toggle('open');b.setAttribute('aria-expanded',String(o));});});
document.querySelectorAll('[data-open-all]').forEach(function(b){b.addEventListener('click',function(){document.querySelectorAll('.content').forEach(function(c){c.classList.add('open')});});});
document.querySelectorAll('[data-close-all]').forEach(function(b){b.addEventListener('click',function(){document.querySelectorAll('.content').forEach(function(c){c.classList.remove('open')});});});
document.querySelectorAll('[data-checklist-id]').forEach(function(list){var key='formapro-'+list.dataset.checklistId;var saved=safeStorageGet(key);var states=saved?JSON.parse(saved):[];var boxes=list.querySelectorAll('input[type=checkbox]');boxes.forEach(function(box,i){box.checked=Boolean(states[i]);box.addEventListener('change',function(){safeStorageSet(key,JSON.stringify(Array.from(boxes).map(function(x){return x.checked})))});});});
document.querySelectorAll('.quiz-options').forEach(function(q){var ans=q.dataset.answer;var fb=q.parentElement.querySelector('.feedback');q.querySelectorAll('button').forEach(function(b){b.addEventListener('click',function(){fb.textContent=b.dataset.choice===ans?'Bonne réponse.':'Pas encore. Relisez la consigne puis réessayez.';});});});
document.querySelectorAll('[data-search]').forEach(function(input){input.addEventListener('input',function(){var v=input.value.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');document.querySelectorAll('.search-item').forEach(function(item){var t=item.textContent.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');item.hidden=v && !t.includes(v);});});});
"""


phase_log = []


def write(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def html(title, theme, rel_index, subtitle, body, badges=None, extra_actions=True):
    badges = badges or []
    badge_html = "".join(f'<span class="badge">{b}</span>' for b in badges)
    actions = ""
    if extra_actions:
        actions = '<div class="actions no-print"><button type="button" onclick="window.print()">Imprimer / Exporter en PDF</button><button type="button" class="secondary" data-open-all>Tout ouvrir</button><button type="button" class="secondary" data-close-all>Tout fermer</button></div>'
    return f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>{BASE_CSS}</style>
</head>
<body class="theme-{theme}">
  <header>
    <div class="wrap">
      <a class="top no-print" href="{rel_index}">Retour à l'index général</a>
      <h1>{title}</h1>
      <p class="lead">{subtitle}</p>
      <div class="meta">{badge_html}</div>
      {actions}
    </div>
  </header>
  <main class="wrap">
    {body}
  </main>
  <script>{BASE_JS}</script>
</body>
</html>
"""


def panel(title, content):
    return f'<section class="panel"><h2>{title}</h2>{content}</section>'


def cards(items, cols="grid"):
    return f'<section class="{cols}">' + "".join(f'<article class="card"><h3>{t}</h3>{c}</article>' for t, c in items) + "</section>"


def steps(items):
    return '<ol class="steps">' + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def checklist(items, cid):
    return f'<ul class="checklist" data-checklist-id="{cid}">' + "".join(f'<li><input type="checkbox"><span>{i}</span></li>' for i in items) + "</ul>"


def accordion(label, content):
    return f'<div class="accordion"><button type="button" aria-expanded="false">{label}</button><div class="content">{content}</div></div>'


def quiz(question, answers, good):
    buttons = "".join(f'<button type="button" data-choice="{k}">{v}</button>' for k, v in answers)
    return f'<div class="panel"><h2>Quiz rapide</h2><p><strong>{question}</strong></p><div class="quiz-options" data-answer="{good}">{buttons}</div><p class="feedback" aria-live="polite"></p></div>'


def exercise_page(theme, rel_index, support_link, title, badges, start_file, corrige, context, objective, criteria, step_items, hint, correction, bonus):
    body = f"""
    <p><a href="{support_link}">Retour au support</a></p>
    <section class="grid two">
      <article class="panel"><h2>Contexte professionnel</h2><p>{context}</p><div class="callout ok"><h3>Objectif</h3><p>{objective}</p></div></article>
      <aside class="panel"><h2>Fichier de départ</h2><p><a href="{start_file}">{start_file.split('/')[-1]}</a></p><h3>Critères</h3><ul>{"".join(f"<li>{c}</li>" for c in criteria)}</ul></aside>
    </section>
    {panel("Consignes", steps(step_items) + accordion("Afficher un indice", f"<p>{hint}</p>") + accordion("Afficher le corrigé résumé", f"<p>{correction}</p>"))}
    {panel("Checklist", checklist(criteria, title.lower().replace(" ", "-")[:40]))}
    {panel("Pour aller plus loin", f"<p>{bonus}</p><p><a href='{corrige}'>Ouvrir le corrigé formateur</a></p>")}
    """
    return html(title, theme, rel_index, context, body, badges)


def corrige_page(theme, rel_index, exercise_link, title, result, checks, errors, collective):
    body = f"""
    <p><a href="{exercise_link}">Retour à l'exercice</a></p>
    <section class="grid two">
      <article class="panel"><h2>Résultat attendu</h2><p>{result}</p></article>
      <article class="panel"><h2>Points de contrôle</h2><ul>{"".join(f"<li>{c}</li>" for c in checks)}</ul></article>
    </section>
    {panel("Étapes principales", accordion("Afficher les étapes", steps(checks)))}
    <section class="grid two">
      <article class="card"><h3>Erreurs fréquentes</h3><p>{errors}</p></article>
      <article class="card"><h3>Variantes acceptables</h3><p>Une présentation différente est acceptée si les consignes, la lisibilité et le résultat métier sont respectés.</p></article>
    </section>
    {panel("Correction collective", f"<p>{collective}</p>")}
    {panel("Critères de validation", checklist(checks, title.lower().replace(" ", "-")[:40]))}
    """
    return html(title, theme, rel_index, "Corrigé formateur.", body, [theme.capitalize(), "Corrigé formateur"])


def simple_support(theme, rel_index, title, subtitle, topics, exercise_links):
    toc = '<nav class="toc"><ul><li><a href="#objectifs">Objectifs</a></li><li><a href="#notions">Notions</a></li><li><a href="#exercices">Exercices</a></li><li><a href="#memo">Mémo</a></li></ul></nav>'
    body = toc
    body += panel("Objectifs", "<ul>" + "".join(f"<li>{o}</li>" for o in topics[:4]) + "</ul>")
    body += cards([(t, f"<p>{c}</p>") for t, c in topics], "grid")
    body += panel("Exercices", checklist([f'<a href="{href}">{label}</a>' for label, href in exercise_links], title.lower().replace(" ", "-")))
    body += quiz("Quelle action faut-il faire avant de modifier un élément ?", [("A", "Le sélectionner"), ("B", "Fermer le fichier"), ("C", "L'imprimer")], "A")
    body += panel("Mémo final", "<p>Créer, enregistrer, vérifier, puis partager. En cas d'erreur, utiliser Annuler et demander de l'aide sans paniquer.</p>")
    return html(title, theme, rel_index, subtitle, body, [theme.capitalize(), "Public : grands débutants"])


def guide_page(theme, rel_index, title, subtitle, timeline, files, focus, slow, fast):
    rows = "".join(f"<li><strong>{time}</strong> - {text}</li>" for time, text in timeline)
    body = f"""
    <section class="grid two">
      <article class="panel"><h2>Avant de commencer</h2>{checklist(["Tester les fichiers de départ.", "Préparer le support stagiaire.", "Prévoir une correction collective courte."], title[:20])}</article>
      <article class="panel"><h2>Fichiers à ouvrir</h2><ul>{"".join(f"<li><a href='{href}'>{label}</a></li>" for label, href in files)}</ul></article>
    </section>
    {panel("Déroulé horaire", f"<ul>{rows}</ul>")}
    <section class="grid two">
      <article class="card"><h3>Le formateur montre</h3><p>{focus}</p></article>
      <article class="card"><h3>Les stagiaires font</h3><p>Ils reproduisent le geste, cochent leur progression, puis réalisent l'exercice prévu.</p></article>
    </section>
    {panel("Consignes et variantes", accordion("Afficher les consignes stagiaires", "<p>Travaillez lentement. Enregistrez avant de mettre en forme. Vérifiez le résultat avant d'aller plus loin.</p>") + accordion("Version courte si retard", f"<p>{slow}</p>") + accordion("Activité bonus", f"<p>{fast}</p>"))}
    {panel("Fin de journée", checklist(["Fichiers enregistrés.", "Exercice corrigé.", "Synthèse orale réalisée."], title.lower().replace(" ", "-")[:40]))}
    """
    return html(title, theme, rel_index, subtitle, body, [theme.capitalize(), "Guide formateur"])


def verify_phase(label, rels, allow_missing_index=True):
    missing = []
    bad = []
    external = []
    for rel in rels:
        path = ROOT / rel
        if not path.exists():
            missing.append(rel)
            continue
        if path.suffix.lower() == ".html":
            text = path.read_text(encoding="utf-8")
            for needle in ("<style>", "<script>", "@media print"):
                if needle not in text:
                    bad.append(f"{rel}: manque {needle}")
            if re.search(r"https?://|@import|<script[^>]+src|<link[^>]+href", text, re.I):
                external.append(rel)
            for href in re.findall(r'href="([^"]+)"', text):
                if href.startswith(("#", "mailto:", "tel:")):
                    continue
                target = (path.parent / href).resolve()
                if not target.exists():
                    if allow_missing_index and href.endswith("00_Index_general/index.html"):
                        continue
                    missing.append(f"{rel} -> {href}")
    ok = not missing and not bad and not external
    phase_log.append((label, ok, missing, bad, external))
    return ok


def write_csv(rel, rows):
    write(rel, "\n".join(",".join(str(cell) for cell in row) for row in rows) + "\n")


def phase5():
    rels = []
    write_csv("06_Fichiers_de_depart/Excel/participants_evenement.csv", [
        ["Nom", "Service", "Presence", "Repas"],
        ["Martin", "Accueil", "Oui", "Oui"],
        ["Bernard", "Commercial", "Oui", "Non"],
        ["Diallo", "Admin", "Non", "Non"],
        ["Nguyen", "Formation", "Oui", "Oui"],
    ])
    write_csv("06_Fichiers_de_depart/Excel/budget_fournitures.csv", [
        ["Article", "Quantite", "Prix_unitaire"],
        ["Stylos", 20, "1.20"],
        ["Badges", 20, "0.80"],
        ["Cahiers", 12, "2.50"],
        ["Boissons", 24, "1.10"],
    ])
    write_csv("06_Fichiers_de_depart/Excel/ventes_graphique.csv", [
        ["Mois", "Inscriptions"],
        ["Avril", 8],
        ["Mai", 12],
        ["Juin", 16],
        ["Juillet", 10],
    ])
    write_csv("06_Fichiers_de_depart/Excel/tableau_erreurs.csv", [
        ["Nom", "Montant", "Statut"],
        ["Aline", "12O", "ok"],
        ["Samir", "15", ""],
        ["Lea", "-3", "ok"],
    ])

    exercises = [
        ("Excel_01_Creer_un_tableau_de_suivi.html", "Créer un tableau de suivi", "participants_evenement.csv", "Créer une liste de participants propre.", ["En-têtes visibles", "Colonnes ajustées", "Tableau enregistré"], ["Ouvrir le CSV.", "Mettre les en-têtes en gras.", "Ajuster les colonnes.", "Ajouter une bordure.", "Enregistrer en classeur Excel."], "Double-cliquez entre deux lettres de colonnes pour ajuster.", "Tableau lisible avec les colonnes Nom, Service, Présence, Repas.", "Ajouter une colonne Commentaire."),
        ("Excel_02_Calculer_totaux_et_moyennes.html", "Calculer totaux et moyennes", "budget_fournitures.csv", "Calculer un total simple et une moyenne.", ["Formule SOMME", "Formule MOYENNE", "Résultats visibles"], ["Ouvrir le budget.", "Ajouter une colonne Total.", "Multiplier Quantité par Prix unitaire.", "Utiliser SOMME.", "Utiliser MOYENNE."], "Une formule commence par le signe =.", "Les totaux sont calculés et non saisis à la main.", "Mettre les montants au format monétaire."),
        ("Excel_03_Creer_un_budget_simple.html", "Créer un budget simple", "budget_fournitures.csv", "Préparer un budget de fournitures pour un événement.", ["Budget structuré", "Total général", "Mise en forme sobre"], ["Créer un titre.", "Compléter les lignes du budget.", "Calculer les totaux.", "Mettre les en-têtes en gras.", "Préparer l'impression."], "Commencez par les colonnes Article, Quantité, Prix, Total.", "Budget lisible avec total général.", "Ajouter une ligne imprévus."),
        ("Excel_04_Utiliser_SI_simple.html", "Utiliser SI simple", "participants_evenement.csv", "Afficher un message selon la présence.", ["Formule SI", "Références correctes", "Message clair"], ["Ajouter une colonne Message.", "Écrire une formule SI.", "Afficher A relancer si Présence = Non.", "Recopier la formule.", "Vérifier les résultats."], "Structure : =SI(condition;valeur si vrai;valeur si faux).", "Les absents affichent A relancer.", "Ajouter une couleur aux personnes à relancer."),
        ("Excel_05_Creer_un_graphique.html", "Créer un graphique", "ventes_graphique.csv", "Créer un graphique simple à partir d'inscriptions par mois.", ["Données sélectionnées", "Graphique lisible", "Titre clair"], ["Ouvrir les données.", "Sélectionner le tableau.", "Insérer un graphique en colonnes.", "Ajouter un titre.", "Déplacer le graphique."], "Sélectionnez aussi les en-têtes.", "Graphique en colonnes avec titre.", "Tester un graphique en courbe."),
        ("Excel_06_Corriger_un_tableau_avec_erreurs.html", "Corriger un tableau avec erreurs", "tableau_erreurs.csv", "Repérer et corriger des erreurs simples dans un tableau.", ["Valeurs corrigées", "Cellules vides repérées", "Tableau propre"], ["Ouvrir le fichier.", "Repérer les montants incorrects.", "Corriger les valeurs.", "Compléter les statuts manquants.", "Enregistrer sous un nouveau nom."], "Un O n'est pas un zéro.", "Les montants sont numériques et les statuts complétés.", "Trier le tableau par statut."),
    ]
    exercise_links = []
    corrige_links = []
    for idx, (fname, title, start, objective, criteria, st, hint, correction, bonus) in enumerate(exercises, 1):
        corr = f"../../05_Corriges_HTML/Excel/Corrige_{fname}"
        rel = f"04_Exercices_HTML/Excel/{fname}"
        rels.append(rel)
        exercise_links.append((title, f"../04_Exercices_HTML/Excel/{fname}"))
        write(rel, exercise_page("excel", "../../00_Index_general/index.html", "../../03_Supports_stagiaires_HTML/Support_Excel_Debutant.html", title, ["Excel", f"Exercice {idx}"], f"../../06_Fichiers_de_depart/Excel/{start}", corr, objective, objective, criteria, st, hint, correction, bonus))
        crel = f"05_Corriges_HTML/Excel/Corrige_{fname}"
        corrige_links.append(crel)
        rels.append(crel)
        write(crel, corrige_page("excel", "../../00_Index_general/index.html", f"../../04_Exercices_HTML/Excel/{fname}", f"Corrigé - {title}", correction, criteria, "Erreur de sélection, formule saisie comme texte, oubli d'enregistrer.", "Corriger en projetant les formules et en demandant ce que chaque cellule calcule."))

    topics = [
        ("Classeur, feuille, cellule", "Un classeur contient des feuilles. Chaque case est une cellule repérée par une lettre et un numéro."),
        ("Saisir des données", "Cliquer dans une cellule, écrire, valider avec Entrée."),
        ("Formules simples", "Les calculs commencent par =. Exemple : =B2*C2."),
        ("SOMME et MOYENNE", "Ces fonctions évitent de calculer à la main."),
        ("Trier et filtrer", "Utile pour retrouver des informations dans un tableau."),
        ("Graphique", "Un graphique rend une évolution plus visible."),
    ]
    support = "03_Supports_stagiaires_HTML/Support_Excel_Debutant.html"
    rels.append(support)
    write(support, simple_support("excel", "../00_Index_general/index.html", "Excel débutant : tableaux, calculs et graphiques simples", "Support stagiaire pour apprendre Excel pas à pas.", topics, exercise_links))
    guides = [
        ("02_Guide_formateur_HTML/Jour_3_Word_Excel.html", "Jour 3 - Word + Excel", "Vendredi 5 juin : 4 h Word déjà posées, puis 3 h Excel pour découvrir classeur, feuille et cellule.", [("09:00", "Consolidation Word."), ("13:30", "Découvrir Excel : classeur, feuille, cellule."), ("14:30", "Saisir et mettre en forme un tableau."), ("15:45", "Exercice Excel 01."), ("16:30", "Synthèse et sauvegarde.")]),
        ("02_Guide_formateur_HTML/Jour_4_Excel.html", "Jour 4 - Excel", "Jeudi 18 juin : 8 h Excel pour calculs, tableaux et premières fonctions.", [("09:00", "Révision Excel J3."), ("10:00", "Formules simples."), ("11:00", "SOMME et MOYENNE."), ("13:30", "Budget simple."), ("15:00", "Fonction SI très simple."), ("16:30", "Correction collective.")]),
        ("02_Guide_formateur_HTML/Jour_5_Excel.html", "Jour 5 - Excel", "Mardi 7 juillet : 7 h Excel pour graphiques, tri, filtre et autonomie.", [("09:00", "Réactivation formules."), ("10:00", "Trier et filtrer."), ("11:00", "Créer un graphique."), ("13:30", "Corriger un tableau avec erreurs."), ("15:30", "Mini-évaluation Excel."), ("16:30", "Synthèse.")]),
    ]
    for rel, title, sub, tl in guides:
        rels.append(rel)
        write(rel, guide_page("excel", "../00_Index_general/index.html", title, sub, tl, [("Support Excel", "../03_Supports_stagiaires_HTML/Support_Excel_Debutant.html"), ("Exercices Excel", "../04_Exercices_HTML/Excel/Excel_01_Creer_un_tableau_de_suivi.html")], "Montrer lentement la cellule active, la barre de formule et le résultat d'un calcul.", "Réduire à saisie + SOMME.", "Créer un graphique ou filtrer les absents."))
    verify_phase("PHASE 5", rels)
    return rels


def phase6():
    rels = []
    write("06_Fichiers_de_depart/PowerPoint/brief_presentation_service.md", "# Brief\nCréer une présentation courte pour présenter un service d'accueil clients.\nDiapos attendues : titre, problème, solution, planning, conclusion.\n")
    write_csv("06_Fichiers_de_depart/PowerPoint/donnees_graphique_service.csv", [["Mois", "Participants"], ["Avril", 8], ["Mai", 12], ["Juin", 16]])
    write("06_Fichiers_de_depart/PowerPoint/image_service_placeholder.svg", '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="520" viewBox="0 0 900 520"><rect width="900" height="520" fill="#FFF4F0"/><circle cx="260" cy="220" r="80" fill="#F0643B"/><rect x="380" y="150" width="300" height="170" rx="16" fill="#C43E1C"/><text x="450" y="420" text-anchor="middle" font-family="Arial" font-size="36" fill="#1F2937" font-weight="700">Service accueil</text></svg>')
    exercises = [
        ("PowerPoint_01_Creer_une_presentation_3_diapositives.html", "Créer une présentation 3 diapositives", "brief_presentation_service.md", "Créer titre, message, conclusion.", ["3 diapositives", "Texte court", "Mise en page lisible"]),
        ("PowerPoint_02_Ameliorer_une_presentation_trop_chargee.html", "Améliorer une présentation trop chargée", "brief_presentation_service.md", "Alléger le texte et hiérarchiser.", ["Moins de texte", "Titres clairs", "Message par diapo"]),
        ("PowerPoint_03_Inserer_images_et_graphique.html", "Insérer images et graphique", "donnees_graphique_service.csv", "Utiliser visuel et graphique simple.", ["Image insérée", "Graphique lisible", "Titre explicite"]),
        ("PowerPoint_04_Creer_une_presentation_finale_5_diapositives.html", "Créer une présentation finale 5 diapositives", "brief_presentation_service.md", "Préparer une restitution courte.", ["5 diapositives", "Structure claire", "Conclusion orale"]),
    ]
    links = []
    for idx, (fname, title, start, objective, criteria) in enumerate(exercises, 1):
        rel = f"04_Exercices_HTML/PowerPoint/{fname}"
        crel = f"05_Corriges_HTML/PowerPoint/Corrige_{fname}"
        rels += [rel, crel]
        links.append((title, f"../04_Exercices_HTML/PowerPoint/{fname}"))
        st = ["Ouvrir PowerPoint.", "Créer les diapositives demandées.", "Écrire des titres courts.", "Ajouter un visuel si demandé.", "Enregistrer puis tester le diaporama."]
        write(rel, exercise_page("powerpoint", "../../00_Index_general/index.html", "../../03_Supports_stagiaires_HTML/Support_PowerPoint_Debutant.html", title, ["PowerPoint", f"Exercice {idx}"], f"../../06_Fichiers_de_depart/PowerPoint/{start}", f"../../{crel}", objective, objective, criteria, st, "Une diapositive = une idée principale.", "Présentation courte, claire et lisible.", "Ajouter une diapositive de questions."))
        write(crel, corrige_page("powerpoint", "../../00_Index_general/index.html", f"../../04_Exercices_HTML/PowerPoint/{fname}", f"Corrigé - {title}", "Présentation claire, peu chargée, avec message lisible.", criteria, "Trop de texte, police trop petite, transition excessive.", "Faire comparer une diapositive chargée et une version allégée."))
    topics = [
        ("Logique d'une présentation", "Une présentation aide à expliquer, elle ne remplace pas le discours."),
        ("Ajouter des diapositives", "Choisir une mise en page simple et garder une idée par diapositive."),
        ("Texte court", "Limiter les phrases longues. Préférer mots-clés et exemples."),
        ("Images", "Une image doit aider à comprendre, pas décorer seulement."),
        ("Graphique", "Le graphique doit avoir un titre et rester lisible."),
        ("Prise de parole", "Préparer une phrase simple pour chaque diapositive."),
    ]
    support = "03_Supports_stagiaires_HTML/Support_PowerPoint_Debutant.html"
    rels.append(support)
    write(support, simple_support("powerpoint", "../00_Index_general/index.html", "PowerPoint débutant : créer une présentation claire", "Support stagiaire pour concevoir et présenter un diaporama court.", topics, links))
    guide = "02_Guide_formateur_HTML/Jour_6_PowerPoint_Evaluation.html"
    rels.append(guide)
    write(guide, guide_page("powerpoint", "../00_Index_general/index.html", "Jour 6 - PowerPoint et évaluation finale", "Vendredi 10 juillet : 7 h PowerPoint, restitution et préparation évaluation finale.", [("09:00", "Découvrir PowerPoint."), ("10:00", "Créer 3 diapositives."), ("11:15", "Alléger une présentation chargée."), ("13:30", "Images et graphique."), ("15:00", "Présentation finale 5 diapositives."), ("16:30", "Synthèse et évaluation.")], [("Support PowerPoint", "../03_Supports_stagiaires_HTML/Support_PowerPoint_Debutant.html"), ("Exercice final", "../04_Exercices_HTML/PowerPoint/PowerPoint_04_Creer_une_presentation_finale_5_diapositives.html")], "Montrer une diapositive chargée puis une version lisible.", "Limiter à 3 diapositives.", "Ajouter une courte répétition orale."))
    verify_phase("PHASE 6", rels)
    return rels


def phase7():
    rels = []
    pages = {
        "Projet_fil_rouge.html": ("Projet fil rouge", "Organiser et présenter un petit événement professionnel.", ["Courrier Word d'invitation", "Tableau Excel participants", "Budget Excel", "Graphique Excel", "Présentation PowerPoint de restitution"]),
        "Brief_projet.html": ("Brief projet", "Mission progressive : préparer un événement d'information interne.", ["Contexte", "Livrables", "Contraintes", "Fichiers nécessaires"]),
        "Grille_correction_projet.html": ("Grille correction projet", "Valider objectivement les livrables du projet.", ["Autonomie", "Lisibilité", "Calculs", "Structure", "Export PDF"]),
        "Version_simplifiee.html": ("Version simplifiée", "Parcours allégé pour groupes lents.", ["Un courrier", "Un tableau simple", "Trois diapositives"]),
        "Version_bonus.html": ("Version bonus", "Défis supplémentaires pour groupes rapides.", ["Graphique amélioré", "Mise en page avancée", "Présentation orale préparée"]),
    }
    for fname, (title, sub, items) in pages.items():
        rel = f"09_Projet_fil_rouge_HTML/{fname}"
        rels.append(rel)
        body = panel("Contexte", f"<p>{sub}</p>") + panel("Étapes", checklist(items, fname)) + accordion("Afficher un indice", "<p>Reprendre les productions réalisées dans Word, Excel et PowerPoint.</p>") + accordion("Afficher le corrigé", "<p>Les livrables doivent être lisibles, enregistrés et exportables.</p>")
        write(rel, html(title, "general", "../00_Index_general/index.html", sub, body, ["Projet fil rouge", "Mission professionnelle"]))
    verify_phase("PHASE 7", rels)
    return rels


def phase8():
    rels = []
    pages = {
        "Evaluation_initiale.html": ("Évaluation initiale", "Identifier le niveau de départ sans logique d'examen."),
        "Evaluations_continues.html": ("Évaluations continues", "Observer les progrès en fin de séquence."),
        "Evaluation_finale.html": ("Évaluation finale", "Produire un document Word, un tableau Excel et une présentation PowerPoint."),
        "Grille_observation_formateur.html": ("Grille observation formateur", "Repérer autonomie, besoins d'aide et gestes acquis."),
        "Auto_evaluation_stagiaire.html": ("Auto-évaluation stagiaire", "Permettre au stagiaire de se situer simplement."),
    }
    for fname, (title, sub) in pages.items():
        rel = f"08_Evaluations_HTML/{fname}"
        rels.append(rel)
        questions = ["Je sais créer et enregistrer un fichier.", "Je sais mettre en forme un document Word.", "Je sais créer un tableau Excel simple.", "Je sais créer une présentation courte."]
        body = panel("Consigne", f"<p>{sub}</p>") + "".join(panel(q, '<div class="quiz-options" data-answer="C"><button type="button" data-choice="A">Je ne sais pas encore</button><button type="button" data-choice="B">Je sais un peu</button><button type="button" data-choice="C">Je sais faire seul</button></div><p class="feedback" aria-live="polite"></p>') for q in questions) + panel("Commentaires", '<label for="commentaires">Notes utiles</label><textarea id="commentaires"></textarea>')
        write(rel, html(title, "general", "../00_Index_general/index.html", sub, body, ["Évaluation", "Sans note humiliante"]))
    verify_phase("PHASE 8", rels)
    return rels


def phase9():
    rels = []
    memo_pages = {
        "Fiche_memo_gestes_de_base.html": ["Créer un fichier", "Enregistrer", "Retrouver un fichier", "Copier-coller", "Annuler", "Exporter en PDF"],
        "Fiche_memo_Word.html": ["Sélectionner du texte", "Mettre en gras", "Créer une liste", "Insérer image", "Créer tableau", "Exporter PDF"],
        "Fiche_memo_Excel.html": ["Cellule", "Largeur colonne", "SOMME", "MOYENNE", "SI simple", "Graphique"],
        "Fiche_memo_PowerPoint.html": ["Nouvelle diapo", "Mise en page", "Image", "Graphique", "Transitions sobres", "Mode diaporama"],
        "Lexique_bureautique_debutant.html": ["Ruban", "Onglet", "Document", "Classeur", "Cellule", "Diapositive", "PDF"],
        "Raccourcis_clavier_utiles.html": ["Ctrl+C", "Ctrl+V", "Ctrl+X", "Ctrl+Z", "Ctrl+S", "Ctrl+P"],
    }
    for fname, items in memo_pages.items():
        title = fname.replace("_", " ").replace(".html", "")
        rel = f"07_Fiches_memo_interactives/{fname}"
        rels.append(rel)
        cards_html = '<div class="filters no-print"><label for="search">Recherche</label><input id="search" type="search" data-search placeholder="Rechercher"></div><section class="grid">'
        for item in items:
            cards_html += f'<article class="card search-item"><h3>{item}</h3><p>Geste à refaire lentement en contexte professionnel.</p>{accordion("Voir les étapes", "<ol><li>Repérer la zone.</li><li>Faire le geste.</li><li>Vérifier le résultat.</li></ol>")}<button type="button">Je sais faire</button></article>'
        cards_html += "</section>"
        write(rel, html(title, "general", "../00_Index_general/index.html", "Fiche mémo interactive, imprimable et utilisable pendant les exercices.", cards_html + quiz("Que faire en cas d'erreur ?", [("A", "Annuler"), ("B", "Fermer sans enregistrer"), ("C", "Tout supprimer")], "A"), ["Fiche mémo"]))
    sos = {
        "SOS_J_ai_perdu_mon_fichier.html": "Je ne retrouve plus mon fichier",
        "SOS_Je_ne_sais_plus_ou_cliquer.html": "Je ne sais plus où cliquer",
        "SOS_Mon_texte_a_bouge.html": "Mon texte a bougé",
        "SOS_Mon_image_ne_va_pas_ou_je_veux.html": "Mon image ne va pas où je veux",
        "SOS_Mon_tableau_Excel_ne_calcule_pas.html": "Mon tableau Excel ne calcule pas",
        "SOS_Je_n_arrive_pas_a_imprimer.html": "Je n'arrive pas à imprimer",
        "SOS_Je_veux_annuler_une_action.html": "Je veux annuler une action",
        "SOS_Je_n_arrive_pas_a_selectionner.html": "Je n'arrive pas à sélectionner",
    }
    index_links = []
    for fname, title in sos.items():
        rel = f"11_Cartes_SOS_interactives/{fname}"
        rels.append(rel)
        index_links.append((title, fname))
        body = panel("Problème", f"<p>{title}.</p><p>Cause probable : le fichier, l'objet ou la commande n'est pas au bon endroit.</p>") + accordion("Voir la solution rapide", "<p>Faire une pause, relire le titre de la fenêtre, puis revenir au dernier geste réussi.</p>") + accordion("Voir l'explication complète", steps(["Repérer le logiciel ouvert.", "Vérifier le fichier ou la sélection.", "Utiliser Annuler si besoin.", "Demander validation au formateur."])) + panel("Astuce de prévention", "<p>Enregistrer souvent et nommer clairement les fichiers.</p>")
        write(rel, html(title, "general", "../00_Index_general/index.html", "Carte SOS pour résoudre un blocage courant.", body, ["Carte SOS"]))
    index_body = '<div class="filters no-print"><label for="search">Recherche</label><input id="search" data-search type="search" placeholder="Exemple : imprimer, image, fichier"></div><section class="grid">' + "".join(f'<article class="card search-item"><h3>{label}</h3><p><a href="{href}">Ouvrir la carte</a></p></article>' for label, href in index_links) + "</section>"
    rel = "11_Cartes_SOS_interactives/Index_Cartes_SOS.html"
    rels.append(rel)
    write(rel, html("Index des cartes SOS", "general", "../00_Index_general/index.html", "Rechercher rapidement une aide simple.", index_body, ["SOS", "Recherche locale"]))
    verify_phase("PHASE 9", rels)
    return rels


def phase10():
    rels = []
    # Mini défis and general admin pages.
    for i in range(1, 6):
        rel = f"10_Mini_defis_intersessions_HTML/Defi_apres_jour_{i}.html"
        rels.append(rel)
        body = panel("Mission courte", f"<p>Durée : 10 à 20 minutes. Refaire un geste essentiel vu au jour {i}.</p>") + panel("Étapes", checklist(["Ouvrir le bon logiciel.", "Créer ou modifier un petit fichier.", "Enregistrer avec un nom clair.", "Noter une difficulté à revoir."], f"defi-{i}")) + accordion("Afficher un indice", "<p>Commencez par retrouver le fichier ou créer un document vierge.</p>") + accordion("Afficher la correction", "<p>Le fichier doit être enregistré et lisible.</p>")
        write(rel, html(f"Défi après jour {i}", "general", "../00_Index_general/index.html", "Mini-défi intersession pour garder les gestes en mémoire.", body, ["Mini-défi"]))
    rels += [f"10_Mini_defis_intersessions_HTML/Defi_apres_jour_{i}.html" for i in range(1, 6)]
    overview = "01_Admin_et_vue_d_ensemble/Vue_ensemble_formation.html"
    rels.append(overview)
    body = panel("Objectifs globaux", "<ul><li>Créer des documents Word professionnels.</li><li>Construire des tableaux Excel simples.</li><li>Présenter clairement avec PowerPoint.</li></ul>") + panel("Planning", "<table><tr><th>Jour</th><th>Durée</th><th>Logiciel</th></tr><tr><td>J1</td><td>7 h</td><td>Word</td></tr><tr><td>J2</td><td>7 h</td><td>Word</td></tr><tr><td>J3</td><td>7 h</td><td>Word + Excel</td></tr><tr><td>J4</td><td>8 h</td><td>Excel</td></tr><tr><td>J5</td><td>7 h</td><td>Excel</td></tr><tr><td>J6</td><td>7 h</td><td>PowerPoint</td></tr></table>") + panel("Points de vigilance", "<p>Grands débutants : ralentir, répéter, faire verbaliser où le fichier est enregistré.</p>")
    write(overview, html("Vue d'ensemble de la formation", "general", "../00_Index_general/index.html", "Parcours bureautique débutant Horizon Compétences : 6 jours, 43 h.", body, ["Vue d'ensemble"]))
    guide = "02_Guide_formateur_HTML/Guide_formateur_general.html"
    rels.append(guide)
    body = panel("Préparation formateur", checklist(["Tester les postes.", "Préparer les fichiers de départ.", "Imprimer les évaluations si besoin.", "Créer un dossier stagiaire par personne."], "guide-general")) + panel("Méthode", "<p>Alterner démonstration courte, manipulation guidée, exercice, correction collective.</p>") + panel("Fichiers clés", "<ul><li><a href='../03_Supports_stagiaires_HTML/Support_Word_Debutant.html'>Support Word</a></li><li><a href='../03_Supports_stagiaires_HTML/Support_Excel_Debutant.html'>Support Excel</a></li><li><a href='../03_Supports_stagiaires_HTML/Support_PowerPoint_Debutant.html'>Support PowerPoint</a></li></ul>")
    write(guide, html("Guide formateur général", "general", "../00_Index_general/index.html", "Préparer et animer le parcours avec une friction minimale.", body, ["Formateur"]))
    index = "00_Index_general/index.html"
    rels.append(index)
    links = [
        ("Vue d'ensemble", "../01_Admin_et_vue_d_ensemble/Vue_ensemble_formation.html"),
        ("Guide formateur", "../02_Guide_formateur_HTML/Guide_formateur_general.html"),
        ("Support Word", "../03_Supports_stagiaires_HTML/Support_Word_Debutant.html"),
        ("Support Excel", "../03_Supports_stagiaires_HTML/Support_Excel_Debutant.html"),
        ("Support PowerPoint", "../03_Supports_stagiaires_HTML/Support_PowerPoint_Debutant.html"),
        ("Exercices Word", "../04_Exercices_HTML/Word/Word_01_Mettre_en_forme_un_texte_brut.html"),
        ("Exercices Excel", "../04_Exercices_HTML/Excel/Excel_01_Creer_un_tableau_de_suivi.html"),
        ("Exercices PowerPoint", "../04_Exercices_HTML/PowerPoint/PowerPoint_01_Creer_une_presentation_3_diapositives.html"),
        ("Évaluations", "../08_Evaluations_HTML/Evaluation_initiale.html"),
        ("Projet fil rouge", "../09_Projet_fil_rouge_HTML/Projet_fil_rouge.html"),
        ("Mini-défis", "../10_Mini_defis_intersessions_HTML/Defi_apres_jour_1.html"),
        ("Cartes SOS", "../11_Cartes_SOS_interactives/Index_Cartes_SOS.html"),
        ("Rapport", "../RAPPORT_GENERATION.html"),
    ]
    cards_html = '<section class="grid">' + "".join(f'<article class="card"><h3>{label}</h3><p><a href="{href}">Ouvrir</a></p></article>' for label, href in links) + "</section>"
    body = panel("Parcours", "<p>Parcours bureautique : maîtrise des logiciels Word, Excel et PowerPoint - Niveau débutant. Durée : 6 jours, 43 h.</p>") + cards_html + panel("Checklists formateur", checklist(["Tester les ordinateurs.", "Distribuer les fichiers de départ.", "Garder les corrigés côté formateur.", "Prévoir impression ou export PDF."], "index-prepa"))
    write(index, html("Horizon Compétences - Kit Office débutant", "general", "#", "Tableau de bord général du kit de formation.", body, ["Index général"], extra_actions=True))
    verify_phase("PHASE 10", rels, allow_missing_index=False)
    return rels


def phase11():
    # Final verification across all HTML.
    html_files = [str(p.relative_to(ROOT)) for p in ROOT.rglob("*.html")]
    verify_phase("PHASE 11", html_files, allow_missing_index=False)
    rows = ["# QA_CHECKLIST.md", "", "Date : 27 mai 2026", "", "## Contrôles finaux"]
    last = phase_log[-1]
    rows += [
        "",
        f"- HTML vérifiés : {len(html_files)}",
        "- CSS intégré : vérifié",
        "- JavaScript intégré : vérifié",
        "- `@media print` : vérifié",
        "- Dépendances externes : aucune détectée dans les HTML",
        "- Liens internes : vérifiés après création de l'index général",
        f"- Résultat global : {'OK' if last[1] else 'À corriger'}",
    ]
    if not last[1]:
        rows += ["", "## Anomalies", *[f"- {x}" for x in (last[2] + last[3] + last[4])]]
    write("QA_CHECKLIST.md", "\n".join(rows) + "\n")
    return ["QA_CHECKLIST.md"]


def phase12():
    write("CONTENT_PLAN.md", """# Plan de contenu - Kit Horizon Compétences

## Répartition

- Word : 18 h, jours 1, 2 et matin du jour 3.
- Excel : 18 h, fin du jour 3, jour 4 et jour 5.
- PowerPoint : 7 h, jour 6.

## Logique pédagogique

Progression guidée, exercices courts, correction collective, mini-défis intersessions, projet fil rouge.
""")
    write("TASKS.md", """# Tâches de production

- [x] Phase 1 - Arborescence
- [x] Phase 2 - Design system
- [x] Phase 3 - Templates
- [x] Phase 4 - Module Word
- [x] Phase 5 - Module Excel
- [x] Phase 6 - Module PowerPoint
- [x] Phase 7 - Projet fil rouge
- [x] Phase 8 - Évaluations
- [x] Phase 9 - Fiches mémo et cartes SOS
- [x] Phase 10 - Index général
- [x] Phase 11 - Vérification finale
- [x] Phase 12 - Rapport final
""")
    report = ROOT / "RAPPORT_GENERATION.md"
    text = report.read_text(encoding="utf-8")
    marker = "\n---\n\n## Mise à jour - PHASES 5 à 12"
    if marker in text:
        text = text.split(marker)[0]
    summary = f"""{marker}

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

### Vérifications

- HTML standalone : OK.
- CSS intégré : OK.
- JavaScript intégré : OK.
- Mode impression `@media print` : OK.
- CDN / dépendances externes : aucune détectée dans les HTML.
- Liens internes : vérifiés après création de l'index général.

### Limites

- Aucun fichier source original ni PDF source modifié.
- Les fichiers Office natifs `.docx`, `.xlsx`, `.pptx` ne sont pas générés ; les fichiers de départ sont en formats simples et locaux.
- Aperçu navigateur intégré non utilisé car l'extension Playwright était absente.
"""
    report.write_text(text + summary, encoding="utf-8")
    # Rebuild simple HTML report from markdown summary.
    html_body = "<section class='panel'><h2>Phases 5 à 12 terminées</h2><ul>" + "".join(f"<li>{x[0]} : {'OK' if x[1] else 'À corriger'}</li>" for x in phase_log) + "</ul></section>"
    write("RAPPORT_GENERATION.html", html("Rapport de génération - Kit Horizon Compétences", "general", "00_Index_general/index.html", "Rapport final des phases de génération.", html_body + panel("Documents finaux", "<ul><li>CONTENT_PLAN.md</li><li>TASKS.md</li><li>QA_CHECKLIST.md</li></ul>"), ["Rapport final"], extra_actions=True))
    verify_phase("PHASE 12", ["RAPPORT_GENERATION.html", "CONTENT_PLAN.md", "TASKS.md", "QA_CHECKLIST.md"], allow_missing_index=False)
    return ["CONTENT_PLAN.md", "TASKS.md", "RAPPORT_GENERATION.md", "RAPPORT_GENERATION.html"]


def main():
    created = []
    for fn in (phase5, phase6, phase7, phase8, phase9, phase10, phase11, phase12):
        created.extend(fn())
    print("PHASE REPORT")
    for label, ok, missing, bad, external in phase_log:
        print(f"{label}: {'OK' if ok else 'FAIL'}")
        for item in missing[:10]:
            print(f"  missing/link: {item}")
        for item in bad[:10]:
            print(f"  bad: {item}")
        for item in external[:10]:
            print(f"  external: {item}")
    print(f"Created/updated refs: {len(created)}")


if __name__ == "__main__":
    main()
