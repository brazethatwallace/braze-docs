---
nav_title: Push
article_title: Push
page_order: 7
page_type: landing
description: "Envoyez des appels à l'action urgents via des notifications push mobiles et web pour réengager les utilisateurs et les inciter à agir."
channel:
  - push
search_rank: 3
---

# Push {#push}

> Les notifications push envoient des appels à l'action urgents sur les appareils mobiles et web, et réengagent les utilisateurs qui n'ont pas ouvert votre application récemment. Elles dirigent directement vers le contenu pertinent et démontrent la valeur continue de votre produit. Ce hub couvre l'intégration des notifications push, la stratégie d'abonnement, les types de messages, les bonnes pratiques et les paramètres spécifiques aux plateformes iOS, Android et Web. Envisagez d'utiliser des [messages in-app de push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) avant de demander l'autorisation système. Consultez les guides d'intégration pour [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android) et [Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web) pour commencer.

[![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}

## Conditions préalables {#prerequisites}

Avant de commencer, assurez-vous de disposer des éléments suivants :

- **Les notifications push intégrées à votre application ou site web.** Collaborez avec vos développeurs pour effectuer cette configuration. Pour connaître les étapes détaillées, consultez les guides d'intégration pour [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications?tab=android) et [Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web).
- **Une stratégie d'abonnement aux notifications push.** Les utilisateurs doivent accorder l'autorisation de recevoir des notifications push sur leur appareil. Envisagez d'utiliser des [messages in-app de push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) pour expliquer la valeur ajoutée avant de les solliciter.

## Cas d'usage {#use-cases}

| Cas d'usage | Explication |
| --- | --- |
| Onboarding initial | Tant que les utilisateurs n'ont pas effectué les premières étapes d'utilisation de votre application (comme la création d'un compte), leur valeur reste très limitée. Utilisez les notifications push pour les inciter à accomplir ces étapes afin qu'ils puissent commencer à utiliser pleinement votre application. |
| Premiers achats | Une fois que les utilisateurs sont à l'aise avec votre application, vous pouvez utiliser les notifications push pour les convertir en acheteurs in-app. |
| Nouvelles fonctionnalités | Les notifications push peuvent être efficaces pour informer les utilisateurs désengagés de nouvelles fonctionnalités susceptibles de les ramener vers votre application. |
| Offres à durée limitée | Si une offre est soumise à un compte à rebours, les notifications push sont un excellent moyen d'en informer vos utilisateurs avant son expiration. Ces messages véhiculent généralement un fort sentiment d'urgence et sont particulièrement adaptés pour rappeler votre application aux utilisateurs récemment inactifs. Par exemple, si votre application est un jeu et que vous offrez un bonus de monnaie virtuelle pour une série de connexions quotidiennes, alerter un utilisateur que sa série est en danger peut constituer une notification push efficace après un certain nombre de jours consécutifs. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'usage" }

## Réglementations relatives aux notifications push {#push-message-regulations}

Les notifications push atteignent directement l'appareil de votre client, c'est pourquoi les politiques des applications et des boutiques d'applications encadrent leur utilisation.

{% alert important %}
Vos notifications push doivent respecter les [Directives d'évaluation de l'App Store d'Apple](https://developer.apple.com/app-store/review/guidelines/) et les [Règles de Google Play](https://support.google.com/googleplay/android-developer/answer/9888379). Cela inclut les règles relatives à l'utilisation des notifications push à des fins publicitaires, de spam, de promotions et de sujets connexes.
{% endalert %}

| Source de la politique | Résumé |
| --- | --- |
| Apple [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) | Les utilisations inacceptables incluent la création d'une interface pour afficher des applications, extensions ou plug-ins tiers similaires à l'App Store ou sous forme de collection d'intérêt général. |
| Apple [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) | Les notifications push ne doivent pas être nécessaires au fonctionnement de l'application et ne doivent pas contenir d'informations personnelles sensibles ou confidentielles. N'utilisez pas les notifications push à des fins promotionnelles ou de marketing direct, sauf si les clients s'y sont explicitement abonnés via un consentement dans l'interface de votre application et peuvent se désabonner depuis l'application. |
| Apple [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) | Vous ne pouvez pas monétiser les fonctionnalités intégrées telles que les notifications push, l'appareil photo ou le gyroscope, ni les services Apple tels qu'Apple Music ou iCloud. |
| Google Play — [Utilisation non autorisée ou imitation des fonctionnalités système](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) | Les applications ne doivent pas imiter ou interférer avec les notifications système. Les notifications au niveau système sont réservées aux fonctionnalités essentielles de l'application (par exemple, une application de compagnie aérienne informant les utilisateurs d'offres, ou un jeu notifiant les utilisateurs de promotions en jeu). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Réglementations relatives aux notifications push" }

## Questions fréquentes {#frequently-asked-questions}

### Quand Braze enregistre-t-il un envoi réussi pour les notifications push ? {#when-does-braze-record-a-successful-send-for-push}

Braze enregistre généralement un **envoi** une fois que le message est transmis depuis Braze vers Apple, Google ou votre service de notification push Web. Les indicateurs **livré**, ouvertures, rebonds et signaux de désinstallation sont suivis séparément et peuvent arriver ultérieurement. Utilisez les analyses au niveau de l'étape et de la Campaign conjointement avec la [résolution des problèmes push]({{site.baseurl}}/user_guide/channels/push/troubleshooting) lorsque les **envois** et les indicateurs en aval semblent désalignés.

## Étapes suivantes {#next-steps}

- [Configuration des notifications push]({{site.baseurl}}/user_guide/channels/push/push_setup)
- [Créer un message push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)