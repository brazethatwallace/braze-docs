---
nav_title: Générateur de rapports (ancien)
article_title: Générateur de rapports (ancien)
alias: /report_builder_legacy/
page_order: 1
page_type: reference
description: "Cette page explique comment exécuter un rapport à l'aide de l'ancien générateur de rapports, y compris la création de rapports de comparaison de campagnes et de Canvas, ainsi que la création de rapports et de graphiques."
tool:
  - Reports

---

# Générateur de rapports (ancien) {#report-builder-legacy}

> Le générateur de rapports vous permet de comparer les résultats de plusieurs campagnes ou Canvas dans une seule vue, afin de déterminer facilement quelles stratégies d'engagement ont le plus impacté vos indicateurs clés. Pour les campagnes comme pour les Canvas, vous pouvez exporter vos données et enregistrer votre rapport pour le consulter ultérieurement.<br><br>Pour une liste descriptive des indicateurs que vous trouverez dans vos rapports, consultez le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

![Exemple de comparaison de campagnes]({% image_buster /assets/img/campaign_comparison/campaign_main.png %}){: style="max-width:80%;"}

Utilisez ce rapport pour répondre à des questions clés sur l'engagement, par exemple :

- Quelles ont été les campagnes ou les Canvas les plus performants pour une étiquette ou un canal spécifique ?
- Quelles variantes des campagnes multivariantes ont eu le plus d'impact par rapport au groupe de contrôle ?
- Quelle campagne promotionnelle saisonnière a généré un taux d'achat plus élevé : les soldes d'été, d'automne ou d'hiver ?
- Quelles notifications push dans ce Canvas ont eu les meilleurs taux d'ouverture ?
- Quelles étapes de ce groupe de Canvas ont généré le plus de conversions ?
- La version 1 d'un e-mail de bienvenue ou la version 2 a-t-elle conduit à un meilleur engagement et une meilleure conversion ? Les modifications ont-elles fonctionné ?
- Comment les différentes méthodes de distribution (par exemple, 3 notifications push planifiées, 3 notifications push déclenchées par action et 3 notifications push déclenchées par API) impactent-elles vos taux d'ouverture, taux de conversion ou taux d'achat ?
- Les améliorations continues apportées aux messages destinés aux utilisateurs inactifs ont-elles eu un impact positif sur vos indicateurs clés de performance au fil du temps ?

{% alert tip %}
Essayez d'utiliser les mêmes événements de conversion pour les conversions A, B, etc. dans les campagnes et les Canvas que vous souhaitez comparer, afin de pouvoir aligner ces conversions dans vos rapports du générateur de rapports.
{% endalert %}

## Exécuter un rapport {#running-a-report}

### Étape 1 : Créer un nouveau rapport {#step-1-create-a-new-report}

Dans le tableau de bord, accédez à **Analytics** > **Générateur de rapports**.

Sélectionnez **Créer un nouveau rapport** et choisissez un rapport de comparaison de campagnes ou un rapport de comparaison de Canvas.

Si vous choisissez d'exécuter un rapport sur les campagnes, vous pouvez sélectionner un rapport **Manuel** ou **Automatisé**. Les rapports peuvent contenir soit des campagnes, soit des Canvas, mais pas les deux ensemble. Toutes les campagnes et tous les Canvas dont les derniers messages ont été envoyés au cours des 12 derniers mois seront éligibles pour un rapport.

![Tableau de bord des campagnes]({% image_buster /assets/img/campaign_comparison/create_report.png %}){: style="max-width:80%;"}

Voici les différences entre ces deux options :

| **Action** | **Manuel** | **Automatisé** |
| ---- | ---------- | ------------- |
| **Création du rapport** | Vous pourrez affiner votre liste de campagnes à l'aide de filtres, puis cocher des campagnes spécifiques. | Vous créerez votre rapport en utilisant les options de filtre pour affiner votre liste de campagnes. |
| **Enregistrement et consultation du rapport** | Vous pouvez enregistrer votre rapport. La prochaine fois que vous le consulterez, vous pourrez voir les mêmes campagnes que vous aviez précédemment ajoutées, car elles correspondent toujours à votre filtre « Dernier envoi ». | Vous pouvez enregistrer votre rapport. La prochaine fois que vous le consulterez, le rapport se mettra automatiquement à jour pour inclure toutes les campagnes correspondant actuellement à vos filtres. |
| **Modification du rapport** | Vous pouvez sélectionner **Modifier le rapport** pour ajouter ou supprimer des campagnes de votre rapport. | Vous pouvez modifier votre rapport en ajustant vos critères de filtre. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 1 : Créer un nouveau rapport" }

