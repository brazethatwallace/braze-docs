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

# Push

> Les notifications push sont un moyen éprouvé d'envoyer des appels à l'action urgents via mobile ou web, ainsi que de réengager les utilisateurs qui ne se sont pas connectés à l'application depuis un certain temps. Elles dirigent l'utilisateur directement vers le contenu et démontrent la valeur de votre application.

[![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}

## Conditions préalables {#prerequisites}

Avant de commencer, assurez-vous de disposer des éléments suivants :

- **Push intégré à votre application ou site web.** Collaborez avec vos développeurs pour mettre cela en place. Pour les étapes détaillées, consultez les guides d'intégration pour [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications?tab=android) et [Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web).
- **Une stratégie d'abonnement push.** Les utilisateurs doivent accorder l'autorisation push sur leur appareil. Envisagez d'utiliser des [messages in-app de push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) pour expliquer la valeur avant de demander l'autorisation.

## Cas d'utilisation {#use-cases}

| Cas d'utilisation | Explication |
| --- | --- |
| Onboarding initial | Tant que les utilisateurs n'ont pas effectué les premières étapes d'utilisation de votre application (comme la création d'un compte), leur valeur est très limitée. Utilisez les notifications push pour inciter les utilisateurs à accomplir ces étapes afin qu'ils puissent commencer à utiliser pleinement votre application. |
| Premiers achats | Une fois que les utilisateurs sont à l'aise avec votre application, vous pouvez utiliser les notifications push pour les convertir en acheteurs in-app. |
| Nouvelles fonctionnalités | Les notifications push peuvent être efficaces pour informer les utilisateurs désengagés de nouvelles fonctionnalités susceptibles de les ramener vers votre application. |
| Offres à durée limitée | Si une offre est limitée dans le temps, le push est un excellent moyen d'en informer vos utilisateurs avant son expiration. Ces messages véhiculent généralement un fort sentiment d'urgence et sont optimaux pour rappeler votre application aux utilisateurs récemment inactifs. Par exemple, si votre application est un jeu et que vous offrez un bonus de monnaie in-game pour une série de jeux quotidiens, alerter un utilisateur que sa série est menacée peut être un push efficace après qu'il a atteint un certain nombre de jours. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'utilisation" }

## Réglementations relatives aux messages push {#push-message-regulations}

Le push atteint directement l'appareil de votre client, c'est pourquoi les politiques des applications et des stores réglementent son utilisation.

{% alert important %}
Vos messages push doivent respecter les [directives de l'App Store d'Apple](https://developer.apple.com/app-store/review/guidelines/) et les [politiques de Google Play](https://support.google.com/googleplay/android-developer/answer/9888379). Cela inclut les règles relatives à l'utilisation du push pour la publicité, le spam, les promotions et les sujets connexes.
{% endalert %}

| Source de la politique | Résumé |
| --- | --- |
| Apple [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) | Les utilisations inacceptables incluent la création d'une interface pour afficher des applications, extensions ou plug-ins tiers similaires à l'App Store ou en tant que collection d'intérêt général. |
| Apple [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) | Le push ne doit pas être requis pour le fonctionnement de l'application et ne doit pas transmettre d'informations personnelles sensibles ou confidentielles. N'utilisez pas le push pour des promotions ou du marketing direct, sauf si les clients ont explicitement donné leur accord via un texte de consentement dans l'interface de votre application et peuvent se désabonner dans l'application. |
| Apple [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) | Vous ne pouvez pas monétiser les fonctionnalités intégrées telles que les notifications push, l'appareil photo ou le gyroscope, ni les services Apple tels qu'Apple Music ou iCloud. |
| Google Play — [Utilisation non autorisée ou imitation de fonctionnalités système](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) | Les applications ne doivent pas imiter ni interférer avec les notifications système. Les notifications au niveau du système sont réservées aux fonctionnalités essentielles de l'application (par exemple, une application de compagnie aérienne informant les utilisateurs d'offres, ou un jeu informant les utilisateurs de promotions in-game). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Réglementations relatives aux messages push" }

## Questions fréquentes {#frequently-asked-questions}

### Quand Braze enregistre-t-il un envoi réussi pour le push ? {#when-does-braze-record-a-successful-send-for-push}

Braze enregistre généralement un **envoi** une fois que le message est transmis depuis Braze vers Apple, Google ou votre service de notification push web. Les indicateurs **Livré**, ouvertures, rebonds et signaux de désinstallation sont suivis séparément et peuvent arriver plus tard. Utilisez les analyses au niveau des étapes et des Campaigns conjointement avec la [résolution des problèmes push]({{site.baseurl}}/user_guide/channels/push/troubleshooting) lorsque les **envois** et les indicateurs en aval semblent désalignés.

## Étapes suivantes {#next-steps}

- [Configuration des notifications push]({{site.baseurl}}/user_guide/channels/push/push_setup)
- [Créer un message push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)