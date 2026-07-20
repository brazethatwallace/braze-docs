---
nav_title: Journal d'activité des messages
article_title: Journal d'activité des messages
page_order: 3
page_type: reference
description: "Cet article de référence décrit le journal d'activité des messages, qui affiche les messages associés à vos campagnes et envois. Vous y trouverez également des informations sur la manière de comprendre les messages du journal."

---

# Journal d'activité des messages {#dev-console-troubleshooting}

> Le **Journal d'activité des messages** vous permet de consulter tous les messages (en particulier les messages d'erreur) associés à vos campagnes et envois.

Vous pouvez visualiser les transactions de Campaigns API, résoudre les problèmes liés aux messages en échec et obtenir des informations pour améliorer la distribution des notifications ou résoudre des problèmes techniques existants.

Pour accéder au journal, rendez-vous dans **Paramètres** > **Journal d'activité des messages**.

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
- Erreurs de Live Activity
- Erreurs de déclencheur utilisateur incorrect
- Erreurs de [limite d'invocations quotidiennes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#monitor-your-agent) de Braze Agents
- Erreurs de [modèle]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) indisponible de Braze Agents

Ces messages peuvent provenir de notre propre système, de vos applications ou plateformes, ou de nos partenaires tiers. Cela peut entraîner un nombre infini de messages susceptibles d'apparaître dans ce journal.

## Comprendre les messages du journal {#understanding-log-messages}

Pour déterminer la signification de vos messages, prêtez attention à la formulation de chaque message et aux colonnes correspondantes, car cela peut vous aider à résoudre les problèmes grâce aux indices contextuels.

