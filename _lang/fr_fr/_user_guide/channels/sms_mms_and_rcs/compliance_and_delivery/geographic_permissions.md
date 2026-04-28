---
nav_title: "Autorisations géographiques"
article_title: "Autorisations géographiques"
description: "Cet article présente la liste de pays autorisés pour les autorisations géographiques, qui vous permet de choisir vers quels pays les SMS, MMS et RCS peuvent être envoyés."
page_order: 4
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/

---

# Autorisations géographiques {#geographic-permissions}

> Les autorisations géographiques renforcent la sécurité et protègent contre le trafic frauduleux de SMS, MMS et RCS en appliquant des contrôles sur les pays vers lesquels vous pouvez envoyer des messages. Vous pouvez spécifier une liste de pays autorisés pour vous assurer que les messages SMS, MMS et RCS ne sont envoyés que vers des régions approuvées. Seuls les administrateurs peuvent modifier la liste de pays autorisés. Les utilisateurs non administrateurs ont accès à une version en lecture seule de la liste qui indique vers quels pays un groupe d'abonnement peut envoyer des messages.

Si vous êtes administrateur, vous pouvez configurer les pays figurant sur la liste autorisée. La liste de pays autorisés est configurée au niveau du [groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/). Vous pouvez y accéder en allant dans **Audience** > **Subscriptions** et en sélectionnant un groupe d'abonnement SMS, MMS ou RCS. La liste autorisée se trouve sous **Geographic Permissions**.

![La section modifiable des autorisations géographiques SMS pour un administrateur, avec plusieurs pays sélectionnés dans la « liste de pays autorisés ».]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

### Sélection des pays {#selecting-countries}

Ajoutez des pays à la liste autorisée à l'aide du menu déroulant. Les pays les plus courants pour les SMS et RCS sont affichés en haut, les autres apparaissant en dessous. Vous pouvez également rechercher des pays en saisissant du texte dans le champ de recherche.

![Le menu déroulant « liste de pays autorisés » avec les pays les plus courants affichés en haut.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Supprimez des pays précédemment sélectionnés en décochant les cases correspondantes à côté de chacun d'entre eux.

### Enregistrement de vos modifications {#saving-your-changes}

Les modifications prendront effet après avoir sélectionné **Save**. Supprimer des pays de votre liste autorisée empêchera l'envoi de tous les messages SMS, MMS et RCS vers les numéros de ces pays.

![Fenêtre modale d'avertissement confirmant les pays qui seront supprimés de la liste autorisée.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## Pays à risque fort {#high-risk-countries}

Certains pays présentent un risque plus élevé de « traffic pumping » SMS et RCS. Ces pays sont signalés par une étiquette **High Risk** dans le menu déroulant des pays.

![Le menu déroulant des pays avec l'Azerbaïdjan portant une étiquette « High Risk ».]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

Si vous autorisez l'envoi vers ces pays, vous devez d'abord reconnaître le risque associé avant que le pays ne soit ajouté à votre liste autorisée.

{% alert note %}
Limitez les pays de votre liste autorisée à ceux strictement nécessaires pour répondre à vos besoins commerciaux. Cela réduira votre exposition potentielle au trafic frauduleux. Pour plus de conseils sur la prévention du « SMS traffic pumping », consultez la [FAQ sur la fraude par SMS traffic pumping]({{site.baseurl}}/sms_traffic_pumping_fraud/).
{% endalert %}

## Visibilité des envois bloqués {#visibility-of-blocked-sends}

Les tentatives d'envoi vers des pays ne figurant pas sur votre liste autorisée seront abandonnées. Les messages abandonnés seront enregistrés dans le [Journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) et dans l'[événement d'engagement lié aux messages d'abandon SMS]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).

Les messages abandonnés en raison d'envois bloqués apparaissent comme **Aborted Message Errors** et portent le message « The recipient's phone number is in a blocked country ».

![Journal d'abandon montrant plusieurs envois SMS bloqués parce que le numéro de téléphone se trouve dans un pays bloqué.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}