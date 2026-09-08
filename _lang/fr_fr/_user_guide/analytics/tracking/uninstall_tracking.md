---
nav_title: Suivi des désinstallations
article_title: Suivi des désinstallations
page_order: 1
page_type: reference
description: "Cet article de référence couvre la mise en œuvre du suivi des désinstallations pour les statistiques au niveau de la Campaign et de l'application."
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

Braze collecte automatiquement un niveau de base d'informations sur les désinstallations à partir de vos Campaigns push classiques. Cependant, comme la fréquence à laquelle les différents utilisateurs reçoivent des Campaigns push peut varier, nous proposons le suivi des désinstallations pour fournir un aperçu plus précis de l'activité de désinstallation parmi vos utilisateurs.

Lorsque Braze détecte une désinstallation, l'utilisateur est marqué comme ayant désinstallé. Si vous utilisez le filtre **Has Not Uninstalled** dans une Campaign, ces utilisateurs marqués sont exclus. Si un utilisateur réinstalle l'application mais ne l'ouvre pas, l'étiquette de désinstallation reste sur son profil. L'étiquette n'est supprimée que lorsque l'utilisateur démarre une nouvelle session dans l'application réinstallée. Cela signifie qu'un utilisateur qui réinstalle l'application mais ne l'ouvre jamais continue d'apparaître comme ayant désinstallé.

Pour en savoir plus sur l'utilisation du suivi des désinstallations, consultez notre article de blog [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Activation du suivi des désinstallations {#turning-on-uninstall-tracking}

Vous pouvez activer le suivi des désinstallations sur la page **Paramètres de l'application**, sous **Paramètres**, pour chaque application que vous souhaitez suivre.

Lorsque vous activez le suivi des désinstallations pour une application, Braze envoie chaque nuit une notification push silencieuse en arrière-plan aux utilisateurs qui n'ont pas enregistré de session ni reçu de notification push au cours des dernières 24 heures.

### Configuration {#configuration}

Pour configurer le suivi des désinstallations pour votre application iOS, utilisez une [méthode utilitaire]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls?sdktab=swift). Pour votre application Android, utilisez [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html). Lorsque Braze détecte une désinstallation, que ce soit via le suivi des désinstallations ou la distribution normale d'une Campaign de notification push, l'heure estimée la plus précise de la désinstallation est enregistrée sur le profil utilisateur. Cette heure est stockée dans le profil utilisateur en tant qu'attribut standard et peut être utilisée pour définir un Segment d'utilisateurs pour des campagnes de reconquête.

## Filtrer les Segments par désinstallations {#filtering-segments-by-uninstalls}

Le filtre **Désinstallé** sélectionne les utilisateurs qui ont désinstallé votre application au cours d'une période donnée. Comme il est difficile de déterminer le moment exact d'une désinstallation, nous recommandons d'utiliser des plages de temps plus larges pour les filtres de désinstallation afin de s'assurer que tous les utilisateurs ayant désinstallé l'application soient inclus dans le Segment à un moment donné.

Les statistiques quotidiennes sur les désinstallations se trouvent sur la page **Accueil**.

