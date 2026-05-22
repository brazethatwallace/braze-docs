---
nav_title: Paramètres de notifications push
article_title: Paramètres de notifications push
page_order: 5
page_type: reference
description: "Cet article donne un aperçu des paramètres de notifications push dans le tableau de bord de Braze."
channel: push

---

# Paramètres de notifications push {#push-settings}

> La page **Paramètres de notifications push** vous permet de configurer les paramètres clés de vos notifications push, notamment la durée de vie des notifications push (TTL) et la priorité FCM par défaut pour les campagnes Android. Ces paramètres permettent d'optimiser la réception et l'efficacité de vos notifications push, garantissant ainsi une meilleure expérience à vos utilisateurs.

## Qu'est-ce que le TTL des notifications push ? {#what-is-push-ttl}

La durée de vie des notifications push (TTL) contrôle la durée pendant laquelle Braze tentera de délivrer une notification push aux appareils qui sont hors ligne au moment de l'envoi de la campagne. Si un appareil se reconnecte après l'expiration du TTL, le message ne sera pas distribué. Ce paramètre ne supprime pas une notification si elle a déjà été reçue par l'appareil de l'utilisateur — il contrôle uniquement la durée pendant laquelle le fournisseur push tente de délivrer une notification.

## Réglage des valeurs TTL push par défaut {#setting-default-push-ttl-values}

Par défaut, Braze définit le TTL des notifications push au maximum pour chaque service d'envoi de messages push.

| Service d'envoi de messages push | TTL maximum |
| --- | --- |
| Web (par le biais des services FCM ou Web Push) | 28 jours |
| Firebase Cloud Messaging (FCM) | 28 jours |
| Kindle (ADM) | 31 jours |
| Huawei (HMS) | 15 jours |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Setting default Push TTL values" }

Ces paramètres s'appliquent globalement à toutes les campagnes push, sauf si un TTL différent est défini pour un message spécifique. Pour ajuster le TTL d'un message, consultez [Paramètres avancés de campagne]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings/#ttl).

Pour définir un TTL push par défaut différent :

1. Accédez à **Settings** > **Manage Settings** > **Push Settings**.
2. Pour chaque plateforme Android, définissez une valeur de durée de vie par défaut. Vous pouvez définir des incréments plus petits comme des heures ou des secondes pour un contrôle plus précis.
3. Sélectionnez **Save** pour appliquer vos modifications.

![Paramètres de TTL push pour les appareils Firebase, Web, Kindle et Huawei.]({% image_buster /assets/img/push_ttl.png %})

## Priorité FCM par défaut pour les campagnes Android {#default-fcm-priority-for-android-campaigns}

Vous pouvez définir la priorité Firebase Cloud Messaging (FCM) par défaut pour toutes les campagnes push Android. Cette priorité détermine la manière dont la notification push est délivrée aux appareils des utilisateurs.

Les options de priorité FCM sont les suivantes :

| Priorité | Description | Cas d'utilisation |
| --- | --- | --- |
| Normal | Priorité de distribution standard, optimisée pour l'autonomie de la batterie | Contenu ne nécessitant pas une attention immédiate |
| High | Les messages sont envoyés immédiatement | Notifications urgentes nécessitant une distribution rapide |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Default FCM Priority for Android Campaigns" }

Pour définir la priorité FCM par défaut :

1. Accédez à **Settings** > **Manage Settings** > **Push Settings**.
2. Dans la section Priorité FCM, sélectionnez « Normal » ou « High » comme paramètre par défaut.
3. Sélectionnez **Save** pour appliquer vos modifications.

![Paramètres de priorité de distribution Android.]({% image_buster /assets/img/push_fcm_priority_settings.png %})

Ce paramètre s'applique globalement à toutes les nouvelles campagnes push Android, sauf si une priorité différente est sélectionnée lors de la création d'une campagne spécifique.

{% alert note %}
Si FCM détecte que votre application envoie fréquemment des messages à priorité élevée qui ne génèrent pas de notifications visibles par l'utilisateur ou d'engagement, ces messages peuvent être automatiquement rétrogradés à une priorité normale.
{% endalert %}

Pour plus d'informations sur les niveaux de priorité FCM et la rétrogradation, consultez [Paramètres avancés de campagne]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings/#fcm-priority).