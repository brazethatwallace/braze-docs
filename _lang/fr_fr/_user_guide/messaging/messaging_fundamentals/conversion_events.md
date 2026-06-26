---
nav_title: Événements de conversion
article_title: Événements de conversion
page_order: 3
page_type: reference
description: "Cet article de référence définit les événements de conversion, explique comment les utiliser pour définir vos indicateurs de réussite dans Braze, et comment exploiter ces événements pour mesurer l'engagement de vos utilisateurs."
tool:
    - Campaigns
    - Canvas
---

# Événements de conversion {#conversion-events}

> Un événement de conversion est un type d'indicateur de réussite qui permet de suivre si un destinataire de votre message effectue une action à forte valeur ajoutée dans un délai défini après avoir reçu votre communication. Utilisez ces événements pour vous assurer de collecter des informations pertinentes et utiles que vous pourrez ensuite exploiter pour obtenir des insights sur votre Campaign ou votre Canvas.

## Comment ça fonctionne {#how-it-works}

Pour une campagne personnalisée de fêtes ciblant les utilisateurs actifs, un événement de conversion **Démarrer une session** dans un délai de deux à trois jours peut être approprié, car il vous permet d'évaluer l'engagement des utilisateurs suite à la réception de votre message. Vous pouvez également sélectionner des événements supplémentaires comme **Passer une commande**, **Mettre à jour l'application**, ou n'importe lequel de vos événements personnalisés comme événements de conversion.

### Quand le suivi des conversions commence-t-il ? {#when-does-conversion-tracking-begin}

{% tabs %}
{% tab Campaign %}

Le suivi des conversions commence lorsqu'un utilisateur reçoit la Campaign ou entre dans le groupe de contrôle de la Campaign. La réception d'un message et l'affectation à une variante se produisent généralement en même temps. Pour les campagnes de messages in-app, le suivi des conversions commence lorsque Braze enregistre une impression.

{% endtab %}
{% tab Canvas %}

Le suivi des conversions commence lorsqu'un utilisateur entre dans le Canvas. Pour les étapes du Canvas, les conversions sont attribuées tant que l'utilisateur est actif dans cette étape. Lorsque l'utilisateur passe à une autre étape, le suivi des conversions s'arrête pour l'étape précédente et commence pour l'étape suivante.

Tant qu'un utilisateur se trouve dans une étape de délai ou une autre étape sans message, les conversions survenant pendant cette attente sont toujours attribuées à la dernière étape de message reçue, jusqu'à ce que l'utilisateur reçoive une autre étape de message. Après que l'utilisateur a reçu la dernière étape de message de son parcours, les conversions peuvent encore être enregistrées jusqu'à la date limite de conversion (calculée à partir de l'entrée dans le Canvas), même s'il n'y a plus d'étapes de message.

{% endtab %}
{% endtabs %}

