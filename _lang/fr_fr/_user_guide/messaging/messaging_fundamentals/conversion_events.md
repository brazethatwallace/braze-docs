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

## Fonctionnement {#how-it-works}

Pour une campagne personnalisée de fêtes ciblant les utilisateurs actifs, un événement de conversion de type **Démarrer une session** dans un délai de deux ou trois jours peut être approprié, car il vous permet d'évaluer l'engagement des utilisateurs suite à la réception de votre message. Vous pouvez également sélectionner des événements supplémentaires comme **Passer une commande**, **Mettre à jour l'application**, ou l'un de vos événements personnalisés comme événements de conversion.

### Quand le suivi des conversions commence-t-il ? {#when-does-conversion-tracking-begin}

{% tabs %}
{% tab Campaign %}

Le suivi des conversions commence lorsqu'un utilisateur reçoit la campagne ou entre dans le groupe de contrôle de la campagne. La réception d'un message et l'attribution à une variante se produisent généralement en même temps. Pour les campagnes de messages in-app, le suivi des conversions commence lorsque Braze enregistre une impression.

{% endtab %}
{% tab Canvas %}

Le suivi des conversions commence lorsqu'un utilisateur entre dans le Canvas. Pour les étapes du Canvas, les conversions sont attribuées tant que l'utilisateur est actif dans cette étape. Lorsque l'utilisateur passe à une autre étape, le suivi des conversions s'arrête pour l'étape précédente et commence pour l'étape suivante.

Lorsqu'un utilisateur se trouve dans une étape de délai ou une autre étape sans message, les conversions qui se produisent pendant cette attente sont toujours attribuées à la dernière étape de message reçue, jusqu'à ce que l'utilisateur reçoive une autre étape de message. Après que l'utilisateur a reçu la dernière étape de message dans son parcours, les conversions peuvent encore être enregistrées jusqu'à la date limite de conversion (comptée à partir de l'entrée dans le Canvas), même s'il n'y a plus d'étapes de message ultérieures.

{% endtab %}
{% endtabs %}

