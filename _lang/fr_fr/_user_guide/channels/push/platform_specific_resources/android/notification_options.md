---
nav_title: "Options de notification"
article_title: Options de notification Android
page_order: 2
page_type: reference
description: "Cet article de référence couvre plusieurs options de notification Android et comment les utiliser au mieux dans les campagnes Braze."

platform: Android
channel:
  - Push

---

# Options de notification {#notification-options}

> Voici quelques-unes des options de notification push spécifiques à Android disponibles via Braze.

## Notifications silencieuses {#silent-notifications}

Lorsque vous [rédigez votre message de notification push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/?tab=android#step-4-compose-your-push-message), vous **ne pouvez pas** envoyer un message push Android sans titre&#8212;cependant, vous pouvez saisir un simple espace à la place. Gardez à l'esprit que si votre message ne contient qu'un seul espace, il sera envoyé en tant que notification push silencieuse. Pour en savoir plus, consultez [Notifications push silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).

## Groupes de notifications {#notification-groups}

Si vous souhaitez catégoriser vos messages et les regrouper dans le tiroir de notifications de votre utilisateur, vous pouvez utiliser la fonctionnalité de canaux de notification Android via Braze.

Commencez par créer votre campagne push Android, puis regardez en haut de l'onglet **Rédiger** pour trouver le menu déroulant **Notification Channel**.

![]({% image_buster /assets/img_archive/notification_channel_dropdown.png %}){: style="max-width:60%;"}

Sélectionnez votre canal de notification dans le menu déroulant. Vous devez également sélectionner un canal de secours au cas où les paramètres de votre canal de notification dysfonctionneraient.

Si vous n'avez aucun [canal de notification]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels/) répertorié ici, vous pouvez en ajouter un en utilisant l'ID du canal de notification. Contactez vos développeurs pour identifier vos ID de canal de notification ou pour créer de nouveaux ID si nécessaire.

Pour ajouter un ID de notification à votre canal de notification, cliquez sur **Manage Notification Channel** dans le menu déroulant **Notification Channel** et remplissez les champs requis. Les canaux de notification doivent être définis dans l'application avant de pouvoir être utilisés dans la plateforme Braze.

![]({% image_buster /assets/img_archive/notification_channels.png %}){: style="max-width:80%;" }