![Segment de désinstallation.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

Le graphique peut être décomposé par application et par Segment, de manière similaire aux autres statistiques fournies par Braze. Dans la section **Aperçu des performances**, sélectionnez votre plage de dates et, si vous le souhaitez, une application. Ensuite, faites défiler jusqu'au graphique **Performance Over Time** et procédez comme suit :

1. Dans le menu déroulant **Statistics For**, sélectionnez **Uninstalls**.
2. Dans le menu déroulant **Breakdown**, sélectionnez **By segment**.
3. Dans le menu déroulant **Breakdown Values**, sélectionnez les Segments à inclure dans le graphique.

{% alert note %}
Les applications pour lesquelles le suivi des désinstallations n'est pas activé ne signaleront les désinstallations que pour un sous-ensemble de leurs utilisateurs (ceux ciblés par des notifications push), de sorte que le nombre total de désinstallations quotidiennes peut être supérieur à ce qui est affiché.
{% endalert %}

## Suivi des désinstallations pour les campagnes {#uninstall-tracking-for-campaigns}

Le suivi des désinstallations pour les Campaigns affiche le nombre d'utilisateurs qui ont reçu une Campaign spécifique et qui ont ensuite désinstallé votre application dans la période sélectionnée. Cet outil fournit des informations sur la manière dont les Campaigns peuvent encourager des comportements utilisateurs négatifs involontaires et aide à mesurer l'efficacité globale des Campaigns.

Les statistiques de désinstallation pour les Campaigns se trouvent sur la page **Campaign Analytics** d'une Campaign spécifique. Pour les Campaigns multicanaux et multivariantes, les désinstallations peuvent être réparties respectivement par canal et par variante.

![Désinstallations au niveau de la Campaign.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### Comment ça fonctionne

Braze suit les désinstallations en observant quand les notifications push envoyées aux appareils des utilisateurs renvoient un signal de Firebase Cloud Messaging (FCM) ou d'Apple Push Notification Service (APNs) indiquant que l'application n'est plus installée. Si vous activez le suivi global des désinstallations pour une application, Braze envoie quotidiennement une notification push silencieuse aux utilisateurs pour détecter s'ils ont désinstallé l'application. Braze envoie cette notification push « silencieuse » à tous les utilisateurs (sauf si l'utilisateur a désactivé les notifications push silencieuses dans les paramètres de son application) ; la notification push n'apparaît pas aux utilisateurs. Si Braze détecte qu'un utilisateur a désinstallé l'application, nous :

* Incrémentons le nombre total de désinstallations de l'application de un.
* Incrémentons le nombre de désinstallations de un pour chaque Campaign que l'utilisateur a reçue avec succès au cours des dernières 24 heures.
* Si un utilisateur reçoit trois Campaigns sur une période de 24 heures puis désinstalle l'application, nous incrémentons le compteur de « désinstallations » pour les trois Campaigns.

FCM et APNs imposent des restrictions sur le suivi des désinstallations. Braze incrémente le nombre de désinstallations uniquement lorsque FCM ou APNs nous informent qu'un utilisateur a désinstallé, mais ces systèmes tiers peuvent nous notifier des désinstallations à tout moment. Utilisez le suivi des désinstallations pour détecter des tendances directionnelles plutôt que des statistiques précises.

Braze traite une réponse FCM comme une réponse de suppression de jeton (désinstallation) lorsque FCM signale que le jeton d'enregistrement n'est plus valide, comme `DEVICE_UNREGISTERED` ou `NotRegistered`. Braze enregistre les autres erreurs de notification push comme des rebonds sans supprimer le jeton.

Pour en savoir plus sur l'utilisation du suivi des désinstallations, consultez notre article de blog [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Résolution des problèmes {#troubleshooting}

### Quand le profil d'un utilisateur est-il marqué comme désinstallé ? Quand l'étiquette de désinstallation est-elle supprimée ? {#when-is-a-users-profile-flagged-as-uninstalled-when-is-the-uninstall-tag-cleared}

Braze marque un utilisateur comme ayant désinstallé lorsqu'il détecte que l'application n'est plus sur l'appareil (consultez [Fonctionnement](#how-it-works) pour la détection avec les notifications push régulières et le suivi optionnel des désinstallations). Après la réinstallation de votre application, l'étiquette de désinstallation peut rester sur le profil de l'utilisateur jusqu'à ce qu'il **ouvre l'application et démarre une nouvelle session** — la simple réinstallation ne supprime pas l'étiquette. Jusqu'à cette session, les Segments et filtres utilisant l'état de désinstallation (par exemple **Has Not Uninstalled**) continuent de considérer l'utilisateur comme désinstallé.

### Pourquoi est-ce que je constate soudainement un pic de désinstallations ? {#why-am-i-suddenly-seeing-a-spike-in-uninstalls}

Si vous constatez un pic de désinstallations, cela peut être dû au fait que Firebase Cloud Messaging (FCM) et Apple Push Notification Service (APNS) révoquent les anciens jetons à une fréquence différente.

{% alert note %}
Pour des raisons de confidentialité, les fournisseurs de notifications push de Braze peuvent révoquer les jetons à des intervalles irréguliers, ce qui signifie que le nombre de désinstallations peut parfois augmenter brusquement sur une période donnée.<br><br>Pour valider ces changements, surveillez le suivi des désinstallations en parallèle d'un indicateur d'action utilisateur, comme le taux d'ouverture directe des notifications push. Si les désinstallations augmentent fortement mais que les ouvertures directes des notifications push restent stables, le pic reflète probablement la révocation d'anciens jetons par un partenaire plutôt qu'un comportement réel des utilisateurs.
{% endalert %}

### Comment déterminer si une Campaign spécifique a provoqué des désinstallations ? {#how-do-i-determine-if-a-specific-campaign-caused-uninstalls}

Vérifiez les analyses des Campaigns qui ont envoyé des messages autour de la même période que le pic de désinstallations. Si un message particulier est corrélé à une augmentation des désinstallations, il peut inciter les utilisateurs à désinstaller.

Pour consulter les désinstallations par Segment :
1. Accédez à la page **Accueil** du tableau de bord.
2. Dans la section **Performance Over Time**, sélectionnez **Uninstalls** pour **Statistics For** et **By Segment** pour **Breakdown**.

Si vous disposez d'un Segment suivant les utilisateurs inactifs avec le [suivi analytique]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) activé, comparez sa tendance de désinstallation à la tendance globale de l'application.

### Comment confirmer que les désinstallations sont authentiques ? {#how-do-i-confirm-uninstalls-are-genuine}

Pour APNs, vérifiez les profils utilisateurs pour l'erreur push `BadDeviceToken`. Si vous constatez cette erreur en masse autour de la même période que le pic de désinstallations, les désinstallations sont probablement authentiques. `BadDeviceToken` indique que le jeton push de l'appareil n'est plus valide, ce qui se produit généralement lorsque l'application est désinstallée.

### Pourquoi le nombre de désinstallations de l'application est-il différent de ce qui figure dans APNs ? {#why-are-the-number-of-app-uninstalls-different-from-whats-in-apns}

Cette différence est attendue.

Apple utilise un calendrier aléatoire pour retarder le signalement de l'invalidation d'un jeton push, ce qui signifie que même après la désinstallation d'une application par un utilisateur, APNs peut continuer à renvoyer des réponses positives aux notifications push pendant un certain temps. Ce délai est intentionnel et conçu pour protéger la vie privée des utilisateurs. Aucun rebond ou échec ne sera signalé tant qu'APNs ne renvoie pas un statut `410` pour un jeton invalide.

### Quel est le rapport entre le suivi des désinstallations et les notifications push silencieuses ou en arrière-plan ? {#how-does-uninstall-tracking-relate-to-silent-or-background-push}

La détection des désinstallations peut utiliser des notifications push en arrière-plan de faible priorité qui ne s'affichent pas sous forme de notification visible. Celles-ci sont distinctes des [**envois**]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) de Campaign dans les analyses de messagerie standard. Lorsque vous analysez les tendances de désinstallation, examinez les graphiques de désinstallation en parallèle des indicateurs d'engagement des notifications push plutôt que de comparer directement les notifications push de désinstallation aux totaux d'envois marketing.