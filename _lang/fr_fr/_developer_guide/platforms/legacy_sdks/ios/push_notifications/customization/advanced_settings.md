---
nav_title: Paramètres avancés
article_title: Paramètres avancés de notification push
platform: iOS
page_order: 5
description: "Cet article de référence couvre les paramètres avancés de notification push pour iOS tels que les options d'alerte, les sons, l'expiration, etc."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Paramètres avancés {#advanced-settings}

Lors de la création d'une campagne push, à l'étape de composition, sélectionnez **Settings** pour afficher les paramètres avancés disponibles.

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

## Extraire des données à partir des paires clé-valeur de notifications push {#extracting-data-from-push-key-value-pairs}

Braze vous permet d'envoyer des paires clé-valeur définies de manière personnalisée sous forme de chaînes de caractères, appelées `extras`, avec une notification push à votre application. Ces extras peuvent être définis via le tableau de bord ou l'API et seront disponibles en tant que paires clé-valeur dans le dictionnaire `notification` transmis à vos implémentations de délégué de notification push.

## Options d'alerte {#alert-options}

Cochez la case **Alert Options** pour voir une liste déroulante de valeurs clés disponibles pour ajuster l'apparence de la notification sur les appareils.

## Ajouter un indicateur de contenu disponible {#adding-content-available-flag}

Cochez la case **Add Content-Available Flag** pour indiquer aux appareils de télécharger le nouveau contenu en arrière-plan. Le plus souvent, vous pouvez cocher cette case si vous souhaitez envoyer des [notifications silencieuses]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications/).

## Ajouter un indicateur de contenu mutable {#adding-mutable-content-flag}

Cochez la case **Add Mutable-Content Flag** pour activer les personnalisations avancées du récepteur sur les appareils équipés d'iOS 10+. Cet indicateur sera automatiquement envoyé lors de la composition d'une [notification enrichie]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/rich_notifications/), quelle que soit la valeur de cette case à cocher.

## Mettre à jour le nombre de badges de l'application {#update-app-badge-count}

Saisissez le nombre souhaité pour mettre à jour votre compteur de badges, ou utilisez la syntaxe Liquid pour définir vos conditions personnalisées. Vous pouvez également mettre à jour manuellement votre compteur de badges par l'intermédiaire de la propriété `applicationIconBadgeNumber` de votre application ou du payload de notification push. Pour en savoir plus, consultez notre article dédié au [nombre de badges]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/badges/).

## Sons {#sounds}

Vous pouvez entrer ici un chemin d'accès à un fichier audio dans votre bundle d'application afin de spécifier un son à lire lorsque la notification push est reçue. Si le fichier audio spécifié n'existe pas ou si le mot-clé « default » est saisi, Braze utilisera le son d'alerte par défaut de l'appareil. Pour plus d'informations sur la personnalisation, consultez notre article dédié aux [sons personnalisés]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/custom_sounds/).

## ID de réduction {#collapse-id}

Spécifiez un ID de réduction pour fusionner les notifications similaires. Si vous envoyez plusieurs notifications avec le même ID de réduction, l'appareil n'affichera que la notification la plus récente. Reportez-vous à la documentation d'Apple sur les [notifications fusionnées](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

## Expiration {#expiry}

Cochez la case **Expiry** pour définir une durée d'expiration pour votre message. Si l'appareil d'un utilisateur perd sa connexion, Braze continuera d'essayer d'envoyer le message jusqu'à l'heure spécifiée. Si cette option n'est pas définie, la plateforme applique par défaut un délai d'expiration de 30 jours. Notez que les notifications push qui expirent avant d'être distribuées ne sont pas considérées comme ayant échoué et ne seront pas enregistrées comme un rebond.