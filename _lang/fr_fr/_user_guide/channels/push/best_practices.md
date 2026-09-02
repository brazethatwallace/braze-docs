---
page_order: 22
nav_title: Bonnes pratiques
article_title: Bonnes pratiques pour les notifications push
description: "Cette page présente les bonnes pratiques et les cas d'usage des notifications push pour que vos messages suscitent l'engagement plutôt que l'agacement."
channel: push
---

# Bonnes pratiques pour les notifications push {#push-best-practices}

> Cette page présente les bonnes pratiques et les cas d'usage des notifications push pour que vos messages suscitent l'engagement plutôt que l'agacement.

Les notifications push sont des outils puissants pour interagir avec les utilisateurs de votre application, mais elles doivent être utilisées avec précaution afin de garantir la diffusion de messages pertinents et opportuns. Avant d'envoyer votre notification push, consultez les bonnes pratiques suivantes pour connaître les points importants à vérifier.

{% alert important %}
Vos notifications push doivent respecter les directives de l'Apple App Store et les politiques du Google Play Store, notamment en ce qui concerne l'utilisation des notifications push comme publicités, spam, promotions, etc. Sur cette page, consultez la section [Réglementations relatives aux notifications push](#push-message-regulations).
{% endalert %}

## Rédigez votre notification push {#compose-your-push-message}

Il est recommandé de limiter chaque ligne de texte à environ 30 à 40 caractères, aussi bien pour le titre optionnel que pour le corps du message d'une notification push mobile. Notez que le compteur de caractères du compositeur ne tient pas compte des caractères Liquid. Cela signifie que le nombre final de caractères d'un message dépend de la manière dont Liquid s'affiche pour chaque utilisateur. En cas de doute, privilégiez la concision.

## Réduire la taille du payload des notifications push {#reduce-push-notification-payload-size}

La taille maximale du payload dépend de la plateforme.

| Plateforme | Taille maximale du payload |
| --- | --- |
| Web | 3 807 octets |
| Android | 3 930 octets |
| iOS | 3 960 octets |
| Kindle | 5 985 octets |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Réduire la taille du payload des notifications push" }

Si votre notification push dépasse la taille maximale du payload, le message peut ne pas être envoyé. En tant que bonne pratique, limitez votre payload à quelques centaines d'octets.

### Qu'est-ce qu'un payload de notification push ? {#what-is-a-push-payload}

Les fournisseurs de services push déterminent si votre notification push peut être affichée à un utilisateur en examinant la taille en octets de l'ensemble du payload. Le payload est limité à **4 Ko (4 096 octets)** pour la plupart des services push, notamment :

- Apple Push Notification service (APNs)
- Firebase Cloud Messaging (FCM) d'Android
- Notification push Web
- Notification push Huawei

Ces services push refuseront toute notification dépassant cette limite.

Braze réserve une partie du payload pour l'intégration et l'analyse. En conséquence, notre taille maximale de payload est de **3 807 octets**. Si votre notification push dépasse cette taille, le message peut ne pas être envoyé. En tant que bonne pratique, limitez votre payload à quelques centaines d'octets.

Les éléments suivants de votre notification push composent votre payload :

- Le texte, tel que le titre et le corps du message
- Le rendu final de toute personnalisation Liquid
- Les URL des images (mais pas la taille de l'image elle-même)
- Les URL des cibles de clic
- Les noms des boutons
- Les paires clé-valeur

### Conseils pour réduire la taille du payload {#tips-to-reduce-payload-size}

Pour réduire la taille du payload :

- Gardez votre message bref. Une bonne règle générale consiste à le rendre exploitable et utile en moins de 40 caractères.
- Supprimez les espaces superflus et les retours à la ligne de votre texte.
- Réfléchissez à la façon dont Liquid sera rendu lors de l'envoi. Le rendu final de toute personnalisation Liquid variant d'un utilisateur à l'autre, Braze ne peut pas déterminer si un payload de notification push dépassera la limite de taille lorsque Liquid est inclus. Si votre Liquid produit un message plus court, cela peut convenir. En revanche, si votre Liquid génère un message plus long, votre notification push peut dépasser la limite de taille du payload. Testez toujours votre notification push sur un appareil réel avant de l'envoyer aux utilisateurs.
- Envisagez de raccourcir les URL à l'aide d'un raccourcisseur d'URL.

## Optimiser le ciblage {#optimize-targeting}

### Collecter des données utilisateur pertinentes {#collect-relevant-user-data}

Les notifications push doivent être utilisées avec soin pour cibler les utilisateurs avec des notifications pertinentes et envoyées au bon moment. Braze collecte des informations utiles sur les appareils et l'utilisation qui peuvent servir à cibler des Segments pertinents. Ces informations doivent être complétées par des événements personnalisés et des attributs spécifiques à votre application. En exploitant ces données, vous pouvez cibler précisément vos messages pour augmenter les taux d'ouverture et réduire les cas où les utilisateurs désactivent les notifications push.

### Créer une page de paramètres de notification {#create-a-notification-settings-page}

Vous pouvez créer une page de paramètres dans votre application qui permet aux utilisateurs de vous indiquer quelles notifications ils souhaitent recevoir. Une approche courante consiste à créer un attribut personnalisé booléen dans Braze correspondant au statut du paramètre dans l'application. Par exemple, une application d'actualités pourrait proposer des paramètres d'abonnement pour les dernières nouvelles, les actualités sportives ou la politique.

Lorsque l'application d'actualités souhaite créer une Campaign ciblant uniquement les utilisateurs intéressés par la politique, il suffit d'ajouter le filtre d'attribut `Subscribes to Politics` au Segment. Lorsqu'il est défini sur vrai, seuls les utilisateurs abonnés aux notifications les recevront.

Pour plus d'informations sur la définition d'attributs personnalisés, consultez les articles suivants pour [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android) ou [REST API]({{site.baseurl}}/api/objects_filters/user_attributes_object).

## Augmenter les abonnements et la pertinence {#increase-opt-ins-and-relevance}

### Obtenir l'autorisation des utilisateurs {#obtain-user-permission}

Les statistiques générales relatives à l'activation des notifications push correspondent au fait que l'utilisateur a approuvé les notifications auprès de son système d'exploitation. Si des utilisateurs désactivent les notifications sur iOS, ils seront automatiquement retirés de notre système, car Apple ne permet pas l'envoi du jeton push.

Android 13 et versions ultérieures nécessitent l'obtention d'une autorisation avant que les notifications push puissent être affichées. Les versions antérieures d'Android abonnent les utilisateurs aux notifications par défaut.

### Préparer les utilisateurs aux notifications push {#prime-users-for-push}

Vous n'avez qu'une seule occasion de demander à un utilisateur l'autorisation d'envoyer des notifications push, et après un refus, il est très difficile de le convaincre de réactiver les notifications push dans les paramètres de son appareil. C'est pourquoi vous devriez préparer les utilisateurs aux notifications push à l'aide d'un message in-app avant d'afficher l'invite système. Consultez [Messages in-app d'amorce push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) pour en savoir plus sur l'augmentation des abonnements.

### Ajouter des contrôles d'abonnement aux notifications push {#add-push-subscription-controls}

Pour éviter que les utilisateurs ne désactivent les notifications au niveau de l'appareil, ce qui supprime complètement leur jeton push de premier plan, laissez-les contrôler leur abonnement push directement dans votre application. Consultez [Mettre à jour les états d'abonnement push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states) pour plus de détails.

