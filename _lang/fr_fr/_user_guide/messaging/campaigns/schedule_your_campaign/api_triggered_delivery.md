---
nav_title: Distribution déclenchée par API
article_title: Distribution déclenchée par API
page_order: 2
page_type: reference
description: "Cet article de référence explique comment planifier et configurer une campagne déclenchée par API."
tool: Campaigns
platform: API

---

# Distribution déclenchée par API {#api-triggered-delivery}

> Les campagnes déclenchées par API, ou campagnes déclenchées par le serveur, sont idéales pour les cas d'utilisation transactionnels plus avancés. Les campagnes Braze déclenchées par API permettent aux marketeurs de gérer le contenu des campagnes, les tests multivariés et les règles de rééligibilité depuis le tableau de bord de Braze, tout en déclenchant la distribution de ce contenu depuis leurs propres serveurs et systèmes. La requête API qui déclenche le message peut également inclure des données supplémentaires à intégrer dynamiquement dans le message en temps réel.

## Configuration d'une campagne déclenchée par API {#setting-up-an-api-triggered-campaign}

La configuration d'une campagne déclenchée par API nécessite quelques étapes. Commencez par créer une nouvelle campagne multicanale ou monocanale (avec test multivarié).

{% alert note %}
Une campagne déclenchée par API est différente d'une [campagne API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns#api-campaigns).
{% endalert %}

Ensuite, configurez votre texte et vos notifications de la même manière que pour des notifications planifiées, puis sélectionnez **API-Triggered Delivery**. Pour plus d'informations sur le déclenchement de ces campagnes depuis votre serveur, consultez cet article sur l'[envoi de campagnes déclenchées par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).

![Configurez votre texte et vos notifications de la même manière que pour des notifications planifiées, puis sélectionnez API-Triggered Delivery. Pour plus d'informations sur le déclenchement de ces campagnes depuis votre serveur, consultez l'article sur l'envoi de campagnes déclenchées par API.]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## Réduire le délai entre votre déclencheur API et l'envoi {#reducing-delay-between-your-api-trigger-and-send}

Si les messages mettent plus de temps que prévu à être envoyés après l'appel à l'endpoint de déclenchement, vérifiez si le profil utilisateur est prêt au moment du déclenchement.

Par défaut, `send_to_existing_only` est défini sur `true` dans [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns). Braze envoie uniquement aux utilisateurs existants et ne crée pas de nouveaux profils lors de cet appel. Pour créer ou mettre à jour un utilisateur et envoyer le message dans la même requête, définissez `send_to_existing_only` sur `false` et incluez un objet `attributes` pour chaque destinataire.

Pour les Campaigns par e-mail, incluez également `email` (ainsi que tout autre champ de distribution requis) dans `attributes`. Si le profil ne possède pas d'adresse e-mail au moment où vous déclenchez l'envoi, Braze effectue de nouvelles tentatives pendant environ 2 heures en attendant l'arrivée des données du profil. Inclure `email` dans le même appel permet d'éviter ce délai.

Pour consulter l'ensemble des paramètres de requête, des exemples et le comportement de nouvelle tentative, reportez-vous à [Envoyer des Campaigns déclenchées par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#recipient-limits-and-profile-creation) et à l'[objet destinataires]({{site.baseurl}}/api/objects_filters/recipient_object).

{% alert note %}
Ces recommandations s'appliquent aux Campaigns déclenchées par API (`/campaigns/trigger/send`). L'[endpoint d'e-mail transactionnel]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) utilise une structure de requête différente (`recipient`, au singulier) et ne prend pas en charge `send_to_existing_only`. Pour créer un utilisateur en ligne avec des envois transactionnels, transmettez `attributes` dans l'objet `recipient` à la place.
{% endalert %}

## Utiliser le contenu modélisé inclus dans une requête API {#using-the-templated-content-included-with-an-api-request}

En plus de déclencher le message, vous pouvez également inclure du contenu dans la requête API pour qu'il soit intégré au message via l'objet `trigger_properties`. Ce contenu peut être référencé dans le corps du message.

Utilisez exactement deux accolades par étiquette Liquid dans `trigger_properties` et dans le texte du message. Par exemple : {% raw %}`{{api_trigger_properties.${your_property}}}`.{% endraw %} Un `{` ou `}` supplémentaire est une cause fréquente d'[échecs de personnalisation déclenchée par API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/faq#why-is-my-api-triggered-liquid-failing-in-braze).

Consultez l'exemple de notification sociale suivant pour plus de contexte.

![La propriété de déclenchement mentionnée ci-dessus, incluse dans le message pour remplir automatiquement le nom de l'utilisateur, suivie du texte : « liked your photo! Click here to see what they've been up to. ».]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## Rééligibilité avec les Campaigns déclenchées par API {#re-eligibility-with-api-triggered-campaigns}

Le nombre de fois qu'un utilisateur reçoit une Campaign déclenchée par API peut être limité à l'aide des paramètres de rééligibilité. Cela signifie que l'utilisateur ne reçoit la Campaign qu'une seule fois, ou une seule fois dans une fenêtre donnée, quel que soit le nombre de fois où le déclencheur API est activé.

Par exemple, imaginons que vous utilisez une Campaign déclenchée par API pour envoyer à l'utilisateur un message à propos d'un article qu'il a récemment consulté. Dans ce cas, vous pouvez limiter la Campaign à l'envoi d'un maximum d'un message par jour, quel que soit le nombre d'articles consultés, tout en activant le déclencheur API pour chaque article. Si votre Campaign déclenchée par API est transactionnelle, assurez-vous que l'utilisateur reçoit la Campaign à chaque transaction en définissant le délai à zéro minute.

![Capture d'écran relative à la rééligibilité avec les Campaigns déclenchées par API.]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})