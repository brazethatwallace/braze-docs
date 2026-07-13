---
nav_title: "Configuration"
article_title: Configuration des notifications push
page_order: 0
layout: dev_guide
guide_top_header: "Configuration des notifications push"
guide_top_text: "Comprenez le cycle de vie des jetons de notification push et les états d'abonnement pour vous assurer que vos notifications push atteignent les bons utilisateurs."

page_type: landing
description: "Découvrez le cycle de vie des jetons de notification push et les états d'abonnement pour les notifications push dans Braze."

guide_featured_title: "Articles de la section"
guide_featured_list:
  - name: Cycle de vie des jetons de notification push
    link: /docs/user_guide/channels/push/push_setup/push_token_lifecycle
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: États d'abonnement push
    link: /docs/user_guide/channels/push/push_setup/push_subscription_states
    image: /assets/img/braze_icons/users-01.svg
---

## Conditions préalables {#prerequisites}

Avant de pouvoir créer et envoyer des notifications push avec Braze, vous devez collaborer avec vos développeurs pour intégrer les notifications push à votre site web ou à votre application. Pour connaître les étapes détaillées, consultez nos guides d'intégration pour chaque plateforme :

- [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web)

## Amorce de notification push {#push-priming}

Gardez à l'esprit que les utilisateurs doivent s'abonner aux notifications push pour recevoir vos messages, ce qui signifie qu'il est judicieux d'utiliser des messages in-app pour expliquer à vos clients pourquoi vous souhaitez leur envoyer des notifications push, et en quoi l'activation des notifications push leur sera bénéfique. Ce processus est appelé [amorce de notification push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).