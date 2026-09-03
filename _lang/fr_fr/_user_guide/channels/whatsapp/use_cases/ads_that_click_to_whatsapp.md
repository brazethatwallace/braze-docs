---
nav_title: "Publicités qui redirigent vers WhatsApp"
article_title: "Publicités qui redirigent vers WhatsApp"
page_order: 1
description: "Cet article de référence fournit un guide étape par étape pour configurer et utiliser les publicités qui redirigent vers WhatsApp."
page_type: reference
alias: /whatsapp_use_cases/
channel:
  - WhatsApp
---

# Publicités qui redirigent vers WhatsApp {#ads-that-click-to-whatsapp}

> Cette page fournit un guide étape par étape pour configurer et utiliser les publicités qui redirigent vers WhatsApp, afin que vous et votre équipe puissiez améliorer votre programme WhatsApp.

Les publicités qui redirigent vers WhatsApp sont un moyen efficace d'attirer des clients nouveaux et existants depuis les publicités Meta sur Facebook, Instagram ou d'autres plateformes. Utilisez ces publicités pour promouvoir vos produits et services tout en informant les utilisateurs de votre présence sur WhatsApp.

![Une publicité Facebook de Calorie Rocket qui annonce la livraison gratuite, et la conversation WhatsApp correspondante qui se produit lorsqu'un utilisateur sélectionne le bouton de la publicité.]({% image_buster /assets/img/whatsapp/ads_that_click_whatsapp.png %}){: style="max-width:70%;"}

## Configuration des publicités qui redirigent vers WhatsApp {#setting-up-ads-that-click-to-whatsapp}

1. Dans le gestionnaire de publicités Meta, créez une publicité sur Facebook, Instagram ou d'autres plateformes en suivant le guide étape par étape [Comment créer des publicités qui redirigent vers WhatsApp](https://business.whatsapp.com/products/create-ads-that-click-to-whatsapp). **Ne configurez pas** de réponses automatisées ; vous configurerez les réponses dans Braze à la place.

![Gestionnaire de publicités avec un compositeur pour créer une publicité d'engagement.]({% image_buster /assets/img/whatsapp/meta_ads_composer.png %})

Lors de la configuration du message pré-rempli, qui sera envoyé par l'utilisateur à votre compte WhatsApp Business, incluez un mot ou une phrase spécifique que vous utiliserez pour déclencher une réponse propre à cette publicité. Dans cet exemple, une application de livraison de repas utilise « free delivery » car c'est ce qui est mis en avant dans la publicité.

![Compositeur de modèles du gestionnaire de publicités avec un message pré-rempli « I want free delivery ».]({% image_buster /assets/img/whatsapp/pre_filled_message.png %})

{% alert tip %}
Indiquez clairement dans la description de la publicité que cliquer sur celle-ci démarrera une conversation avec votre marque en utilisant des phrases comme « Discutez maintenant sur WhatsApp ».
{% endalert %}

{: start="2"}
2. Dans Braze, configurez un Canvas basé sur une action où l'option basée sur l'action est **Send a WhatsApp inbound message** et le corps du message est « VOTRE_MOT_DÉCLENCHEUR ». Dans cet exemple, une application de livraison de repas utilise « free delivery ».

![Planification d'entrée pour un Canvas Braze basé sur une action, avec l'événement déclencheur « Send a WhatsApp inbound message » et un corps de message correspondant à l'expression régulière « free delivery ».]({% image_buster /assets/img/whatsapp/action_based_free_delivery.png %})

{: start="3"}
3. Configurez un message de réponse dans le Canvas qui s'envoie immédiatement après l'entrée du client dans le Canvas (par exemple, sans délai). Bien que cliquer sur la publicité constitue techniquement un abonnement, nous vous recommandons de configurer votre message de réponse pour demander à l'utilisateur s'il souhaite recevoir de futurs messages marketing de votre part sur WhatsApp.

{% alert tip %}
Configurez votre message de réponse avec des réponses rapides (comme « Oui » ou « Non merci ») afin que les utilisateurs puissent rapidement indiquer s'ils souhaitent s'abonner.
{% endalert %}

N'oubliez pas de fournir également tout code de réduction, offre ou autre information promise dans la publicité !

![Compositeur de messages WhatsApp avec des boutons de réponse « Yes » et « No Thanks ».]({% image_buster /assets/img/whatsapp/quick_replies.png %})

![Étape du Canvas avec un groupe « Opting in » ayant un événement déclencheur « Sent inbound WhatsApp to subscription group » et un mot déclencheur « YES ».]({% image_buster /assets/img/whatsapp/opting_in_step.png %})

{: start="4"}
4. Abonnez les utilisateurs en mettant à jour le statut d'abonnement des profils utilisateur avec l'une des méthodes de mise à jour suivantes :
    - Créez un webhook Braze-vers-Braze qui met à jour le statut d'abonnement via la REST API.
    - Utilisez l'éditeur JSON avancé pour mettre à jour le profil utilisateur avec le modèle permettant de [mettre à jour le statut d'abonnement d'un utilisateur vers un Canvas WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-opt-in-and-opt-out-process).

![Étape de mise à jour utilisateur du Canvas utilisant l'éditeur JSON avancé pour mettre à jour le profil utilisateur.]({% image_buster /assets/img/whatsapp/user_update_step_json.png %})

![Canvas montrant le flux de travail pour l'envoi de publicités qui redirigent vers WhatsApp, incluant trois parcours d'action : abonnement, désabonnement et tous les autres.]({% image_buster /assets/img/whatsapp/ads_that_click_canvas.png %})

## Considérations {#considerations}

Les conversations initiées à partir d'une publicité qui redirige vers WhatsApp sont gratuites si les conditions suivantes sont remplies :

- Si un utilisateur vous envoie un message via un [point d'entrée gratuit](https://developers.facebook.com/docs/whatsapp/pricing#free-entry-point-conversations), tel qu'une publicité qui redirige vers WhatsApp, une [fenêtre de service client](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows) de 24 heures s'ouvre, pendant laquelle vous pouvez envoyer à cet utilisateur tout type de message.
- Si vous répondez dans la fenêtre de service client (dans les 24 heures), un point d'entrée gratuit s'ouvre pour 72 heures, et tous les messages envoyés dans cette fenêtre de 72 heures seront gratuits.