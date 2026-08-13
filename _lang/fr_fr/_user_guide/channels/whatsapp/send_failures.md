---
nav_title: Échecs d'envoi
article_title: Investiguer les échecs d'envoi WhatsApp
page_order: 22
page_type: reference
description: "Utilisez l'analyse de Campaign, le journal d'activité des messages et Currents pour investiguer les échecs d'envoi WhatsApp et les codes d'erreur Meta courants."
tool:
  - Reports
channel:
  - WhatsApp
---

# Investiguer les échecs d'envoi WhatsApp {#investigate-whatsapp-send-failures}

> Utilisez cette page lorsque les réceptions ou les lectures WhatsApp sont inférieures aux attentes, ou lorsque les **Échecs** dans l'analyse de Campaign semblent élevés.

## Flux d'investigation {#investigation-workflow}

Suivez les étapes ci-dessous dans l'ordre.

1. **Confirmez les échecs dans l'analyse de Campaign ou de Canvas.** Ouvrez l'étape du message et examinez le nombre d'**Échecs** ainsi que le taux d'échec. Si les échecs semblent élevés par rapport aux envois ou aux réceptions, passez à l'étape suivante.
2. **Trouvez le code d'erreur dans le journal d'activité des messages.** Ouvrez le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) pour le même envoi, filtrez sur les messages en échec et notez le code d'erreur du fournisseur (par exemple, `131049` pour les limites de marketing par utilisateur). Utilisez les [Codes d'échec courants](#common-failure-codes) pour interpréter le code et décider des prochaines étapes.
3. **Exportez les échecs avec Currents pour l'analyse ou le reciblage.** Une fois le code d'erreur identifié, exportez les événements d'échec d'envoi WhatsApp via Currents. Utilisez ces données pour analyser les tendances d'échec dans votre entrepôt de données ou pour créer des segments et recibler les utilisateurs sur un autre canal.

## Codes d'échec courants {#common-failure-codes}

| Code d'erreur | Cause typique | Étape suivante |
|---|---|---|
| `131049` | Limite de fréquence marketing par utilisateur imposée par Meta ou pause marketing aux États-Unis | Voir [Ressources Meta]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources) et [Recibler les utilisateurs sur d'autres canaux Braze]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery#retargeting-users-on-other-braze-channels) |
| `130472` | Groupe de contrôle d'expérimentation marketing Meta | Voir la [FAQ des ressources Meta]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources#faq) |
| `131026` | Diverses raisons de non-réception (Meta ne divulgue pas les détails) | Évitez les nouvelles tentatives immédiates ; consultez la [résolution des problèmes de l'API Cloud Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Codes d'échec WhatsApp courants" }