---
nav_title: Rapport sur les revenus
article_title: Rapport sur les revenus
page_order: 7
page_type: reference
description: "Cette page décrit où trouver le rapport sur les revenus dans le tableau de bord de Braze et comment consulter les données de chiffre d'affaires sur des périodes spécifiques, le chiffre d'affaires d'un produit donné et le chiffre d'affaires total de votre application."
tool: Reports
---

# Rapport sur les revenus {#revenue-report}

> La page **Revenue Report** vous permet de consulter les données de chiffre d'affaires sur des périodes spécifiques, le chiffre d'affaires d'un produit donné et le chiffre d'affaires total de votre application.

Pour afficher votre rapport sur les revenus dans le tableau de bord de Braze, accédez à **Analytics** > **Reports** > **Revenue Report**.

## Personnalisation de votre rapport de revenus {#customizing-your-revenue-report}

Vous pouvez personnaliser votre rapport de revenus en sélectionnant une plage de dates, les applications sur lesquelles générer le rapport et les paramètres souhaités.

![La page « Rapport de revenus » affichant le graphique « Performance au fil du temps » avec « Revenus » défini comme paramètre.]({% image_buster /assets/img/revenue_report.png %})

### Filtrage par date et applications {#filtering-by-date-and-apps}

Sélectionnez la plage de dates pour votre rapport de revenus et, si vous le souhaitez, une application spécifique ou une sélection d'applications.

### Filtrage par paramètres {#filtering-by-parameters}

Le graphique **Performance Over Time** affiche les données pour différents paramètres, qui peuvent être sélectionnés dans le menu déroulant **Statistics for**. Vous pouvez également ventiler les données de certains paramètres dans le menu déroulant **Breakdown**.

Vous pouvez consulter les données suivantes dans le graphique **Performance Over Time** :
- Formules KPI
- Achats
    - (Facultatif) Achats par produit
- Chiffre d'affaires
    - (Facultatif) Chiffre d'affaires par Segment
    - (Facultatif) Chiffre d'affaires par produit
- Chiffre d'affaires par heure
    - (Facultatif) Chiffre d'affaires par heure par Segment
- Chiffre d'affaires par utilisateur

## Comprendre les calculs de chiffre d'affaires {#understanding-revenue-calculations}

{% alert note %}
Lorsque vous enregistrez un chiffre d'affaires dans une devise sans taux de change, Braze l'enregistre comme un achat de 0,00 $ US.
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Comprendre les calculs de chiffre d'affaires">
  <caption>Comprendre les calculs de chiffre d'affaires</caption>
    <thead>
        <tr>
            <th>Indicateur</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-revenue">Chiffre d'affaires à vie</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-value-per-user">Valeur à vie par utilisateur</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#average-daily-revenue">Chiffre d'affaires quotidien moyen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-purchases">Achats quotidiens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-revenue-per-user">Chiffre d'affaires quotidien par utilisateur</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

## Afficher la répartition par produit {#viewing-the-product-breakdown}

Consultez le tableau **Product Breakdown** pour obtenir la liste des produits achetés au cours de la période sélectionnée, le nombre d'achats pour chaque produit et le chiffre d'affaires généré par chaque produit.

![Le tableau « Product Breakdown » affichant les colonnes « Product Name », « Purchased » et « Revenue ».]({% image_buster /assets/img/revenue_report_product_breakdown.png %})

## Exportation des données de chiffre d'affaires {#exporting-revenue-data}

Pour exporter vos données de chiffre d'affaires, sélectionnez <i class="fas fa-bars" title="Menu contextuel du graphique"></i> **Menu contextuel du graphique** dans le graphique **Performance Over Time** et sélectionnez votre option d'exportation.

{% alert tip %}
Vous cherchez d'autres moyens d'obtenir des données de chiffre d'affaires ? Essayez d'ajouter le comportement d'achat (ainsi que l'achat d'un produit) aux Campaigns ou aux Canvas en tant qu'[événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events).
{% endalert %}

Vous pouvez également consulter les statistiques de chiffre d'affaires au cas par cas sur les pages [Analyse de Campaign]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) ou [Analyse de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

{% alert tip %}
Les rapports de chiffre d'affaires ne peuvent pas être exportés via l'API. Pour obtenir de l'aide sur les exportations CSV, consultez la [résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}