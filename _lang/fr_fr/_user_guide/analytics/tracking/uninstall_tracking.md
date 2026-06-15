---
nav_title: Suivi des désinstallations
article_title: Suivi des désinstallations
page_order: 1
page_type: reference
description: "Cet article de référence couvre la mise en œuvre du suivi des désinstallations pour les statistiques au niveau de la campagne et de l'application."
tool: Reports

---

# Suivi des désinstallations {#uninstall-tracking}

> Cet article montre comment visualiser l'ensemble des désinstallations d'applications au fil du temps pour repérer les tendances et les anomalies, et suivre les désinstallations au niveau des Campaigns pour déterminer si une Campaign spécifique favorise ou empêche les installations d'applications.

Le suivi des désinstallations dans Braze fournit les détails suivants :

1. Statistiques quotidiennes de désinstallation au niveau de l'application dans un graphique chronologique sur la page **d'accueil**.
2. Statistiques de désinstallation au niveau de la Campaign dans un graphique chronologique sur la page **Détails de la Campaign** d'une Campaign spécifique. Cette statistique indique le nombre de destinataires de la Campaign qui désinstallent chaque jour.

{% alert note %}
Il est nécessaire d'activer le suivi des désinstallations sur votre tableau de bord de Braze. Cette fonctionnalité est disponible pour les applications sur iOS, Android et Fire OS.
{% endalert %}

## Fonctionnement {#how-it-works}

Braze collecte automatiquement des informations basiques sur les désinstallations dans le cadre de vos Campaigns de notification push habituelles. Cependant, comme la fréquence à laquelle les différents utilisateurs reçoivent des Campaigns push peut varier, nous proposons un suivi des désinstallations pour fournir un aperçu plus précis de l'activité de désinstallation parmi vos utilisateurs.

Lorsque Braze détecte une désinstallation, l'utilisateur est marqué comme ayant désinstallé l'application. Si vous utilisez le filtre **N'a pas désinstallé** dans une Campaign, ces utilisateurs marqués sont exclus. Si un utilisateur réinstalle l'application sans l'ouvrir, le marqueur de désinstallation reste sur son profil. Ce marqueur n'est supprimé que lorsque l'utilisateur démarre une nouvelle session dans l'application réinstallée. Cela signifie qu'un utilisateur qui réinstalle l'application sans jamais l'ouvrir continue d'apparaître comme ayant désinstallé.

Pour en savoir plus sur l'utilisation du suivi des désinstallations, consultez notre article de blog [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Activer le suivi des désinstallations {#turning-on-uninstall-tracking}

Vous pouvez activer le suivi des désinstallations sur la page **Paramètres des applications**, sous **Paramètres**, pour chaque application que vous souhaitez suivre.

Lorsque vous activez le suivi des désinstallations pour une application, Braze envoie chaque nuit un message push en arrière-plan aux utilisateurs qui n'ont pas enregistré de session ou reçu de push au cours des dernières 24 heures.

### Configuration {#configuration}

Pour configurer le suivi des désinstallations pour votre application iOS, utilisez une [méthode utilitaire]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls/?sdktab=swift). Pour votre application Android, utilisez [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html). Lorsque Braze détecte une désinstallation, qu'il s'agisse du suivi des désinstallations ou de la distribution normale d'une Campaign push, nous enregistrons la meilleure estimation de l'heure de désinstallation sur le profil de l'utilisateur. Cette information est stockée dans le profil utilisateur en tant qu'attribut standard et peut être utilisée pour définir un segment d'utilisateurs pour les Campaigns de reconquête.

## Filtrage des segments en fonction des désinstallations {#filtering-segments-by-uninstalls}

Le filtre **Désinstallé** sélectionne les utilisateurs qui ont désinstallé votre application dans une période donnée. Comme il est difficile de déterminer l'heure exacte d'une désinstallation, nous recommandons d'utiliser des plages de temps plus larges pour les filtres de désinstallation afin de s'assurer que toutes les personnes ayant désinstallé l'application soient incluses dans le segment à un moment donné.

Les statistiques quotidiennes sur les désinstallations sont disponibles sur la page **d'accueil**.

