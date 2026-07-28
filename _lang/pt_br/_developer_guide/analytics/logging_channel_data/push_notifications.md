---
nav_title: Notificações por push
article_title: Registre os dados de notificação por push pelo SDK da Braze
page_order: 7.2
description: "Aprenda como registrar os dados de notificação por push pelo SDK da Braze."
noindex: true
---

# Registre os dados de notificação por push {#log-push-notification-data}

> Aprenda como registrar os dados de notificação por push pelo SDK da Braze.

{% sdktabs %}
{% sdktab android %}
## Registrando dados com a API da Braze (recomendado) {#logging-data-with-the-braze-api-recommended}

Você pode registrar análises em tempo real fazendo chamadas para o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Para registrar análises, envie o valor `braze_id` do dashboard da Braze para identificar qual perfil de usuário atualizar.

![Exemplo de dashboard de push personalizado]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:79%;"}

## Registrando dados manualmente {#manually-logging-data}

Dependendo dos detalhes da sua carga útil, você pode registrar análises manualmente dentro da sua implementação de `FirebaseMessagingService.onMessageReceived` ou da sua activity de inicialização. Sua subclasse de `FirebaseMessagingService` deve concluir a execução em até 9 segundos após a invocação para evitar ser [sinalizada ou encerrada](https://firebase.google.com/docs/cloud-messaging/android/receive) pelo sistema Android.

{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/analytics/logging_push_data.md %}
{% endsdktab %}
{% endsdktabs %}