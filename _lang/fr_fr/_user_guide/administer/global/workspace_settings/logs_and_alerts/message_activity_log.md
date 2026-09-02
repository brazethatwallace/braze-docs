---
nav_title: Journal d'activité des messages
article_title: "Journal d'activité des messages {#dev-console-troubleshooting}"
page_order: 3
page_type: reference
description: "Cet article de référence décrit le journal d'activité des messages, qui affiche les messages associés à vos campagnes et envois. Vous y trouverez également des informations utiles."
---

# Journal d'activité des messages {#dev-console-troubleshooting}

> Le **Journal d'activité des messages** vous permet de consulter tous les messages (en particulier les messages d'erreur) associés à vos campagnes et envois.

Vous pouvez visualiser les transactions de Campaigns API, résoudre les problèmes liés aux messages en échec et obtenir des informations pour améliorer la distribution des notifications ou résoudre des problèmes techniques existants.

Pour accéder au journal, rendez-vous dans **Paramètres** > **Configuration et test** > **Journal d'activité des messages**.

![Journal d'activité des messages]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
En complément de cet article, nous vous recommandons également de consulter notre cours d'apprentissage Braze [Outils d'assurance qualité et de débogage](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), qui explique comment utiliser le journal d'activité des messages pour effectuer votre propre résolution de problèmes et débogage.
{% endalert %}

Vous pouvez filtrer par les contenus suivants enregistrés dans le **Journal d'activité des messages** :

- Erreurs de notification push
- Erreurs de messages in-app modélisés abandonnés
- Erreurs de webhook
- Erreurs d'e-mail
- Enregistrements de messages API
- Erreurs de contenu connecté
- Erreurs d'audience connectée via la REST API
- Erreurs d'aliasing de l'utilisateur
- Erreurs de test A/B
- Erreurs SMS/MMS
- Erreurs WhatsApp
- Erreurs de en direct or en ligne/en production/instantané Activity
- Erreurs de déclencheur utilisateur incorrect
- Erreurs de [limite d'invocations quotidiennes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#monitor-your-agent) de Braze Agents
- Erreurs de [modèle]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) indisponible de Braze Agents

Ces messages peuvent provenir de notre propre système, de vos applications ou plateformes, ou de nos partenaires tiers. Cela peut entraîner un nombre infini de messages susceptibles d'apparaître dans ce journal.

## Comprendre les messages du journal {#understanding-log-messages}

Pour déterminer la signification de vos messages, prêtez attention à la formulation de chaque message et aux colonnes qui lui correspondent, car cela peut vous aider à résoudre les problèmes grâce aux indices contextuels.

