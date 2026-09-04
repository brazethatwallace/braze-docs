---
nav_title: Annuler des messages
article_title: Annuler des messages Liquid
page_order: 7
description: "Cet article de référence traite de l'annulation de messages Liquid et présente quelques exemples de cas d'usage."

---

# Annuler des messages {#abort-messages}

> Vous pouvez utiliser la balise Liquid `abort_message("optional reason for aborting")` dans des conditions pour empêcher l'envoi d'un message à un utilisateur. Cet article de référence présente quelques exemples d'utilisation de cette fonctionnalité dans des campagnes marketing.

{% alert note %}
Si une étape de message est annulée dans un Canvas, l'utilisateur **ne quittera pas** le Canvas et **passera** à l'étape suivante.
{% endalert %}

## Envois test avec `abort_message()` {#test-sends-with-abort_message}

`abort_message()` empêche l'envoi pour les utilisateurs qui ne remplissent pas votre condition. Le message n'apparaîtra pas sur leur profil et ne sera pas comptabilisé dans les réceptions ni dans la limite de fréquence.

Si les envois test n'arrivent jamais, prévisualisez en tant qu'utilisateur qui satisfait la condition d'abandon, puis dans **Test Send** activez **Override recipients' attributes with current preview user's attributes** (ou ajoutez un membre d'un groupe de test de contenu qui remplit les critères).

## Abandonner le message si « Number Games Attended » = 0 {#abort-message-if-number-games-attended-0}

Par exemple, supposons que vous ne souhaitiez pas envoyer de message aux clients qui n'ont pas assisté à un match :

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

Ce message sera envoyé uniquement aux clients qui sont connus pour avoir assisté à un match.

## Envoyer des messages uniquement aux clients anglophones {#message-english-speaking-customers-only}

Vous pouvez envoyer des messages uniquement aux clients anglophones en créant une instruction « if » qui correspondra lorsque la langue d'un client est l'anglais, et une instruction « else » qui interrompra le message pour toute personne ne parlant pas anglais ou n'ayant pas de langue définie dans son profil.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

Par défaut, Braze enregistrera un message d'erreur générique dans votre journal d'activité des messages :

```text
{% abort_message %} called
```

Vous pouvez également faire en sorte que le message d'interruption enregistre un élément dans votre journal d'activité des messages en incluant une chaîne de caractères entre les parenthèses :

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![Journal d'erreurs de messages dans la console de développement avec un message d'interruption indiquant « language was nil ».]({% image_buster /assets/img_archive/developer_console.png %})

## Requête pour les messages d'abandon {#query-for-abort-messages}

Vous pouvez utiliser le [générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder) ou votre propre entrepôt de données, s'il est connecté à Braze, pour rechercher des messages d'abandon spécifiques qui sont déclenchés lorsque la logique Liquid provoque l'abandon d'un message.

## Quand la logique d'abandon est évaluée {#when-abort-logic-is-evaluated}

Le moment où la logique d'abandon est évaluée dépend du canal de message.

### Notifications push, e-mail, SMS, webhooks et Content Cards {#push-email-sms-webhooks-and-content-cards}

La logique d'abandon est évaluée au moment de l'envoi, lorsque Braze traite le message pour la distribution.

### Messages in-app {#in-app-messages}

La logique d'abandon est évaluée pour les [messages in-app modélisés]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#templated_iam-templated) uniquement au moment où le message in-app est déclenché (par exemple, lorsque l'utilisateur effectue l'événement déclencheur ou démarre une session), et non lorsque le message est initialement envoyé à l'appareil. Les messages in-app sont transmis au SDK au démarrage de la session et mis en cache localement ; le Liquid, y compris les appels à `abort_message()`, est exécuté lorsque la condition de déclenchement est remplie.

## Résolution des problèmes de taux d'abandon élevés {#troubleshooting-high-abort-rates}

Si une campagne ou une étape Canvas montre que de nombreux utilisateurs sont entrés mais que peu d'envois ont été effectués, ou si les réceptions semblent inférieures aux attentes, la logique d'abandon est une cause fréquente, en particulier lorsque Liquid nécessite des attributs, des données de catalogue ou des valeurs de liste qui sont absents au moment de l'évaluation.

### Vérifier le journal d'activité des messages {#check-the-message-activity-log}

1. Dans le tableau de bord de Braze, ouvrez le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) pour la Campaign ou l'étape de message Canvas.
2. Filtrez les entrées liées aux abandons. Par défaut, Braze consigne les appels à {% raw %}`{% abort_message %}`{% endraw %}. Si vous avez transmis une chaîne de caractères de motif à `abort_message()`, ce texte apparaît à la place.
3. Notez si les abandons se concentrent sur un seul canal (par exemple uniquement l'e-mail) ou sur plusieurs canaux au sein du même Canvas.

### Vérifier les attributs et le Liquid au moment de l'envoi {#verify-attributes-and-liquid-at-send-time}

Pour les notifications push, les e-mails, les SMS, les webhooks et les Content Cards, la logique d'abandon s'exécute lorsque Braze traite le message pour la réception, et non lorsque l'utilisateur est entré dans un Canvas ou lorsqu'un événement déclencheur s'est produit précédemment.

- Confirmez que les [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), les propriétés d'événement ou les champs de [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs) requis sont définis sur l'utilisateur avant l'exécution de l'étape de message.
- Ajoutez des vérifications explicites de valeurs nil ou vides avant d'appeler `abort_message()`. Une branche `else` qui abandonne lorsqu'une valeur est manquante bloque l'envoi pour tout utilisateur ne disposant pas de cette donnée.
- Si la personnalisation dépend d'une liste, d'un Segment ou d'une réponse de contenu connecté, confirmez que les données sont disponibles au moment de l'exécution de l'étape de message. Un utilisateur peut entrer dans un Canvas avant que l'appartenance à une liste ou les données en aval ne soient prêtes.

### Comportement spécifique à Canvas {#canvas-specific-behavior}

Si une étape de message est abandonnée dans un Canvas, l'utilisateur ne quitte pas le Canvas. Il passe à l'étape suivante. Les abandons n'affectent que le nombre d'envois de cette étape de message.

Lors du diagnostic des abandons Canvas :

- Comparez les utilisateurs entrés dans l'étape de message aux utilisateurs ayant reçu un envoi sur la même étape.
- Si un seul canal est abandonné, vérifiez le Liquid spécifique au canal ou le statut d'abonnement pour cette étape.
- Si les abandons augmentent soudainement après une mise à jour de liste ou de catalogue, vérifiez si l'étape de message s'est exécutée avant la fin de la mise à jour.

### Valider avec l'aperçu et les envois de test {#validate-with-preview-and-test-sends}

Affichez l'aperçu en tant qu'utilisateur dans le composeur de messages dont le profil correspond à un destinataire concerné. Pour les envois de test, activez **Remplacer les attributs des destinataires par ceux de l'utilisateur en aperçu** lorsque votre logique d'abandon dépend des données du profil.

Pour plus d'exemples d'abandon, consultez [Rechercher les messages d'abandon](#query-for-abort-messages).

## Considérations {#considerations}

La balise de message Liquid `abort_message()` empêche l'envoi de messages aux utilisateurs, ce qui signifie que le message ne s'affichera pas sur les profils utilisateur et ne sera pas comptabilisé dans les réceptions ni dans la limite de fréquence.