### Utiliser la planification avancée ou ajouter des délais {#use-advanced-scheduling-or-add-delays}

En fonction de la taille de votre audience et du temps à l'avance prévu pour l'envoi de votre notification push, des retards dans la réception des notifications push peuvent survenir. Le temps nécessaire pour envoyer des notifications push dépend de la puissance de traitement allouée. Par exemple, si votre notification push utilise plusieurs appels de contenu connecté, cela peut augmenter la complexité de la mise en forme du message push et entraîner des vitesses limitées par la rapidité avec laquelle vos API tierces renvoient les données.

Un payload push plus léger et une priorité de notification plus élevée peuvent aider à réduire les retards et à dimensionner vos messages. Vous pouvez ajouter `Push Enabled = true` dans votre filtre d'audience afin de réduire la taille de l'audience pour que seuls les utilisateurs ayant activé les notifications push soient traités pour l'envoi de la Campaign.

Nous recommandons également de minimiser le nombre d'appels API en optimisant les données dont vous avez besoin. Si possible, essayez d'obtenir toutes les données nécessaires en un seul appel API plutôt que d'effectuer plusieurs appels.

### Comprendre les états d'abonnement push {#understand-push-subscription-states}

L'état d'abonnement push ne garantit pas qu'une notification push sera réceptionnée — les utilisateurs doivent également avoir les notifications push activées pour recevoir des notifications. En effet, un profil utilisateur peut posséder plusieurs appareils avec des autorisations de notification push de premier plan différentes, mais un seul état d'abonnement push.

Si un utilisateur ne dispose pas d'un jeton push de premier plan valide pour une application (c'est-à-dire qu'il a désactivé les jetons push au niveau de l'appareil via les paramètres, choisissant de ne pas recevoir de notifications), son état d'abonnement peut toujours être considéré comme `subscribed` aux notifications push. Cependant, cet utilisateur ne serait pas `Foreground Push Enabled for App` dans Braze, car le jeton push de premier plan n'est pas valide.

De plus, si un profil utilisateur n'a pas de jeton push valide ou enregistré pour d'autres applications, son filtre `Foreground Push Enabled` dans la segmentation sera également faux.

## Mettre en place une politique de désengagement pour les utilisateurs non réactifs {#implement-a-sunset-policy-for-unresponsive-users}

Même lorsque vous envoyez uniquement des notifications push pertinentes et opportunes, certains utilisateurs peuvent rester non réactifs et les percevoir comme du spam. Si un utilisateur montre un historique d'ignorance répétée de vos notifications push, il est judicieux de cesser de lui en envoyer avant qu'il ne soit agacé par les communications de votre application ou qu'il ne la désinstalle complètement.

