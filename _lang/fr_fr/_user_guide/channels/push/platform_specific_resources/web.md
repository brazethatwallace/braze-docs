---
nav_title: "Notification push Web"
article_title: Notifications push Web
page_order: 8.5
page_type: reference
description: "Cette page de référence présente brièvement les notifications push Web et renvoie vers les étapes nécessaires pour en créer une."
platform: Web
channel:
  - push

---

# Notifications push Web {#web-push}

> Découvrez les notifications push Web chez Braze et trouvez des ressources pour créer les vôtres.

Les notifications push Web sont un excellent moyen d'interagir avec les utilisateurs de votre application Web. Les clients qui visitent votre site Web depuis des [navigateurs pris en charge](#supported-browsers) peuvent s'abonner pour recevoir des notifications push Web de votre application, que la page Web soit chargée ou non.

## Conditions préalables {#prerequisites}

Avant de pouvoir créer et envoyer des notifications push avec Braze, vous devez collaborer avec vos développeurs pour intégrer les notifications push à votre site Web. Pour les étapes détaillées, consultez notre [guide d'intégration des notifications push Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web).

### Autorisation de notification push {#push-permission}

Toute marque peut intégrer et utiliser les notifications push Web sur son site. Les notifications peuvent atteindre les visiteurs actuels et précédents tant qu'ils ont un navigateur Web ouvert, mais les visiteurs doivent [s'abonner pour recevoir les notifications]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#push-permission), tout comme pour les notifications push classiques sur application mobile.

{% alert tip %}
Envisagez d'utiliser un message dans le navigateur pour inciter les utilisateurs à s'abonner aux notifications push Web, également connu sous le nom d'[amorce de notification push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).
{% endalert %}

## Aperçu {#overview}

Les notifications push Web délivrent des mises à jour urgentes et exploitables qui favorisent des conversions rapides. Avec les notifications push Web, vous pouvez :

- Déclencher des messages dès qu'une donnée importante change, comme une baisse de prix
- Ramener les utilisateurs sur votre site Web grâce à des boutons d'appel à l'action clairs
- Personnaliser vos notifications push avec des informations sur les produits et les clients pour rendre votre message pertinent

Les notifications push Web fonctionnent de la même manière que les notifications push d'application sur votre téléphone. Pour plus d'informations sur la composition d'une notification push Web, consultez [Créer une notification push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message).

![Exemple de notification push Web avec le même message affiché sur un ordinateur portable et un téléphone.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Cas d'usage potentiels {#potential-use-cases}

Voici quelques exemples de cas d'usage courants des notifications push Web.

| Cas d'usage | Description |
| --- | --- |
| Essai gratuit | Encouragez les nouveaux visiteurs de votre site Web à s'inscrire pour des essais gratuits. En donnant aux utilisateurs la possibilité de découvrir ce qui vous rend unique, vous augmentez les chances qu'ils deviennent des clients payants. |
| Téléchargement d'application | Attirez les utilisateurs Web vers votre application mobile pour les aider à tirer encore plus de valeur de vos produits. Envisagez d'exploiter la personnalisation pour mettre en avant les avantages de l'application en fonction de leurs habitudes d'engagement actuelles. |
| Réductions et promotions | Augmentez la visibilité des événements et promotions à durée limitée auprès de vos clients. Envoyez des messages sur plusieurs canaux, y compris les notifications push Web, pour accroître la visibilité des promotions de votre marque. |
| Abandon de panier | Envoyez des rappels automatisés aux utilisateurs qui n'ont pas terminé leurs transactions pour les ramener vers le processus de paiement. <br><br>Une étude menée par Braze a révélé que les notifications push Web sont 53 % plus efficaces que l'e-mail et 23 % plus impactantes que les notifications push mobiles pour inciter les destinataires à revenir et finaliser un achat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'usage potentiels" }

## Navigateurs pris en charge {#supported-browsers}

Les navigateurs suivants prennent en charge les notifications push Web.

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

- Chrome (et Chrome pour Android mobile)
- Safari (version 16 ou ultérieure)
- Firefox (et Firefox pour Android mobile)
- Opera
- Edge

Pour plus d'informations sur les standards du protocole push et la prise en charge par les navigateurs, vous pouvez consulter les ressources en fonction de votre navigateur :

- [Safari (ordinateur de bureau)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (mobile)]({{site.baseurl}}/developer_guide/push_notifications?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)

## Endpoints push Web 410 (Gone) et invalides {#410-gone-and-invalid-web-push-endpoints} {#410-gone-and-invalid-web-push-endpoints}

Les navigateurs et les services push peuvent renvoyer une erreur **410 Gone** (ou des erreurs similaires de type « endpoint non valide ») lorsqu'un abonnement push Web n'est plus accepté. Les causes courantes incluent :

- L'utilisateur a désactivé les notifications pour votre site dans les paramètres du navigateur ou du système d'exploitation.
- Un profil utilisateur différent s'est abonné sur le même profil de navigateur, de sorte que l'endpoint a été réattribué au nouvel abonné.
- L'abonnement a expiré après une longue période sans engagement. Lorsque l'utilisateur s'abonne à nouveau, un nouvel abonnement est créé lors de la session suivante.

Une fois que l'utilisateur a réactivé les notifications, déclenchez à nouveau le flux d'inscription push Web habituel de votre site afin que Braze enregistre le nouvel endpoint d'abonnement.