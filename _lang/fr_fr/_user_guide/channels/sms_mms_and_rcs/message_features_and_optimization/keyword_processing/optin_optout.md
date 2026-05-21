---
nav_title: Mots-clés d'abonnement et de désabonnement
article_title: Mots-clés d'abonnement et de désabonnement SMS
page_order: 0
description: "Cet article de référence explique comment Braze traite les mots-clés de base d'abonnement et de désabonnement pour l'envoi de messages SMS."
page_type: reference
alias: /optin_optout/
tool:
  - Dashboard

channel:
  - SMS
---

# Mots-clés d'abonnement et de désabonnement {#opt-in-and-opt-out-keywords}

> La réglementation exige que des réponses soient fournies pour tous les mots-clés d'abonnement, de désabonnement et d'aide/information. Braze traite automatiquement les messages suivants (_exacts, composés d'un seul mot, insensibles à la casse_), en mettant automatiquement à jour l'[état du groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/) de l'utilisateur et de son numéro de téléphone associé pour toutes les demandes entrantes.

## Mots-clés par défaut {#default-keywords}

Braze traite automatiquement les mots-clés suivants et met à jour l'état du groupe d'abonnement pour le numéro de téléphone sur toutes les demandes entrantes. Notez que ces mots-clés et réponses par défaut peuvent également être personnalisés, et que vous pouvez ajouter des [mots-clés personnalisés]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling/).

{% alert tip %}
Vous souhaitez étendre le traitement de vos désabonnements ? Essayez le [désabonnement approximatif]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/), une fonctionnalité qui tente de reconnaître lorsqu'un message entrant ne correspond pas à un mot-clé de désabonnement, mais indique une intention de désabonnement.
{% endalert %}

| Type | Mot-clé | Changement |
|-|-------|---|
| Abonnement | `START`<br> `YES`<br> `UNSTOP` | Toute demande entrante contenant l'un de ces mots-clés d'`abonnement` entraînera un changement de l'état du groupe d'abonnement vers `abonné`. De plus, le pool d'expéditeurs associé à ce groupe d'abonnement pourra désormais envoyer un message SMS, MMS ou RCS à ce client (selon le type d'envoi de messages pris en charge par les expéditeurs). <br><br>L'utilisateur recevra votre réponse automatique d'abonnement définie. |
| Désabonnement | `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Toute demande entrante contenant l'un de ces mots-clés de `désabonnement` entraînera un changement de l'état du groupe d'abonnement vers `désabonné`. De plus, le pool de numéros associé à ce groupe d'abonnement ne pourra plus envoyer de messages à ce client.<br><br>L'utilisateur recevra votre réponse automatique de désabonnement définie. |
| Aide | `HELP`<br> `INFO` | L'utilisateur recevra votre réponse automatique d'aide définie. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Default keywords" }

Seul le **message exact, composé d'un seul mot** sera traité (insensible à la casse). Les mots-clés tels que `STOP PLEASE` seront ignorés, sauf si le [désabonnement approximatif]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/) est activé.

Si un destinataire utilise les mots-clés `HELP` ou `INFO`, une réponse sera déclenchée automatiquement. Le message de réponse par défaut pour ces réponses automatiques sera défini lors de votre période d'[onboarding]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/) et d'acquisition de numéros de téléphone. Notez que vous pouvez continuer à mettre à jour ces réponses après la période d'onboarding initiale.

{% alert tip %}
Vous souhaitez étendre le traitement de vos désabonnements ? Essayez le [désabonnement approximatif]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/), une fonctionnalité qui tente de reconnaître lorsqu'un message entrant ne correspond pas à un mot-clé de désabonnement, mais indique une intention de désabonnement.
{% endalert %}

## Gérer les désabonnements en langage naturel {#handle-natural-language-opt-outs}

Vous pouvez créer un [Braze Agent]({{site.baseurl}}/user_guide/brazeai/agents/) qui utilise l'analyse de sentiment pour capturer les intentions de désabonnement qui ne correspondent pas aux mots-clés standard ou personnalisés (par exemple « Merci de ne plus m'envoyer de messages »). Consultez [Gérer les désabonnements en langage naturel dans la Console des agents]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/#handle-natural-language-opt-outs-in-the-agent-console) pour connaître les étapes à suivre.