---
nav_title: Paires clé-valeur
article_title: Paires clé-valeur
page_order: 4
description: "Cet article de référence couvre les paires clé-valeur et comment les utiliser pour envoyer des payloads de données supplémentaires aux appareils des utilisateurs."
channel:
  - push
  - in-app messages
  - content cards

---

# Paires clé-valeur {#key-value-pairs}

> Cette page explique comment utiliser les paires clé-valeur pour envoyer des payloads de données supplémentaires aux appareils des utilisateurs. Cette fonctionnalité est disponible pour les canaux de communication push, in-app, e-mail et Content Cards.

Utilisez les paires clé-valeur pour ajouter des métadonnées structurées à vos messages. Ces payloads de données supplémentaires peuvent enrichir les messages avec des informations contextuelles qui influencent la manière dont un message est affiché ou traité.

Comme les paires clé-valeur sont des métadonnées, ces données ne sont pas nécessairement visibles par le destinataire, mais peuvent être utilisées par vos systèmes ou processus connectés pour personnaliser le traitement des messages.

Chaque paire se compose de :

- **Clé :** L'identifiant (Exemple : `utm_source`)
- **Valeur :** La donnée associée (Exemple : `newsletter`)

## Cas d'usage {#use-cases}

Voici quelques exemples de cas d'usage pour ajouter des métadonnées avec des paires clé-valeur :

1. **Paramètres de suivi :** Joindre des paramètres UTM à des fins d'analyse
   - Clé : `utm_campaign`
   - Valeur : `spring_sale`
2. **Tags personnalisés :** Ajouter des tags pour le routage interne ou la catégorisation
   - Clé : `priority`
   - Valeur : `high`
3. **Déclencheurs de comportement :** Métadonnées utilisées pour déclencher ou personnaliser des comportements in-app
   - Clé : `deep_link`
   - Valeur : `app://promo-page`

## Notifications push {#push-notifications}

Les paires clé-valeur peuvent être ajoutées aux notifications push Android, iOS et web. Vous pouvez les utiliser pour mettre à jour des indicateurs internes et le contenu de l'application, ou pour personnaliser les propriétés des notifications push, comme la priorisation des alertes, la localisation et les sons.

Dans le composeur de messages, sélectionnez l'onglet **Settings**, sélectionnez **Add New Pair** et spécifiez vos paires clé-valeur.

Lorsque vous ajoutez des paires clé-valeur dans le composeur de messages, les valeurs sont envoyées sous forme de chaînes de caractères. Pour les notifications push iOS, les clés d'alerte réservées de l'Apple Push Notification service (APNs) que vous ajoutez via **Alert Options** (telles que `loc-args` pour les arguments de localisation) sont formatées avec les types JSON appropriés dans le payload. Pour les clés personnalisées, votre application reçoit des valeurs de type chaîne de caractères, sauf si vous les analysez dans votre intégration.

### iOS

L'Apple Push Notification service (APNs) prend en charge la définition de préférences d'alerte et l'envoi de données personnalisées à l'aide de paires clé-valeur. APNs utilise la bibliothèque réservée par Apple `aps`, qui comprend des clés et valeurs prédéterminées régissant les propriétés des alertes.

#### Bibliothèque APS {#aps-library}

| Clé  | Type de valeur  | Description de la valeur |
|-------------------|-----------------------------|----------------------------------|
| alert             | chaîne de caractères ou objet dictionnaire | Pour les entrées de type chaîne, affiche une alerte avec la chaîne comme message accompagné des boutons Fermer et Afficher ; pour les entrées d'un autre type, affiche une alerte ou une bannière selon les propriétés enfant de l'entrée |
| badge             | nombre                      | Régit le nombre affiché comme badge sur l'icône de l'application                                                                                                                              |
| sound             | chaîne de caractères                      | Le nom du fichier son à jouer comme alerte ; doit se trouver dans le bundle de l'application ou dans le dossier ```Library/Sounds```                                                                                    |
| content-available | nombre                      | Les valeurs d'entrée de 1 signalent à l'application la disponibilité de nouvelles informations au lancement ou à la reprise de session |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Bibliothèque APS" }


##### Bibliothèque des propriétés d'alerte {#alert-properties-library}

| Clé            | Type de valeur               | Description de la valeur                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| title         | chaîne de caractères                   | Une courte chaîne de caractères qu'Apple Watch affiche brièvement dans le cadre d'une notification                                                                    |
| body         | chaîne de caractères                   | Le contenu de la notification push                                                                                                                  |
| title-loc-key  | chaîne de caractères ou null           | Une clé qui définit la chaîne de titre pour la localisation actuelle à partir du fichier ```Localizable.strings```                                          |
| title-loc-args | tableau de chaînes de caractères ou null | Des valeurs de chaîne qui peuvent apparaître à la place des spécificateurs de format de localisation du titre dans title-loc-key                                           |
| action-loc-key | tableau de chaînes de caractères ou null  | Si présent, la chaîne spécifiée définit la localisation des boutons Fermer et Afficher                                                         |
| loc-key        | chaîne de caractères ou null           | Une clé qui définit le message de notification pour la localisation actuelle à partir du fichier ```Localizable.strings```                                  |
| loc-args       | tableau de chaînes de caractères         | Des valeurs de chaîne qui peuvent apparaître à la place des spécificateurs de format de localisation dans loc-key                                                       |
| launch-image   | chaînes de caractères                  | Le nom d'un fichier image dans le bundle de l'application que vous souhaitez utiliser comme image de lancement lorsque les utilisateurs appuient sur le bouton d'action ou déplacent le curseur d'action |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Bibliothèque des propriétés d'alerte" }