{% alert tip %}
Pour en savoir plus sur les conversions, consultez notre [cours d'apprentissage Braze](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sur la configuration des campagnes.
{% endalert %}

### Règles de suivi des conversions {#conversion-tracking-rules}

Les événements de conversion attribuent les actions des utilisateurs à un point d'engagement. En général, tant qu'une fenêtre de conversion est ouverte, un utilisateur effectue au maximum une conversion par événement de conversion pour cette campagne ou ce Canvas. S'il effectue la même action de conversion plus d'une fois avant la date limite (par exemple, deux achats), Braze ne comptabilise qu'une seule conversion pour cet événement. Les campagnes multicanales peuvent enregistrer une opportunité de conversion distincte pour chaque canal de communication, ce qui peut produire des taux de conversion supérieurs à 100 % lorsque vous comparez le nombre de conversions avec le nombre de destinataires uniques (comme décrit dans les points suivants).

Notez les points suivants concernant la façon dont Braze gère les conversions multiples :

- **Campagnes monocanales :** les conversions sont comptabilisées par utilisateur, et non par appareil. Au sein d'un même canal, un utilisateur ne se convertit qu'une seule fois par événement de conversion, même si un message est envoyé à plusieurs appareils. Par exemple, si une campagne n'a qu'un seul événement de conversion défini sur « Effectue un achat » et qu'un utilisateur effectue deux achats distincts avant la date limite de conversion, Braze ne comptabilise qu'une seule conversion. Cependant, lorsque la [rééligibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) est activée, les utilisateurs qui reçoivent la campagne plusieurs fois peuvent se convertir à nouveau à chaque envoi. Dans les campagnes avec rééligibilité, le mécanisme de conversion est d'une fois par utilisateur par envoi de campagne, ce qui peut entraîner des nombres de conversions plus élevés lorsque les utilisateurs reçoivent et se convertissent à partir de la même campagne plusieurs fois.
- **Campagnes multicanales :** pour les campagnes multicanales, chaque canal dispose de sa propre opportunité de conversion. Un utilisateur peut se convertir une fois par canal après avoir reçu un message sur ce canal. Cela signifie que si un utilisateur reçoit des messages sur plusieurs canaux (par exemple, e-mail et notification push) et effectue l'action de conversion, Braze comptabilise une conversion pour chaque canal, ce qui peut entraîner des taux de conversion supérieurs à 100 %.
- **Étapes de message Canvas :** Braze attribue les conversions qui se produisent dans la fenêtre de conversion à la dernière étape de message Canvas que l'utilisateur a reçue. Après avoir reçu l'étape de message suivante, l'attribution passe à cette étape. Braze mesure cette fenêtre à partir du moment où l'utilisateur entre dans le Canvas, et non à partir de chaque message individuellement. Les conversions qui se produisent pendant les délais entre les étapes de message sont comptabilisées dans l'attribution de l'étape de message précédente jusqu'à ce que l'utilisateur avance ; les conversions après la dernière étape de message sont toujours comptabilisées jusqu'à la date limite de conversion du Canvas.
- **Rétention historique des événements :** le suivi des conversions sur les tableaux de bord des campagnes et Canvas mesure les actions historiques, et non les profils utilisateurs actuels. Lorsqu'un utilisateur remplit une règle de conversion dans la fenêtre désignée, Braze enregistre une conversion dans les analyses et ne la supprime pas, même si le profil de cet utilisateur est ultérieurement supprimé, fusionné ou archivé lors d'opérations de routine d'hygiène des données ou de conformité RGPD. Les comptages de Segments en direct peuvent naturellement être inférieurs à vos journaux d'événements permanents du tableau de bord, car les segments dynamiques ne filtrent que les profils actifs qui existent actuellement dans la base de données.
- Si un utilisateur effectue un événement de conversion dans les fenêtres de conversion de deux campagnes ou Canvas distincts qu'il a reçus, la conversion est enregistrée sur les deux.
- Un utilisateur est considéré comme converti s'il a effectué l'événement de conversion spécifique dans la fenêtre, même s'il n'a pas ouvert ou cliqué sur le message.

### Événement de conversion principal {#primary-conversion-event}

L'événement de conversion principal est le premier événement que vous ajoutez lors de la création d'une campagne ou d'un Canvas. Cet événement a la plus grande incidence sur votre engagement et vos rapports. Braze utilise votre événement de conversion principal pour :

- Sélectionner la variante de message la plus performante dans les [campagnes multivariantes]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) ou les Canvas.
- Déterminer la fenêtre pendant laquelle le chiffre d'affaires est calculé pour la campagne ou le Canvas.
- Ajuster les distributions de messages pour les campagnes et les Canvas en utilisant [Optimiser avec BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

Le nombre d'événements de conversion principaux correspond au nombre d'événements de conversion qui se sont produits. Pour les campagnes multicanales, Braze comptabilise les conversions par canal (comme décrit dans les [Règles de suivi des conversions](#conversion-tracking-rules)), ce qui signifie que le nombre de conversions peut dépasser le nombre d'utilisateurs uniques et entraîner des taux de conversion supérieurs à 100 %. Braze calcule le taux d'événement de conversion principal en divisant ce nombre par le nombre de destinataires uniques. Braze considère qu'un utilisateur est un destinataire lorsque le message est envoyé ou affiché, selon le canal. Par exemple, pour les notifications push ou les e-mails, un utilisateur devient destinataire après que Braze a envoyé le message. Pour les messages in-app ou les Content Cards, l'utilisateur doit visualiser le message pour être considéré comme destinataire.

{% alert note %}
Si vous annulez des messages en utilisant la balise Liquid `abort`, Braze n'annule les messages que pour les utilisateurs qui passent par les variantes. Les messages destinés aux utilisateurs du groupe de contrôle ne sont pas annulés, ce qui peut entraîner des pourcentages de conversion biaisés entre les variantes et les groupes de contrôle. Pour contourner ce problème, utilisez la [segmentation]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) pour cibler vos utilisateurs à l'entrée de la campagne et du Canvas.
{% endalert %}

## Créer une campagne avec suivi des conversions {#creating-a-campaign-with-conversion-tracking}

### Étape 1 : Configurer votre campagne {#step-1-set-up-your-campaign}

[Créez une campagne]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign) pour le canal de communication souhaité. Après avoir configuré les messages et la planification de votre campagne, vous pouvez ajouter jusqu'à quatre événements de conversion pour le suivi.

Utilisez autant d'événements de conversion que nécessaire. L'ajout d'un deuxième ou troisième événement de conversion enrichit considérablement vos rapports. Par exemple, pour une campagne ciblant les utilisateurs en perte d'engagement, l'ajout d'un événement de conversion secondaire en complément de l'événement de conversion principal **Starts Session** vous aide à comprendre l'efficacité de votre campagne pour ramener les utilisateurs dans votre application.

### Étape 2 : Ajouter les événements de conversion {#step-2-add-the-conversion-events}

Commencez par sélectionner le type général d'événement que vous souhaitez utiliser :

| Type d'événement de conversion | Description |
|-------------------------|----------------------------|
| **Starts Session** | Un utilisateur est comptabilisé comme ayant converti lorsqu'il ouvre l'une des applications que vous spécifiez (par défaut, toutes les applications de l'espace de travail). |
| **Makes Purchase** | Un utilisateur est comptabilisé comme ayant converti lorsqu'il enregistre un [événement d'achat]({{site.baseurl}}/api/objects_filters/purchase_object). Cela suit tout achat par défaut, mais vous pouvez spécifier un produit particulier. |
| **Places Order** | Un utilisateur est comptabilisé comme ayant converti lorsqu'il déclenche l'[événement recommandé eCommerce Order Placed]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#ecommerce-recommended-events?tab=ecommerce.order_placed). Cela suit toute commande par défaut, mais vous pouvez filtrer par produit spécifique.<br><br>L'événement « Places Order » est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé. |
| **Performs Custom Event** | Un utilisateur est comptabilisé comme ayant converti lorsqu'il effectue l'un de vos événements personnalisés existants (pas de valeur par défaut, vous devez spécifier l'événement). |
| **Upgrade App** | Un utilisateur est comptabilisé comme ayant converti lorsqu'il met à jour la version de l'application sur l'une des applications que vous spécifiez (par défaut, toutes les applications de l'espace de travail). Braze effectue une comparaison numérique au mieux pour déterminer si le changement était une mise à jour. Les versions non numériques sont comptabilisées comme des conversions si la version change. |
| **Opens email** | Un utilisateur est comptabilisé comme ayant converti lorsqu'il ouvre l'e-mail (uniquement pour les campagnes par e-mail). |
| **Clicks email** | Un utilisateur est comptabilisé comme ayant converti lorsqu'il clique sur un lien dans l'e-mail (uniquement pour les campagnes par e-mail). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Ajouter les événements de conversion" }

{% alert important %}
**Les propriétés imbriquées ne sont pas prises en charge dans les événements de conversion**. Vous ne pouvez pas utiliser de propriétés imbriquées dans les événements de conversion. Par exemple, si `product_code` ou `product_name` sont des propriétés imbriquées au sein d'un tableau `products` (comme `products[].product_code`), vous ne pouvez pas les utiliser pour vérifier si un achat de produit spécifique a été effectué dans un événement de conversion.
{% endalert %}

Définissez votre délai de conversion. Il s'agit du temps maximum pouvant s'écouler avant que Braze considère une conversion. Vous pouvez définir une fenêtre allant jusqu'à 30 jours pendant laquelle Braze comptabilise la conversion si l'utilisateur effectue l'action spécifiée.

![Le type d'événement de conversion « Makes Purchase » comme exemple pour enregistrer les conversions des utilisateurs qui effectuent un achat. Le délai de conversion est de 12 heures.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Après avoir sélectionné vos événements de conversion, poursuivez le processus de création de la campagne et commencez à envoyer votre campagne.

### Étape 3 : Consulter vos résultats {#step-3-view-your-results}

Accédez à la page **Details** pour afficher les détails de chaque événement de conversion associé à la campagne que vous avez créée. Quels que soient les événements de conversion sélectionnés, vous pouvez également voir le chiffre d'affaires total attribué à cette campagne spécifique, ainsi qu'aux variantes spécifiques, pendant la fenêtre de l'événement de conversion principal.

{% alert note %}
Si vous ne sélectionnez aucun événement de conversion lors de la création de la campagne, le délai est par défaut de trois jours.
{% endalert %}

De plus, pour les messages multivariés, vous pouvez voir le nombre de conversions et les pourcentages de conversion pour votre groupe de contrôle et chaque variante.

![Quatre événements de conversion qui suivent les conversions en fonction du moment où un achat a été effectué dans les trois heures, un achat effectué dans les deux heures, une session démarrée dans les 30 minutes et une session démarrée dans les 25 minutes.]({% image_buster /assets/img_archive/conversion_event_details.png %})

## Taux de conversion des étapes Canvas et des variantes {#canvas-step-versus-variant-conversion-rates}

Il est courant que le nombre total de conversions d'une variante du Canvas soit supérieur à la somme des conversions de ses étapes individuelles. Cela s'explique par le fait que les conversions sont comptabilisées différemment au niveau de la variante et au niveau de l'étape :

- Les conversions de variante sont comptabilisées dès que l'utilisateur entre dans la variante.
- Les conversions d'étape ne sont comptabilisées qu'après l'envoi du message de l'étape à l'utilisateur.

Cela signifie que tout utilisateur qui entre dans le Canvas et effectue l'événement de conversion avant de recevoir une étape est comptabilisé dans le total de la variante, mais pas dans celui d'une étape.

Les scénarios suivants peuvent également provoquer cet écart :

- **L'utilisateur quitte le Canvas avant de recevoir une étape.** Si un utilisateur entre dans le Canvas mais en sort (par exemple, en raison d'un filtre ou d'une incompatibilité d'audience) avant l'envoi d'un message, une conversion qu'il effectue est tout de même comptabilisée au niveau de la variante, mais pas au niveau d'une étape.
- **L'étape cible un sous-ensemble d'utilisateurs.** Si une étape est configurée pour n'envoyer qu'à une plateforme spécifique (comme le mobile), les utilisateurs sur d'autres plateformes (comme le web) peuvent toujours entrer dans le Canvas et convertir. Comme ces utilisateurs ne reçoivent jamais le message de l'étape, la conversion n'est pas comptabilisée au niveau de l'étape — uniquement au niveau de la variante.

Pour en savoir plus sur l'analytique Canvas, consultez [Mesurer et tester avec l'analytique Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).