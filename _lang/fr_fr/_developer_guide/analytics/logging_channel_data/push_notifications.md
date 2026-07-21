---
nav_title: Notifications push
article_title: Enregistrer les données de notification push via le SDK Braze
page_order: 7.2
description: "Découvrez comment enregistrer les données des notifications push via le SDK de Braze."
noindex: true
---

# Enregistrer les données des notifications push {#log-push-notification-data}

> Découvrez comment enregistrer les données des notifications push via le SDK de Braze.

{% sdktabs %}
{% sdktab android %}
## Enregistrer les données avec l'API Braze (recommandé) {#logging-data-with-the-braze-api-recommended}

Vous pouvez enregistrer les données analytiques en temps réel en effectuant des appels vers l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Pour enregistrer ces données, envoyez la valeur `braze_id` depuis le tableau de bord de Braze afin d'identifier le profil utilisateur à mettre à jour.

![Exemple de tableau de bord de notification push personnalisée]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:79%;"}

## Enregistrer les données manuellement {#manually-logging-data}

En fonction des détails de votre payload, vous pouvez enregistrer les données analytiques manuellement dans votre implémentation de `FirebaseMessagingService.onMessageReceived` ou dans votre activité de démarrage. Votre sous-classe `FirebaseMessagingService` doit terminer son exécution dans les 9 secondes suivant son invocation pour éviter d'être [signalée ou interrompue](https://firebase.google.com/docs/cloud-messaging/android/receive) par le système Android.

{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/analytics/logging_push_data.md %}
{% endsdktab %}
{% endsdktabs %}