Le composeur de messages Braze gère automatiquement la création des clés suivantes : **alert** et **ses propriétés**, **content-available**, **sound** et **category**.

Ces valeurs peuvent être saisies dans l'onglet **Settings** lors de la création d'un message push. Sélectionnez **Alert Options** puis sélectionnez une clé de dictionnaire d'alerte pour que la clé soit automatiquement renseignée dans une nouvelle entrée clé-valeur.

![Ces valeurs peuvent être saisies dans l'onglet Settings lors de la création d'un message push. Sélectionnez Alert Options puis sélectionnez une clé de dictionnaire d'alerte pour que la clé soit automatiquement renseignée dans une nouvelle entrée clé-valeur.]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
{% raw %}
Lorsque Braze envoie une notification push à APNs, le payload est formaté en JSON.

**Payload simple**

```
{
    "aps" : { "alert" : "Message received from Spencer" },
}
```

**Payload complexe**

```
{
    "aps" : {
        "alert" : {
            "body" : "Hi, welcome to our app!",
            "loc-key" : "France",
            "loc-args" : ["Bonjour", "bienvenue"],
            "action-loc-key" : "Button_Type_1",
            "launch-image" : "Paris"
      },
        "content-available" : 1
    },
}
```

{% endraw %}

##### Paires clé-valeur personnalisées {#custom-key-value-pairs}

En plus des valeurs de payload de la bibliothèque `aps`, vous pouvez envoyer des paires clé-valeur personnalisées à l'appareil d'un utilisateur. Les valeurs de ces paires sont limitées aux types primitifs : dictionnaire (objet), tableau, chaîne de caractères, nombre et booléen.

![Capture d'écran relative aux paires clé-valeur personnalisées.]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

Les cas d'usage des paires clé-valeur personnalisées incluent, entre autres, le suivi d'indicateurs internes et la définition du contexte de l'interface utilisateur. Braze vous permet d'envoyer des paires clé-valeur supplémentaires avec une notification push, utilisables par votre application via la [clé extras]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=swift#swift_settings). Si vous préférez utiliser une autre clé, vérifiez que votre application peut gérer cette clé personnalisée.

{% alert warning %}
Vous devez éviter de gérer une clé ou un dictionnaire de premier niveau appelé ab dans votre application.
{% endalert %}

Apple recommande aux clients d'éviter d'inclure des informations client ou des données sensibles dans les données de payload personnalisées. De plus, Apple recommande que toute action associée à un message d'alerte ne supprime pas de données sur un appareil.

{% alert warning %}
Si vous utilisez l'API du fournisseur HTTP/2, tout payload individuel que vous envoyez à APNs ne peut pas dépasser 4 096 octets. L'ancienne interface binaire, qui sera bientôt dépréciée, ne prend en charge qu'une taille de payload de 2 048 octets.
{% endalert %}

###### Campaigns déclenchées par l'API {#api-triggered-campaigns}

Braze vous permet d'envoyer des paires clé-valeur personnalisées de type chaîne de caractères, appelées `extras`. Pour accéder à vos extras dans les Campaigns déclenchées par l'API et les Campaigns planifiées déclenchées par l'API, définissez dans le tableau de bord une clé comme « example_key » et une valeur comme {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Le résultat dans la console de développement sera `"extras": { "test": { "foo": 1, "bar": 1 }`.

### Android

Braze vous permet d'envoyer des payloads de données supplémentaires dans les notifications push à l'aide de paires clé-valeur.

#### Payload de données {#data-payload}

Comme pour les notifications push iOS, vous pouvez envoyer des paires clé-valeur personnalisées à l'appareil d'un utilisateur.

Certains cas d'usage des paires clé-valeur personnalisées incluent le suivi d'indicateurs internes et la définition du contexte de l'interface utilisateur, mais elles peuvent être utilisées à toute fin de votre choix.

{% alert important %}
Le backend de votre application doit être capable de traiter les paires clé-valeur personnalisées pour que le payload de données fonctionne correctement.
{% endalert %}

##### Campaigns déclenchées par l'API

Braze vous permet d'envoyer des paires clé-valeur personnalisées de type chaîne de caractères, appelées `extras`. Pour accéder à vos extras dans les Campaigns déclenchées par l'API et les Campaigns planifiées déclenchées par l'API, définissez dans le tableau de bord une clé comme « example_key » et une valeur comme {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Le résultat dans la console de développement sera `"extras": { "test": { "foo": 1, "bar": 1 }`.

##### Options de messagerie FCM {#fcm-messaging-options}

Les notifications push Android peuvent être davantage personnalisées avec les options de message FCM. Celles-ci incluent la [priorité de notification]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings), le [son]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings), le délai, la durée de vie et la réductibilité. Ces valeurs peuvent être spécifiées dans l'onglet **Settings** lors de la création d'un message push. Consultez les [paramètres avancés des notifications push]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings) pour obtenir des instructions supplémentaires sur la configuration de ces options dans le composeur de messages Braze.

