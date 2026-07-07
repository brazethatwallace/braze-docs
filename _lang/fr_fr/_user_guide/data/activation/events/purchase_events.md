---
nav_title: Événements d'achat
article_title: Événements d'achat
page_order: 3
page_type: reference
description: "Cet article de référence décrit les événements et propriétés d'achat, leur utilisation, leur segmentation, où voir les analyses qui s'y rapportent, etc."
search_rank: 3
---

# Événements d'achat {#purchase-events}

> Cette page traite des événements et propriétés d'achat, de leur utilisation, de la segmentation, de l'affichage des analyses pertinentes, etc.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

Les événements d'achat sont des actions d'achat effectuées par vos utilisateurs. Ils servent à enregistrer les achats in-app et à établir la valeur vie client (LTV) pour chaque profil utilisateur. Ces événements doivent être mis en place par votre équipe. L'enregistrement des événements d'achat vous permet d'ajouter des propriétés telles que la quantité et le type, ce qui vous aide à mieux cibler vos utilisateurs en fonction de ces propriétés.

## Enregistrer les événements d'achat {#log-purchase-events}

Vous pouvez enregistrer vos achats en transmettant un [objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object) via l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), ou en utilisant l'une de nos bibliothèques SDK répertoriées ci-dessous.

{% alert note %}
Les propriétés d'événement d'achat utilisent les mêmes types de données que les [propriétés d'événement personnalisé]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events#expected-format).
{% endalert %}

La liste suivante énumère les méthodes utilisées pour enregistrer les achats sur les différentes plateformes. Dans ces pages, vous trouverez également la documentation sur la façon d'ajouter des propriétés et des quantités à votre événement d'achat. Vous pouvez cibler davantage vos utilisateurs en fonction de ces propriétés.

- [Android et FireOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=unity)
- [.NET MAUI (anciennement Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=roku)

## Consulter les données d'achat {#view-purchase-data}

Une fois que vous avez configuré et commencé à enregistrer les événements d'achat, vous pouvez consulter ces données d'achat sur le profil d'un utilisateur dans l'[onglet Aperçu]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#overview-tab).

## Utiliser les données d'achat {#use-purchase-data}

Il existe plusieurs façons d'utiliser les données d'achat dans Braze :

- **[Segmentation](#purchase-event-segmentation) :** Utilisez les données d'achat pour créer des segments d'utilisateurs en fonction de leur comportement d'achat.
- **[Personnalisation](#personalization) :** Utilisez les données d'achat pour personnaliser les messages envoyés aux utilisateurs.
- **[Déclenchement de messages](#trigger-messages) :** Configurez des messages qui se déclenchent en fonction des événements d'achat.
- **[Analytique](#analytics) :** Analysez vos données d'achat pour obtenir des informations sur le comportement des utilisateurs et l'efficacité de vos campagnes marketing.

### Segmentation {#purchase-event-segmentation}

Vous pouvez déclencher n'importe quel nombre ou type de campagnes de suivi en fonction des événements d'achat enregistrés. Par exemple, vous pouvez créer un segment d'utilisateurs ayant effectué un achat au cours des 30 derniers jours, ou un segment d'utilisateurs ayant dépensé plus d'un certain montant.

Les filtres de segmentation suivants sont disponibles pour cibler les utilisateurs :

- Premier achat effectué
- Premier achat pour l'application
- Dernier produit acheté
- Montant dépensé
- Produit acheté
- Nombre total d'achats
- Montant X dépensé en Y jours
- Produit X acheté en Y jours
- Propriété d'achat X en Y jours
- X achats au cours des Y derniers jours

Pour plus de détails sur chaque filtre, consultez le glossaire des [filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) et filtrez par « Purchase behavior ».

![Filtrage des utilisateurs ayant effectué exactement trois achats]({% image_buster /assets/img/purchase_filter_example.gif %}){: style="max-width:80%;"}

{% alert tip %}
Pour segmenter sur le nombre de fois qu'un achat spécifique a été effectué, enregistrez cet achat individuellement en tant qu'[attribut personnalisé incrémentiel]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview#custom-attribute-storage).
{% endalert %}

### Personnalisation {#personalization}

Comme tout autre type de données que vous collectez auprès de vos utilisateurs, vous pouvez utiliser les données d'achat pour personnaliser vos messages via Liquid. Par exemple, vous pouvez envoyer un e-mail personnalisé à un utilisateur en lui recommandant des produits similaires à ceux qu'il vient d'acheter.

Supposons que vous ayez une propriété d'événement d'achat appelée `last_purchased_product` qui stocke le nom du dernier produit acheté par un utilisateur. Vous pouvez utiliser cette propriété pour personnaliser un e-mail de cette façon :

{% raw %}

```liquid
{% if ${last_purchased_product} == "Running Shoes" %}
  We hope you're enjoying your new running shoes! Based on your recent purchase, you might also like these running shorts and water bottles.
{% elsif ${last_purchased_product} == "Yoga Mat" %}
  We hope you're enjoying your new yoga mat! Based on your recent purchase, you might also like these yoga blocks and straps.
{% else %}
  Thank you for your recent purchase! We hope you're enjoying your new item.
{% endif %}
```

{% endraw %}

Dans cet exemple, le message est personnalisé en fonction de la propriété `last_purchased_product`. Si le dernier produit acheté par l'utilisateur était « Running Shoes », il reçoit un message recommandant des shorts de course et des gourdes. Si le dernier produit était « Yoga Mat », il reçoit un message recommandant des briques et des sangles de yoga. Si `last_purchased_product` correspond à autre chose, il reçoit un message de remerciement générique.

### Déclencher des messages {#trigger-messages}

Un cas d'utilisation courant consiste à envoyer automatiquement un message, comme un e-mail, lorsqu'un utilisateur effectue un achat. Par exemple, vous pouvez envoyer un message de remerciement ou un code de réduction pour un prochain achat.

Pour ce faire, créez une campagne ou un Canvas basé sur une action, puis définissez l'action de déclenchement sur **Effectuer un achat**. Vous pouvez également spécifier des conditions supplémentaires pour le déclencheur, comme le produit acheté ou le montant de l'achat.

Vous pouvez aussi personnaliser votre message déclenché avec Liquid. Dans l'exemple suivant, `${purchase_product_name}` est un attribut personnalisé que vous remplaceriez par le nom réel de l'attribut qui stocke le nom du produit acheté dans votre configuration Braze.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

### Analytique {#analytics}

En plus du suivi des indicateurs d'achat pour la segmentation, Braze enregistre également le nombre d'achats pour chaque produit et le chiffre d'affaires généré au fil du temps. Cela peut être utile pour identifier les produits les plus populaires ou mesurer l'impact d'une campagne promotionnelle sur les ventes.

Vous pouvez trouver ces données sur la page [Rapport sur les revenus]({{site.baseurl}}/user_guide/analytics/reports/revenue_report#revenue-data).

### Calculs du chiffre d'affaires {#revenue-calculations}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Calculs du chiffre d'affaires">
  <caption>Calculs du chiffre d'affaires</caption>
    <thead>
        <tr>
            <th>Indicateur</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-revenue">Chiffre d'affaires sur la durée de vie</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-value-per-user">Valeur vie par utilisateur</a></td>
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

#### Conversion de devises {#currency-conversion}

Lorsque des événements d'achat sont enregistrés dans une devise autre que l'USD, Braze convertit le montant en USD en utilisant les taux de change d'[Open Exchange Rates](http://openexchangerates.org). Ces taux sont actualisés toutes les 24 heures. Comme les taux de change sont mis en cache, il peut y avoir de légères différences par rapport au taux du marché en temps réel, en particulier pour les devises connaissant des fluctuations rapides.

#### Calcul du chiffre d'affaires sur la durée de vie {#lifetime-revenue-calculation}

Braze utilise les événements d'achat pour calculer le chiffre d'affaires sur la durée de vie (également appelé valeur vie client ou LTV) d'un utilisateur, qui est une prédiction du bénéfice net attribué à l'ensemble de la relation future avec un client. Cela peut vous aider à prendre des décisions éclairées concernant les stratégies d'acquisition et de fidélisation des clients.

$$\text{Valeur moyenne d'achat} = \frac{\text{Dépenses totales en dollars}}{\text{Nombre total d'événements d'achat}}$$

Il existe deux endroits principaux dans Braze où vous pouvez consulter la LTV de vos utilisateurs :

- Pour des indicateurs globaux comme le *chiffre d'affaires sur la durée de vie* et la *valeur vie par utilisateur* pour chaque application et site, consultez votre [Rapport sur les revenus]({{site.baseurl}}/user_guide/analytics/reports/revenue_report#revenue-data).
- Pour comprendre le chiffre d'affaires sur la durée de vie d'un utilisateur spécifique, consultez son [profil utilisateur]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#overview-tab).

##### Impact des remboursements sur le chiffre d'affaires sur la durée de vie {#impact-of-refunds-on-lifetime-revenue}

Lorsque vous utilisez des événements d'achat pour suivre les données d'achat, vous devez enregistrer les remboursements en consignant un événement d'achat Braze avec une propriété `price` négative. Cette approche maintient un total précis pour le chiffre d'affaires sur la durée de vie.

Cependant, gardez à l'esprit que le remboursement comptera comme un événement d'achat supplémentaire. Prenons l'exemple suivant. Sam effectue son premier achat pour 12 $ mais retourne une partie de l'achat pour un remboursement de 5 $. Le profil de Sam enregistrerait :

- 1 achat avec un prix de 12 $
- 1 achat avec un prix de -5 $
- Un chiffre d'affaires sur la durée de vie de 7 $

Bien que Sam ait deux événements d'achat sur son profil, en réalité, il n'a effectué qu'un seul achat. C'est un point important à considérer si vous avez des segments ou des cas d'utilisation basés sur le nombre d'achats effectués par un utilisateur. Les remboursements fréquents gonflent le nombre d'achats sur le profil de l'utilisateur.

## Propriétés d'événement d'achat {#purchase-properties}

Avec les propriétés d'événement d'achat, vous pouvez définir des propriétés sur les achats qui peuvent être utilisées pour affiner les conditions de déclenchement, augmenter la personnalisation des messages et générer des analyses plus sophistiquées via l'exportation de données brutes. Les types de valeurs de propriété (chaîne de caractères, numérique, valeur booléenne, date) varient selon la plateforme et sont souvent attribués sous forme de paires clé-valeur.

{% alert warning %}
Les clés suivantes sont réservées et ne peuvent pas être utilisées comme noms de propriété d'événement d'achat : `time`, `product_id`, `quantity`, `event_name`, `price` et `currency`. L'utilisation d'une clé réservée dans l'objet `properties` renverra l'erreur « Invalid 'properties' field ».
{% endalert %}

Par exemple, si vous avez une application e-commerce et souhaitez envoyer un message à un utilisateur après un achat, vous pourriez améliorer votre audience cible et permettre une personnalisation accrue de la campagne en ajoutant une propriété d'événement d'achat `brand_name`.

**Exemple de déclenchement basé sur les propriétés d'événement d'achat :**

![Paramètres de livraison par événement pour envoyer une campagne aux utilisateurs qui achètent des écouteurs avec un nom de marque égal à HeadphoneMart]({% image_buster /assets/img/purchase2.png %}){: style="max-width:80%;margin-left:15px;"}

Consultez l'[objet de propriétés d'achat]({{site.baseurl}}/api/objects_filters/purchase_object#purchase-properties-object) pour en savoir plus.

### Segmentation par propriété d'événement {#event-property-segmentation}

La segmentation par propriété d'événement vous permet de cibler les utilisateurs non seulement en fonction des événements personnalisés effectués, mais aussi en fonction des propriétés associées à ces événements. Cela ajoute des options de filtrage supplémentaires lors de la segmentation des achats et des événements personnalisés.

![Filtres de segmentation pour les propriétés d'événement d'achat, affichant des options pour filtrer les utilisateurs en fonction de valeurs spécifiques de propriétés d'événement d'achat, comme le filtrage des utilisateurs ayant acheté un produit avec une certaine propriété dans un délai défini.]({% image_buster /assets/img/purchase_event_property.png %}){: style="max-width:80%;margin-left:15px;"}

Ces filtres de segmentation incluent :
- A effectué l'événement personnalisé avec la propriété Y ayant la valeur V, X fois au cours des Y derniers jours
- A effectué des achats avec la propriété Y ayant la valeur V, X fois au cours des Y derniers jours
- Ajoute une segmentation de 1 à 30 jours sur tous les achats, événements et propriétés au sein des achats et événements

Contrairement aux [extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension), les segments utilisés sont mis à jour en temps réel, prennent en charge un nombre illimité de segments, offrent un historique de consultation de 30 jours maximum et consomment des points de donnée. En raison du coût supplémentaire en points de donnée, vous devez contacter votre gestionnaire de la satisfaction client Braze pour activer les propriétés d'événement sur vos événements personnalisés.

Une fois approuvées, des propriétés supplémentaires peuvent être ajoutées dans le tableau de bord sous **Paramètres des données** > **Événements personnalisés** en sélectionnant **Gérer les propriétés**. Vous pouvez ensuite utiliser ces propriétés d'événement dans l'étape de ciblage du générateur de campagne ou de Canvas.

{% include data_activation/segmentable_purchase_properties_keys_note.md %}

### Propriétés d'entrée Canvas et propriétés d'événement {#canvas-entry-properties-and-event-properties}

{% multi_lang_include canvas/entry_event_properties.md %}

### Enregistrer les achats au niveau de la commande {#log-purchases-at-the-order-level}

Pour enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, utilisez le nom de la commande ou la catégorie de commande comme `product_id`. Consultez notre [spécification de l'objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object#product-id-naming-conventions) pour en savoir plus.

### Conventions de nommage des identifiants de produit {#product-id-naming-conventions}

Chez Braze, nous proposons quelques conventions de nommage générales pour le `product_id` de l'objet d'achat. Lors du choix du `product_id`, Braze suggère d'utiliser des noms simples tels que le nom du produit ou la catégorie de produit (plutôt que des unités de gestion des stocks) dans le but de regrouper tous les éléments enregistrés par ce `product_id`.

Cela rend les produits faciles à identifier pour la segmentation et le déclenchement.

## Bloquer des événements d'achat {#blocklist-purchase-events}

Il peut arriver que vous identifiiez des événements d'achat qui consomment trop de points de donnée, ne sont plus utiles à votre stratégie marketing ou ont été enregistrés par erreur. Pour empêcher l'envoi de ces données à Braze, vous pouvez bloquer l'objet de données personnalisées pendant que votre équipe technique travaille à le supprimer du backend de votre application ou site web.

Dans le tableau de bord de Braze, vous pouvez gérer le blocage depuis **Paramètres des données** > **Produits**. Consultez [Gestion des données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data) pour en savoir plus.