{% alert tip %}
Pour en savoir plus sur les conversions, consultez notre [cours Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sur la configuration des campagnes.
{% endalert %}

### Règles de suivi des conversions {#conversion-tracking-rules}

Les événements de conversion attribuent les actions des utilisateurs à un point d'engagement. De manière générale, tant qu'une fenêtre de conversion est ouverte, un utilisateur ne convertit qu'une seule fois au maximum par événement de conversion pour cette Campaign ou ce Canvas. S'il effectue la même action de conversion plus d'une fois avant la date limite (par exemple, deux achats), Braze ne comptabilise qu'une seule conversion pour cet événement. Les campagnes multicanal peuvent enregistrer une opportunité de conversion distincte pour chaque canal de communication, ce qui peut produire des taux de conversion supérieurs à 100 % lorsque vous comparez le nombre de conversions avec les destinataires uniques (voir ci-dessous).

Notez les points suivants concernant la manière dont Braze gère les conversions multiples :

- **Campagnes monocanal** : les conversions sont comptabilisées par utilisateur, et non par appareil. Au sein d'un même canal, un utilisateur ne convertit qu'une seule fois par événement de conversion, même si un message est envoyé à plusieurs appareils. Par exemple, si une Campaign n'a qu'un seul événement de conversion défini sur « Effectue un achat quelconque » et qu'un utilisateur effectue deux achats distincts avant la date limite de conversion, Braze ne comptabilise qu'une seule conversion.
- **Campagnes multicanal** : pour les campagnes multicanal, chaque canal dispose de sa propre opportunité de conversion. Un utilisateur peut convertir une fois par canal après avoir reçu un message sur ce canal. Cela signifie que si un utilisateur reçoit des messages sur plusieurs canaux (par exemple, e-mail et push) et effectue l'action de conversion, Braze comptabilise une conversion pour chaque canal, ce qui peut entraîner des taux de conversion supérieurs à 100 %.
- **Étapes de message Canvas** : Braze attribue les conversions survenues dans le délai de conversion à la dernière étape de message Canvas que l'utilisateur a reçue. Après réception de l'étape de message suivante, l'attribution passe à cette étape. Braze mesure cette fenêtre à partir du moment où l'utilisateur entre dans le Canvas, et non à partir de chaque message individuellement. Les conversions survenant pendant les délais entre les étapes de message sont comptabilisées pour l'attribution de l'étape de message précédente jusqu'à ce que l'utilisateur avance ; les conversions après la dernière étape de message sont toujours comptabilisées jusqu'à la date limite de conversion du Canvas.
- Si un utilisateur effectue un événement de conversion dans les délais de conversion de deux Campaigns ou Canvas distincts qu'il a reçus, la conversion est enregistrée pour les deux.
- Un utilisateur est considéré comme converti s'il a effectué l'événement de conversion spécifique dans la fenêtre définie, même s'il n'a pas ouvert ou cliqué sur le message.

### Événement de conversion principal {#primary-conversion-event}

L'événement de conversion principal est le premier événement que vous ajoutez lors de la création d'une Campaign ou d'un Canvas. Cet événement a le plus d'impact sur votre engagement et vos rapports. Braze utilise votre événement de conversion principal pour :

- Déterminer la variante gagnante dans les campagnes ou Canvas [multivariés]({{site.baseurl}}/user_guide/messaging/ab_testing/#multivariate-and-ab-testing).
- Définir la fenêtre de calcul du chiffre d'affaires pour la Campaign ou le Canvas.
- Ajuster la distribution des messages pour les campagnes et Canvas utilisant la [Sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/).

Le nombre d'événements de conversion principaux correspond au nombre d'événements de conversion survenus. Pour les campagnes multicanal, Braze comptabilise les conversions par canal (comme décrit dans les [Règles de suivi des conversions](#conversion-tracking-rules)), ce qui signifie que le nombre de conversions peut dépasser le nombre d'utilisateurs uniques et entraîner des taux de conversion supérieurs à 100 %. Braze calcule le taux de l'événement de conversion principal en divisant ce nombre par le nombre de destinataires uniques. Braze considère un utilisateur comme destinataire lorsque le message est envoyé ou affiché, selon le canal. Par exemple, pour les notifications push ou les e-mails, un utilisateur devient destinataire après l'envoi du message par Braze. Pour les messages in-app ou les Content Cards, l'utilisateur doit visualiser le message pour être considéré comme destinataire.

{% alert note %}
Si vous annulez des messages à l'aide de la balise Liquid `abort`, Braze n'annule les messages que pour les utilisateurs qui passent par les variantes. Les messages destinés aux utilisateurs du groupe de contrôle ne sont pas annulés, ce qui peut entraîner des pourcentages de conversion biaisés entre les variantes et les groupes de contrôle. Pour contourner ce problème, utilisez la [segmentation]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/) pour cibler vos utilisateurs à l'entrée de la Campaign ou du Canvas.
{% endalert %}

## Créer une Campaign avec suivi des conversions {#creating-a-campaign-with-conversion-tracking}

### Étape 1 : Configurer votre Campaign {#step-1-set-up-your-campaign}

[Créez une Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/) pour le canal de communication souhaité. Après avoir configuré les messages et la planification de votre Campaign, vous pouvez ajouter jusqu'à quatre événements de conversion pour le suivi.

Utilisez autant d'événements de conversion que nécessaire. L'ajout d'un deuxième ou troisième événement de conversion enrichit considérablement vos rapports. Par exemple, pour une Campaign ciblant les utilisateurs inactifs, l'ajout d'un événement de conversion secondaire en complément de l'événement de conversion principal **Démarrer une session** vous aide à comprendre l'efficacité de votre Campaign pour ramener les utilisateurs dans votre application.

### Étape 2 : Ajouter les événements de conversion {#step-2-add-the-conversion-events}

Commencez par sélectionner le type général d'événement que vous souhaitez utiliser :

| Type d'événement de conversion | Description |
|-------------------------|----------------------------|
| **Démarrer une session** | Un utilisateur est considéré comme converti lorsqu'il ouvre l'une des applications que vous spécifiez (par défaut, toutes les applications de l'espace de travail). |
| **Effectuer un achat** | Un utilisateur est considéré comme converti lorsqu'il enregistre un [événement d'achat]({{site.baseurl}}/api/objects_filters/purchase_object/). Cela suit tout achat par défaut, ou vous pouvez spécifier un produit particulier. |
| **Passer une commande** | Un utilisateur est considéré comme converti lorsqu'il déclenche l'[événement eCommerce recommandé Commande passée]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#ecommerce-recommended-events?tab=ecommerce.order_placed). Cela suit toute commande par défaut, ou vous pouvez filtrer par un produit spécifique.<br><br>L'événement « Passer une commande » est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé. |
| **Effectuer un événement personnalisé** | Un utilisateur est considéré comme converti lorsqu'il effectue l'un de vos événements personnalisés existants (pas de valeur par défaut, vous devez spécifier l'événement). |
| **Mettre à jour l'application** | Un utilisateur est considéré comme converti lorsqu'il met à jour la version de l'application sur l'une des applications que vous spécifiez (par défaut, toutes les applications de l'espace de travail). Braze effectue une comparaison numérique au mieux pour déterminer si le changement constitue une mise à jour. Les versions non numériques sont comptabilisées comme des conversions si la version change. |
| **Ouvrir un e-mail** | Un utilisateur est considéré comme converti lorsqu'il ouvre l'e-mail (uniquement pour les campagnes par e-mail). |
| **Cliquer dans un e-mail** | Un utilisateur est considéré comme converti lorsqu'il clique sur un lien dans l'e-mail (uniquement pour les campagnes par e-mail). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Ajouter les événements de conversion" }

{% alert important %}
**Les propriétés imbriquées ne sont pas prises en charge dans les événements de conversion**. Vous ne pouvez pas utiliser de propriétés imbriquées dans les événements de conversion. Par exemple, si `product_code` ou `product_name` sont des propriétés imbriquées dans un tableau `products` (comme `products[].product_code`), vous ne pouvez pas les utiliser pour vérifier si un achat de produit spécifique a été effectué dans un événement de conversion.
{% endalert %}

Définissez votre date limite de conversion. Il s'agit du délai maximum pouvant s'écouler avant que Braze ne considère une conversion. Vous pouvez définir une fenêtre allant jusqu'à 30 jours pendant laquelle Braze comptabilise la conversion si l'utilisateur effectue l'action spécifiée.

![Le type d'événement de conversion « Effectuer un achat » comme exemple pour enregistrer les conversions des utilisateurs qui effectuent un achat quelconque. La date limite de conversion est de 12 heures.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Après avoir sélectionné vos événements de conversion, poursuivez le processus de création de la Campaign et commencez à envoyer votre Campaign.

### Étape 3 : Consulter vos résultats {#step-3-view-your-results}

Accédez à la page **Détails** pour voir les détails de chaque événement de conversion associé à la Campaign que vous avez créée. Indépendamment des événements de conversion sélectionnés, vous pouvez également voir le chiffre d'affaires total attribué à cette Campaign spécifique, ainsi qu'aux variantes spécifiques, pendant la fenêtre de l'événement de conversion principal.

{% alert note %}
Si vous ne sélectionnez aucun événement de conversion lors de la création de la Campaign, le délai par défaut est de trois jours.
{% endalert %}

De plus, pour les messages multivariés, vous pouvez voir le nombre de conversions et les pourcentages de conversion pour votre groupe de contrôle et chaque variante.

![Quatre événements de conversion qui suivent les conversions en fonction du moment où un achat a été effectué dans les trois heures, un achat effectué dans les deux heures, une session démarrée dans les 30 minutes et une session démarrée dans les 25 minutes.]({% image_buster /assets/img_archive/conversion_event_details.png %})