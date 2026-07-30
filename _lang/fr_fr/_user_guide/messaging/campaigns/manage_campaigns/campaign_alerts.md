---
nav_title: Alertes de campagne
article_title: Alertes de campagne
page_order: 6

page_type: reference
description: "Cet article de référence donne un aperçu des alertes de campagne, de leurs avantages et de la manière de les configurer pour vous offrir une tranquillité d'esprit."
tool: Campaigns
channel:
- email
- webhooks

---

# Alertes de campagne {#campaign-alerts}

> Nous souhaitons vous alerter lorsque quelque chose ne semble pas fonctionner comme prévu et vous offrir la tranquillité d'esprit que tout se déroule sans accroc. Les alertes de seuil de Campaign vous permettent d'être la première personne informée si une Campaign importante envoie plus ou moins de messages que prévu.

Vous recherchez la même fonctionnalité pour un Canvas ? Consultez les [alertes de seuil Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_threshold_alerts).

Les alertes de Campaign sont disponibles pour les Campaigns suivantes :

- Campaigns récurrentes planifiées
- Campaigns basées sur une action
- Campaigns déclenchées par API

## Configuration de votre alerte de campagne {#setting-up-your-campaign-alert}

Accédez à la page d'analyse de votre campagne pour commencer à configurer votre alerte. Lorsque vous sélectionnez **Set Up Alert**, vous pouvez spécifier des seuils d'alerte supérieurs et inférieurs, ainsi que les destinataires et les canaux de l'alerte.

![Boîte de dialogue de suivi de campagne avec deux boutons : Annuler et Enregistrer.]({% image_buster /assets/img_archive/campaign_alerts.png %})

Pour une campagne récurrente planifiée, vous pouvez définir des seuils supérieurs et inférieurs pour les messages envoyés à chaque envoi de la campagne. Pour une campagne déclenchée, vous pouvez définir des seuils supérieurs et inférieurs pour le nombre de messages envoyés par heure et par jour.

Vous pouvez configurer une alerte par e-mail, une alerte par webhook, ou les deux. Les alertes par webhook peuvent être très utiles, car elles vous permettent d'envoyer une alerte vers un canal Slack. Pour plus d'informations sur l'intégration des alertes de campagne avec Slack, consultez la documentation de Slack sur l'[envoi de messages à l'aide de webhooks entrants](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/).

{% alert note %}
Lorsque vous configurez des alertes de campagne pour des campagnes futures, vous pouvez recevoir des mises à jour avant le début de la campagne et après sa fin. En effet, les alertes de campagne continueront d'être envoyées tant que la campagne n'aura pas été arrêtée manuellement.
{% endalert %}

## Payload du webhook d'alerte de Campaign {#campaign-alert-webhook-payload}

Voici un exemple de payload pour le corps d'un webhook d'alerte de Campaign. Cet exemple utilise une alerte configurée pour être envoyée lorsque le nombre de messages envoyés est inférieur à 500 pour un envoi de Campaign donné.

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

