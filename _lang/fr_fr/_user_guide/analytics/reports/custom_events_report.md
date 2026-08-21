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

## Consulter un rapport {#view-a-report}

Pour consulter ce rapport depuis le tableau de bord, accédez à **Analytics** > **Custom Events Report**. Sélectionnez les événements personnalisés que vous souhaitez analyser. Le graphique s'affiche automatiquement après la sélection d'un événement.

![Événements personnalisés]({% image_buster /assets/img_archive/Export_events.png %})

### Événements personnalisés via l'API et filtres d'application {#api-custom-events-and-app-filters}

Les événements personnalisés envoyés via l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) peuvent éventuellement inclure un `app_id`. Contrairement aux événements enregistrés via le SDK, les événements envoyés par l'API ne sont pas automatiquement associés à une application. Sans `app_id`, les événements sont enregistrés mais n'apparaissent pas dans le graphique des événements personnalisés lorsqu'un filtre d'application est appliqué.

## Configurer votre rapport {#configure-your-report}

Utilisez les options suivantes pour personnaliser les données qui apparaissent dans le graphique des événements personnalisés.

| Option | Description |
| --- | --- |
| Apps | Par défaut, le rapport inclut les données de toutes les apps. Utilisez ce menu déroulant pour restreindre le rapport à une app spécifique. |
| Ventiler les événements personnalisés par | Contrôle la façon dont la série temporelle de l'événement personnalisé sélectionné est regroupée. Par défaut, le graphique affiche la tendance agrégée globale par date. Passez à **Événements personnalisés par heure** pour visualiser les tendances intrajournalières, ou à **Événements personnalisés par MAU** pour normaliser le volume d'événements par rapport à votre nombre d'utilisateurs actifs mensuels. |
| Filtrer par Segments | Activez cette option pour ventiler le nombre d'événements par un ou plusieurs Segments. Lorsque cette option est activée, sélectionnez les Segments que vous souhaitez comparer. Le graphique affiche le nombre d'utilisateurs dans chaque Segment ayant effectué l'événement personnalisé. |
| Formule KPI | Remplace le nombre brut d'événements par un indicateur calculé à partir d'un numérateur (tel qu'un nombre d'événements personnalisés) et d'un dénominateur (tel que le nombre d'utilisateurs actifs quotidiens, d'utilisateurs actifs mensuels ou la taille d'un Segment avec l'analytique activée). Lorsque vous sélectionnez une ou plusieurs formules, le graphique trace la valeur de chaque formule sur la plage de dates sélectionnée afin de comparer les performances normalisées (par exemple, « événements par utilisateur actif ») plutôt que le volume total d'événements. Si aucune donnée n'est disponible pour la plage de dates et les formules sélectionnées, Braze affiche un message « aucune donnée » — élargissez la plage de dates ou choisissez d'autres formules. Sélectionnez **Gérer les formules KPI** pour créer ou modifier des formules. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurer votre rapport" }

## Exporter les données {#export-data}

Pour exporter les données de vos événements personnalisés, sélectionnez <i class="fas fa-bars" title="Menu contextuel du graphique"></i> **Menu contextuel du graphique** dans le graphique des événements personnalisés et sélectionnez votre option d'exportation.

{% alert tip %}
Pour obtenir de l'aide concernant les exportations CSV et API, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

## Résolution des problèmes {#troubleshooting}

### La répartition par Segment ne correspond pas aux totaux de l'espace de travail {#segment-breakdown-doesnt-match-workspace-totals}

Lorsque vous utilisez **Filtrer par Segments** ou affinez le rapport avec le menu déroulant **Apps**, le graphique comptabilise les utilisateurs du Segment (ou de l'application) sélectionné qui ont effectué l'événement personnalisé, et non chaque occurrence de l'événement dans l'ensemble de l'espace de travail.

Si vous comparez une ligne de Segment à une vue non filtrée (ou à **All Apps**), les totaux diffèrent souvent pour les raisons suivantes :

- **All Apps** peut inclure les utilisateurs et les événements de toutes les applications de l'espace de travail.
- Un filtre sur une seule application n'inclut que les profils associés à cette application.
- Les filtres par Segment comptabilisent les utilisateurs qui correspondent à la définition du Segment au moment de la requête, ce qui peut exclure les utilisateurs ayant effectué l'événement en dehors des critères du Segment.

Pour comparer des données comparables, utilisez le même filtre d'application et la même sélection de Segment pour chaque série que vous comparez, ou exportez les données et rapprochez les totaux dans votre outil d'analyse.