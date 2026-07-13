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

Les Segments Braze vous offrent des outils de ciblage puissants pour créer des groupes dynamiques d'utilisateurs. Pour la plupart des cas d'usage, cela suffit pour atteindre votre audience efficacement. Les extensions de segments sont conçues pour des cas d'usage avancés où vous devez analyser des comportements remontant jusqu'à deux ans ou appliquer une logique complexe, sans compromettre la rétention des données ni les performances du système. Vous pouvez utiliser des requêtes [SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) (extensions de segments SQL) ou des données provenant de votre propre [entrepôt de données]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) pour affiner davantage votre audience.

Par exemple, la segmentation par défaut de Braze trouvera les utilisateurs correspondant à des critères spécifiques que vous définissez, comme identifier un utilisateur qui a récemment acheté l'un de vos produits. Les extensions de segments vous permettent d'aller plus loin, par exemple en identifiant les utilisateurs qui ont acheté une couleur particulière d'un produit spécifique au moins deux fois entre 18 et 24 mois auparavant. Les extensions de segments sont un enrichissement, pas une obligation. Si vous avez besoin de filtres plus avancés ou d'une fenêtre de rétrospection plus longue, c'est un excellent outil qui vous aide tout en optimisant votre utilisation des données.

{% alert note %}
Il existe une allocation par défaut de 25 extensions de segments actives par espace de travail à un moment donné. Si vous devez augmenter cette limite, contactez votre gestionnaire du succès des clients Braze pour discuter de votre cas d'usage.
{% endalert %}

## Créer une extension de segments {#creating-a-segment-extension}

Pour créer une extension de segments, vous allez créer un filtre pour affiner un segment de vos utilisateurs en fonction des propriétés d'événement personnalisé. Lors de la création d'une extension de segments, vous choisirez si le segment sera statique ou actualisé dynamiquement à un intervalle défini.

### Étape 1 : Accéder aux extensions de segments {#step-1-navigate-to-segment-extensions}

Allez dans **Audience** > **Extensions de segments**.

Depuis le tableau des extensions de segments, sélectionnez **Créer une nouvelle extension**, puis choisissez votre expérience de création d'extension de segments :

- **Simple extension :** Créez une extension de segments centrée sur un seul événement à l'aide d'un formulaire guidé. Idéal lorsque vous ne souhaitez pas utiliser SQL.
- **Start with a template :** Créez un segment SQL avec un modèle personnalisable utilisant les données Snowflake.
- **Incremental refresh :** Rédigez un segment SQL Snowflake qui actualise automatiquement les données des 2 derniers jours ou actualisez manuellement selon vos besoins. Idéal pour équilibrer précision et rentabilité.
- **Full refresh :** Rédigez un segment SQL avec les données Snowflake ou toute [source connectée CDI]({{site.baseurl}}/cdi_segment_extensions) qui recalcule l'ensemble de l'audience lors d'une actualisation manuelle. Idéal lorsque vous avez besoin d'une vue complète et à jour de votre audience.