![Capture d'écran relative aux options de messagerie FCM.]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### Notifications push silencieuses {#silent-push-notifications}

Une notification push silencieuse est une notification push ne contenant aucun message d'alerte ni son, utilisée pour mettre à jour l'interface ou le contenu de votre application en arrière-plan. Ces notifications utilisent des paires clé-valeur pour déclencher ces actions en arrière-plan. Les notifications push silencieuses alimentent également notre [suivi des désinstallations]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

Les marketeurs doivent vérifier que les notifications push silencieuses déclenchent le comportement attendu avant de les envoyer aux utilisateurs de leur application. Après avoir composé votre notification push silencieuse [iOS]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift) ou [Android]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android), assurez-vous de ne cibler qu'un utilisateur test en filtrant par [ID utilisateur externe]({{site.baseurl}}/api/endpoints/messaging#external-user-id) ou [adresse e-mail]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

Au lancement de la Campaign, vérifiez que vous n'avez reçu aucune notification push visible sur votre appareil de test.

{% alert note %}
Le contrôle des notifications silencieuses par iOS peut provoquer les symptômes suivants :

- Des indicateurs de suivi des désinstallations inférieurs aux attentes pour les utilisateurs iOS
- Une distribution incohérente ou retardée des notifications push silencieuses
- Des [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) qui ne s'affichent pas
- Des Push Stories qui arrivent sans les images, vidéos ou pages attendues

Il s'agit d'une limitation de la plateforme Apple et non d'un problème lié à Braze. iOS peut retarder ou abandonner les notifications en arrière-plan pour certaines fonctionnalités Braze, y compris le suivi des désinstallations et les Push Stories. Pour plus de détails sur ce qu'iOS contrôle et à quel moment, consultez les [limitations iOS]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift#ios-limitations).
{% endalert %}

## Messages in-app {#in-app-messages}

Vous pouvez ajouter une paire clé-valeur à un message in-app dans l'[éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) en sélectionnant l'onglet **Paramètres**, puis **Ajouter une nouvelle paire**, et en spécifiant vos paires clé-valeur.

{% alert note %}
Les paires clé-valeur ne peuvent pas être définies via l'éditeur par glisser-déposer pour les messages in-app.
{% endalert %}
![Capture d'écran relative aux messages in-app.]({% image_buster /assets/img_archive/keyvalue_iam.png %})

### Campaigns déclenchées par API

Braze vous permet d'envoyer des paires clé-valeur de chaînes de caractères personnalisées, appelées `extras`. Pour accéder à vos extras dans les Campaigns déclenchées par API et les Campaigns planifiées déclenchées par API, définissez dans le tableau de bord une clé comme « example_key » et une valeur comme {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Cela produira une sortie dans la console de développement de type `"extras": { "test": { "foo": 1, "bar": 1 }`.

## E-mails {#emails}

SparkPost et SendGrid prennent tous deux en charge les paires clé-valeur dans les e-mails. Si vous utilisez SendGrid, les paires clé-valeur seront envoyées en tant qu'[arguments uniques](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments). SendGrid vous permet d'associer un nombre illimité de paires clé-valeur jusqu'à 10 000 octets de données. Ces paires clé-valeur peuvent être consultées dans les publications du [webhook d'événement](https://sendgrid.com/docs/for-developers/tracking-events/event/) de SendGrid.

{% alert note %}
Les e-mails rejetés ne transmettront pas les paires clé-valeur à SparkPost ou SendGrid.
{% endalert %}

![Onglet Informations d'envoi du compositeur d'e-mail dans Braze.]({% image_buster /assets/img_archive/keyvalue_email.png %})

## Content Cards

Pour ajouter une paire clé-valeur à une Content Card, accédez à l'onglet **Settings** dans le composeur de messages Braze et sélectionnez **Add New Pair**.

![Ajouter une paire clé-valeur à une Content Card]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}

{% alert note %}
Les variantes de contrôle ne prennent pas en charge les paires clé-valeur. Si vous devez capturer des analyses pour les groupes de contrôle dans les tests A/B, créez une variante de message avec une paire clé-valeur telle que `control=true` et masquez-la dans le code de votre application tout en enregistrant les impressions.
{% endalert %}