---
nav_title: Intégration de balise
article_title: Intégration de balise pour iOS
platform: iOS
page_order: 4
description: "Cet article traite de la journalisation des événements personnalisés à l'aide des balises Infillion pour iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Intégration de balise {#beacon-integration}

Nous allons découvrir ici comment intégrer des types spécifiques de balises avec Braze pour permettre la segmentation et l'envoi de messages.

## Balises Infillion {#infillion-beacons}

Une fois vos balises Infillion configurées et intégrées à votre application, vous pouvez enregistrer des événements personnalisés tels que le début ou la fin d'une visite, ou l'observation d'une balise. Vous pouvez également enregistrer des propriétés pour ces événements, comme le nom du lieu ou la durée de présence.

Pour enregistrer un événement personnalisé lorsqu'un utilisateur accède à un lieu, saisissez ce code dans la méthode `didBeginVisit` :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"Entered %@", visit.place.name];
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("Entered %@", visit.place.name)
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

La méthode `flushDataAndProcessRequestQueue` garantit que votre événement est enregistré même si l'application est en arrière-plan. Le même processus peut être implémenté pour le départ d'un emplacement. Notez que cela créera et incrémentera un événement personnalisé unique pour chaque nouveau lieu visité par l'utilisateur. Si vous prévoyez de créer plus de 50 lieux, nous vous recommandons de créer un événement personnalisé générique « Place Entered » et d'inclure le nom du lieu comme propriété d'événement.