![Tableau présentant les différentes expériences de création d'extensions de segments parmi lesquelles choisir.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

Si vous sélectionnez une expérience utilisant SQL, consultez [Extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) pour plus d'informations. Si vous sélectionnez **Simple extension**, passez à l'étape 2.

#### Utilisation des crédits SQL {#sql-credit-usage}

Les types d'extensions de segments suivants consomment des crédits SQL :

- Extensions de segments SQL (actualisation incrémentielle et complète)
- Segments de catalogue
- Segments CDI
    - Les crédits sont consommés au sein de votre propre entrepôt de données

### Étape 2 : Nommer votre extension de segments {#step-2-name-your-segment-extension}

Nommez votre extension de segments en décrivant le type d'utilisateurs que vous souhaitez filtrer. Cela garantira que cette extension pourra être facilement et précisément trouvée lorsque vous l'appliquerez comme filtre dans votre segment.

![Extension de segments nommée « Online Shoppers Extension - 90 Days ».]({% image_buster /assets/img/segment/segment_extension2.png %})

### Étape 3 : Choisir vos critères {#step-3-choose-your-criteria}

Sélectionnez entre les critères d'achat, d'engagement par message, d'événement eCommerce recommandé ou d'événement personnalisé pour le ciblage. Après avoir sélectionné les critères de type d'événement souhaités, choisissez quel article acheté, quelle interaction de message, quel événement eCommerce recommandé ou quel événement personnalisé vous souhaitez cibler pour votre liste d'utilisateurs. Ensuite, choisissez combien de fois (plus de, moins de ou égal à) l'utilisateur devrait avoir effectué l'événement, ainsi que la période — pour les extensions de segments spécifiquement, vous pouvez remonter jusqu'aux 730 derniers jours (2 ans).

La segmentation basée sur des données d'événement de plus de 730 jours peut être effectuée à l'aide d'autres filtres situés dans **Segments**. Lorsque vous choisissez votre période, vous pouvez spécifier une plage de dates relative pour sélectionner les X derniers jours, une date de début, une date de fin ou une plage de dates exacte (date A à date B).

![Critères de segmentation pour les utilisateurs ayant effectué un événement personnalisé plus de 2 fois dans la plage de dates du 1er mars 2025 au 31 mars 2025.]({% image_buster /assets/img/segment/segment_extension1.png %})

Si vous créez une extension de segments à l'aide d'un événement eCommerce recommandé, sélectionnez d'abord **eCommerce Recommended Event** comme critère, puis sélectionnez un événement dans le menu déroulant.

![Un critère d'événement eCommerce recommandé avec un menu déroulant des événements recommandés disponibles.]({% image_buster /assets/img/segment/ecommerce_recommended_event_criterion.png %})

#### Segmentation par propriété d'événement {#event-property-segmentation}

Pour augmenter la précision du ciblage, cochez la case **Add Property Filters**. Cela vous permettra d'affiner en fonction des propriétés spécifiques de votre achat ou événement personnalisé. Nous prenons en charge la segmentation par propriété d'événement basée sur les objets de type chaîne de caractères, numérique, booléen et date/heure.

Pour les propriétés de type chaîne de caractères, vous pouvez saisir plusieurs valeurs à la fois. Dans l'exemple ci-dessous, ce filtre recherche les utilisateurs dont le statut est égal à l'une des valeurs suivantes : gold, silver ou bronze.

![Segmentation basée sur les propriétés de type chaîne de caractères.]({% image_buster /assets/img/segment/property5.png %})

![Segmentation basée sur les propriétés numériques.]({% image_buster /assets/img/segment/property2.png %})

![Segmentation basée sur les propriétés booléennes.]({% image_buster /assets/img/segment/property3.png %})

![Segmentation basée sur les objets date/heure.]({% image_buster /assets/img/segment/property4.png %})

Si vous utilisez des événements eCommerce recommandés et ajoutez une propriété d'événement, le menu déroulant des propriétés se remplira automatiquement avec les propriétés disponibles pour cet événement eCommerce recommandé spécifique.

![Détails de l'extension de segments avec un menu déroulant des propriétés disponibles.]({% image_buster /assets/img/segment/ecommerce_recommended_event_properties.png %})

Nous prenons également en charge la segmentation basée sur les [propriétés de l'événement imbriqué]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects). Dans le menu déroulant de comparaison, sélectionnez la comparaison qui correspond au type de données de votre propriété imbriquée. Vous pouvez utiliser la même syntaxe de propriété d'événement imbriqué pour ajouter des propriétés imbriquées pour tout événement eCommerce recommandé contenant des propriétés imbriquées. Pour plus d'informations sur les différentes propriétés imbriquées disponibles, consultez [Types d'événements eCommerce recommandés]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events). Pour générer le schéma nécessaire pour le nom de propriété de votre extension de segments, suivez les étapes dans [Objets imbriqués dans les événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

![Segmentation basée sur les propriétés de l'événement imbriqué.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

Les extensions de segments s'appuient sur le stockage à long terme des propriétés d'événement et n'ont pas de limite de stockage horodaté des propriétés. Vous pouvez consulter les propriétés d'événement suivies au cours des deux dernières années. L'utilisation des propriétés d'événement au sein des extensions de segments n'affecte pas la consommation de points de donnée.

{% alert note %}
Vous n'avez pas besoin des extensions de segments pour utiliser les propriétés d'événement ou les attributs personnalisés imbriqués dans votre segment. Les extensions de segments étendent simplement la fenêtre historique utilisée pour créer un segment par défaut. Vous pouvez créer un [segment]({{site.baseurl}}/user_guide/audience/segments) par défaut en temps réel qui utilise les propriétés d'événement des 30 derniers jours ou qui utilise des attributs personnalisés imbriqués. De même, vous pouvez [planifier votre message]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) pour qu'il se déclenche en temps réel en fonction d'une propriété d'événement, sans extension de segments nécessaire.
{% endalert %}

### Étape 4 : Définir les paramètres d'actualisation (facultatif) {#step-4-designate-refresh-settings-optional}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

### Étape 5 : Enregistrer votre extension de segments {#step-5-save-your-segment-extension}

Après avoir sélectionné **Enregistrer**, votre extension de segments commencera à être traitée. La durée nécessaire pour générer votre extension de segments dépend du nombre d'utilisateurs que vous avez, du nombre d'événements personnalisés ou d'événements d'achat que vous capturez, et du nombre de jours de rétrospection dans l'historique.

Pendant le traitement de votre extension de segments, vous verrez une petite animation à côté du nom de l'extension de segments, et le mot « Processing » dans la colonne **Last Processed** de la liste des extensions de segments. Notez que vous ne pourrez pas modifier une extension de segments pendant son traitement.

![Page « Extensions de segments » avec deux extensions actives.]({% image_buster /assets/img/segment/segment_extension5.png %})

Lorsqu'une extension de segments est en cours de traitement, Braze continuera d'utiliser la version historique du segment par défaut d'avant le début du traitement à des fins de segmentation d'audience. Le traitement a lieu chaque fois qu'une sauvegarde ou une actualisation se produit, et implique l'interrogation et la mise à jour des profils utilisateur — en d'autres termes, l'appartenance à votre segment par défaut ne se met pas à jour instantanément. Cela signifie qu'à moins que l'action d'un utilisateur ne soit effectuée avant le début du traitement de l'actualisation, nous ne pouvons pas garantir que l'utilisateur sera inclus dans l'extension de segments une fois cette actualisation particulière terminée. Inversement, les utilisateurs qui faisaient partie de l'extension de segments avant l'actualisation et qui ne répondent plus aux critères continueront de correspondre à votre segment par défaut jusqu'à ce que le processus d'actualisation soit terminé et que les mises à jour soient appliquées.

### Étape 6 : Utiliser votre extension dans un segment {#step-6-use-your-extension-in-a-segment}

Après avoir créé une extension de segments, vous pouvez l'utiliser comme filtre lors de la création d'un segment ou de la définition d'une audience pour une Campaign ou un Canvas. Commencez par choisir **Braze Segment Extension** dans la liste des filtres sous la section **Attributs utilisateur**.

![Section « Filtres » avec un menu déroulant de filtres affichant « Braze Segment Extensions ».]({% image_buster /assets/img/segment/segment_extension7.png %})

Dans la liste des filtres Braze Segment Extension, choisissez l'extension de segments que vous souhaitez inclure ou exclure dans ce segment.

![Un filtre « Braze Segment Extensions » qui inclut un segment « 1 email click in the last 56 days ».]({% image_buster /assets/img/segment/segment_extension6.png %})

Pour afficher les critères de l'extension de segments, sélectionnez **View Extension Details** pour afficher les détails dans une nouvelle fenêtre.

![Extension pour « 1 email click in the last 56 days ».]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Vous pouvez maintenant procéder comme d'habitude avec la [création de votre segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

## Questions fréquemment posées {#frequently-asked-questions}

### Puis-je créer une extension de segments qui utilise plusieurs événements personnalisés ? {#can-i-create-a-segment-extension-that-uses-multiple-custom-events}

Oui. Vous pouvez ajouter plusieurs événements ou référencer plusieurs tables Snowflake en utilisant les [extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).

Lorsque vous utilisez des extensions de segments de type **Simple extension**, vous pouvez sélectionner un événement personnalisé, un événement d'achat ou une interaction de canal. Cependant, vous pouvez combiner plusieurs extensions de segments avec un ET ou un OU lors de la création du segment par défaut.

### Puis-je archiver des extensions de segments si elles existent dans une Campaign active ? {#can-i-archive-segment-extensions-if-they-exist-in-an-active-campaign}

Non. Avant de pouvoir archiver une extension de segments, vous devez la retirer de tous les envois de messages actifs.

### Puis-je utiliser des tableaux dans les extensions de segments ? {#can-i-use-arrays-in-segment-extensions}

Oui. Pour utiliser des tableaux, ajoutez des crochets (`[]`) au nom de votre propriété. Si votre propriété est `location_code`, vous saisiriez `location_code[]`.

Braze utilise `[]` pour parcourir les tableaux et vérifier si un élément du tableau parcouru correspond à la propriété d'événement. Par exemple, vous pourriez créer une extension de segments d'utilisateurs correspondant à au moins une valeur d'une propriété de type tableau.

### Comment Braze calcule-t-il la période pour une période relative de « derniers __ jours » ? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-__-days}

Lorsque les extensions de segments calculent la période relative (« derniers X jours »), l'heure de début est fixée à minuit UTC. Par exemple, pour une extension de segments qui s'actualise à 2024-09-16 21:00 UTC et spécifie 10 jours, l'heure de début est fixée à 2024-09-06 00:00 UTC, et non à 2024-09-06 21:00 UTC.

Cependant, vous pouvez spécifier les fuseaux horaires en utilisant des segments SQL pour identifier les utilisateurs qui ont effectué l'événement personnalisé il y a 10 jours en se basant sur minuit dans le fuseau horaire de l'entreprise, ou les utilisateurs qui ont effectué l'événement il y a 10 jours en se basant sur l'heure actuelle.