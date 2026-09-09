---
nav_title: Extensions de segments
article_title: Extensions de segments
page_order: 5
page_type: reference
description: "Cet article pratique vous guidera dans la configuration et l'utilisation d'une extension de segments pour améliorer vos capacités de segmentation."
tool: Segments
---

# Extensions de segments {#segment-extensions}

> Les extensions de segments vous permettent de créer des segments très précis sur une période étendue de l'historique d'un utilisateur. Par exemple, en utilisant les extensions de segments, vous pouvez cibler les utilisateurs qui ont acheté un produit particulier au cours des seize derniers mois ou qui ont dépensé un certain montant avec votre service. Affinez cette audience en utilisant les propriétés d'événement pour rendre le ciblage encore plus granulaire.

La segmentation Braze vous permet de cibler les utilisateurs en fonction d'un événement personnalisé ou d'un comportement d'achat. Les extensions de segments renforcent cette capacité en vous permettant d'exploiter les données historiques enregistrées dans le profil utilisateur. Grâce aux extensions de segments, vous pouvez identifier et atteindre les utilisateurs qui ont effectué n'importe quel événement personnalisé ou événement d'achat un nombre quelconque de fois au cours des deux dernières années (730 jours).

## Pourquoi utiliser les extensions de segments ? {#why-use-segment-extensions}

Les Segments Braze vous offrent des outils de ciblage puissants pour créer des groupes dynamiques d'utilisateurs. Pour la plupart des cas d'usage, cela suffit pour atteindre efficacement votre audience. Les extensions de segments sont conçues pour les cas d'usage avancés où vous devez analyser des comportements remontant jusqu'à deux ans ou appliquer une logique complexe, sans compromettre la rétention des données ni les performances du système. Vous pouvez utiliser des requêtes [SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) (extensions de segments SQL) ou des données provenant de votre propre [entrepôt de données]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) pour affiner davantage votre audience.

Par exemple, la segmentation par défaut de Braze permet de trouver des utilisateurs correspondant à des critères spécifiques que vous définissez, comme identifier un utilisateur ayant récemment acheté l'un de vos produits. Les extensions de segments vous permettent d'aller plus loin, par exemple en identifiant les utilisateurs qui ont acheté une couleur particulière d'un produit spécifique au moins deux fois entre 18 et 24 mois auparavant. Les extensions de segments sont un complément, pas une obligation. Si vous avez besoin de filtres plus avancés ou d'une fenêtre d'analyse rétrospective plus longue, c'est un excellent outil qui vous aide tout en optimisant votre consommation de données.

{% alert note %}
Il existe une allocation par défaut de 50 extensions de segments actives par espace de travail à un moment donné. Si vous devez augmenter cette limite, contactez votre gestionnaire de la satisfaction client Braze pour discuter de votre cas d'usage.
{% endalert %}

## Créer une extension de segment {#creating-a-segment-extension}

Pour créer une extension de segment, vous créez un filtre afin d'affiner un segment de vos utilisateurs en fonction des propriétés d'événements personnalisés. Lors de la création d'une extension de segment, vous choisissez si le segment est statique ou s'il est actualisé dynamiquement à un intervalle défini.

### Étape 1 : Accéder aux extensions de segments {#step-1-navigate-to-segment-extensions}

Accédez à **Audience** > **Extensions de segments**.

Depuis le tableau des extensions de segments, sélectionnez **Créer une nouvelle extension**, puis choisissez votre mode de création d'extension de segment :

- **Extension simple :** Créez une extension de segment centrée sur un seul événement à l'aide d'un formulaire guidé. Idéal lorsque vous ne souhaitez pas utiliser SQL.
- **Commencer avec un modèle :** Créez un segment SQL avec un modèle personnalisable utilisant des données Snowflake.
- **Actualisation incrémentale :** Écrivez un segment SQL Snowflake qui actualise automatiquement les données des 2 derniers jours ou actualisez-le manuellement selon vos besoins. Idéal pour trouver un équilibre entre précision et rentabilité.
- **Actualisation complète :** Écrivez un segment SQL avec des données Snowflake ou toute [source connectée CDI]({{site.baseurl}}/cdi_segment_extensions) qui recalcule l'ensemble de l'audience lors d'une actualisation manuelle. Idéal lorsque vous avez besoin d'une vue complète et à jour de votre audience.