{% alert note %}
Les rapports **Manuels** et **Automatisés** peuvent inclure un maximum de 250 campagnes par rapport.
{% endalert %}

Les rapports Canvas fonctionnent de manière similaire à un rapport manuel de campagnes, en ce sens que les sélections de Canvas et les mises à jour du rapport doivent également être effectuées manuellement. Vous pouvez inclure au maximum cinq Canvas dans un seul rapport.

### Étape 2 : Choisir vos indicateurs {#step-2-choose-your-metrics}

Après avoir créé votre rapport, vous trouverez un tableau vide contenant des campagnes sur chaque ligne. Le tableau se remplira après avoir sélectionné **Modifier les colonnes** et choisi les indicateurs que vous souhaitez ajouter.

![Options de campagnes]({% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}){: style="max-width:80%;"}

Votre tableau se remplira avec les indicateurs que vous avez choisis. Pour les définitions de ces indicateurs, consultez le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary). Certains indicateurs ne sont disponibles que pour les rapports de comparaison de campagnes.

Vous pouvez également basculer les calculs pour la **Moyenne** de tout taux ou indicateur numérique et le **Total** pour tout indicateur numérique.

### Étape 3 : Choisir une période {#step-3-choose-a-time-period}

Vous pouvez sélectionner une période spécifique pour consulter les données de votre rapport. Si une campagne, un Canvas, une variante de Canvas ou un composant de Canvas particulier ne dispose d'aucune donnée pour la période sélectionnée, les résultats de cette ligne seront vides.

![Indicateur numérique de campagne]({% image_buster /assets/img/campaign_comparison/metric.png %}){: style="max-width:60%;"}

### Étape 4 : Nommer et enregistrer votre rapport {#step-4-name-and-save-your-report}

Nommez votre rapport avant de l'enregistrer. Si un rapport est enregistré sans être nommé, Braze appliquera un nom par défaut : « Campaign Comparison Report ».

![Note de campagne]({% image_buster /assets/img/campaign_comparison/comparison_name.png %}){: style="max-width:60%;"}

Lorsque vous êtes prêt, sélectionnez **Enregistrer**. Les rapports enregistrés peuvent être consultés ultérieurement sur la page du **Générateur de rapports**.

## Rapport de comparaison de campagnes avec des campagnes multivariantes {#campaign-comparison-report-with-multivariate-campaigns}

Pour toute campagne multivariante, vous pouvez consulter ces indicateurs ventilés par variantes et groupe de contrôle en cliquant sur la flèche à côté du nom de la campagne. Les lignes contenant vos variantes incluront les résultats de performance pour cette variante, et la ligne contenant votre groupe de contrôle n'inclura que les résultats de vos événements de conversion.

