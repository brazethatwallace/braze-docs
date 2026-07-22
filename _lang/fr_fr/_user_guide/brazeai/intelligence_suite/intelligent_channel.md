---
nav_title: Filtre de canal
article_title: Filtre de canal intelligent
page_order: 1.5
description: "Cet article traite du filtre de canal intelligent, un filtre qui sélectionne la partie de votre audience pour laquelle le canal de communication sélectionné est son meilleur canal. Dans ce cas, « le meilleur » signifie celui qui a la plus forte probabilité d'engagement, compte tenu de l'historique de l'utilisateur."
search_rank: 11
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"} Filtre de canal intelligent {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecommost-engaged-channel-stylefloatrightwidth120pxborder0-classnoimgborderintelligent-channel-filter}

> Le filtre `Intelligent Channel` (précédemment `Most Engaged`) sélectionne la partie de votre audience pour laquelle le canal de communication sélectionné est leur « meilleur » canal.

## À propos du filtre {#about-the-filter}

![Le filtre de canal intelligent avec une liste déroulante pour les différents canaux pouvant être sélectionnés.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

Dans ce cas, « le meilleur » signifie le canal qui a la plus forte probabilité d'engagement, compte tenu de l'historique de l'utilisateur. Vous pouvez sélectionner l'e-mail, le SMS, WhatsApp, les notifications push Web ou les notifications push mobiles (incluant tout système d'exploitation ou appareil mobile disponible) en tant que canal.

Le canal intelligent calcule un taux d'engagement pour chaque utilisateur sur chaque canal pris en charge, classe ces canaux, et considère le canal le mieux classé comme le meilleur canal de cet utilisateur.

Pour activer le filtre de canal intelligent, sélectionnez le filtre **Intelligent Channel** sur la page **Target Audiences** lors de la création d'une Campaign ou d'un Canvas.

## Comment l'engagement est calculé par canal {#how-engagement-is-calculated-by-channel}

Le canal intelligent compare les canaux à l'aide d'un taux d'engagement : le nombre d'interactions avec les messages divisé par le nombre de messages reçus. Braze évalue jusqu'aux 100 derniers messages reçus par canal au cours des six derniers mois.

Chaque fois qu'un message est envoyé à un utilisateur ou qu'un utilisateur interagit avec un message, le taux d'engagement est recalculé en quelques secondes. Un utilisateur ne peut être compté comme ayant interagi avec un message qu'une seule fois (par exemple, une ouverture et un clic sur le même e-mail feront que ce message sera marqué comme ayant généré une interaction une seule fois, et non deux).

### Données d'interaction par canal {#interaction-data-by-channel}

Braze suit les événements suivants lors du calcul des taux d'engagement :

- **E-mail :** ouvertures (les [ouvertures automatiques]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) sont exclues). Les clics sur les e-mails ne sont pas inclus.
- **Notification push mobile :** ouvertures directes. Chaque plateforme mobile (comme iOS, Android et Kindle) est évaluée séparément. Les ouvertures influencées par les notifications push ne sont pas incluses.
- **Notification push Web :** ouvertures
- **SMS :** clics sur les liens raccourcis
- **WhatsApp :** lectures de messages ou clics sur les liens suivis

Les ouvertures influencées par les notifications push, les clics sur les e-mails et l'activité de session ne sont pas utilisés par le canal intelligent. L'activité de session est utilisée par le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#about-intelligent-timing).

Le canal intelligent ne prend pas en charge les webhooks, LINE, Kakao Talk, les In-App Messages ou les Content Cards.

{% alert important %}
Pour calculer le taux d'engagement du canal SMS, activez le [raccourcissement des liens SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) avec suivi avancé et suivi des clics. Sans ce suivi, le SMS peut être sélectionné comme canal intelligent avec un taux d'engagement de 0 % en raison de notre [comportement de départage]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel#tie-breaking).
{% endalert %}

## Données insuffisantes {#not-enough-data}

Pour que Braze détermine quel canal est « le meilleur », il doit disposer de suffisamment de données. Cela signifie qu'un utilisateur doit avoir reçu au moins trois messages ou plus sur un canal avant que ce canal puisse être classé, et doit disposer de données suffisantes sur au moins deux canaux pris en charge.

Si les utilisateurs n'ont pas reçu suffisamment de messages sur les différents canaux, ils basculeront dans l'option « Not Enough Data » de ce filtre. Cela vous permet d'utiliser n'importe quel canal de communication pris en charge pour cibler ces utilisateurs.

Supposons par exemple que vous souhaitiez que les utilisateurs qui préfèrent les notifications push en reçoivent et que les utilisateurs ne disposant pas de données suffisantes reçoivent le même message push. Dans ce cas, vous pourriez définir le filtre de canal intelligent sur **Mobile push** et utiliser **OR** pour ajouter un second filtre de canal intelligent défini sur **Not Enough Data**. Une Campaign séparée avec le filtre de canal intelligent réglé sur l'e-mail pourrait cibler les utilisateurs qui préfèrent ce canal.

![Filtres de canal intelligents pour les notifications push mobiles ou en cas de données insuffisantes.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
Les Campaigns et les étapes du Canvas qui ignorent la [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-rules) ne sont pas prises en compte par le canal intelligent et ne peuvent pas contribuer aux exigences en matière de données.
{% endalert %}

## Notification push mobile {#mobile-push}

La notification push mobile intègre Android, iOS, Kindle ainsi que les autres canaux d'appareils mobiles disponibles sur Braze. Braze évalue chaque plateforme mobile séparément lors du calcul des taux d'engagement.

Lorsque vous utilisez le filtre de canal intelligent défini sur **Mobile push**, un utilisateur correspond si la notification push iOS ou Android est son canal le mieux classé. Cela ne force pas l'utilisateur à recevoir des notifications push sur un appareil spécifique. Le classement est uniquement utilisé pour déterminer si la notification push mobile est le meilleur canal de cet utilisateur par rapport à l'e-mail, la notification push Web, le SMS et WhatsApp.

## Filtre de probabilité d'ouverture des messages pour chaque canal {#individual-channels}

Plutôt que de laisser Braze sélectionner le meilleur canal pour un utilisateur, vous pouvez utiliser le [filtre de segmentation « Message Open Likelihood »]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#message-open-likelihood) pour filtrer les utilisateurs en fonction de leur probabilité d'ouvrir un message sur un canal spécifique de votre choix. Ce filtre est calculé en divisant le pourcentage d'interactions par le nombre total de messages reçus pour les 100 derniers messages envoyés par canal.

Le filtre Message Open Likelihood utilise les mêmes données d'engagement sous-jacentes que le canal intelligent, mais vous permet de définir un seuil pour un canal unique au lieu de sélectionner le meilleur canal de l'utilisateur. Il est disponible pour l'e-mail, la notification push mobile, le SMS et la notification push Web.

Notez qu'un utilisateur doit avoir reçu au moins trois messages sur un canal spécifique avant de pouvoir obtenir un score de probabilité pour ce canal. Les utilisateurs sans données suffisantes pour mesurer une probabilité pour un canal peuvent être sélectionnés en utilisant « is blank ».

## Bonnes pratiques et stratégie d'utilisation efficace {#best-practices-and-effective-use-strategy}

### Départage {#tie-breaking}

Comme certains utilisateurs reçoivent peu de messages, il n'est pas rare d'observer des taux d'engagement identiques entre les canaux disponibles pour un utilisateur donné (par exemple, un utilisateur ayant un taux d'engagement de 20 % à la fois pour l'e-mail et la notification push mobile). Dans ce cas, les égalités sont départagées en priorisant (en attribuant un classement plus élevé à) le canal avec les événements d'interaction les plus récents.

Si les canaux à égalité ont tous un taux d'engagement de 0 %, Braze départage en utilisant le canal ayant reçu le message le plus récent.

### Canaux inaccessibles {#unreachable-channels}

Un utilisateur peut disposer de suffisamment de données pour que Braze détermine un classement de canaux, mais devenir ensuite inaccessible sur son canal le mieux classé. Par exemple, un utilisateur dont le meilleur canal historique est l'e-mail peut s'être récemment désabonné de l'e-mail. Si vous envoyez un message sur ce canal, il ne sera pas distribué à cet utilisateur. Les utilisateurs inaccessibles sur des canaux spécifiques doivent être ciblés ou redirigés séparément.

### Dimensionnement de l'audience {#audience-sizing}

Le canal intelligent vous permet de cibler de manière sélective et en amont la part des utilisateurs qui ont une probabilité beaucoup plus élevée d'interagir avec un message que le reste de votre audience. Cela ne représente probablement pas la majorité des utilisateurs d'une audience typique. Attendez-vous plutôt à ce que ce filtre identifie 5 à 20 % de votre audience habituelle, c'est-à-dire les utilisateurs ayant un historique d'engagement avéré sur un canal particulier.