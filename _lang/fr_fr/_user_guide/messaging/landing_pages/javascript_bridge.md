---
nav_title: Pont JavaScript
article_title: Pont JavaScript pour les pages de destination
page_order: 5
page_type: reference
description: "Découvrez comment utiliser le pont JavaScript brazeBridge pour enregistrer des événements, définir des attributs personnalisés et déclencher des actions Braze depuis le bloc de code personnalisé d'une page de destination."
---

# Pont JavaScript pour les pages de destination {#javascript-bridge-for-landing-pages}

> Les pages de destination prennent en charge un « pont » JavaScript pour connecter votre code personnalisé (HTML, CSS et JavaScript) au SDK Braze.

Accédez au pont en utilisant `brazeBridge` dans un bloc de code personnalisé pour enregistrer des événements, définir des attributs personnalisés, identifier des utilisateurs et plus encore lorsqu'un visiteur interagit avec votre page de destination.

## Fonctionnement {#how-it-works}

Les pages de destination vous permettent d'ajouter du HTML, du CSS et du JavaScript personnalisés dans un bloc **Code personnalisé** pour un meilleur contrôle de l'apparence, du ressenti et du comportement de votre page. Les blocs de code personnalisé peuvent utiliser le [pont JavaScript](#supported-methods) pour enregistrer des événements, définir des attributs personnalisés, identifier des utilisateurs et plus encore :
- Enregistrer des événements personnalisés et des achats
- Définir des attributs utilisateur standard et personnalisés
- Suivre les clics et les soumissions de formulaires
- Identifier des utilisateurs

Si vous réutilisez du code `brazeBridge` provenant de messages in-app ou de bannières, il devrait toujours fonctionner sur les pages de destination. Les méthodes qui ne s'appliquent pas aux pages de destination sont ignorées et enregistrent un avertissement dans la console du navigateur au lieu de provoquer une erreur. Pour plus de détails, consultez [Méthodes non prises en charge sur les pages de destination](#methods-not-supported-on-landing-pages).

{% alert important %}
Le pont des pages de destination est asynchrone ; chaque méthode renvoie une Promise. Cela diffère du [pont des messages in-app HTML personnalisés]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge), dont les méthodes renvoient immédiatement. Si l'étape suivante de votre script dépend de la fin d'un appel au pont — comme la redirection de la page, la soumission d'un formulaire ou l'envoi de données à Braze — utilisez `await` ou `.then()` et ne supposez pas que l'appel s'est terminé de manière synchrone.
{% endalert %}

## Disponibilité du pont {#bridge-availability}

Lorsqu'un visiteur ouvre votre page de destination, `brazeBridge` est déjà disponible dans le JavaScript de votre bloc **Code personnalisé**. Appelez les méthodes du pont directement dans les pages de destination — vous n'avez pas besoin d'attendre un événement « ready » séparé comme les messages in-app le font avec `ab.BridgeReady`.

Le fait que l'objet pont soit disponible ne signifie pas que le SDK Braze est initialisé pour ce visiteur. Le SDK s'initialise lors d'une visite de page de destination dans l'un de ces cas :

- Le visiteur ouvre la page via une [balise Liquid de page de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) envoyée par un canal Braze (e-mail, SMS, notification push, etc.). Le SDK s'initialise automatiquement au chargement de la page.
- Le visiteur soumet le formulaire de la page — par exemple, en cliquant sur un bouton **Soumettre** qui envoie les données du formulaire. Cela inclut les appels `brazeBridge` effectués dans les rappels `registerFormInput` d'un [bloc de formulaire personnalisé]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks), puisque ceux-ci s'exécutent dans le cadre de la soumission du formulaire.

Si un visiteur ouvre la page de destination directement, sans balise Liquid de page de destination, et ne soumet jamais le formulaire, la page est anonyme pour Braze et les appels aux méthodes du pont n'ont aucun effet.

{% alert note %}
`window.lpBridge` et `window.appboyBridge` font référence au même objet pont, mais les deux sont obsolètes. Utilisez `window.brazeBridge`.
{% endalert %}

## Exemple {#example}

Comme les méthodes sont asynchrones, utilisez un gestionnaire async et attendez les appels avec `await` lorsque l'ordre ou la complétion est important :

```html
<button id="button">Set Favorite Color</button>
<script>
  document.querySelector("#button").onclick = async function () {
    // Track a click for analytics
    await brazeBridge.logClick("set-favorite-color");
    // Set the user's custom attribute
    await brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    await brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    await brazeBridge.requestImmediateDataFlush();
  };
</script>
```

## Méthodes prises en charge {#supported-methods}

Les méthodes `brazeBridge` suivantes renvoient une promesse et sont prises en charge dans les blocs **Code personnalisé** des pages de destination. Utilisez `await` ou `.then()` lorsque vous devez séquencer des opérations ou garantir leur complétion.

### Méthodes de niveau supérieur {#top-level-methods}

