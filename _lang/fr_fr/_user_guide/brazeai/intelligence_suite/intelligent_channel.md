---
nav_title: Filtre de canal
article_title: Filtre de canal intelligent
page_order: 1.5
description: "Cet article traite du filtre de canal intelligent, un filtre qui sélectionne la partie de votre audience pour laquelle le canal de communication sélectionné est son meilleur canal. Dans ce cas, « le meilleur » signifie celui qui a la plus forte probabilité d'engagement, compte tenu de l'historique de l'utilisateur."
search_rank: 11
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"} Filtre de canal intelligent {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecommost-engaged-channel-stylefloatrightwidth120pxborder0-classnoimgborderintelligent-channel-filter}

> Le filtre `Intelligent Channel` (précédemment `Most Engaged`) sélectionne la partie de votre audience pour laquelle le canal de communication sélectionné est leur « meilleur » canal.

## À propos du filtre de canal {#about-the-channel-filter}

![Le filtre de canal intelligent avec une liste déroulante pour les différents canaux pouvant être sélectionnés.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

Dans ce cas, « le meilleur » signifie le canal qui a la plus forte probabilité d'engagement, compte tenu de l'historique de l'utilisateur. Vous pouvez sélectionner l'e-mail, le SMS, WhatsApp, les notifications push Web ou les notifications push mobiles (incluant tout système d'exploitation ou appareil mobile disponible) en tant que canal.

Le canal intelligent calcule le taux d'engagement de chaque utilisateur pour chacun des canaux disponibles en prenant le rapport entre les interactions avec les messages (ouvertures ou clics) et le nombre de messages reçus au cours des six derniers mois d'activité. Les canaux disponibles sont classés selon leurs taux d'engagement respectifs et le canal ayant le rapport le plus élevé est considéré comme celui avec « le plus d'interactions » pour cet utilisateur.

Chaque fois qu'un message est envoyé à un utilisateur ou qu'un utilisateur interagit avec un message, le taux d'engagement est recalculé en quelques secondes. Un utilisateur ne peut être compté comme ayant interagi avec un message qu'une seule fois (par exemple, une ouverture et un clic sur le même e-mail feront que ce message sera marqué comme ayant généré une interaction une seule fois, et non deux).

Pour activer le filtre de canal intelligent, sélectionnez le filtre **Intelligent Channel** sur la page **Audiences cibles** lors de la création d'une Campaign d'e-mail, de notification push Web ou de notification push mobile.

{% alert important %}
Pour calculer le taux d'engagement du canal SMS, activez le [raccourcissement des liens SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) avec suivi avancé et suivi des clics. Sans ce suivi, le SMS peut être sélectionné comme canal intelligent avec un taux d'engagement de 0 % en raison de notre [comportement de départage]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel#tie-breaking).
{% endalert %}

## Option « Données insuffisantes » {#the-not-enough-data-option}

Pour que Braze détermine quel canal est « le meilleur », il doit disposer de suffisamment de données. Cela signifie qu'un utilisateur doit avoir reçu au moins trois messages ou plus par canal sur au moins deux des trois canaux disponibles. Les messages n'ont pas nécessairement besoin d'avoir été ouverts.

Si les utilisateurs n'ont pas reçu suffisamment de messages sur les différents canaux, ils basculeront dans l'option « Not Enough Data » de ce filtre. Cela vous permet d'utiliser n'importe lequel des trois canaux de communication disponibles pour cibler ces utilisateurs.

Supposons par exemple que vous souhaitiez que les utilisateurs qui préfèrent les notifications push en reçoivent et que les utilisateurs ne disposant pas de données suffisantes reçoivent le même message push. Dans ce cas, vous pourriez définir le filtre de canal intelligent sur **Mobile push** et utiliser **OR** pour ajouter un second filtre de canal intelligent défini sur **Not Enough Data**. Une Campaign séparée avec le filtre de canal intelligent réglé sur l'e-mail pourrait cibler les utilisateurs qui préfèrent ce canal.

![Filtres de canal intelligents pour les notifications push mobiles ou en cas de données insuffisantes.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
Les Campaigns et les étapes du Canvas qui ignorent la [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-rules) ne seront pas prises en compte par le canal intelligent et ne pourront pas contribuer aux exigences en matière de données.
{% endalert %}

## Option « Notification push mobile » {#the-mobile-push-option}

La notification push mobile intègre Android, iOS, Kindle ainsi que les autres canaux d'appareils mobiles disponibles sur Braze. Lors du calcul du canal intelligent, Braze examine chaque type d'appareil mobile séparément, puis choisit le taux d'engagement le plus élevé parmi eux pour représenter la catégorie « Mobile Push » lors de la comparaison avec l'e-mail et la notification push Web.

Par exemple, si un utilisateur dispose de plusieurs appareils mobiles, son taux d'engagement mobile sera représenté par le taux le plus élevé constaté parmi les appareils. Cela ne forcera toutefois pas l'utilisateur à recevoir des notifications push exclusivement sur cet appareil. Ce taux est uniquement utilisé lors de la comparaison avec l'e-mail et la notification push Web.

## Filtre de probabilité d'ouverture des messages pour chaque canal {#individual-channels}

Plutôt que de laisser Braze sélectionner le canal le plus approprié pour un utilisateur, vous pouvez utiliser le [filtre de segmentation « Message Open Likelihood »]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#message-open-likelihood) pour filtrer les utilisateurs en fonction de leur probabilité d'ouvrir un message sur un canal spécifique de votre choix. Ce filtre est calculé en divisant le pourcentage d'interactions par le nombre total de messages reçus pour les 100 derniers messages envoyés par canal.

Notez qu'un utilisateur doit avoir reçu au moins trois messages sur un canal spécifique avant de pouvoir obtenir un score de probabilité pour ce canal. Les utilisateurs sans données suffisantes pour mesurer une probabilité pour un canal peuvent être sélectionnés en utilisant « is blank ».

## Bonnes pratiques et stratégie d'utilisation efficace {#best-practices-and-effective-use-strategy}

### Départager les égalités {#tie-breaking}

Comme certains utilisateurs recevront peu de messages, il n'est pas rare d'observer des taux d'engagement identiques entre les canaux disponibles pour un utilisateur donné (par exemple, un utilisateur ayant un taux d'engagement de 0,2 à la **fois** pour l'e-mail et le push mobile). Dans ce cas, les égalités seront départagées en priorisant (en attribuant un classement plus élevé à) le canal avec les événements d'ouverture les plus récents.

### Canaux inaccessibles {#unreachable-channels}

Un utilisateur peut disposer de suffisamment de données pour que Braze détermine un classement de canaux, mais devenir ensuite inaccessible sur son canal le mieux classé. Par exemple, un utilisateur dont le meilleur canal historique est l'e-mail peut s'être récemment désabonné de l'e-mail. Si vous envoyez un message sur ce canal, il ne sera pas distribué à cet utilisateur. Les utilisateurs inaccessibles sur des canaux spécifiques doivent être ciblés ou redirigés séparément.

### Dimensionnement de l'audience {#audience-sizing}

Le canal intelligent vous permet de cibler de manière sélective et en amont la part des utilisateurs qui ont une probabilité beaucoup plus élevée d'interagir avec un message que le reste de votre audience. Cela ne représente probablement pas la majorité des utilisateurs d'une audience typique. Attendez-vous plutôt à ce que ce filtre identifie 5 à 20 % de votre audience habituelle, c'est-à-dire les utilisateurs ayant un historique d'engagement avéré sur un canal particulier.