Par exemple, les entrées **Aborted Message Error** peuvent survenir pour de nombreuses raisons, pas seulement les [messages d'abandon Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages). Consultez la colonne **Message** pour connaître la raison spécifique :

- Si l'envoi a été abandonné par une balise Liquid `abort_message`, la colonne **Message** affiche l'extrait Liquid exact qui a été appelé, par exemple {% raw %}`{% abort_message('Module count is less than or equal to 1') %} called`{% endraw %}.
- Pour les autres raisons d'abandon, la colonne **Message** explique pourquoi l'envoi a été annulé.

### Payloads des Campaigns API {#api-campaign-payloads}

Le journal d'activité des messages enregistre des informations différentes selon le type de Campaign API. L'[endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) enregistre le corps du message (messages) dans les enregistrements de messages API, tandis que l'[endpoint `/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) n'enregistre pas le payload de la requête ni les `api_trigger_properties` dans le journal d'activité des messages.

### Messages courants {#common-messages}

Il existe certains types de messages courants que vous pourriez voir, et certains d'entre eux peuvent même fournir des liens de résolution des problèmes pour vous aider à diagnostiquer et corriger les problèmes.

Les messages suivants sont fournis à titre d'exemple et peuvent ne pas correspondre exactement à ce qui est affiché dans la colonne **Message** de votre journal.

| Type de message | Message potentiel | Description |
|---|---|---|
| Échec provisoire d'envoi | The email address same@example.com soft bounced. | L'adresse e-mail était valide et le message a atteint le serveur de messagerie du destinataire, mais a été rejeté pour un problème « temporaire ». <br><br>Les raisons courantes d'un échec provisoire d'envoi sont les suivantes : {::nomarkdown} <ul> <li> La boîte de réception était pleine (l'utilisateur a dépassé son quota) </li> <li> Le serveur était hors service </li> <li> Le message était trop volumineux pour la boîte de réception du destinataire </li>  </ul> {:/} Si un e-mail a subi un échec provisoire d'envoi, nous réessayons généralement dans un délai de 72 heures, mais le nombre de tentatives varie d'un destinataire à l'autre. |
| Échec d'envoi définitif | The email account that you tried to reach does not exist. Try double-checking the recipient's email address for typos or unnecessary spaces. | Votre message n'a jamais atteint la boîte de réception de cette personne car il n'y avait pas de boîte de réception à atteindre. Si vous souhaitez approfondir vos recherches, des messages comme celui-ci peuvent parfois contenir des liens dans la colonne **View Details** qui vous permettent de consulter le profil du destinataire prévu.|
| Blocage | Spam message is rejected because of anti-spam policy. | Votre message a été catégorisé comme spam. Cette erreur de messagerie est enregistrée pour un utilisateur si nous avons reçu un événement du fournisseur de services Internet indiquant que l'e-mail a été rejeté. Il peut s'agir uniquement du destinataire prévu, mais si vous voyez ce message fréquemment, vous devriez réévaluer vos habitudes d'envoi ou le contenu de votre message. Pensez-y également : avez-vous [préchauffé votre IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) ? Si ce n'est pas le cas, contactez Braze pour obtenir des conseils à ce sujet.|
| Aborted Message Error | {% raw %}`{% abort_message('Module count is less than or equal to 1') %} called`{% endraw %} | Lorsqu'un envoi est abandonné par une balise Liquid `abort_message`, la colonne **Message** affiche l'extrait Liquid exact qui a été appelé. D'autres entrées **Aborted Message Error** peuvent contenir des messages différents décrivant la raison de l'abandon. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messages courants" }

### Pourquoi mon message ne figure-t-il pas ici ? {#why-isnt-my-message-listed-here}

Les messages du journal d'activité des messages peuvent provenir de diverses sources : Braze, vos applications ou plateformes, ou nos partenaires tiers. Cela signifie qu'il existe un nombre infini de messages susceptibles d'apparaître dans ce journal. Comme vous pouvez l'imaginer, nous ne pouvons pas tous les répertorier !

Par exemple, certains messages de « Blocage » potentiels, en plus de celui répertorié dans le tableau précédent, pourraient être :

- Unfortunately, messages from [_IP_ADDRESS_] weren't sent. Please contact your Internet Service provider since part of their network is on our block list.
- Message rejected due to local policy.
- The message was blocked by the receiver as spam.
- Service unavailable, Client host [_IP_ADDRESS_] blocked using Spamhaus.

## Période de conservation du stockage {#storage-retention-period}

Les erreurs des 60 dernières heures sont disponibles dans les journaux d'activité des messages. Les journaux de plus de 60 heures sont nettoyés et ne sont plus accessibles.

### Nombre de journaux d'erreurs stockés {#number-of-error-logs-stored}

Le nombre de journaux enregistrés est influencé par plusieurs conditions. Par exemple, si une Campaign planifiée est envoyée à des milliers d'utilisateurs, nous pourrions potentiellement voir un échantillon des erreurs dans le journal d'activité des messages au lieu de toutes les erreurs. Voici un aperçu des conditions qui affectent le nombre de journaux enregistrés :
- Jusqu'à 20 journaux d'erreurs du même type d'erreur sont enregistrés pour la même Campaign ou étape du Canvas au cours d'une heure fixe pour les types d'erreurs suivants :
    - Erreurs de contenu connecté
    - Erreurs d'abandon de message
    - Erreurs de webhook
    - Erreurs de rejet SMS
    - Erreurs d'échec de distribution SMS
    - Erreurs d'échec WhatsApp
    - Erreurs de test A/B
- Jusqu'à 20 journaux d'erreurs de notification push du même type d'erreur sont enregistrés pour la même Campaign ou étape du Canvas et combinaison d'application pour les types d'erreurs suivants :
    - Identifiants push invalides
    - Jeton push invalide
    - Aucun identifiant push
    - Erreurs de jeton
    - Quota dépassé
    - Délai de nouvelle tentative expiré
    - Payload invalide
    - Erreur inattendue
- Jusqu'à 100 journaux d'erreurs du même type d'erreur sont enregistrés pour la même application au cours d'une heure fixe pour les types d'erreurs suivants :
    - Erreur en direct or en ligne/en production/instantané Activity (aucun identifiant push)
    - Erreur en direct or en ligne/en production/instantané Activity (identifiant push invalide)
    - Autres erreurs en direct or en ligne/en production/instantané Activity
    - Erreurs de jeton supprimé par retour APNS
- Jusqu'à 100 journaux d'erreurs du même type d'erreur sont enregistrés pour la même Campaign ou étape du Canvas au cours d'une heure fixe pour les types d'erreurs suivants :
    - Erreurs d'échec provisoire d'envoi d'e-mail
    - Erreurs d'échec d'envoi définitif d'e-mail
    - Erreurs de blocage d'e-mail
- Jusqu'à 100 journaux d'erreurs d'aliasing de l'utilisateur sont enregistrés pour le même espace de travail au cours d'une heure fixe.

## Envois de test {#test-sends}

Le **Journal d'activité des messages** affiche les journaux de test pour les canaux de communication suivants :

- SMS
- WhatsApp
- LINE
- KakaoTalk
- Webhook

Les journaux d'envois de test ne sont pas disponibles pour les canaux suivants : e-mail, Content Cards, messages in-app et notifications push.

Les journaux d'envois de test sont préfixés par « [TEST SEND] », mais il n'est pas garanti que tous les journaux d'envois de test comportent ce préfixe (par exemple, les erreurs de contenu connecté n'ont pas ce préfixe).