| Méthode | Description |
| --- | --- |
| `brazeBridge.changeUser(userId, signature?)` | Identifie l'utilisateur avec un ID unique. |
| `brazeBridge.logCustomEvent(eventName, eventProperties?)` | Enregistre un événement personnalisé. |
| `brazeBridge.logPurchase(productId, price, currencyCode?, quantity?, purchaseProperties?)` | Enregistre un achat. |
| `brazeBridge.requestImmediateDataFlush(callback?)` | Envoie les données en file d'attente aux serveurs Braze. |
| `brazeBridge.logClick(trackingId)` | Enregistre un clic sur la page de destination (`lp_c`) pour l'ID de suivi donné. Voir [Suivi des clics](#click-tracking). |
| `brazeBridge.logSubmit()` | Enregistre une soumission de formulaire de page de destination (`lp_fs`). Spécifique aux pages de destination. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Méthodes de niveau supérieur" }

### Méthodes `getUser()` {#getuser-methods}

{% alert note %}
`brazeBridge.getUser()` renvoie un objet simple de manière synchrone, vous n'avez donc pas besoin d'utiliser `await getUser()` ; les méthodes de l'objet renvoyé (comme `getUser().setEmail(email)`) renvoient des Promises.
{% endalert %}

`getUser()` renvoie un objet exposant les méthodes utilisateur suivantes. Chaque méthode renvoie une Promise.

| Méthode | Description |
| --- | --- |
| `getUser().setFirstName(firstName)` | Définit le prénom de l'utilisateur. |
| `getUser().setLastName(lastName)` | Définit le nom de famille de l'utilisateur. |
| `getUser().setEmail(email)` | Définit l'adresse e-mail de l'utilisateur. |
| `getUser().setPhoneNumber(phoneNumber)` | Définit le numéro de téléphone de l'utilisateur. |
| `getUser().setGender(gender: "m" \| "f" \| "o" \| "u" \| "n" \| "p")` | Définit le genre de l'utilisateur : masculin, féminin, autre, inconnu, non applicable ou préfère ne pas répondre, respectivement. |
| `getUser().setDateOfBirth(year, month, day)` | Définit la date de naissance de l'utilisateur. |
| `getUser().setCountry(country)` | Définit le pays de l'utilisateur. |
| `getUser().setHomeCity(city)` | Définit la ville de résidence de l'utilisateur. |
| `getUser().setLanguage(language)` | Définit la langue de l'utilisateur. |
| `getUser().setCustomUserAttribute(key, value, merge?)` | Définit un attribut personnalisé de l'utilisateur. |
| `getUser().addToCustomAttributeArray(key, value)` | Ajoute une valeur à un tableau d'attributs personnalisés. |
| `getUser().removeFromCustomAttributeArray(key, value)` | Supprime une valeur d'un tableau d'attributs personnalisés. |
| `getUser().incrementCustomUserAttribute(key, incrementValue?)` | Incrémente un attribut personnalisé numérique. |
| `getUser().setCustomLocationAttribute(key, latitude, longitude)` | Définit un attribut d'emplacement personnalisé. |
| `getUser().addToSubscriptionGroup(subscriptionGroupId)` | Ajoute l'utilisateur à un groupe d'abonnement e-mail ou SMS. |
| `getUser().removeFromSubscriptionGroup(subscriptionGroupId)` | Supprime l'utilisateur d'un groupe d'abonnement e-mail ou SMS. |
| `getUser().setEmailNotificationSubscriptionType(type: "opted_in" \| "subscribed" \| "unsubscribed")` | Définit le statut d'abonnement aux notifications par e-mail. |
| `getUser().setPushNotificationSubscriptionType(type: "opted_in" \| "subscribed" \| "unsubscribed")` | Définit le statut d'abonnement aux notifications push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Méthodes getUser()" }

## Suivi des clics {#click-tracking}

Utilisez `brazeBridge.logClick(trackingId)` pour suivre les clics sur votre page de destination. Chaque appel enregistre un événement de clic sur la page de destination (`lp_c`) associé à l'ID de suivi que vous transmettez :

```html
<a href="#" onclick="brazeBridge.logClick('cta-hero')">Get started</a>
```

{% alert note %}
Le suivi des clics sur les pages de destination diffère de celui des messages in-app, qui utilisent `logClick('0')` et `logClick('1')` comme ID conventionnels pour « Bouton 1 » et « Bouton 2 ». Les pages de destination n'ont pas d'ID de bouton spéciaux équivalents. Chaque appel `logClick(trackingId)` enregistre un événement `lp_c` indexé par l'ID de suivi que vous fournissez.
{% endalert %}

## Méthodes non prises en charge sur les pages de destination {#methods-not-supported-on-landing-pages}

Les méthodes suivantes fonctionnent dans les messages in-app et les bannières, mais ne sont pas prises en charge sur les pages de destination. Si votre code en appelle une sur une page de destination, Braze ignore l'appel. Votre page continue de fonctionner, mais vous pouvez voir un avertissement dans la console de développement du navigateur.

| Méthode | Notes |
| --- | --- |
| `brazeBridge.closeMessage()` | Il n'y a pas d'interface de message à fermer sur une page de destination. |
| `brazeBridge.requestPushPermission(successCallback?, deniedCallback?)` | La permission push n'est pas demandée depuis une page de destination. |
| `brazeBridge.web.registerAppboyPushMessages(successCallback?, deniedCallback?)` | L'inscription aux notifications push Web n'est pas disponible sur les pages de destination. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Méthodes non prises en charge sur les pages de destination" }

## Contenu connexe {#related-content}

- [Créer des blocs de formulaire personnalisés]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks) couvre une utilisation plus avancée de ce pont : connecter une interface entièrement personnalisée à un formulaire de page de destination.
- [Créer des pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)