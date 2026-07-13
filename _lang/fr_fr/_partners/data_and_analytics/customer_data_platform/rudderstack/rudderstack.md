---
nav_title: Rudderstack
article_title: Rudderstack
description: "Cet article présente le partenariat entre Braze et RudderStack, une infrastructure de données client open-source offrant une intégration fluide de Braze pour vos applications Android, iOS et web. Avec RudderStack, vous pouvez envoyer vos données d'événements client in-app directement à Braze pour une analyse contextuelle."
page_type: partner
search_tag: Partner

---

# RudderStack

> [RudderStack](https://rudderstack.com/) est une infrastructure de données client open-source permettant de collecter et d'acheminer les données d'événements client vers votre entrepôt de données préféré et des dizaines d'autres fournisseurs d'analytique, tels que Braze. Elle est prête pour l'entreprise et offre un cadre de transformation robuste pour traiter vos données d'événements à la volée.

L'intégration entre Braze et RudderStack offre une intégration SDK native pour vos applications Android, iOS et web, ainsi qu'une intégration de serveur à serveur à partir de vos services backend.

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte RudderStack | Un [compte RudderStack](https://app.rudderstack.com/) est nécessaire pour bénéficier de ce partenariat. |
| Source configurée | Une [source](https://www.rudderstack.com/docs/dashboard-guides/sources/) est essentiellement l'origine de toute donnée envoyée à RudderStack, comme les sites web, les applications mobiles ou les serveurs backend. Vous devez configurer la source avant de configurer Braze comme destination dans RudderStack. |
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations `users.track`, `users.identify`, `users.delete` et `users.alias.new`.<br><br>Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Clé d'application Braze | Pour obtenir votre clé d'application dans le tableau de bord de Braze, accédez à **Paramètres** > **Paramètres des applications** > **Identification** et trouvez le nom de votre application. Enregistrez la chaîne de caractères de l'identifiant associé.
| Centre de données | Votre centre de données correspond à votre [instance]({{site.baseurl}}/api/basics#endpoints) du tableau de bord de Braze.  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Ajouter une source {#step-1-add-a-source}

Pour commencer à envoyer des données à Braze, vous devez d'abord vous assurer qu'une source est configurée dans votre application RudderStack. Consultez le site de [RudderStack](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started) pour savoir comment configurer votre source de données.

### Étape 2 : Configurer la destination {#step-2-configure-destination}

Maintenant que votre source de données est configurée, dans le tableau de bord de RudderStack, sélectionnez **ADD DESTINATION** sous **Destinations**. Dans la liste des destinations disponibles, sélectionnez **Braze** et cliquez sur **Next**.

Dans la destination Braze, indiquez la clé d'application, la clé API REST de Braze, le cluster de données et l'option du SDK natif (mode appareil uniquement). Lorsque l'option du SDK natif est activée, le SDK natif de Braze sera utilisé pour envoyer les événements.

### Étape 3 : Choisir le type d'intégration {#step-3-choose-the-type-of-integration}

Vous pouvez choisir d'intégrer les bibliothèques web et natives côté client de RudderStack avec Braze en utilisant l'une des approches suivantes :

- [Intégration côte à côte / mode appareil](#device-mode) **:** RudderStack enverra les données d'événement à Braze directement depuis votre client (navigateur ou application mobile).
- [Serveur à serveur / mode cloud](#cloud-mode) **:** Le SDK de Braze envoie les données d'événement directement à RudderStack, où elles sont transformées puis acheminées vers Braze.
- [Mode hybride](#hybrid-mode) **:** Utilisez le mode hybride pour envoyer les événements iOS et Android générés automatiquement et générés par l'utilisateur vers Braze à l'aide d'une seule connexion.

{% alert note %}
Découvrez les [modes de connexion](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/) de RudderStack et les avantages de chacun d'entre eux.
{% endalert %}

#### Intégration côte à côte (mode appareil) {#device-mode}

Avec ce mode, vous pouvez envoyer vos événements à Braze en utilisant le SDK de Braze configuré sur votre site web ou votre application mobile.

Configurez les mappages vers le SDK de RudderStack pour votre plateforme sur le dépôt GitHub de Braze, comme décrit dans les [méthodes prises en charge](#supported-methods) :

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master)
- [Swift](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [Web](https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

Pour terminer l'intégration en mode appareil, reportez-vous aux instructions détaillées de RudderStack concernant l'[ajout de Braze à votre projet](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration).

#### Intégration serveur à serveur (mode cloud) {#cloud-mode}

Dans ce mode, le SDK envoie les données d'événement directement au serveur RudderStack. RudderStack transforme ensuite ces données et les achemine vers la destination souhaitée. Cette transformation est effectuée dans le backend de RudderStack à l'aide du module de transformation de RudderStack.

Pour activer l'intégration, vous devrez mapper les méthodes de RudderStack à Braze, comme décrit dans les [méthodes prises en charge](#supported-methods).

{% alert note %}
Les SDK côté serveur de RudderStack (Java, Python, Node.js, Go, Ruby) ne prennent en charge que le mode cloud. En effet, leurs SDK côté serveur fonctionnent dans le backend de RudderStack et ne peuvent charger aucun SDK spécifique à Braze.
{% endalert %}

{% alert important %}
L'intégration serveur à serveur ne prend pas en charge les fonctionnalités de l'interface de Braze, telles que les notifications push ou les messages in-app. Ces fonctionnalités sont toutefois prises en charge par l'intégration en mode appareil.
{% endalert %}

#### Mode hybride {#hybrid-mode}

Utilisez le mode hybride pour envoyer tous les événements à Braze depuis vos sources iOS et Android.

Lorsque vous choisissez le mode hybride pour envoyer des événements à Braze, RudderStack :
1. Initialise le SDK de Braze.
2. Envoie tous les événements générés par l'utilisateur (identify, track, page, screen et group) à Braze uniquement via le mode cloud et bloque leur envoi via le mode appareil.
3. Envoie les événements générés automatiquement (messages in-app, notifications push qui nécessitent le SDK de Braze) via le mode appareil.

Pour [envoyer des événements via le mode hybride](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode), utilisez l'option de mode hybride lors de la connexion de votre source à la destination Braze. Ensuite, ajoutez l'intégration de Braze à votre projet.

## Étape 4 : Configurer des paramètres supplémentaires {#step-4-configure-additional-settings}

Une fois la configuration initiale terminée, configurez les paramètres suivants pour recevoir correctement vos données dans Braze :

- **Enable subscription groups in group call** : activez ce paramètre pour envoyer le statut du groupe d'abonnement dans vos événements de groupe. Pour plus d'informations, consultez la section [Group](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group).
- **Use Custom Attributes Operation** : activez ce paramètre si vous souhaitez utiliser la fonctionnalité d'[attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) de Braze pour créer des segments et personnaliser vos messages à l'aide d'un objet d'attribut personnalisé. Pour plus d'informations, consultez la section [Send user traits as nested custom attributes](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes).
- **Track events for anonymous users** : activez ce paramètre pour suivre l'activité des utilisateurs anonymes et envoyer ces informations à Braze.

### Paramètres du mode appareil {#device-mode-settings}

Les paramètres suivants ne s'appliquent que si vous envoyez des événements à Braze via le [mode appareil](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode) :

- **Client-side Events Filtering** : ce paramètre vous permet de spécifier quels événements doivent être bloqués ou autorisés à transiter vers Braze. Pour plus d'informations sur ce paramètre, consultez la section [Client-side Events Filtering](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/).
- **Deduplicate Traits** : activez ce paramètre pour dédupliquer les traits de l'utilisateur dans l'appel [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify).
- **Show Braze logs** : ce paramètre ne s'applique que lorsque vous utilisez le [SDK JavaScript](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/) comme source. Activez-le pour afficher les journaux de Braze à vos utilisateurs.
- **OneTrust Cookie Categories** : ce paramètre vous permet d'associer les groupes de consentement aux cookies [OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/) à Braze.

## Méthodes prises en charge {#supported-methods}

Braze prend en charge les méthodes RudderStack identify, track, screen, page, group et alias.

{% tabs %}
{% tab Identify %}

La [méthode `identify`](https://rudderstack.com/docs/destinations/marketing/braze/#identify) de RudderStack associe les utilisateurs à leurs actions. RudderStack enregistre un ID utilisateur unique et des traits facultatifs associés à cet utilisateur, tels que le nom, l'e-mail, l'adresse IP, etc.

**Gestion du delta pour les appels identify**<br>
Si vous envoyez des événements à Braze via le mode appareil, vous pouvez réduire vos coûts en dédupliquant vos appels `identify`. Pour ce faire, activez le paramètre Deduplicate Traits dans le tableau de bord. RudderStack n'envoie alors à Braze que les attributs (traits) modifiés ou changés.

**Suppression d'un utilisateur**<br>
Vous pouvez supprimer un utilisateur dans Braze à l'aide de la [règle Suppression with Delete](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation) de l'[API Data Regulation](https://www.rudderstack.com/docs/api/data-regulation-api/) de RudderStack.

{% endtab %}
{% tab Track %}

La [méthode `track`](https://rudderstack.com/docs/destinations/marketing/braze/#track) de RudderStack capture toutes les activités de l'utilisateur et les propriétés associées à ces activités.

**Commande terminée**<br>
En utilisant l'[API eCommerce de RudderStack](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/) pour appeler la méthode track pour un événement portant le nom `Order Completed`, RudderStack envoie les produits listés dans cet événement à Braze en tant que [`purchases`]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data).

{% endtab %}
{% tab Screen %}

La [méthode `screen`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen) de RudderStack vous permet d'enregistrer les vues d'écran mobiles de vos utilisateurs avec toute information supplémentaire sur l'écran visualisé.

{% endtab %}
{% tab Page %}

La [méthode `page`](https://rudderstack.com/docs/destinations/marketing/braze/#page) de RudderStack vous permet d'enregistrer les pages consultées de votre site web. Elle capture également toute autre information pertinente concernant cette page.

{% endtab %}
{% tab Group %}

La [méthode `group`](https://rudderstack.com/docs/destinations/marketing/braze/#group) de RudderStack vous permet d'associer un utilisateur à un groupe.

**Statut du groupe d'abonnement**<br>
Pour mettre à jour le statut du groupe d'abonnement, activez le paramètre « Enable subscription groups in group call » dans le tableau de bord de RudderStack et envoyez le statut du groupe d'abonnement dans l'appel group.

{% endtab %}
{% tab Alias %}

La [méthode `alias`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias) de RudderStack vous permet de fusionner différentes identités d'un utilisateur connu. Notez que RudderStack prend en charge l'appel alias pour Braze uniquement en mode cloud.

{% endtab %}
{% endtabs %}

## Envoyer les traits utilisateur sous forme d'attributs personnalisés imbriqués {#send-user-traits-as-nested-custom-attributes}

Vous pouvez envoyer les traits utilisateur à Braze sous forme d'attributs personnalisés imbriqués et effectuer des opérations d'ajout, de mise à jour et de suppression sur ces traits. Pour ce faire, activez le paramètre « Use Custom Attributes Operation dashboard » dans RudderStack lors de la configuration de la destination Braze. Cette fonctionnalité n'est disponible qu'en mode cloud.

Vous pouvez envoyer les traits utilisateur sous forme d'attributs personnalisés imbriqués dans vos événements `identify` au format suivant :
```javascript
rudderanalytics.identify("1hKOmRA4GRlm", {
  "cars": {
    "add": [{
      "age": 27,
      "id": 1,
      "name": "Alex Keener"
    }],
    "update": [{
        "age": 30,
        "id": 2,
        "identifier": "id",
        "name": "Rowan"
      },
      {
        "age": 27,
        "id": 1,
        "identifier": "id",
        "name": "Alex"
      }
    ]
  },
  "country": "USA",
  "email": "alex@example.com",
  "firstName": "Alex",
  "gender": "M",
  "pets": [{
      "breed": "beagle",
      "id": 1,
      "name": "Scooby",
      "type": "dog"
    },
    {
      "breed": "calico",
      "id": 2,
      "name": "Garfield",
      "type": "cat"
    }
  ]
})
```

Pour envoyer les traits utilisateur sous forme d'attributs personnalisés via les appels `track`, `page` ou `screen`, transmettez `traits` comme champ contextuel dans l'événement :
```javascript
rudderanalytics.track("Product Viewed", {
    revenue: 8.99,
    currency: "USD",
 },{
  "traits": {
    "cars": {
      "add": [{
        "age": 27,
        "id": 1,
        "name": "Alex Keener"
      }],
      "update": [{
          "age": 30,
          "id": 2,
          "identifier": "id",
          "name": "Alex"
        },
        {
          "age": 27,
          "id": 1,
          "identifier": "id",
          "name": "Rowan"
        }
      ]
    },
    "city": "Disney",
    "country": "USA",
    "email": "alexa@example.com",
    "firstName": "Alexa",
    "gender": "woman",
    "pets": [{
        "breed": "beagle",
        "id": 1,
        "name": "Scooby",
        "type": "dog"
      },
      {
        "breed": "calico",
        "id": 2,
        "name": "Garfield",
        "type": "cat"
      }
    ]
  }
});
```

{% alert note %}
Pour les opérations de mise à jour et de suppression, `identifier` est une clé obligatoire. Si les opérations d'ajout, de mise à jour ou de suppression ne sont pas présentes dans le tableau imbriqué, RudderStack utilise par défaut l'opération de création pour créer les propriétés. Reportez-vous à la section [Tableau d'objets]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) pour plus d'informations sur l'envoi d'attributs personnalisés imbriqués.
{% endalert %}