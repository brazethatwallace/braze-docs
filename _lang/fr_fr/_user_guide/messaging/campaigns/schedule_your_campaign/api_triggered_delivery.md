---
nav_title: Distribution déclenchée par API
article_title: Distribution déclenchée par API
page_order: 2
page_type: reference
description: "Cet article de référence explique comment planifier et configurer une campagne déclenchée par API."
tool: Campaigns
platform: API

---

# Distribution déclenchée par API

> Les campagnes déclenchées par API, ou campagnes déclenchées par le serveur, sont idéales pour les cas d'utilisation transactionnels plus avancés. Les campagnes Braze déclenchées par API permettent aux marketeurs de gérer le contenu des campagnes, les tests multivariés et les règles de rééligibilité depuis le tableau de bord de Braze, tout en déclenchant la distribution de ce contenu depuis leurs propres serveurs et systèmes. La requête API qui déclenche le message peut également inclure des données supplémentaires à intégrer dynamiquement dans le message en temps réel.

## Configurer une campagne déclenchée par API

La configuration d'une campagne déclenchée par API se fait en quelques étapes. Commencez par créer une nouvelle campagne multicanale ou monocanale (avec test multivarié).

{% alert note %}
Une campagne déclenchée par API est différente d'une [campagne API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns).
{% endalert %}

Ensuite, configurez votre contenu et vos notifications de la même manière que pour des notifications planifiées, puis sélectionnez **API-Triggered Delivery**. Pour en savoir plus sur le déclenchement de ces campagnes depuis votre serveur, consultez cet article sur l'[envoi de campagnes déclenchées par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).

![]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## Utiliser le contenu modélisé inclus dans une requête API

En plus de déclencher le message, vous pouvez également inclure du contenu dans la requête API pour qu'il soit intégré au message via l'objet `trigger_properties`. Ce contenu peut être référencé dans le corps du message. Par exemple, vous pouvez inclure :
``{% raw %} {{ api_trigger_properties.${ some_value_included_with_request }}} {% endraw %}``. Consultez l'exemple de notification sociale ci-dessous pour plus de contexte :

![La propriété de déclenchement mentionnée ci-dessus, incluse dans le message pour remplir automatiquement le nom de l'utilisateur, suivie du texte : « liked your photo! Click here to see what they've been up to. ».]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## Rééligibilité pour les campagnes déclenchées par API

Le nombre de fois qu'un utilisateur reçoit une campagne déclenchée par API peut être limité grâce aux paramètres de rééligibilité. Cela signifie que l'utilisateur ne recevra la campagne qu'une seule fois, ou une seule fois dans une période donnée, quel que soit le nombre de fois où le déclencheur API est activé.

Par exemple, imaginons que vous utilisez une campagne déclenchée par API pour envoyer à l'utilisateur un message concernant un article qu'il a récemment consulté. Dans ce cas, vous pouvez limiter la campagne à l'envoi d'un maximum d'un message par jour, quel que soit le nombre d'articles consultés, tout en activant le déclencheur API pour chaque article. En revanche, si votre campagne déclenchée par API est transactionnelle, vous voudrez vous assurer que l'utilisateur reçoit la campagne à chaque transaction en définissant le délai à zéro minute.

![]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})