![Segment de désinstallation.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

Le graphique peut être décomposé par application et par segment, à l'instar d'autres statistiques fournies par Braze. Dans la section **Performance overview**, sélectionnez votre plage de dates et, si vous le souhaitez, une application. Ensuite, faites défiler la page jusqu'au graphique **Performance Over Time** et procédez comme suit :

1. Dans le menu déroulant **Statistics For**, sélectionnez **Uninstalls**.
2. Dans le menu déroulant **Breakdown**, sélectionnez **By Segment**.
3. Dans le menu déroulant **Breakdown Values**, sélectionnez les segments à inclure dans le graphique.

{% alert note %}
Les applications sans suivi des désinstallations activé n'affichent les désinstallations que pour un sous-ensemble de leurs utilisateurs (ceux qui ont été ciblés avec des notifications push). Le nombre total de désinstallations quotidiennes peut donc être plus élevé que celui affiché.
{% endalert %}

## Suivi des désinstallations pour les Campaigns {#uninstall-tracking-for-campaigns}

Le suivi des désinstallations de Campaigns indique le nombre d'utilisateurs qui ont reçu une Campaign spécifique et qui ont ensuite désinstallé votre application dans le délai sélectionné. Cet outil permet de comprendre comment les Campaigns peuvent encourager des comportements négatifs involontaires de la part des utilisateurs et aide à mesurer l'efficacité globale de la Campaign.

Les statistiques de désinstallation des Campaigns se trouvent sur la page **Campaign Analytics** d'une Campaign spécifique. Pour les Campaigns multicanaux et multivariées, les désinstallations peuvent être ventilées respectivement par canal et par variante.

![Désinstallation au niveau de la Campaign.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### Fonctionnement

Braze suit les désinstallations en observant lorsque les messages push envoyés aux appareils des utilisateurs renvoient un signal provenant de Firebase Cloud Messaging (FCM) ou d'Apple Push Notification Service (APNs) indiquant que l'application n'est plus installée. Si vous activez le suivi global des désinstallations pour une application, Braze envoie quotidiennement un message push silencieux aux utilisateurs afin de détecter s'ils ont désinstallé l'application. Braze envoie cette notification « silencieuse » à tous les utilisateurs (à moins que l'utilisateur n'ait désactivé les notifications silencieuses dans les paramètres de son application) ; la notification n'apparaît pas aux utilisateurs. Si Braze détecte qu'un utilisateur a désinstallé l'application, nous :

* Incrémentons d'une unité le nombre total de désinstallations de l'application.
* Incrémentons d'une unité le nombre de désinstallations pour chaque Campaign que l'utilisateur a reçue avec succès au cours des dernières 24 heures.
* Si un utilisateur reçoit trois Campaigns au cours d'une période de 24 heures puis désinstalle l'application, nous incrémentons le nombre de « désinstallations » pour les trois Campaigns.

FCM et APNs imposent des restrictions sur le suivi des désinstallations. Braze incrémente uniquement le nombre de désinstallations lorsque FCM ou APNs nous informe qu'un utilisateur a désinstallé l'application. Cependant, ces systèmes tiers peuvent nous notifier les désinstallations à tout moment. Utilisez le suivi des désinstallations pour identifier les tendances générales plutôt que pour obtenir des statistiques précises.

Braze traite les réponses FCM suivantes comme des réponses de suppression de jeton (désinstallation) : `DEVICE_UNREGISTERED`, `BAD_REGISTRATION` et `SENDER_ID_MISMATCH`.

Pour en savoir plus sur l'utilisation du suivi des désinstallations, consultez notre article de blog [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Résolution des problèmes {#troubleshooting}

### Pourquoi le nombre de désinstallations augmente-t-il soudainement ? {#why-am-i-suddenly-seeing-a-spike-in-uninstalls}

Si vous constatez un pic de désinstallations de l'application, cela peut être dû à la révocation des anciens jetons à une fréquence différente par Firebase Cloud Messaging (FCM) et Apple Push Notification Service (APNs).

{% alert note %}
Pour des raisons de confidentialité, les fournisseurs de services push de Braze peuvent révoquer les jetons à intervalles irréguliers, ce qui signifie que le nombre de désinstallations peut parfois augmenter de manière significative au cours d'une période donnée.<br><br>Pour valider ces variations, surveillez le suivi des désinstallations parallèlement à un indicateur d'action utilisateur, tel que le taux d'ouverture directe des notifications push. Si les désinstallations augmentent fortement mais que les ouvertures directes restent stables, le pic reflète probablement la révocation d'anciens jetons par un fournisseur plutôt que le comportement réel des utilisateurs.
{% endalert %}

### Comment déterminer si une Campaign spécifique a provoqué des désinstallations ? {#how-do-i-determine-if-a-specific-campaign-caused-uninstalls}

Vérifiez les analyses des Campaigns qui ont envoyé des messages au moment où le pic de désinstallations s'est produit. Si un message particulier est corrélé à une augmentation des désinstallations, il est possible qu'il incite les utilisateurs à désinstaller l'application.

Pour afficher les désinstallations par segment :
1. Accédez à la page **d'accueil** du tableau de bord.
2. Dans la section **Performance Over Time**, sélectionnez **Uninstalls** pour **Statistics For** et **By Segment** pour **Breakdown**.

Si vous disposez d'un segment qui suit les utilisateurs inactifs avec le [suivi analytique]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) activé, comparez sa tendance de désinstallation à la tendance globale de l'application.

### Comment confirmer que les désinstallations sont réelles ? {#how-do-i-confirm-uninstalls-are-genuine}

Pour APNs, vérifiez les profils utilisateurs pour l'erreur push `BadDeviceToken`. Si vous constatez cette erreur en masse dans la même période que le pic de désinstallations, les désinstallations sont probablement réelles. `BadDeviceToken` indique que le jeton push de l'appareil n'est plus valide, ce qui se produit généralement lorsque l'application est désinstallée.

### Pourquoi le nombre de désinstallations d'applications diffère-t-il de ce qui figure dans APNs ? {#why-are-the-number-of-app-uninstalls-different-from-whats-in-apns}

Cette différence est normale.

Apple utilise une planification aléatoire pour retarder le signalement lorsqu'un jeton push devient invalide, ce qui signifie que même après qu'un utilisateur a désinstallé une application, APNs peut continuer à renvoyer des réponses positives aux notifications push pendant un certain temps. Ce délai est intentionnel et vise à protéger la vie privée des utilisateurs. Aucun rebond ou échec ne sera signalé tant qu'APNs ne renvoie pas un statut `410` pour un jeton invalide.