![Tableau présentant les différents modes de création d'extensions de segments disponibles.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

Si vous sélectionnez un mode utilisant SQL, consultez [Extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) pour plus d'informations. Si vous sélectionnez **Extension simple**, passez à l'étape 2.

#### Utilisation des crédits SQL {#sql-credit-usage}

Les types d'extensions de segments suivants consomment des crédits SQL :

- Extensions de segments SQL (actualisation incrémentale et complète)
- Segments de catalogue
- Segments CDI
    - Les crédits sont consommés dans votre propre entrepôt de données

### Étape 2 : Nommer votre extension de segment {#step-2-name-your-segment-extension}

Nommez votre extension de segment en décrivant le type d'utilisateurs que vous souhaitez filtrer. Cela permet aux autres de trouver et d'appliquer l'extension avec précision.

![Extension de segment nommée « Online Shoppers Extension - 90 Days ».]({% image_buster /assets/img/segment/segment_extension2.png %})

### Étape 3 : Choisir vos critères {#step-3-choose-your-criteria}

Sélectionnez des critères basés sur les achats, l'interaction avec les messages, les événements eCommerce recommandés ou les événements personnalisés pour le ciblage. Après avoir sélectionné les critères de type d'événement souhaités, choisissez quel article acheté, quelle interaction avec un message, quel événement eCommerce recommandé ou quel événement personnalisé vous souhaitez cibler pour votre liste d'utilisateurs. Ensuite, choisissez combien de fois (plus que, moins que ou égal à) l'utilisateur devrait avoir réalisé l'événement, ainsi que la période — pour les extensions de segments en particulier, vous pouvez remonter jusqu'à 730 jours (2 ans) dans le passé.

La segmentation basée sur des données d'événements datant de plus de 730 jours peut être effectuée à l'aide d'autres filtres disponibles dans **Segments**. Lorsque vous choisissez votre période, vous pouvez spécifier une plage de dates relative pour sélectionner les X derniers jours, une date de début, une date de fin ou une plage de dates exacte (date A à date B).

![Critères de segmentation pour les utilisateurs ayant effectué un événement personnalisé plus de 2 fois dans la plage de dates du 1er mars 2025 au 31 mars 2025.]({% image_buster /assets/img/segment/segment_extension1.png %})

Si vous créez une extension de segment à l'aide d'un événement eCommerce recommandé, sélectionnez d'abord **eCommerce Recommended Event** comme critère, puis sélectionnez un événement dans la liste déroulante.

![Un critère d'événement eCommerce recommandé avec une liste déroulante des événements recommandés disponibles.]({% image_buster /assets/img/segment/ecommerce_recommended_event_criterion.png %})

#### Segmentation par propriétés d'événement {#event-property-segmentation}

Pour augmenter la précision du ciblage, cochez la case **Add Property Filters**. Cela vous permettra d'affiner en fonction des propriétés spécifiques de votre achat ou événement personnalisé. La segmentation par propriétés d'événement est prise en charge pour les types string, numérique, booléen et temporel.

##### Types de données des propriétés {#property-data-types}

Pour les propriétés de type string, vous pouvez saisir plusieurs valeurs à la fois. Dans l'exemple suivant, ce filtre recherche les utilisateurs possédant une race de chien correspondant à l'une des six races de chien spécifiques.

![Segmentation basée sur les propriétés de type string.]({% image_buster /assets/img/segment/property5.png %})

##### Propriétés des événements eCommerce recommandés {#ecommerce-recommended-event-properties}

Lorsque vous ajoutez une propriété d'événement pour un événement eCommerce recommandé, la liste déroulante des propriétés se remplit automatiquement avec les propriétés disponibles pour cet événement.

Les extensions de segments prennent uniquement en charge les propriétés d'événements figurant dans la liste autorisée documentée pour chaque événement eCommerce recommandé. Les propriétés de niveau supérieur personnalisées que vous envoyez via l'API ou le SDK ne sont pas valides pour les filtres de propriétés des extensions — même si ces propriétés apparaissent dans vos données d'événements. L'utilisation d'une propriété de niveau supérieur non autorisée empêche l'enregistrement ou le désarchivage de l'extension.

Si vous avez besoin de filtrer sur des propriétés non standard, imbriquez-les sous `metadata` lorsque vous enregistrez l'événement (par exemple, `metadata.color` au lieu de `color`). Pour les propriétés prises en charge, consultez [Schémas d'événements]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-schemas) et [Types d'événements eCommerce recommandés]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events).

![Détails de l'extension de segment avec une liste déroulante des propriétés disponibles.]({% image_buster /assets/img/segment/ecommerce_recommended_event_properties.png %})

##### Propriétés d'événements imbriquées {#nested-event-properties}

La segmentation basée sur les [propriétés d'événements imbriquées]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects) est également prise en charge. Dans la liste déroulante de comparaison, sélectionnez la comparaison correspondant au type de données de votre propriété imbriquée. Vous pouvez utiliser la même syntaxe de propriétés d'événements imbriquées pour ajouter des propriétés imbriquées pour tout événement eCommerce recommandé contenant des propriétés imbriquées.

Pour en savoir plus sur les différentes propriétés imbriquées disponibles, consultez [Types d'événements eCommerce recommandés]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events). Pour générer le schéma nécessaire au nom de propriété de votre extension de segment, suivez les étapes dans [Objets imbriqués dans les événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

![Segmentation basée sur les propriétés d'événements imbriquées.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

##### Fenêtre de rétroactivité et points de donnée {#lookback-window-and-data-points}

Les extensions de segments s'appuient sur un stockage à long terme des propriétés d'événements et ne sont pas soumises à une limite de stockage horodatée. Vous pouvez consulter les propriétés d'événements suivies au cours des deux dernières années. L'utilisation des propriétés d'événements au sein des extensions de segments n'a pas d'impact sur la consommation de points de donnée.

{% alert note %}
Vous n'avez pas besoin d'extensions de segments pour utiliser les propriétés d'événements ou les attributs personnalisés imbriqués dans votre segment. Les extensions de segments étendent simplement la fenêtre historique utilisée pour créer un segment par défaut. Vous pouvez créer un [segment]({{site.baseurl}}/user_guide/audience/segments) par défaut en temps réel qui utilise les propriétés d'événements des 30 derniers jours ou qui utilise des attributs personnalisés imbriqués. De même, vous pouvez [planifier votre message]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) pour qu'il se déclenche en temps réel en fonction d'une propriété d'événement — sans extension de segment nécessaire.
{% endalert %}

### Étape 4 : Définir les paramètres d'actualisation (facultatif) {#step-4-designate-refresh-settings-optional}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

### Étape 5 : Enregistrer votre extension de segment {#step-5-save-your-segment-extension}

Après avoir sélectionné **Enregistrer**, votre extension de segment commence à être traitée. La durée de génération de votre extension de segment dépend du nombre d'utilisateurs que vous avez, du nombre d'événements personnalisés ou d'événements d'achat que vous capturez, et du nombre de jours de rétroactivité.

Pendant le traitement de votre extension de segment, une petite animation s'affiche à côté du nom de l'extension et la mention **Processing** apparaît dans la colonne **Status** de la liste des extensions de segments. Notez que vous ne pouvez pas modifier une extension de segment pendant son traitement.

![Page « Extensions de segments » avec deux extensions actives.]({% image_buster /assets/img/segment/segment_extension5.png %})

Lorsqu'une extension de segment est en cours de traitement, Braze continue d'utiliser la version historique du segment par défaut antérieure au début du traitement à des fins de segmentation de l'audience. Le traitement a lieu à chaque enregistrement ou actualisation et implique l'interrogation et la mise à jour des profils utilisateurs — autrement dit, l'appartenance à votre segment par défaut ne se met pas à jour instantanément. Cela signifie que, sauf si l'action d'un utilisateur est effectuée avant le début du traitement de l'actualisation, il n'est pas garanti que l'utilisateur sera inclus dans l'extension de segment une fois cette actualisation terminée. Inversement, les utilisateurs qui faisaient partie de l'extension de segment avant l'actualisation et qui ne répondent plus aux critères continueront à correspondre à votre segment par défaut jusqu'à ce que le processus d'actualisation soit terminé et que les mises à jour soient appliquées.

#### Statuts des extensions de segments {#segment-extension-statuses}

Sur la page **Extensions de segments**, chaque extension affiche un **Status** et un horodatage **Last Processed**. Après avoir enregistré ou actualisé une extension, utilisez ces colonnes pour confirmer que le traitement s'est terminé avec succès.

| Statut | Description |
|---|---|
| Active | L'extension a été traitée avec succès et est disponible pour la segmentation. **Last Processed** indique quand la dernière actualisation a été finalisée. |
| Draft | L'extension est enregistrée mais n'a pas encore été activée. |
| Archived | L'extension est archivée et n'est pas disponible pour la segmentation. |
| Refresh disabled | Les mises à jour récurrentes de l'audience sont désactivées. |
| Processing | Braze traite un enregistrement ou une actualisation. La colonne **Status** affiche **Processing**, une petite animation apparaît à côté du nom de l'extension, et vous ne pouvez pas modifier l'extension tant que le traitement n'est pas terminé. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Statuts des extensions de segments" }

Lorsque le traitement ne se termine pas avec succès, une icône d'erreur apparaît à côté du nom de l'extension, même si la colonne **Status** peut encore afficher **Active**. Survolez l'icône pour voir la raison de l'échec. Si vous obtenez un échec mais que vous pensez que l'extension aurait dû être traitée, essayez d'abord d'actualiser l'extension — le statut peut être obsolète.

### Étape 6 : Utiliser votre extension dans un segment {#step-6-use-your-extension-in-a-segment}

Après avoir créé une extension de segment, vous pouvez l'utiliser comme filtre lors de la création d'un segment ou de la définition d'une audience pour une Campaign ou un Canvas. Commencez par choisir **Braze Segment Extension** dans la liste des filtres sous la section **User Attributes**.

![Section « Filtres » avec une liste déroulante de filtres affichant « Braze Segment Extensions ».]({% image_buster /assets/img/segment/segment_extension7.png %})

Dans la liste des filtres Braze Segment Extension, choisissez l'extension de segment que vous souhaitez inclure ou exclure de ce segment.

![Un filtre « Braze Segment Extensions » qui inclut un segment « 1 email click in the last 56 days ».]({% image_buster /assets/img/segment/segment_extension6.png %})

Pour afficher les critères de l'extension de segment, sélectionnez **View Extension Details** pour afficher les détails dans une nouvelle fenêtre.

![Extension pour « 1 email click in the last 56 days ».]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Vous pouvez maintenant procéder comme d'habitude à la [création de votre segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

## Questions fréquentes {#frequently-asked-questions}

### Puis-je créer une extension de segment qui utilise plusieurs événements personnalisés ? {#can-i-create-a-segment-extension-that-uses-multiple-custom-events}

Oui. Vous pouvez ajouter plusieurs événements ou référencer plusieurs tables Snowflake lorsque vous utilisez les [extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).

Lorsque vous utilisez les extensions de segments de type **Extension simple**, vous pouvez sélectionner un événement personnalisé, un événement d'achat ou une interaction de canal. Cependant, vous pouvez combiner plusieurs extensions de segments avec un ET ou un OU lors de la création du segment par défaut.

### Puis-je archiver des extensions de segments si elles sont utilisées dans une Campaign active ? {#can-i-archive-segment-extensions-if-they-exist-in-an-active-campaign}

Non. Avant de pouvoir archiver une extension de segment, vous devez la retirer de toutes les communications actives.

### Puis-je utiliser des tableaux dans les extensions de segments ? {#can-i-use-arrays-in-segment-extensions}

Oui. Pour utiliser des tableaux, ajoutez des crochets (`[]`) au nom de votre propriété. Si votre propriété est `location_code`, vous devez saisir `location_code[]`.

Braze utilise `[]` pour parcourir les tableaux et vérifier si un élément du tableau parcouru correspond à la propriété de l'événement. Par exemple, vous pourriez créer une extension de segment regroupant les utilisateurs correspondant à au moins une valeur d'une propriété de type tableau.

### Comment Braze calcule-t-il la période pour une période relative de type « X derniers jours » ? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-__-days}

Lorsque les extensions de segments calculent la période relative (« X derniers jours »), l'heure de début est fixée à minuit UTC. Par exemple, pour une extension de segment qui s'actualise le 2024-09-16 à 21:00 UTC et qui spécifie 10 jours, l'heure de début est fixée au 2024-09-06 à 00:00 UTC, et non au 2024-09-06 à 21:00 UTC.

Cependant, vous pouvez spécifier les fuseaux horaires en utilisant les segments SQL pour identifier les utilisateurs ayant effectué l'événement personnalisé il y a 10 jours en se basant sur minuit dans le fuseau horaire de l'entreprise, ou les utilisateurs ayant effectué l'événement il y a 10 jours en se basant sur l'heure actuelle.