---
nav_title: Rapport d'événements personnalisés
article_title: Rapport d'événements personnalisés
page_order: 6
page_type: reference
description: "Cette page décrit comment utiliser le rapport d'événements personnalisés pour visualiser les occurrences d'événements personnalisés au fil du temps, ventilées par segment."
tool: Reports
---

# Rapport d'événements personnalisés {#custom-events-report}

> Le rapport d'événements personnalisés vous permet de visualiser les occurrences d'un ou plusieurs événements personnalisés au fil du temps. Vous pouvez ventiler les résultats par segment, appliquer des formules d'indicateurs clés de performance et exporter les données pour une analyse approfondie.

## Consulter un rapport {#viewing-a-report}

Pour consulter ce rapport depuis le tableau de bord, accédez à **Analytics** > **Custom events report**. Sélectionnez les événements personnalisés que vous souhaitez analyser, puis sélectionnez **Apply** pour générer le graphique.

![Événements personnalisés]({% image_buster /assets/img_archive/Export_events.png %})

## Configurer votre rapport {#configuring-your-report}

Utilisez les options suivantes pour personnaliser les données affichées dans le graphique **Performance Over Time**.

| Option | Description |
| --- | --- |
| **Apps** | Par défaut, le rapport inclut les données de toutes les applications. Utilisez ce menu déroulant pour restreindre le rapport à une application spécifique. |
| **Breakdown custom events by** | Contrôle la façon dont la série temporelle de l'événement personnalisé sélectionné est regroupée. Par défaut, le graphique affiche la tendance agrégée globale par date. Passez à **Custom Events by Hour** pour voir les tendances intrajournalières, ou à **Custom Events per MAU** pour normaliser le volume d'événements par rapport à votre nombre de MAU. |
| **Filter by Segments** | Activez cette option pour ventiler le nombre d'événements par un ou plusieurs segments. Lorsqu'elle est activée, sélectionnez les segments que vous souhaitez comparer. Le graphique affiche le nombre d'utilisateurs dans chaque segment ayant effectué l'événement personnalisé. |
| **KPI formula** | Remplace le nombre brut d'événements par un indicateur calculé à partir d'un numérateur (tel qu'un nombre d'événements personnalisés) et d'un dénominateur (tel que le nombre d'utilisateurs actifs quotidiens, de MAU ou la taille d'un segment activé pour l'analytique). Lorsque vous sélectionnez une ou plusieurs formules, le graphique trace la valeur de chaque formule sur la période sélectionnée afin de comparer les performances normalisées (par exemple, « événements par utilisateur actif ») plutôt que le volume total d'événements. Si aucune donnée n'est disponible pour la période et les formules sélectionnées, Braze affiche un message « no data » — élargissez la période ou choisissez d'autres formules. Sélectionnez **Manage KPI formulas** pour créer ou modifier des formules. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Exporter les données {#exporting-data}

Pour exporter vos données d'événements personnalisés, sélectionnez <i class="fas fa-bars" title="Menu contextuel du graphique"></i> dans le graphique **Performance Over Time** et sélectionnez votre option d'exportation.

{% alert tip %}
Pour obtenir de l'aide concernant les exportations CSV et API, consultez [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).
{% endalert %}