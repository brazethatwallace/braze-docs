---
nav_title: Rapports par Segment
article_title: Rapports par Segment dans le générateur de rapports
permalink: /segment_reporting_report_builder/
description: "Cet article de référence traite de l'utilisation des Segments comme dimension de rapport dans le générateur de rapports, y compris comment créer des rapports sur les Segments, ventiler par Segment et quelles combinaisons sont prises en charge."
hidden: true
noindex: true
page_type: reference
---

# Rapports par Segment dans le générateur de rapports {#segment-reporting-in-report-builder}

> Cet article explique comment utiliser les Segments comme dimension de rapport dans le générateur de rapports, y compris comment créer des rapports sur les Segments, ventiler par Segment et quelles combinaisons sont prises en charge.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Segment reporting' contact='customer success manager' %}

Le générateur de rapports prend en charge les **Segments** dans les lignes et comme option de ventilation, afin que vous puissiez voir les performances de vos Segments et ventiler les performances des Campaigns ou des Canvas par appartenance à un Segment. Si **Segments** n'apparaît pas dans vos menus déroulants **Rows** ou **Drilldown**, cette fonctionnalité n'a pas été activée pour votre compte.

Vous pouvez répondre à des questions telles que :

- Comment un Segment spécifique performe-t-il au fil du temps ?
- Quelles Campaigns et quels Canvas ciblent un Segment donné, et comment chacun a-t-il performé ?
- Comment l'engagement se compare-t-il entre les Segments pour une seule Campaign ou un seul Canvas ?

{% alert note %}
Les rapports par Segment sont disponibles uniquement pour les Segments avec le [suivi analytique]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) activé. Pour sélectionner **Segments** dans le menu déroulant **Rows**, vous devez disposer de la [permission « View Dashboard Reports » au niveau de l'espace de travail]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).
{% endalert %}

## Créer des rapports sur les Segments {#report-on-segments}

Pour créer des rapports directement sur les Segments :

1. Accédez à **Analytics** > **Report Builder (New)**.
2. Cliquez sur **Create New Report**.
3. Dans le menu déroulant **Rows**, sélectionnez **Segments**.
4. (Facultatif) Sélectionnez **Add drilldown** pour ventiler davantage les données du Segment :
   - **Campaigns and Canvases :** voir quelles Campaigns et quels Canvas ciblent le Segment, et comment chacun a performé.
   - **Date :** voir comment la taille ou les performances d'un Segment évoluent au fil du temps. Associez avec un graphique en courbes pour visualiser la tendance.
5. Dans **Report content**, ouvrez le menu déroulant **Segments** et sélectionnez les Segments à ajouter à votre rapport.
6. Sélectionnez les indicateurs dans **Columns** > **Customize Metrics**, puis définissez votre plage de dates dans **Report content**.
7. Si vous avez ajouté une ventilation **Campaigns and Canvases**, ajoutez les Campaigns et Canvas à inclure dans le rapport.
8. Cliquez sur **Save and run**.

Pour le flux de travail complet du générateur de rapports, consultez [Créer un rapport]({{site.baseurl}}/user_guide/analytics/reports/report_builder#creating-a-report).

## Ventiler par Segment {#drill-down-by-segment}

Pour ventiler les rapports de Campaigns, Canvas ou canaux par Segment :

1. Dans le menu déroulant **Rows**, sélectionnez **Campaigns**, **Canvases** ou **Campaigns and Canvases**.
2. Sélectionnez **Add drilldown**, puis choisissez **Segment**.
3. Dans **Report content**, ouvrez le menu déroulant **Segments** et sélectionnez les Segments à ajouter à votre rapport.
4. Sélectionnez les indicateurs dans **Columns** > **Customize Metrics**, puis définissez votre plage de dates dans **Report content**.
5. Ajoutez les Campaigns ou Canvas à inclure dans le rapport.
6. Cliquez sur **Save and run** pour voir les performances ventilées par chaque Segment ciblé par vos Campaigns ou Canvas.

Cette approche est particulièrement utile pour les espaces de travail qui envoient la même Campaign ou le même Canvas à plusieurs Segments. Vous pouvez voir comment chaque Segment a répondu sans avoir à croiser manuellement l'appartenance au Segment et les performances de la Campaign.

## Combinaisons prises en charge {#supported-combinations}

Les combinaisons de **Rows** et **Drilldown** suivantes sont prises en charge pour les rapports par Segment :

| Rows | Drilldown |
| ----- | ----- |
| Segment | Campaigns and Canvases |
| Segment | Date |
| Campaign | Segment |
| Campaign | Variante |
| Canvas | Segment |
| Campaigns and Canvases | Segment |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Combinaisons de lignes et de ventilations prises en charge"}

{% alert note %}
Le générateur de rapports prend en charge une seule ventilation à la fois. Si vous sélectionnez **Campaigns** dans le menu déroulant **Rows**, vous pouvez ventiler par **Variant** ou **Segment**, mais pas les deux dans le même rapport.
{% endalert %}

## Disponibilité des indicateurs {#metrics-availability}

Tous les indicateurs du générateur de rapports ne sont pas disponibles lorsque vous créez des rapports sur les Segments. Les indicateurs que vous pouvez sélectionner dépendent également du fait que **Segments** se trouve dans **Rows** ou **Drilldown**, et que le rapport inclut ou non une dimension Campaign ou Canvas.

| Indicateur | Disponibilité |
| ----- | ----- |
| Indicateurs de canal et de messagerie générale | Disponibles pour les combinaisons de lignes et de ventilations prises en charge. |
| Nombre de conversions (Conversions A–D) et noms d'événements de conversion | Disponibles lorsque les dimensions Segment et Campaign ou Canvas apparaissent ensemble. Utilisez **Segments** dans les lignes avec une ventilation **Campaigns and Canvases** ; ou utilisez **Campaigns**, **Canvases** ou **Campaigns and Canvases** dans les lignes avec une ventilation **Segment**. |
| Chiffre d'affaires et taux de conversion | Non disponibles pour les rapports dimensionnés par Segment. |
| Chiffre d'affaires et nombre d'achats par Segment | Disponibles uniquement lorsque **Segments** se trouve dans les lignes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Disponibilité des indicateurs pour les rapports par Segment"}

Pour en savoir plus sur l'impact de vos sélections de lignes et de ventilations sur les indicateurs, consultez [Disponibilité des indicateurs]({{site.baseurl}}/user_guide/analytics/reports/report_builder#metrics-availability) dans le générateur de rapports.