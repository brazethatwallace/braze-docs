---
nav_title: Annuler des messages
article_title: Annuler des messages Liquid
page_order: 7
description: "Cet article de référence traite de l'annulation de messages Liquid et présente quelques exemples de cas d'utilisation."

---

# Annuler des messages {#abort-messages}

> Vous pouvez utiliser la balise Liquid `abort_message("optional reason for aborting")` dans des conditions pour empêcher l'envoi d'un message à un utilisateur. Cet article de référence présente quelques exemples d'utilisation de cette fonctionnalité dans des campagnes marketing.

{% alert note %}
Si une étape de message est annulée dans un Canvas, l'utilisateur **ne quittera pas** le Canvas et **passera** à l'étape suivante.
{% endalert %}

## Envois de test avec `abort_message()` {#test-sends-with-abort_message}

`abort_message()` interrompt l'envoi pour les utilisateurs qui ne remplissent pas votre condition. Le message n'apparaîtra pas sur leur profil et ne sera pas comptabilisé dans les réceptions ni dans la limite de fréquence.

Si les envois de test n'arrivent jamais, prévisualisez en tant qu'utilisateur qui satisfait la condition d'annulation, puis dans **Envoi de test**, activez **Remplacer les attributs des destinataires par ceux de l'utilisateur de prévisualisation actuel** (ou ajoutez un membre d'un groupe de test de contenu qui remplit les conditions).

## Annuler le message si « Number Games Attended » = 0 {#abort-message-if-number-games-attended-0}

Par exemple, imaginons que vous ne souhaitiez pas envoyer de message aux clients qui n'ont assisté à aucun match :

{% raw %}
```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
Loved the game? Get 10% off your second one with code SAVE10.
{% elsif custom_attribute.${Number_Game Attended} > 1 %}
Love the games? Get 10% off your next one with code SAVE10.
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

Ce message ne sera envoyé qu'aux clients dont on sait qu'ils ont assisté à un match.

## Envoyer un message uniquement aux clients anglophones {#message-english-speaking-customers-only}

Vous pouvez envoyer un message uniquement aux clients anglophones en créant une instruction « if » qui correspond lorsque la langue du client est l'anglais, et une instruction « else » qui annule le message pour toute personne qui ne parle pas anglais ou dont le profil ne comporte pas de langue.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

Par défaut, Braze enregistre un message d'erreur générique dans votre Journal d'activité des messages :

```text
{% abort_message %} called
```

Vous pouvez également faire en sorte que le message d'annulation enregistre un contenu spécifique dans votre Journal d'activité des messages en incluant une chaîne de caractères entre les parenthèses :

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![Journal d'erreur de message dans la console de développement avec un message d'annulation « language was nil ».]({% image_buster /assets/img_archive/developer_console.png %})

## Rechercher des messages d'annulation {#query-for-abort-messages}

Vous pouvez utiliser le [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder) ou votre propre entrepôt de données, s'il est connecté à Braze, pour rechercher des messages d'annulation spécifiques déclenchés lorsque la logique Liquid provoque l'annulation d'un message.

## Moment d'évaluation de la logique d'annulation {#when-abort-logic-is-evaluated}

Le moment où la logique d'annulation est évaluée dépend du canal de message.

### Push, e-mail, SMS, webhooks et Content Cards {#push-email-sms-webhooks-and-content-cards}

La logique d'annulation est évaluée au moment de l'envoi, lorsque Braze traite le message pour la distribution.

### Messages in-app {#in-app-messages}

La logique d'annulation est évaluée pour les [messages in-app modélisés]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#templated_iam-templated) uniquement au moment où le message in-app est déclenché (par exemple, lorsque l'utilisateur effectue l'événement déclencheur ou démarre une session), et non lorsque le message est initialement envoyé à l'appareil. Les messages in-app sont transmis au SDK au démarrage de la session et mis en cache localement ; le Liquid — y compris les appels `abort_message()` — est exécuté lorsque la condition de déclenchement est remplie.

## Remarques {#considerations}

La balise Liquid `abort_message()` empêche l'envoi de messages aux utilisateurs, ce qui signifie que le message ne s'affichera pas sur les profils utilisateur et ne sera pas comptabilisé dans les réceptions ni dans la limite de fréquence.