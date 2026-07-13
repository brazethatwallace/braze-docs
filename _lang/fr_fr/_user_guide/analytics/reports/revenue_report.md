---
nav_title: Rapport sur les revenus
article_title: Rapport sur les revenus
page_order: 7
page_type: reference
description: "Cette page décrit comment utiliser la page Rapport sur les revenus pour consulter les données de chiffre d'affaires sur des périodes spécifiques, le chiffre d'affaires d'un produit donné et le chiffre d'affaires total de votre application."
tool: Reports
---

# Rapport sur les revenus {#revenue-report}

> La page **Rapport sur les revenus** vous permet de consulter les données de chiffre d'affaires sur des périodes spécifiques, le chiffre d'affaires d'un produit donné et le chiffre d'affaires total de votre application.

Pour afficher un rapport sur votre chiffre d'affaires depuis le tableau de bord, accédez à **Analytics** > **Revenue Report**.

## Personnaliser votre rapport sur les revenus {#customizing-your-revenue-report}

Vous pouvez personnaliser votre rapport sur les revenus en sélectionnant une plage de dates, les applications sur lesquelles générer le rapport et des paramètres.

![La page « Revenue Report » affichant le graphique « Performance Over Time » avec « Revenue » défini comme paramètre.]({% image_buster /assets/img/revenue_report.png %})

### Filtrer par date et applications {#filtering-by-date-and-apps}

Sélectionnez la plage de dates pour votre rapport sur les revenus et, si vous le souhaitez, une application spécifique ou une sélection d'applications.

### Filtrer par paramètres {#filtering-by-parameters}

Le graphique **Performance Over Time** affiche les données pour différents paramètres, qui peuvent être sélectionnés dans le menu déroulant **Statistics for**. Vous pouvez éventuellement ventiler les données de certains paramètres dans le menu déroulant **Breakdown**.

Vous pouvez consulter les données suivantes dans le graphique **Performance Over Time** :
- Formules d'indicateurs clés de performance
- Achats
    - (Facultatif) Achats par produit
- Chiffre d'affaires
    - (Facultatif) Chiffre d'affaires par segment
    - (Facultatif) Chiffre d'affaires par produit
- Chiffre d'affaires par heure
    - (Facultatif) Chiffre d'affaires par heure par segment
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
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-value-per-user">Valeur vie client par utilisateur</a></td>
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

## Consulter la ventilation par produit {#viewing-the-product-breakdown}

Reportez-vous au tableau **Product Breakdown** pour obtenir la liste des produits achetés au cours de la période sélectionnée, le nombre d'achats de chaque produit et le chiffre d'affaires généré par chaque produit.

![Le tableau « Product Breakdown » affichant les colonnes « Product Name », « Purchased » et « Revenue ».]({% image_buster /assets/img/revenue_report_product_breakdown.png %})

## Exporter les données de chiffre d'affaires {#exporting-revenue-data}

Pour exporter vos données de chiffre d'affaires, sélectionnez <i class="fas fa-bars" title="Menu contextuel du graphique"></i> **Menu contextuel du graphique** dans le graphique **Performance Over Time** et choisissez votre option d'exportation.

{% alert tip %}
Vous cherchez d'autres moyens d'obtenir des données de chiffre d'affaires ? Essayez d'ajouter un comportement d'achat (ainsi que l'achat d'un produit) aux campagnes ou aux Canvas en tant qu'[événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events).
{% endalert %}

Vous pouvez également consulter les statistiques de chiffre d'affaires au cas par cas sur les pages [Analyse de Campaign]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) ou [Analyse de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

{% alert tip %}
Les rapports sur les revenus ne peuvent pas être exportés via l'API. Pour obtenir de l'aide concernant les exportations CSV, consultez la [résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}