Pour ce faire, créez une [politique de désengagement]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies) qui finit par cesser d'envoyer des notifications push aux utilisateurs n'ayant pas eu d'ouverture directe ou influencée depuis longtemps.

1. Identifiez les utilisateurs non réactifs en fonction des ouvertures directes ou influencées.
2. Réduisez progressivement l'envoi de notifications push à ces utilisateurs.
3. Avant de supprimer entièrement les notifications push, envoyez une dernière notification expliquant pourquoi ils n'en recevront plus. Cela donne aux utilisateurs la possibilité de manifester leur intérêt pour continuer à recevoir des notifications push en ouvrant cette dernière notification.
4. Une fois la politique de désengagement en vigueur, utilisez un [message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages) pour rappeler à ces utilisateurs que, bien qu'ils ne recevront plus de notifications push, les canaux de messages in-app continueront à leur fournir des informations intéressantes et utiles.

Bien que vous puissiez être réticent à cesser d'envoyer des notifications push aux utilisateurs qui se sont initialement abonnés, n'oubliez pas que d'autres canaux de communication peuvent atteindre ces utilisateurs de manière plus efficace, surtout s'ils ont précédemment ignoré vos notifications push. Si l'utilisateur ouvre vos e-mails, les Campaigns par e-mail constituent un bon moyen de le contacter en dehors de votre application. Dans le cas contraire, les messages in-app sont le meilleur moyen de diffuser du contenu sans risquer que l'utilisateur désinstalle votre application.

## Définir des événements de conversion pour les ouvertures d'application {#set-conversion-events-for-app-opens}

Lorsque vous attribuez des [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) à une Campaign push, vous pouvez suivre les ouvertures d'application pendant une certaine période après la réception de la Campaign. Définir un événement de conversion pour les ouvertures d'application fournit des informations différentes des statistiques de résultats que vous recevez habituellement après une Campaign push.

Bien que tous les résultats d'une Campaign push détaillent les ouvertures directes et les ouvertures totales d'un message (qui incluent à la fois les ouvertures directes et les [ouvertures influencées]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens)), le suivi des conversions comptabilise tout type d'ouverture, qu'elle soit directe ou influencée.

De plus, en utilisant l'événement de conversion « ouvre l'application », vous suivez les ouvertures d'application qui se produisent avant la date limite de conversion (par exemple, trois jours). Cela diffère d'une ouverture influencée, car le délai dont dispose un utilisateur pour enregistrer une ouverture influencée peut varier d'une personne à l'autre, en fonction du comportement d'engagement passé de chaque utilisateur.

## Réglementations relatives aux notifications push {#push-message-regulations}

Comme les notifications push sont un type de message intrusif qui s'affiche directement sur le téléphone ou le navigateur de votre client, il existe des directives pour l'envoi de notifications push via les applications et les sites.

### Réglementations relatives aux notifications push mobiles pour les applications {#mobile-push-regulations-for-apps}

| Politiques de l'Apple App Store |
| --- |
| [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) Inacceptable : (i) Créer une interface permettant d'afficher des applications, extensions ou plug-ins tiers de manière similaire à l'App Store ou sous forme de collection d'intérêt général. |
| [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) Les notifications push ne doivent pas être nécessaires au fonctionnement de l'application et ne doivent pas être utilisées pour envoyer des informations personnelles sensibles ou confidentielles. Les notifications push ne doivent pas être utilisées à des fins de promotion ou de marketing direct, sauf si les clients ont explicitement choisi de les recevoir par le biais d'un consentement affiché dans l'interface utilisateur de votre application, et si vous fournissez dans votre application une méthode permettant à l'utilisateur de refuser de recevoir de tels messages. |
| [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) Vous ne pouvez pas monétiser les fonctionnalités intégrées fournies par le matériel ou le système d'exploitation, telles que les notifications push, l'appareil photo ou le gyroscope ; ni les services et technologies Apple, tels que l'accès à Apple Music, le stockage iCloud ou les API Screen Time. |
{: .reset-td-br-1 aria-label="Réglementations relatives aux notifications push mobiles pour les applications" }

| Politique du Google Play Store |
| --- |
| [Utilisation non autorisée ou imitation de fonctionnalités système](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) Nous n'autorisons pas les applications ou les publicités qui imitent ou interfèrent avec les fonctionnalités système, telles que les notifications ou les avertissements. Les notifications au niveau du système ne peuvent être utilisées que pour les fonctionnalités essentielles d'une application, comme une application de compagnie aérienne qui informe les utilisateurs d'offres spéciales, ou un jeu qui notifie les utilisateurs de promotions en jeu. |
{: .reset-td-br-1 aria-label="Réglementations relatives aux notifications push mobiles pour les applications" }

## Articles connexes {#related-articles}

Vous n'avez pas trouvé ce que vous cherchiez ? Consultez ces articles supplémentaires sur les bonnes pratiques :

- [Formats des messages et images pour les notifications push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)
- [Messages in-app d'amorce push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)
- [Livrabilité pour les appareils Android chinois]({{site.baseurl}}/user_guide/channels/push/best_practices/chinese_push_deliverability)
- [Ce qu'il faut savoir avant d'envoyer : canaux]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send)