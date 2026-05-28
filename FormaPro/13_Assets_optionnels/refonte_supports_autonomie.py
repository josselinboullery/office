from pathlib import Path
import importlib.util


ROOT = Path(__file__).resolve().parents[1]


def load_base_assets():
    generator_path = ROOT / "13_Assets_optionnels" / "generate_phases_5_12.py"
    spec = importlib.util.spec_from_file_location("formapro_generator", generator_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.BASE_CSS, module.BASE_JS


BASE_CSS, BASE_JS = load_base_assets()
BASE_CSS += """
.learning-path{display:grid;gap:1rem}
.lesson{background:#fff;border:1px solid var(--b);border-radius:var(--r);padding:1.25rem;margin-bottom:1rem}
.lesson h3{margin-top:0}
.do-dont{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.kbd{display:inline-block;border:1px solid var(--b);border-bottom-width:3px;border-radius:6px;background:#fff;padding:.08rem .35rem;font-weight:700;font-family:Consolas,monospace}
.mini-task{border-left:5px solid var(--ok);background:#F0FDF4;border-radius:var(--r);padding:1rem;margin:1rem 0}
.rescue{border-left:5px solid var(--w);background:#FFFBEB;border-radius:var(--r);padding:1rem;margin:1rem 0}
.example{border:1px dashed var(--b);border-radius:var(--r);padding:1rem;background:#fff}
.table-scroll{overflow-x:auto}.table-scroll table{min-width:780px}
@media(max-width:760px){.do-dont{grid-template-columns:1fr}.table-scroll table{min-width:640px}}
"""


def write(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def html_page(title, theme, subtitle, body, badges):
    badge_html = "".join(f'<span class="badge">{badge}</span>' for badge in badges)
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
      <a class="top no-print" href="../00_Index_general/index.html">Retour à l'index général</a>
      <h1>{title}</h1>
      <p class="lead">{subtitle}</p>
      <div class="meta">{badge_html}</div>
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


def ul(items):
    return "<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"


def steps(items):
    return '<ol class="steps">' + "".join(f"<li><span>{item}</span></li>" for item in items) + "</ol>"


def checklist(items, cid):
    return f'<ul class="checklist" data-checklist-id="{cid}">' + "".join(
        f'<li><input type="checkbox"><span>{item}</span></li>' for item in items
    ) + "</ul>"


def accordion(label, content):
    return f'<div class="accordion"><button type="button" aria-expanded="false">{label}</button><div class="content">{content}</div></div>'


def table(headers, rows):
    head = "<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>"
    body = "".join("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>" for row in rows)
    return f'<div class="table-scroll"><table>{head}{body}</table></div>'


def toc(items):
    return '<nav class="toc"><ul>' + "".join(f'<li><a href="#{ident}">{label}</a></li>' for ident, label in items) + "</ul></nav>"


def exercise_list(items, cid):
    return panel(
        "Exercices guidés",
        checklist([f'<a href="{href}">{label}</a><br><small>{desc}</small>' for label, href, desc in items], cid),
        "exercices",
    )


def word_support():
    body = toc([
        ("depart", "Départ"),
        ("interface", "Interface"),
        ("texte", "Texte"),
        ("forme", "Mise en forme"),
        ("styles", "Styles"),
        ("page", "Page"),
        ("images", "Images/tableaux"),
        ("pro", "Documents pros"),
        ("controle", "Contrôle"),
        ("exercices", "Exercices"),
    ])
    body += panel(
        "Avant de toucher au document",
        lesson(
            "Créer un fichier propre",
            steps([
                "Ouvrez Word, puis choisissez Document vierge.",
                "Cliquez sur Fichier, puis Enregistrer sous.",
                "Choisissez le dossier de travail demandé.",
                "Donnez un nom clair, par exemple <code>Courrier_invitation_Martin.docx</code>.",
                "Pendant le travail, utilisez <span class=\"kbd\">Ctrl</span> + <span class=\"kbd\">S</span> régulièrement.",
            ])
            + '<div class="rescue"><strong>Si vous ne retrouvez pas le fichier :</strong> ouvrez Fichier &gt; Informations ou Fichier &gt; Ouvrir &gt; Récent. Le chemin du fichier indique le dossier où il est enregistré.</div>',
        )
        + lesson(
            "Comprendre la règle de base",
            "<p>Dans Word, on sélectionne d'abord ce que l'on veut modifier, puis on applique une commande. Si rien n'est sélectionné, la commande agit seulement à l'endroit du curseur ou sur le futur texte.</p>"
            + table(["Action", "Ce qu'il faut sélectionner", "Commande utile"], [
                ["Mettre un mot en gras", "Le mot", "Accueil &gt; G"],
                ["Centrer un titre", "La ligne du titre ou le paragraphe", "Accueil &gt; Centrer"],
                ["Changer tout un document", "Tout le texte avec Ctrl+A", "Accueil &gt; Police, taille, interligne"],
            ]),
        ),
        "depart",
    )
    body += panel(
        "Comprendre l'interface de Word",
        lesson(
            "Les zones à connaître",
            table(["Zone", "Rôle", "Quand l'utiliser"], [
                ["Onglet Fichier", "Ouvre le mode Backstage : nouveau, ouvrir, enregistrer, imprimer, exporter.", "Pour gérer le document lui-même."],
                ["Ruban", "Grande barre de commandes organisée par onglets.", "Pour trouver les outils sans chercher partout."],
                ["Accueil", "Commandes quotidiennes : police, paragraphes, styles, copier/coller.", "Pour corriger et mettre en forme."],
                ["Insertion", "Ajoute tableau, image, page, numéro de page, en-tête/pied.", "Pour enrichir le document."],
                ["Conception", "Thèmes, couleurs, apparence globale.", "Pour harmoniser sans tout modifier à la main."],
                ["Mise en page / Disposition", "Marges, orientation, taille, sauts de page et de section.", "Pour préparer l'impression ou changer la structure."],
                ["Références", "Table des matières, notes, légendes.", "Pour les documents longs."],
                ["Révision", "Orthographe, grammaire, commentaires.", "Pour relire avant d'envoyer."],
            ]),
        )
        + lesson(
            "Barre d'accès rapide",
            "<p>Ajoutez-y les commandes que vous utilisez tout le temps : Enregistrer, Annuler, Rétablir, Aperçu avant impression. Cela évite de chercher les mêmes boutons à chaque exercice.</p>"
            + '<div class="mini-task"><strong>Entraînement :</strong> repérez Fichier, Accueil, Insertion, Mise en page et Révision. Pour chacun, dites à quoi il sert avant de cliquer.</div>',
        ),
        "interface",
    )
    body += panel(
        "Saisir, corriger et déplacer du texte",
        '<section class="learning-path">'
        + lesson("Écrire sans casser la page", steps([
            "Cliquez à l'endroit où le texte doit commencer.",
            "Tapez le texte sans appuyer sur Entrée à la fin de chaque ligne : Word revient à la ligne tout seul.",
            "Appuyez sur Entrée seulement pour créer un nouveau paragraphe.",
            "Utilisez <span class=\"kbd\">Retour arrière</span> pour effacer à gauche du curseur et <span class=\"kbd\">Suppr</span> pour effacer à droite.",
        ]))
        + lesson("Copier, couper, coller", table(["Besoin", "Geste", "À vérifier"], [
            ["Dupliquer un texte", "Sélectionner, Ctrl+C, cliquer à destination, Ctrl+V", "Le texte existe aux deux endroits."],
            ["Déplacer un texte", "Sélectionner, Ctrl+X, cliquer à destination, Ctrl+V", "Le texte n'existe plus à l'ancien endroit."],
            ["Annuler une erreur", "Ctrl+Z", "Le dernier changement disparaît."],
        ]))
        + '<div class="mini-task"><strong>Entraînement 3 minutes :</strong> écrivez trois phrases, sélectionnez la deuxième, copiez-la sous la troisième, puis annulez.</div>'
        + "</section>",
        "texte",
    )
    body += panel(
        "Mettre en forme sans surcharger",
        lesson("Raccourcis essentiels", table(["Raccourci", "Action", "Quand l'utiliser"], [
            ['<span class="kbd">Ctrl</span> + <span class="kbd">N</span>', "Créer un nouveau document.", "Démarrer un document vierge."],
            ['<span class="kbd">Ctrl</span> + <span class="kbd">S</span>', "Enregistrer.", "Après chaque étape importante."],
            ['<span class="kbd">Ctrl</span> + <span class="kbd">Z</span>', "Annuler.", "Quand une mise en forme ou suppression est mauvaise."],
            ['<span class="kbd">Ctrl</span> + <span class="kbd">C</span>', "Copier.", "Dupliquer du texte."],
            ['<span class="kbd">Ctrl</span> + <span class="kbd">V</span>', "Coller.", "Placer ce qui a été copié."],
            ['<span class="kbd">Ctrl</span> + <span class="kbd">A</span>', "Tout sélectionner.", "Modifier tout le document d'un coup."],
            ['<span class="kbd">Ctrl</span> + <span class="kbd">G</span>', "Mettre en gras.", "Faire ressortir un mot ou titre."],
            ['<span class="kbd">Ctrl</span> + <span class="kbd">I</span>', "Mettre en italique.", "Nuancer un mot, un exemple ou une courte citation."],
        ]))
        + lesson("Caractères", "<p>Les commandes de caractères changent l'apparence des lettres : police, taille, gras, italique, souligné, couleur, surlignage, exposant, indice. Utilisez-les pour hiérarchiser l'information, pas pour décorer chaque ligne.</p>")
        + table(["Commande", "Effet", "Bon usage"], [
            ["Police", "Change la forme des lettres.", "Choisir une police sobre : Calibri, Arial, Verdana."],
            ["Taille", "Rend le texte plus grand ou plus petit.", "Titre plus grand que le corps de texte."],
            ["Gras", "Donne du poids visuel.", "Titre, mot clé, information prioritaire."],
            ["Italique", "Nuance ou distingue.", "Exemple, citation courte, terme étranger."],
            ["Souligné", "Ajoute un trait sous le texte.", "À éviter sauf cas précis : cela peut ressembler à un lien."],
            ["Couleur", "Classe ou signale.", "Deux couleurs maximum dans un document simple."],
            ["Exposant / indice", "Décale le texte vers le haut ou le bas.", "m², H₂O, appels de note."],
        ])
        + lesson("Paragraphes", "<p>Les commandes de paragraphe organisent des blocs : alignement, listes, retraits, interligne, espace avant/après. Elles rendent le document plus lisible.</p>")
        + table(["Problème visible", "Cause probable", "Solution"], [
            ["Le texte est collé au titre", "Pas assez d'espace entre paragraphes", "Accueil &gt; Interligne et espacement"],
            ["Tout est en gras", "Trop de texte sélectionné", "Ctrl+Z, puis sélectionner seulement le titre"],
            ["La liste ne s'aligne pas", "Retraits mélangés", "Sélectionner la liste puis réappliquer Puces ou Numérotation"],
        ]),
        "forme",
    )
    body += panel(
        "Utiliser les styles et une table des matières",
        lesson(
            "Pourquoi utiliser les styles",
            "<p>Un style applique plusieurs réglages d'un coup. Il évite de refaire à la main la taille, la couleur et l'espacement de chaque titre. Il permet aussi à Word de reconnaître la structure du document.</p>"
            + table(["Style", "Usage", "Exemple"], [
                ["Normal", "Texte courant.", "Paragraphes du courrier ou de la fiche."],
                ["Titre 1", "Grandes parties.", "1. Présentation, 2. Expérience."],
                ["Titre 2", "Sous-parties.", "Missions, Compétences, Formation."],
            ]),
        )
        + lesson(
            "Créer une table des matières automatique",
            steps([
                "Appliquez Titre 1 aux grandes parties.",
                "Appliquez Titre 2 aux sous-parties.",
                "Placez le curseur au début du document.",
                "Cliquez sur Références &gt; Table des matières.",
                "Choisissez un modèle automatique.",
                "Si les titres changent, cliquez dans la table puis choisissez Mettre à jour.",
            ]),
        )
        + '<div class="rescue"><strong>Si un titre manque dans la table :</strong> retournez sur ce titre et appliquez le bon style. Une mise en gras manuelle ne suffit pas.</div>',
        "styles",
    )
    body += panel(
        "Préparer la page et le PDF",
        lesson("Marges, orientation et aperçu", steps([
            "Cliquez sur Mise en page ou Disposition.",
            "Choisissez Marges normales si le document est simple.",
            "Gardez Portrait pour courrier et fiche ; utilisez Paysage seulement pour un tableau large.",
            "Ouvrez Fichier &gt; Imprimer pour vérifier l'aperçu.",
            "Si tout est lisible, exportez en PDF avec Fichier &gt; Exporter ou Enregistrer sous &gt; PDF.",
        ]))
        + lesson("Numéroter à partir de la page 2", steps([
            "Insérez d'abord les numéros de page : Insertion &gt; Numéro de page.",
            "Double-cliquez dans l'en-tête ou le pied de page.",
            "Cochez Première page différente pour masquer le numéro de la page de garde.",
            "Sur la page 2, ouvrez Numéro de page &gt; Format des numéros de page.",
            "Choisissez À partir de et tapez 1 si la page 2 doit devenir la page 1.",
        ]))
        + lesson("Sauts de page et sauts de section", "<p>Un saut de page force le début d'une nouvelle page. Un saut de section permet de changer une partie du document : orientation, marges, en-tête ou numérotation.</p>")
        + '<div class="rescue"><strong>Si une page vide apparaît :</strong> activez les marques ¶ dans Accueil. Supprimez les paragraphes vides en trop en fin de document.</div>',
        "page",
    )
    body += panel(
        "Insérer une image et un tableau",
        lesson("Image", steps([
            "Placez le curseur à l'endroit voulu.",
            "Cliquez sur Insertion &gt; Images.",
            "Choisissez l'image, puis validez.",
            "Si l'image gêne le texte, cliquez dessus et choisissez Options de disposition.",
            "Pour débuter, utilisez Aligné sur le texte ou Carré.",
        ]))
        + lesson("Tableau", steps([
            "Cliquez sur Insertion &gt; Tableau.",
            "Choisissez le nombre de colonnes et de lignes.",
            "Saisissez une information par cellule.",
            "Utilisez Création de tableau pour les bordures et Disposition pour ajouter/supprimer une ligne.",
            "Ajustez la largeur si le tableau déborde.",
        ])),
        "images",
    )
    body += panel(
        "Créer des documents professionnels",
        lesson(
            "Courrier, fiche, CV : même logique",
            "<p>Un document professionnel doit être facile à lire, nommé clairement et exporté en PDF avant l'envoi. La forme sert le contenu : titres nets, peu de couleurs, polices sobres, espaces réguliers.</p>"
            + table(["Document", "Structure conseillée", "Point de vigilance"], [
                ["Courrier", "Coordonnées, date, objet, corps, formule, signature.", "Objet clair et paragraphes courts."],
                ["Fiche de présentation", "Titre, sections, informations clés, contact.", "Même style pour tous les titres."],
                ["CV", "Identité, titre, compétences, expérience, formation, logiciels/langues, centres d'intérêt.", "Ordre antéchronologique pour les expériences."],
                ["Candidature PDF", "CV + lettre ou message court.", "Nom de fichier clair : CV_Prenom_Nom.pdf."],
            ]),
        )
        + lesson(
            "QuickParts : blocs réutilisables",
            "<p>Les QuickParts servent à réutiliser un bloc de texte ou un élément récurrent : logo, formule de politesse, signature, mention légale. Chemin : Insertion &gt; Texte &gt; QuickPart.</p>"
        )
        + lesson(
            "Envoyer une candidature par email",
            table(["Élément", "Règle simple"], [
                ["Objet", "Intitulé du poste + référence si elle existe."],
                ["Adresse email", "Adresse sobre, lisible, professionnelle."],
                ["Corps du message", "Court : 10 à 15 lignes maximum."],
                ["Pièces jointes", "PDF pour garder la mise en page."],
                ["Formule", "Simple, correcte, sans abréviation."],
            ]),
        )
        + '<div class="rescue"><strong>À éviter :</strong> trop de couleurs, soulignements décoratifs, polices fantaisie, fichier nommé <code>document1.pdf</code>, document envoyé sans relecture.</div>',
        "pro",
    )
    body += panel(
        "Contrôle avant de rendre",
        checklist([
            "Le fichier est enregistré au bon endroit.",
            "Le nom du fichier est clair.",
            "Le titre est visible et le texte principal reste lisible.",
            "Les styles de titres sont utilisés si le document est long.",
            "Les paragraphes ne sont pas collés les uns aux autres.",
            "Les images et tableaux ne coupent pas le texte.",
            "L'orthographe a été vérifiée dans Révision.",
            "L'aperçu avant impression est propre.",
            "Le PDF s'ouvre et ressemble au document Word.",
        ], "word-controle"),
        "controle",
    )
    body += exercise_list([
        ("Word 01 - Mettre en forme un texte brut", "../04_Exercices_HTML/Word/Word_01_Mettre_en_forme_un_texte_brut.html", "S'entraîner à sélectionner, titrer, aérer et corriger."),
        ("Word 02 - Créer un courrier professionnel", "../04_Exercices_HTML/Word/Word_02_Creer_un_courrier_professionnel.html", "Construire un courrier avec adresse, objet, formule et signature."),
        ("Word 03 - Insérer image et tableau", "../04_Exercices_HTML/Word/Word_03_Inserer_image_et_tableau.html", "Ajouter des éléments visuels sans casser la mise en page."),
        ("Word 04 - Créer une fiche de présentation", "../04_Exercices_HTML/Word/Word_04_Creer_une_fiche_de_presentation.html", "Organiser une fiche claire avec titres et sections."),
        ("Word 05 - Corriger un document mal présenté", "../04_Exercices_HTML/Word/Word_05_Corriger_un_document_mal_presente.html", "Diagnostiquer et réparer une mise en forme confuse."),
    ], "support-word-refonte-exercices")
    write(
        "03_Supports_stagiaires_HTML/Support_Word_Debutant.html",
        html_page("Word débutant : créer un document professionnel pas à pas", "word", "Guide pratique pour ouvrir Word, écrire, mettre en forme, insérer des éléments, vérifier et exporter.", body, ["Word", "Support pratique", "Débutant"]),
    )


def excel_support():
    body = toc([
        ("depart", "Départ"),
        ("saisie", "Saisie"),
        ("tableau", "Tableau"),
        ("formules", "Formules"),
        ("references", "Références"),
        ("impression", "Impression"),
        ("graphiques", "Graphiques"),
        ("controle", "Contrôle"),
        ("exercices", "Exercices"),
    ])
    body += panel(
        "Démarrer dans Excel",
        lesson("Se repérer", table(["Élément", "À quoi ça sert", "Ce que vous devez vérifier"], [
            ["Classeur", "Le fichier Excel complet", "Le bon fichier est ouvert et enregistré."],
            ["Feuille", "Un onglet dans le classeur", "Vous travaillez sur le bon onglet."],
            ["Cellule active", "La case où Excel va écrire", "Son adresse s'affiche dans la zone Nom, ex. B2."],
            ["Barre de formule", "Le vrai contenu de la cellule", "Une formule commence par =."],
            ["Poignée de recopie", "Petit carré en bas à droite de la cellule", "Elle sert à recopier ou créer une série."],
        ]))
        + lesson("Créer un classeur propre", steps([
            "Ouvrez Excel et choisissez Nouveau classeur.",
            "Enregistrez immédiatement le fichier dans le bon dossier.",
            "Renommez la feuille avec un nom utile : Budget, Participants, Suivi.",
            "Saisissez d'abord les titres de colonnes.",
            "Enregistrez avec Ctrl+S avant la mise en forme.",
        ])),
        "depart",
    )
    body += panel(
        "Saisir les données correctement",
        lesson("Saisir et valider", steps([
            "Cliquez dans la cellule où l'information doit aller.",
            "Tapez la valeur.",
            "Validez avec Entrée pour descendre ou Tab pour aller à droite.",
            "Pour modifier, recliquez dans la cellule ou utilisez la barre de formule.",
            "Pour supprimer le contenu, sélectionnez la cellule puis appuyez sur Suppr.",
        ]))
        + lesson("Texte, nombre et date", table(["Type", "Signe visible", "Erreur fréquente"], [
            ["Texte", "Souvent aligné à gauche", "Saisir un nombre comme texte : il ne calcule pas."],
            ["Nombre", "Souvent aligné à droite", "Mettre le symbole € à la main au lieu d'utiliser le format."],
            ["Date", "Affichage de date, contenu numérique", "Confondre affichage et valeur réelle."],
        ]))
        + '<div class="mini-task"><strong>Entraînement :</strong> saisissez Nom, Quantité, Prix unitaire et Total sur la première ligne. Ajustez les colonnes par double-clic entre les lettres.</div>',
        "saisie",
    )
    body += panel(
        "Construire un tableau lisible",
        lesson("Ordre conseillé", steps([
            "Ligne 1 : mettez les noms de colonnes.",
            "Une ligne = un élément ou une personne.",
            "Une colonne = un type d'information.",
            "Mettez les en-têtes en gras.",
            "Ajoutez des bordures simples.",
            "Appliquez les formats : nombre, monétaire, pourcentage ou date.",
        ]))
        + table(["Symptôme", "Cause", "Solution"], [
            ["###", "Colonne trop étroite", "Agrandir la colonne."],
            ["Nombre aligné à gauche", "Nombre stocké comme texte", "Retaper proprement ou convertir."],
            ["Tableau difficile à lire", "Trop de couleurs ou pas de bordures", "Garder une couleur d'en-tête et des bordures sobres."],
            ["Tri impossible", "Cellules fusionnées dans la zone", "Éviter Fusionner dans les tableaux de données."],
        ]),
        "tableau",
    )
    body += panel(
        "Créer des formules sans se perdre",
        lesson("La méthode en 5 gestes", steps([
            "Cliquez dans la cellule du résultat.",
            "Tapez <code>=</code>.",
            "Cliquez la première cellule utile ou tapez son adresse.",
            "Tapez l'opérateur : <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>.",
            "Cliquez la deuxième cellule utile, puis validez avec Entrée.",
        ]))
        + lesson("Exemples", table(["Besoin", "Formule", "En langage naturel"], [
            ["Total ligne", "<code>=B2*C2</code>", "Quantité multipliée par prix unitaire."],
            ["Somme", "<code>=SOMME(D2:D8)</code>", "Additionner tous les montants de D2 à D8."],
            ["Moyenne", "<code>=MOYENNE(D2:D8)</code>", "Calculer la valeur moyenne de la plage."],
            ["Condition SI", "<code>=SI(C2=\"Non\";\"A relancer\";\"OK\")</code>", "Si C2 contient Non, afficher A relancer ; sinon afficher OK."],
        ]))
        + '<div class="rescue"><strong>Si une formule donne une erreur :</strong> cliquez la cellule, lisez la barre de formule, vérifiez les cellules utilisées, puis corrigez une seule chose à la fois.</div>',
        "formules",
    )
    body += panel(
        "Recopier, créer des séries et bloquer une référence",
        lesson("Recopie simple", "<p>Quand une formule fonctionne sur une ligne, utilisez la poignée de recopie pour l'étendre. Vérifiez ensuite une formule copiée au milieu du tableau.</p>")
        + lesson("Références", table(["Type", "Ce qui se passe", "Exemple"], [
            ["Relative", "La référence change quand on recopie", "<code>=B2*C2</code> devient <code>=B3*C3</code>."],
            ["Absolue", "La référence reste fixe grâce au signe $", "<code>=B2*$F$2</code> garde toujours le taux en F2."],
            ["Série", "Excel continue une suite", "Janvier, Février, Mars ; ou 1, 2, 3."],
        ])),
        "references",
    )
    body += panel(
        "Préparer l'impression",
        steps([
            "Passez en Affichage &gt; Mise en page ou ouvrez Fichier &gt; Imprimer.",
            "Choisissez Portrait ou Paysage.",
            "Ajustez les marges si le tableau est trop large.",
            "Utilisez l'échelle seulement si le tableau dépasse légèrement.",
            "Définissez une zone d'impression si seule une partie doit sortir.",
            "Vérifiez que le titre, les colonnes et les totaux sont lisibles.",
        ])
        + '<div class="rescue"><strong>Si le tableau est coupé :</strong> passez en paysage, ajustez à 1 page en largeur, ou réduisez les colonnes inutiles.</div>',
        "impression",
    )
    body += panel(
        "Graphiques et mise en forme conditionnelle",
        lesson("Choisir le graphique", table(["Question", "Graphique conseillé", "Exemple"], [
            ["Comparer des montants", "Colonnes ou barres", "Ventes par commercial."],
            ["Montrer une évolution", "Courbe", "Inscriptions par mois."],
            ["Montrer une proportion simple", "Secteur", "Répartition d'un budget."],
        ]))
        + lesson("Créer un graphique", steps([
            "Sélectionnez les données utiles avec les en-têtes.",
            "N'incluez pas les totaux si cela fausse le graphique.",
            "Cliquez sur Insertion, puis choisissez le graphique.",
            "Ajoutez un titre clair.",
            "Vérifiez que les axes et la légende sont compréhensibles.",
        ]))
        + lesson("Repérer automatiquement", "<p>La mise en forme conditionnelle colore ou signale les cellules selon une règle. Exemple : colorer les écarts négatifs en rouge, afficher des barres de données ou repérer les doublons.</p>"),
        "graphiques",
    )
    body += panel(
        "Contrôle avant de rendre",
        checklist([
            "Le classeur est enregistré au bon endroit.",
            "Les en-têtes sont lisibles.",
            "Les montants sont au bon format.",
            "Les formules commencent par = et utilisent les bonnes cellules.",
            "Les formules recopiées ont été vérifiées sur au moins une ligne.",
            "L'aperçu avant impression ne coupe pas le tableau.",
            "Le graphique répond à une question claire.",
        ], "excel-controle"),
        "controle",
    )
    body += exercise_list([
        ("Excel 01 - Créer un tableau de suivi", "../04_Exercices_HTML/Excel/Excel_01_Creer_un_tableau_de_suivi.html", "Saisie, en-têtes, bordures, colonnes."),
        ("Excel 02 - Calculer totaux et moyennes", "../04_Exercices_HTML/Excel/Excel_02_Calculer_totaux_et_moyennes.html", "Formules, SOMME, MOYENNE, formats."),
        ("Excel 03 - Créer un budget simple", "../04_Exercices_HTML/Excel/Excel_03_Creer_un_budget_simple.html", "Structure, total général, présentation."),
        ("Excel 04 - Utiliser SI simple", "../04_Exercices_HTML/Excel/Excel_04_Utiliser_SI_simple.html", "Condition, résultat si vrai, résultat si faux."),
        ("Excel 05 - Créer un graphique", "../04_Exercices_HTML/Excel/Excel_05_Creer_un_graphique.html", "Sélection de données, titre, axes."),
        ("Excel 06 - Corriger un tableau avec erreurs", "../04_Exercices_HTML/Excel/Excel_06_Corriger_un_tableau_avec_erreurs.html", "Diagnostic et correction."),
        ("Excel 07 - Mise en page et impression", "../04_Exercices_HTML/Excel/Excel_07_Mise_en_page_et_impression.html", "Orientation, zone, aperçu."),
        ("Excel 08 - Séries et recopie", "../04_Exercices_HTML/Excel/Excel_08_Series_et_recopie_de_formules.html", "Poignée de recopie, suites, formules."),
        ("Excel 09 - Références absolues", "../04_Exercices_HTML/Excel/Excel_09_References_absolues_commission.html", "Référence $ et taux fixe."),
        ("Excel 10 - Graphiques et MFC", "../04_Exercices_HTML/Excel/Excel_10_Graphiques_et_mise_en_forme_conditionnelle.html", "Graphique, règles visuelles, commentaire."),
    ], "support-excel-refonte-exercices")
    write(
        "03_Supports_stagiaires_HTML/Support_Excel_Debutant.html",
        html_page("Excel débutant : construire, calculer, vérifier", "excel", "Guide pratique pour créer un classeur, saisir des données, calculer, imprimer et présenter les résultats.", body, ["Excel", "Support pratique", "Débutant"]),
    )


def powerpoint_support():
    body = toc([
        ("depart", "Départ"),
        ("structure", "Structure"),
        ("diapos", "Diapos"),
        ("visuels", "Visuels"),
        ("graphiques", "Graphiques"),
        ("oral", "Oral"),
        ("controle", "Contrôle"),
        ("exercices", "Exercices"),
    ])
    body += panel(
        "Démarrer une présentation",
        lesson("Créer et enregistrer", steps([
            "Ouvrez PowerPoint.",
            "Choisissez Nouvelle présentation ou un modèle très simple.",
            "Enregistrez immédiatement le fichier avec un nom clair.",
            "Écrivez le sujet dans la première diapositive.",
            "Enregistrez régulièrement avec Ctrl+S.",
        ]))
        + lesson("Comprendre l'écran", table(["Zone", "Rôle", "À faire"], [
            ["Miniatures à gauche", "Voir l'ordre des diapositives", "Cliquer une miniature pour la modifier."],
            ["Grande diapositive", "Zone de travail", "Sélectionner les textes, images et formes."],
            ["Ruban", "Commandes", "Utiliser Accueil, Insertion, Création, Transitions."],
            ["Notes", "Aide pour l'oral", "Écrire une phrase à dire, pas un paragraphe."],
        ])),
        "depart",
    )
    body += panel(
        "Construire le message avant la décoration",
        lesson("La règle simple", "<p>Une diapositive doit porter une seule idée. Si deux idées se battent sur la même diapositive, créez deux diapositives.</p>")
        + lesson("Plan court conseillé", table(["Diapositive", "Contenu", "Question à se poser"], [
            ["1", "Titre + contexte", "De quoi parle la présentation ?"],
            ["2", "Problème ou besoin", "Pourquoi ce sujet existe ?"],
            ["3", "Données ou exemple", "Quelle preuve ou information appuie le message ?"],
            ["4", "Solution ou proposition", "Que faut-il retenir ou décider ?"],
            ["5", "Conclusion", "Quelle est la prochaine action ?"],
        ]))
        + '<div class="mini-task"><strong>Entraînement :</strong> écrivez le titre de 5 diapositives avant de choisir les couleurs ou les images.</div>',
        "structure",
    )
    body += panel(
        "Créer des diapositives lisibles",
        lesson("Ajouter une diapositive", steps([
            "Cliquez sur Accueil &gt; Nouvelle diapositive.",
            "Choisissez une disposition simple : Titre et contenu, Deux contenus ou Titre seul.",
            "Écrivez un titre précis.",
            "Ajoutez 3 à 5 points maximum.",
            "Relisez en plein écran : si vous devez plisser les yeux, c'est trop petit ou trop chargé.",
        ]))
        + lesson("Texte", table(["À faire", "À éviter"], [
            ["Mots clés, verbes d'action, exemples concrets", "Paragraphes complets copiés depuis Word"],
            ["Police assez grande", "Texte inférieur à 20 pt pour une présentation projetée"],
            ["Alignement régulier", "Objets placés au hasard"],
        ])),
        "diapos",
    )
    body += panel(
        "Images, formes et mise en page",
        lesson("Insérer une image", steps([
            "Cliquez sur Insertion &gt; Images.",
            "Choisissez une image utile au message.",
            "Redimensionnez depuis un coin pour éviter de la déformer.",
            "Alignez-la avec le texte ou les autres objets.",
            "Supprimez l'image si elle ne rend pas le message plus clair.",
        ]))
        + lesson("Utiliser les formes", "<p>Les formes servent à organiser : encadrer une information, montrer une étape, relier deux idées. Gardez peu de couleurs et alignez les objets.</p>")
        + '<div class="rescue"><strong>Si tout bouge mal :</strong> sélectionnez les objets, puis utilisez Format &gt; Aligner. Dupliquez une diapositive propre au lieu de repartir de zéro.</div>',
        "visuels",
    )
    body += panel(
        "Graphiques et données",
        lesson("Quand utiliser un graphique", table(["Besoin", "Choix conseillé", "Point de contrôle"], [
            ["Comparer", "Colonnes ou barres", "Les valeurs sont lisibles."],
            ["Montrer une évolution", "Courbe", "L'ordre chronologique est clair."],
            ["Montrer une part", "Secteur", "Peu de catégories, total cohérent."],
        ]))
        + lesson("Insérer depuis Excel", steps([
            "Préparez le tableau ou graphique dans Excel.",
            "Copiez le graphique.",
            "Collez dans PowerPoint.",
            "Redimensionnez sans déformer.",
            "Ajoutez un titre qui dit ce que le graphique montre.",
        ])),
        "graphiques",
    )
    body += panel(
        "Préparer la prise de parole",
        lesson("Mode diaporama", steps([
            "Cliquez sur Diaporama &gt; À partir du début.",
            "Passez les diapositives avec les flèches du clavier.",
            "Vérifiez que chaque diapositive est lisible sans zoom.",
            "Préparez une phrase d'ouverture et une phrase de conclusion.",
            "Si une diapositive demande trop d'explications, simplifiez-la.",
        ]))
        + lesson("Notes orales", "<p>Les notes servent à vous rappeler quoi dire. Elles ne doivent pas être tout le texte de la diapositive.</p>"),
        "oral",
    )
    body += panel(
        "Contrôle avant de présenter",
        checklist([
            "Le fichier est enregistré au bon endroit.",
            "Chaque diapositive a un titre clair.",
            "Une diapositive = une idée principale.",
            "Le texte est lisible en mode diaporama.",
            "Les images ne sont pas déformées.",
            "Les graphiques ont un titre et des valeurs lisibles.",
            "Les transitions restent sobres.",
            "La présentation a été testée du début à la fin.",
        ], "powerpoint-controle"),
        "controle",
    )
    body += exercise_list([
        ("PowerPoint 01 - Créer une présentation 3 diapositives", "../04_Exercices_HTML/PowerPoint/PowerPoint_01_Creer_une_presentation_3_diapositives.html", "Sujet court, structure simple, lisibilité."),
        ("PowerPoint 02 - Améliorer une présentation trop chargée", "../04_Exercices_HTML/PowerPoint/PowerPoint_02_Ameliorer_une_presentation_trop_chargee.html", "Simplifier, hiérarchiser, alléger."),
        ("PowerPoint 03 - Insérer images et graphique", "../04_Exercices_HTML/PowerPoint/PowerPoint_03_Inserer_images_et_graphique.html", "Visuel utile, graphique lisible, titre clair."),
        ("PowerPoint 04 - Présentation finale 5 diapositives", "../04_Exercices_HTML/PowerPoint/PowerPoint_04_Creer_une_presentation_finale_5_diapositives.html", "Parcours complet et restitution orale."),
    ], "support-powerpoint-refonte-exercices")
    write(
        "03_Supports_stagiaires_HTML/Support_PowerPoint_Debutant.html",
        html_page("PowerPoint débutant : construire une présentation claire", "powerpoint", "Guide pratique pour structurer, créer, illustrer et présenter un diaporama simple.", body, ["PowerPoint", "Support pratique", "Débutant"]),
    )


def update_reports():
    report = ROOT / "RAPPORT_GENERATION.md"
    marker = "\n---\n\n## Mise à jour - refonte supports autonomes"
    text = report.read_text(encoding="utf-8") if report.exists() else "# Rapport de génération - Kit Horizon Compétences\n"
    if marker in text:
        text = text.split(marker)[0]
    text += f"""{marker}

Date de mise à jour : 28 mai 2026

### Supports refondus

- `Support_Word_Debutant.html` : parcours pas-à-pas, gestes de base, mise en forme, page, images/tableaux, contrôle final.
- `Support_Excel_Debutant.html` : démarrage, saisie, tableaux, formules, références, impression, graphiques, contrôle final.
- `Support_PowerPoint_Debutant.html` : structure, diapositives, visuels, graphiques, oral, contrôle final.

### Choix de refonte

- Les exercices HTML/CSS existants sont conservés.
- Les supports contiennent des procédures concrètes, erreurs fréquentes, solutions de dépannage, mini-entraînements et checklists.
- Source de génération ajoutée : `FormaPro/13_Assets_optionnels/refonte_supports_autonomie.py`.
- Enrichissement Word depuis `C:\\Users\\jboul\\OneDrive\\professionnel\\Formations\\office\\Word\\support.md` : interface, sauvegarde, raccourcis, styles, table des matières, QuickParts, numérotation, CV/candidature.
"""
    report.write_text(text, encoding="utf-8")

    qa = ROOT / "QA_CHECKLIST.md"
    qa_text = qa.read_text(encoding="utf-8") if qa.exists() else "# QA_CHECKLIST.md\n"
    if "## Refonte supports autonomes" not in qa_text:
        qa_text += """

## Refonte supports autonomes

- Supports Word, Excel, PowerPoint : refondus.
- Exercices existants : conservés.
- Liens internes : à vérifier après refonte.
"""
    qa.write_text(qa_text, encoding="utf-8")


def main():
    word_support()
    excel_support()
    powerpoint_support()
    update_reports()
    print("Supports Word/Excel/PowerPoint refondus")


if __name__ == "__main__":
    main()
