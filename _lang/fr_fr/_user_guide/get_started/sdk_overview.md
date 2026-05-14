---
nav_title: Aperçu du SDK
article_title: Présentation du SDK
page_order: 9
page_type: reference
description: "Cet article de référence traite des principes fondamentaux du SDK Braze."
---

# Aperçu du SDK {#sdk-overview}

> Le SDK Braze collecte des données de session, identifie les utilisateurs et enregistre les achats et les événements personnalisés via votre site web ou votre application. Vous pouvez également utiliser le SDK pour interagir avec les utilisateurs en envoyant des In-App Messages et des notifications push directement depuis le tableau de bord de Braze.

Le SDK Braze en bref :
* Collecte et synchronise les données de l'utilisateur dans un profil utilisateur consolidé
* Capture les données d'engagement marketing et les données personnalisées spécifiques à votre entreprise
* Alimente les canaux de communication de notifications push, de In-App Messages et de carte de contenu

## Qu'est-ce qu'un SDK ? {#what-is-an-sdk}
Un kit de développement logiciel (SDK) est un ensemble d'outils préfabriqués — de petits blocs de code — qui peuvent être ajoutés aux applications numériques pour prendre en charge de nouvelles fonctionnalités. Le SDK Braze est utilisé pour envoyer et recevoir des informations depuis et vers votre application ou site. Il est conçu pour fournir des fonctionnalités essentielles dès le départ : création de profils utilisateur, journalisation d'événements personnalisés, déclenchement de notifications push, etc.

Étant donné que ces fonctionnalités sont fournies par défaut par Braze, vos développeurs sont libres de se concentrer sur votre activité principale. Sans SDK, chaque client Braze devrait créer depuis le départ toute l'infrastructure et tous les outils nécessaires au traitement des données, à la logique de segmentation, aux options de distribution, à la gestion des utilisateurs anonymes, aux analyses des Campaigns et bien plus encore. Cela prendrait beaucoup plus de temps et serait bien plus pénible que l'heure, environ, nécessaire pour intégrer notre SDK.

## Mise en œuvre {#implementation}

Pour intégrer un SDK dans votre application ou votre site, quelqu'un devra ajouter le code du SDK à la base de code globale qui alimente cette application. Votre équipe d'ingénierie sera donc impliquée pour, en somme, relier nos applications ensemble afin que les informations et les actions circulent entre elles. Mais bien que vos développeurs soient impliqués, le SDK est conçu pour être léger et facile à intégrer.

Pour vous faire gagner du temps et assurer une intégration fluide, nous vous recommandons, à vous et à votre équipe d'ingénierie, de configurer vos événements personnalisés, vos attributs personnalisés et le SDK en même temps. Découvrez les étapes auxquelles vos équipes marketing et ingénierie devront réfléchir ensemble en lisant notre [article sur la mise en œuvre]({{site.baseurl}}/user_guide/get_started/integrations/).

## Agrégation des données {#data-aggregation}

Le SDK Braze recueille automatiquement les données au niveau utilisateur, vous fournissant ainsi des indicateurs clés pour votre application et votre base d'utilisateurs. Regroupez les applications similaires dans un seul espace de travail (par exemple, les versions iOS et Android ensemble) afin de visualiser les données collectées sur toutes les plateformes et d'obtenir une vue d'ensemble complète de l'activité des utilisateurs. Consultez l'article sur la [page d'accueil]({{site.baseurl}}/user_guide/analytics/dashboards/home/) pour plus d'informations.

## Envoi de In-App Messages {#in-app-messaging}

Utilisez le SDK pour rédiger et envoyer directement des In-App Messages. Vous pouvez choisir des messages contextuels, modaux ou plein écran en fonction de votre stratégie de Campaign. Pour plus de détails sur la composition, consultez [Créer un message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/).

![Notification push affichée sur un navigateur web]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Notifications push {#push-notifications}

Les notifications push sont une autre excellente option pour interagir avec vos utilisateurs et sont particulièrement utiles pour gérer les appels à l'action urgents. Les notifications push mobiles apparaissent sur les appareils de vos utilisateurs, et les notifications push web apparaissent même lorsque votre site n'est pas ouvert. Pour en savoir plus sur l'utilisation des notifications push, consultez notre [article sur les notifications push]({{site.baseurl}}/user_guide/channels/push/).

Les utilisateurs de votre site web ou de votre application doivent s'abonner pour recevoir des notifications push. Consultez l'[amorçage de push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/) pour plus de détails.

## Règles de segmentation et de distribution {#segmentation-and-delivery-rules}

Par défaut, une Campaign contenant des In-App Messages sera envoyée à toutes les versions de l'application dans cet espace de travail. Par exemple, le message sera envoyé aux utilisateurs web et mobiles. Pour envoyer un message in-app exclusivement sur le web ou sur mobile, vous devez segmenter votre Campaign en conséquence, ce qui est pris en charge par défaut par le SDK Braze.

Vous pouvez créer un segment de vos utilisateurs web en définissant **Applications et sites web ciblés** sur **Utilisateurs d'applications spécifiques**, puis en sélectionnant uniquement votre site web pour les **Applications spécifiques**.

![Page Détails du segment avec l'application web au premier plan]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

Cela vous permet de cibler de façon intelligente les utilisateurs en fonction de leur comportement. Si vous souhaitez cibler des utilisateurs web pour les encourager à télécharger votre application mobile, vous pouvez créer ce segment comme audience cible. Si vous souhaitez envoyer une Campaign de communication comprenant un message mobile in-app mais pas de message web, décochez l'icône de votre site web dans votre segment.

## Plateformes prises en charge {#supported-platforms}

Braze propose des SDK pour plusieurs plateformes, telles que Web, Android et Swift. Pour obtenir la liste complète, consultez le [Guide du développeur Braze]({{site.baseurl}}/developer_guide/home/).