![Note de campagne]({% image_buster /assets/img/campaign_comparison/compare_note.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Les indicateurs remplissant la ligne de votre campagne globale refléteront la performance de ses variantes, mais n'incluront pas la performance du groupe de contrôle. Par exemple, l'événement de conversion principal A pour votre campagne globale sera la somme de l'événement de conversion principal A pour vos variantes, et n'inclura pas l'événement de conversion principal A pour votre groupe de contrôle.

{% alert important %}
Si vous supprimez une variante d'une campagne multivariante, les données de cette variante ne seront pas disponibles pour une utilisation dans un futur rapport.
{% endalert %}

## Ventilation du rapport de comparaison de Canvas {#canvas-comparison-report-breakdown}

Dans un rapport Canvas, vous pouvez consulter vos Canvas ventilés par variante, étapes ou message.

### Variante {#variant}

Sélectionner **ventilation par variante** vous permet de consulter les statistiques de haut niveau pour l'ensemble de vos Canvas, ainsi que les statistiques pour chaque variante, qui peuvent être développées en sélectionnant la flèche à côté du nom du Canvas.

![Variantes]({% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}){: style="max-width:90%;"}

### Étapes {#steps}

Sélectionner **ventilation par étapes** vous permet de consulter les indicateurs au niveau des étapes, chaque ligne du rapport contenant les données d'une étape.

![Étapes]({% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}){: style="max-width:90%;"}

### Message {#message}

De manière similaire à une ventilation au niveau des étapes, sélectionner **ventilation par message** affiche le nom des étapes dans chaque ligne. Cependant, dans **Modifier les colonnes**, vous aurez accès aux indicateurs au niveau du message, tels que les statistiques spécifiques au canal comme les clics d'e-mail et les ouvertures de notifications push.

![Rapport]({% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}){: style="max-width:90%;"}

Notez que dans le tableau de bord de Braze, vous pouvez prévisualiser les 50 premières lignes de votre rapport Canvas. Vous pouvez accéder au rapport complet lorsque vous exportez un CSV.

## Accéder aux rapports enregistrés {#accessing-saved-reports}

Lorsque vous accédez à un **rapport manuel** enregistré, vous pouvez consulter les mêmes campagnes que vous aviez précédemment ajoutées, car elles correspondent toujours à votre filtre « Dernier envoi ».

Lorsque vous accédez à un **rapport automatisé** enregistré, le rapport se mettra automatiquement à jour pour inclure toutes les campagnes correspondant actuellement à vos filtres. Par exemple, si votre rapport filtrait les campagnes avec l'étiquette « Promotion », alors chaque fois que vous consulterez ce rapport, vous pourrez voir toutes les campagnes avec l'étiquette « Promotion », même si ces campagnes ont été créées après la création de ce rapport.

## Modifier les rapports {#editing-reports}

Dans un **rapport manuel**, vous pouvez modifier un rapport en sélectionnant **Modifier**. À partir de là, vous pouvez sélectionner ou désélectionner les campagnes à inclure dans votre rapport.

Dans un **rapport automatisé**, basculez vos filtres pour affiner les résultats de votre rapport.

## Exporter les rapports {#exporting-reports}

Vous pouvez également sélectionner **Exporter** pour télécharger votre rapport au format CSV.

Si votre rapport contient des campagnes multivariantes, votre export inclura deux fichiers CSV :

- Un fichier contenant uniquement les indicateurs de haut niveau pour chaque campagne
- Un fichier contenant les indicateurs au niveau des variantes

Le fichier contenant les indicateurs des variantes aura `variant_` ajouté au début de son nom. La première fois que vous exportez un rapport automatisé, vous recevrez une fenêtre contextuelle vous demandant d'autoriser le téléchargement de plusieurs fichiers — cliquez sur **Autoriser**.

![Téléchargement de campagne]({% image_buster /assets/img/campaign_comparison/download.png %}){: style="max-width:60%;"}

### Exporter les rapports de comparaison de Canvas {#exporting-canvas-comparison-reports}

Votre export CSV reflétera la vue de ventilation sur laquelle vous vous trouviez lorsque vous avez sélectionné **Exporter**. Par exemple, si vous étiez sur la vue de ventilation au niveau des étapes, votre export contiendra les données sur les indicateurs de vos étapes. Pour exporter les données d'une ventilation différente, vous devrez d'abord naviguer vers cette ventilation, puis sélectionner **Exporter** à partir de là.

Si vous téléchargez un rapport Canvas ventilé par variante, vous recevrez deux fichiers CSV :

- Un fichier contenant uniquement les indicateurs de haut niveau pour chaque Canvas
- Un fichier contenant les indicateurs au niveau des variantes

## Créer des graphiques {#building-charts}

Utilisez les graphiques pour visualiser un indicateur sélectionné dans votre rapport. Les graphiques sont disponibles pour les rapports qui comportent des campagnes et qui ont au moins un indicateur ajouté à leurs colonnes.

![Graphique de performance de campagne avec l'indicateur Messages envoyés sélectionné]({% image_buster /assets/img/campaign_comparison/report_builder_charts.png %})

Par défaut, le graphique de chaque rapport affichera l'indicateur de la première colonne du rapport. Pour sélectionner un indicateur différent à représenter graphiquement, choisissez votre indicateur dans le menu déroulant. Tout indicateur de votre tableau de rapport sera disponible pour l'affichage dans votre graphique.

Vous pouvez représenter graphiquement au maximum trois indicateurs. Les unités de tous les indicateurs doivent être identiques — par exemple, si vous choisissez un taux dans le premier menu déroulant, seuls les taux seront disponibles à la sélection dans le deuxième menu déroulant.

Si votre graphique ne contient qu'un seul indicateur, il affichera jusqu'à 30 campagnes par ordre décroissant en fonction de l'indicateur sélectionné. Par exemple, si l'indicateur de votre graphique est les clics d'e-mail, alors votre graphique affichera les 30 campagnes d'e-mail avec le plus de clics, classées du plus grand au plus petit nombre de clics. Si votre rapport contient plus de 30 campagnes, seules les 30 premières seront affichées dans le graphique. Si vous sélectionnez plus d'un indicateur, votre graphique n'affichera que les cinq premières campagnes en fonction du premier indicateur sélectionné.

Les graphiques ne sont actuellement pas enregistrés lorsque vous enregistrez votre rapport.