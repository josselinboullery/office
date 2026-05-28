import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, "..");
const outputDir = path.join(root, "06_Fichiers_de_depart", "Projet_fil_rouge");
const previewDir = path.join(process.env.TEMP || outputDir, "formapro_projet_fil_rouge_previews");

const participants = [
  [1, "Alice Martin", "alice.martin@example.local", "Demandeuse d'emploi", "Lille", "CV et candidature Word", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [2, "Karim Benali", "karim.benali@example.local", "Salarié en reconversion", "Roubaix", "Budget Excel", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [3, "Sophie Laurent", "sophie.laurent@example.local", "Assistante RH", "Tourcoing", "Présentation PowerPoint", "Oui", "Non", "Arrive à 14h30", "Formulaire inscription interne"],
  [4, "Thomas Petit", "thomas.petit@example.local", "Commercial junior", "Lille", "Budget Excel", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [5, "Nadia Diallo", "nadia.diallo@example.local", "Demandeuse d'emploi", "Villeneuve-d'Ascq", "CV et candidature Word", "À confirmer", "Oui", "Relance prévue le 25/06", "Formulaire inscription interne"],
  [6, "Hugo Moreau", "hugo.moreau@example.local", "Agent logistique", "Seclin", "Budget Excel", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [7, "Léa Nguyen", "lea.nguyen@example.local", "Apprentie", "Lomme", "Présentation PowerPoint", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [8, "Samir Haddad", "samir.haddad@example.local", "Demandeur d'emploi", "Lille", "CV et candidature Word", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [9, "Camille Bernard", "camille.bernard@example.local", "Coordinatrice formation", "Lille", "Présentation PowerPoint", "Oui", "Non", "Organisatrice", "Service formation"],
  [10, "Julien Robert", "julien.robert@example.local", "Technicien", "La Madeleine", "Budget Excel", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [11, "Inès Garcia", "ines.garcia@example.local", "Assistante administrative", "Marcq-en-Baroeul", "CV et candidature Word", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [12, "Mehdi Leroy", "mehdi.leroy@example.local", "Responsable équipe", "Wattrelos", "Budget Excel", "À confirmer", "Non", "A rappeler", "Formulaire inscription interne"],
  [13, "Clara Morel", "clara.morel@example.local", "Demandeuse d'emploi", "Lille", "CV et candidature Word", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [14, "Lucas Dubois", "lucas.dubois@example.local", "Alternant", "Croix", "Présentation PowerPoint", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [15, "Amina Traoré", "amina.traore@example.local", "Agent d'accueil", "Roubaix", "CV et candidature Word", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [16, "Élodie Simon", "elodie.simon@example.local", "Chargée de planning", "Lille", "Budget Excel", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [17, "Yanis Fontaine", "yanis.fontaine@example.local", "Magasinier", "Haubourdin", "Budget Excel", "Non", "Non", "Indisponible", "Formulaire inscription interne"],
  [18, "Marion Lefèvre", "marion.lefevre@example.local", "Assistante commerciale", "Lille", "Présentation PowerPoint", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [19, "Paul Richard", "paul.richard@example.local", "Demandeur d'emploi", "Loos", "CV et candidature Word", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [20, "Sarah Mercier", "sarah.mercier@example.local", "Responsable accueil", "Lille", "Présentation PowerPoint", "Oui", "Non", "Anime l'accueil", "Service formation"],
  [21, "Baptiste Roux", "baptiste.roux@example.local", "Technicien support", "Wasquehal", "Budget Excel", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [22, "Fatou Ndiaye", "fatou.ndiaye@example.local", "Demandeuse d'emploi", "Roubaix", "CV et candidature Word", "À confirmer", "Oui", "Besoin police grande taille", "Formulaire inscription interne"],
  [23, "Romain Girard", "romain.girard@example.local", "Assistant polyvalent", "Lille", "Budget Excel", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
  [24, "Chloé Perrin", "chloe.perrin@example.local", "Apprentie RH", "Tourcoing", "Présentation PowerPoint", "Oui", "Oui", "Aucun", "Formulaire inscription interne"],
];

const budgetRows = [
  [1, "Location salle polyvalente Jean-Moulin", "Lieu", 1, 320.00, "Devis mairie reçu", "Confirmé"],
  [2, "Collations individuelles", "Accueil", 32, 4.50, "Traiteur local", "Confirmé"],
  [3, "Café, thé, eau", "Accueil", 1, 65.00, "Forfait boissons", "Confirmé"],
  [4, "Badges nominatifs", "Signalétique", 35, 0.65, "Fournisseur bureau", "À commander"],
  [5, "Impression programmes A4", "Impression", 45, 0.28, "Copieur interne", "Confirmé"],
  [6, "Affiches A3", "Communication", 10, 2.10, "Imprimeur local", "À valider"],
  [7, "Fournitures atelier", "Ateliers", 1, 85.00, "Papeterie", "Confirmé"],
  [8, "Défraiement intervenants", "Intervenants", 3, 90.00, "Forfait transport", "Confirmé"],
  [9, "Transport matériel", "Logistique", 1, 45.00, "Véhicule utilitaire", "À valider"],
  [10, "Kit papier participant", "Impression", 24, 1.80, "Dossier stagiaire", "Confirmé"],
];

const atelierSummary = [
  ["CV et candidature Word", 7],
  ["Budget Excel", 8],
  ["Présentation PowerPoint", 6],
  ["À confirmer / indisponible", 3],
];

const planningRows = [
  ["13:30", "Installation salle", "Camille Bernard + formateurs", "Brancher vidéoprojecteur, préparer badges, tester fichiers"],
  ["14:00", "Accueil participants", "Sarah Mercier", "Pointage, badges, programme papier"],
  ["14:15", "Ouverture", "Camille Bernard", "Objectif de l'après-midi et règles pratiques"],
  ["14:35", "Atelier 1 : CV et courrier", "Julie Garnier", "Démonstration Word simple"],
  ["15:20", "Pause", "Tous", "Collation et questions"],
  ["15:35", "Atelier 2 : budget événement", "Olivier Petit", "Tableau Excel, formule SOMME, graphique"],
  ["16:20", "Témoignage métier", "Manon Carpentier", "Parcours après formation"],
  ["16:40", "Questions recrutement", "Rachid Morel", "Attentes employeur et compétences bureautiques"],
  ["16:55", "Clôture", "Camille Bernard", "Prochaines étapes et inscription accompagnement"],
];

function usedRange(rows, startColumn = "A") {
  const colCount = rows[0].length;
  const endCode = startColumn.charCodeAt(0) + colCount - 1;
  return `${startColumn}1:${String.fromCharCode(endCode)}${rows.length}`;
}

function styleHeader(sheet, address) {
  sheet.getRange(address).format = {
    fill: "#334155",
    font: { bold: true, color: "#FFFFFF" },
    wrapText: true,
  };
}

function setWidths(sheet, specs) {
  for (const [col, width] of specs) {
    sheet.getRange(`${col}1:${col}80`).format.columnWidthPx = width;
  }
}

async function renderSheets(workbook, workbookName, sheetNames) {
  await fs.mkdir(previewDir, { recursive: true });
  for (const sheetName of sheetNames) {
    const preview = await workbook.render({ sheetName, autoCrop: "all", scale: 1, format: "png" });
    await fs.writeFile(path.join(previewDir, `${workbookName}_${sheetName}.png`), new Uint8Array(await preview.arrayBuffer()));
  }
}

async function exportWorkbook(workbook, filename) {
  const errors = await workbook.inspect({
    kind: "match",
    searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
    options: { useRegex: true, maxResults: 100 },
    summary: "final formula error scan",
  });
  console.log(`${filename} formula scan`);
  console.log(errors.ndjson);
  const xlsx = await SpreadsheetFile.exportXlsx(workbook);
  await xlsx.save(path.join(outputDir, filename));
}

async function buildParticipants() {
  const workbook = Workbook.create();
  const sheet = workbook.worksheets.add("Participants");
  sheet.showGridLines = false;
  const headers = [["ID", "Nom", "Email", "Statut", "Ville", "Atelier prioritaire", "Présence confirmée", "Collation", "Besoin particulier", "Source"]];
  const rows = headers.concat(participants);
  sheet.getRange(usedRange(rows)).values = rows;
  styleHeader(sheet, "A1:J1");
  sheet.freezePanes.freezeRows(1);
  setWidths(sheet, [["A", 48], ["B", 150], ["C", 230], ["D", 160], ["E", 120], ["F", 190], ["G", 145], ["H", 95], ["I", 220], ["J", 190]]);
  sheet.getRange("A2:J25").format = { wrapText: true };
  sheet.tables.add("A1:J25", true, "ParticipantsForum");

  const synth = workbook.worksheets.add("Synthese");
  synth.showGridLines = false;
  synth.getRange("A1:D1").values = [["Indicateur", "Valeur", "Méthode", "Source"]];
  synth.getRange("A2:D7").values = [
    ["Participants inscrits", "", "Nombre total de lignes participants", "Participants!A2:A25"],
    ["Présences confirmées", "", "Nombre de Oui dans la colonne Présence confirmée", "Participants!G2:G25"],
    ["À confirmer", "", "Nombre de À confirmer dans la colonne Présence confirmée", "Participants!G2:G25"],
    ["Absents annoncés", "", "Nombre de Non dans la colonne Présence confirmée", "Participants!G2:G25"],
    ["Collations à prévoir", "", "Nombre de Oui dans la colonne Collation", "Participants!H2:H25"],
    ["Participants avec besoin particulier", "", "Cellules différentes de Aucun", "Participants!I2:I25"],
  ];
  synth.getRange("B2").formulas = [["=COUNTA(Participants!B2:B25)"]];
  synth.getRange("B3").formulas = [["=COUNTIF(Participants!G2:G25,\"Oui\")"]];
  synth.getRange("B4").formulas = [["=COUNTIF(Participants!G2:G25,\"À confirmer\")"]];
  synth.getRange("B5").formulas = [["=COUNTIF(Participants!G2:G25,\"Non\")"]];
  synth.getRange("B6").formulas = [["=COUNTIF(Participants!H2:H25,\"Oui\")"]];
  synth.getRange("B7").formulas = [["=COUNTIFS(Participants!I2:I25,\"<>Aucun\",Participants!I2:I25,\"<>\")"]];
  styleHeader(synth, "A1:D1");
  setWidths(synth, [["A", 210], ["B", 90], ["C", 330], ["D", 210]]);

  const atelier = workbook.worksheets.add("Ateliers");
  atelier.showGridLines = false;
  const atelierRows = [["Atelier", "Participants prévus"], ...atelierSummary];
  atelier.getRange(usedRange(atelierRows)).values = atelierRows;
  styleHeader(atelier, "A1:B1");
  setWidths(atelier, [["A", 230], ["B", 150]]);
  const chart = atelier.charts.add("bar", atelier.getRange("A1:B5"));
  chart.title = "Participants par atelier";
  chart.hasLegend = false;
  chart.setPosition("D2", "J18");
  await renderSheets(workbook, "participants_forum_metiers", ["Participants", "Synthese", "Ateliers"]);
  await exportWorkbook(workbook, "participants_forum_metiers.xlsx");
}

async function buildBudget() {
  const workbook = Workbook.create();
  const budget = workbook.worksheets.add("Budget");
  budget.showGridLines = false;
  const rows = [["Ligne", "Poste", "Catégorie", "Quantité", "Prix unitaire HT", "Total HT", "Source / devis", "Statut"]].concat(budgetRows.map(row => [...row.slice(0, 5), null, row[5], row[6]]));
  budget.getRange(usedRange(rows)).values = rows;
  budget.getRange("F2").formulas = [["=D2*E2"]];
  budget.getRange("F2:F11").fillDown();
  styleHeader(budget, "A1:H1");
  budget.freezePanes.freezeRows(1);
  budget.getRange("E2:F12").format.numberFormat = "# ##0.00 €";
  budget.getRange("D2:D12").format.numberFormat = "0";
  setWidths(budget, [["A", 58], ["B", 260], ["C", 125], ["D", 90], ["E", 125], ["F", 115], ["G", 185], ["H", 115]]);
  budget.tables.add("A1:H11", true, "BudgetForum");

  const synth = workbook.worksheets.add("Synthese");
  synth.showGridLines = false;
  synth.getRange("A1:B4").values = [
    ["Budget maximum autorisé", 1200],
    ["Total prévu", null],
    ["Reste disponible", null],
    ["Taux d'utilisation", null],
  ];
  synth.getRange("B2").formulas = [["=SUM(Budget!F2:F11)"]];
  synth.getRange("B3").formulas = [["=B1-B2"]];
  synth.getRange("B4").formulas = [["=B2/B1"]];
  synth.getRange("A1:A4").format = { fill: "#E2E8F0", font: { bold: true } };
  synth.getRange("B1:B3").format.numberFormat = "# ##0.00 €";
  synth.getRange("B4").format.numberFormat = "0.0%";
  synth.getRange("A6:B6").values = [["Catégorie", "Total HT"]];
  const categories = ["Lieu", "Accueil", "Signalétique", "Impression", "Communication", "Ateliers", "Intervenants", "Logistique"];
  synth.getRange("A7:A14").values = categories.map(c => [c]);
  synth.getRange("B7").formulas = [["=SUMIF(Budget!C2:C11,A7,Budget!F2:F11)"]];
  synth.getRange("B7:B14").fillDown();
  synth.getRange("B7:B14").format.numberFormat = "# ##0.00 €";
  styleHeader(synth, "A6:B6");
  setWidths(synth, [["A", 180], ["B", 120]]);
  const chart = synth.charts.add("bar", synth.getRange("A6:B14"));
  chart.title = "Budget par catégorie";
  chart.hasLegend = false;
  chart.yAxis = { numberFormatCode: "# ##0 €" };
  chart.setPosition("D2", "K20");
  await renderSheets(workbook, "budget_forum_metiers", ["Budget", "Synthese"]);
  await exportWorkbook(workbook, "budget_forum_metiers.xlsx");
}

async function buildRestitution() {
  const workbook = Workbook.create();
  const synth = workbook.worksheets.add("Restitution");
  synth.showGridLines = false;
  synth.getRange("A1:D1").values = [["Indicateur", "Valeur", "Commentaire", "Source"]];
  synth.getRange("A2:D9").values = [
    ["Participants inscrits", 24, "Liste d'inscription complète", "participants_forum_metiers.xlsx"],
    ["Présences confirmées", 20, "Oui dans la liste participants", "participants_forum_metiers.xlsx"],
    ["À relancer", 3, "À confirmer", "participants_forum_metiers.xlsx"],
    ["Absent annoncé", 1, "Non", "participants_forum_metiers.xlsx"],
    ["Budget maximum", 1200, "Plafond imposé", "budget_forum_metiers.xlsx"],
    ["Budget prévu", 1028.55, "Somme des lignes", "budget_forum_metiers.xlsx"],
    ["Reste disponible", 171.45, "Budget maximum - total prévu", "budget_forum_metiers.xlsx"],
    ["Satisfaction cible", 0.85, "Objectif organisateur", "brief_intervenants_forum_metiers.txt"],
  ];
  styleHeader(synth, "A1:D1");
  synth.getRange("B6:B8").format.numberFormat = "# ##0.00 €";
  synth.getRange("B9").format.numberFormat = "0%";
  setWidths(synth, [["A", 190], ["B", 115], ["C", 250], ["D", 235]]);

  const planning = workbook.worksheets.add("Programme");
  planning.showGridLines = false;
  const planningTable = [["Heure", "Séquence", "Responsable", "Détail"]].concat(planningRows);
  planning.getRange(usedRange(planningTable)).values = planningTable;
  styleHeader(planning, "A1:D1");
  setWidths(planning, [["A", 80], ["B", 220], ["C", 210], ["D", 360]]);
  planning.getRange("A2:D10").format = { wrapText: true };
  planning.tables.add("A1:D10", true, "ProgrammeForum");

  const ateliers = workbook.worksheets.add("Graphique ateliers");
  ateliers.showGridLines = false;
  const atelierRows = [["Atelier", "Participants"], ...atelierSummary];
  ateliers.getRange(usedRange(atelierRows)).values = atelierRows;
  styleHeader(ateliers, "A1:B1");
  setWidths(ateliers, [["A", 240], ["B", 120]]);
  const chart = ateliers.charts.add("bar", ateliers.getRange("A1:B5"));
  chart.title = "Répartition des participants";
  chart.hasLegend = false;
  chart.setPosition("D2", "J18");
  await renderSheets(workbook, "donnees_restitution_forum_metiers", ["Restitution", "Programme", "Graphique ateliers"]);
  await exportWorkbook(workbook, "donnees_restitution_forum_metiers.xlsx");
}

await fs.mkdir(outputDir, { recursive: true });
await buildParticipants();
await buildBudget();
await buildRestitution();
console.log(`Sources XLSX créées dans ${outputDir}`);