Par exemple, les entrées **Erreur de message abandonné** peuvent survenir pour de nombreuses raisons, pas uniquement les [messages d'abandon Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages). Consultez la colonne **Message** pour connaître la raison spécifique :

- Si l'envoi a été abandonné par une balise Liquid `abort_message`, la colonne **Message** affiche l'extrait Liquid exact qui a été appelé, par exemple {% raw %}`{% abort_message('Module count is less than or equal to 1') %} called`{% endraw %}.
- Pour les autres raisons d'abandon, la colonne **Message** explique pourquoi l'envoi a été abandonné.

### Payloads de Campaigns API {#api-campaign-payloads}

Le journal d'activité des messages enregistre des informations différentes selon le type de Campaign API. L'[endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) enregistre le corps du message (messages) dans les enregistrements de messages API, tandis que l'[endpoint `/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) n'enregistre pas le payload de la requête ni les `api_trigger_properties` dans le journal d'activité des messages.

### Messages courants {#common-messages}

Il existe certains types de messages courants que vous pourriez rencontrer, et certains peuvent même fournir des liens de résolution de problèmes pour vous aider à diagnostiquer et corriger les problèmes.

Les messages suivants sont donnés à titre d'exemple et peuvent ne pas correspondre exactement à ce qui est affiché dans la colonne **Message** de votre journal.

| Type de message | Message potentiel | Description |
|---|---|---|
| Échec provisoire d'envoi | L'adresse e-mail same@example.com a subi un échec provisoire d'envoi. | L'adresse e-mail était valide et le message a atteint le serveur de messagerie du destinataire, mais a été rejeté pour un problème « temporaire ». <br><br>Les raisons courantes d'un échec provisoire d'envoi incluent : {::nomarkdown} <ul> <li> La boîte de réception était pleine (l'utilisateur a dépassé son quota) </li> <li> Le serveur était indisponible </li> <li> Le message était trop volumineux pour la boîte de réception du destinataire </li>  </ul> {:/} Si un e-mail a subi un échec provisoire d'envoi, nous réessayons généralement dans un délai de 72 heures, mais le nombre de tentatives varie d'un destinataire à l'autre. |
| Échec d'envoi définitif | Le compte e-mail que vous avez essayé de joindre n'existe pas. Vérifiez l'adresse e-mail du destinataire pour détecter d'éventuelles fautes de frappe ou espaces inutiles. | Votre message n'a jamais atteint la boîte de réception de cette personne car il n'y avait pas de boîte de réception à atteindre. Si vous souhaitez approfondir, des messages comme celui-ci peuvent parfois comporter des liens dans la colonne **Afficher les détails** qui vous permettent de consulter le profil du destinataire prévu.|
| Blocage | Le message de spam est rejeté en raison de la politique anti-spam. | Votre message a été catégorisé comme spam. Cette erreur d'e-mail est enregistrée pour un utilisateur si nous avons reçu un événement de l'ESP indiquant que l'e-mail a été rejeté. Cela peut concerner uniquement ce destinataire, mais si vous voyez ce message fréquemment, vous devriez peut-être réévaluer vos habitudes d'envoi ou le contenu de votre message. Réfléchissez également : avez-vous [préchauffé votre IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) ? Si ce n'est pas le cas, contactez Braze pour obtenir des conseils à ce sujet.|
| Erreur de message abandonné | {% raw %}`{% abort_message('Module count is less than or equal to 1') %} called`{% endraw %} | Lorsqu'un envoi est abandonné par une balise Liquid `abort_message`, la colonne **Message** affiche l'extrait Liquid exact qui a été appelé. D'autres entrées **Erreur de message abandonné** peuvent contenir des messages différents décrivant la raison de l'abandon. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messages courants" }

### Pourquoi mon message n'apparaît-il pas ici ? {#why-isnt-my-message-listed-here}

Les messages du journal d'activité des messages peuvent provenir de diverses sources : Braze, vos applications ou plateformes, ou nos partenaires tiers. Cela signifie qu'il existe un nombre infini de messages susceptibles d'apparaître dans ce journal — comme vous pouvez l'imaginer, nous ne pouvons pas tous les répertorier !

Par exemple, certains messages de « blocage » potentiels, en plus de celui répertorié dans le tableau précédent, pourraient être :

- Malheureusement, les messages provenant de [_IP_ADDRESS_] n'ont pas été envoyés. Veuillez contacter votre fournisseur de services Internet car une partie de son réseau figure sur notre liste de blocage.
- Message rejeté en raison d'une politique locale.
- Le message a été bloqué par le destinataire en tant que spam.
- Service indisponible, hôte client [_IP_ADDRESS_] bloqué via Spamhaus.

## Durée de conservation {#storage-retention-period}

Les erreurs des 60 dernières heures sont disponibles dans le journal d'activité des messages. Les journaux datant de plus de 60 heures sont nettoyés et ne sont plus accessibles.

### Nombre de journaux d'erreurs conservés {#number-of-error-logs-stored}

Le nombre de journaux enregistrés est influencé par plusieurs conditions. Par exemple, si une Campaign planifiée est envoyée à des milliers d'utilisateurs, il est possible que seul un échantillon des erreurs apparaisse dans le journal d'activité des messages plutôt que la totalité. Voici un aperçu des conditions affectant le nombre de journaux conservés :
- Jusqu'à 20 journaux d'erreurs du même type sont enregistrés pour la même Campaign ou étape du Canvas au cours d'une heure fixe pour les types d'erreurs suivants :
    - Erreurs de contenu connecté
    - Erreurs de messages abandonnés
    - Erreurs de webhook
    - Erreurs de rejet SMS
    - Erreurs d'échec de distribution SMS
    - Erreurs d'échec WhatsApp
    - Erreurs de test A/B
- Jusqu'à 20 journaux d'erreurs de notification push du même type sont enregistrés pour la même Campaign ou étape du Canvas et combinaison d'application pour les types d'erreurs suivants :
    - Identifiants push invalides
    - Jeton de notification push invalide
    - Aucun identifiant push
    - Erreurs de jeton
    - Quota dépassé
    - Délai de tentatives expiré
    - Payload invalide
    - Erreur inattendue
- Jusqu'à 100 journaux d'erreurs du même type sont enregistrés pour la même application au cours d'une heure fixe pour les types d'erreurs suivants :
    - Erreur de Live Activity (aucun identifiant push)
    - Erreur de Live Activity (identifiant push invalide)
    - Autres erreurs de Live Activity
    - Erreurs de jeton supprimé par retour APNs
- Jusqu'à 100 journaux d'erreurs du même type sont enregistrés pour la même Campaign ou étape du Canvas au cours d'une heure fixe pour les types d'erreurs suivants :
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

Les journaux d'envois de test sont préfixés par « [TEST SEND] », mais il n'est pas garanti que tous les journaux d'envois de test portent ce préfixe (par exemple, les erreurs de contenu connecté ne comportent pas ce préfixe).