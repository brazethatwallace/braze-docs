---
nav_title: Connexion à l'API Customer Data
article_title: Se connecter à l'API Customer Data de Movable Ink
description: "Cet article de référence explique comment se connecter pour activer les données d'événements clients stockées dans Braze afin de générer du contenu personnalisé dans Movable Ink à l'aide de l'API Customer Data."
page_type: partner
search_tag: Partner
---

# Se connecter à l'API Customer Data de Movable Ink {#connect-to-the-movable-ink-customer-data-api}

> L'intégration de l'API Customer Data de Braze et Movable Ink permet aux marketeurs d'activer les données d'événements clients stockées dans Braze pour générer du contenu personnalisé au sein de Movable Ink.

Movable Ink est capable d'ingérer des événements comportementaux depuis Braze via leur API Customer Data. Les événements sont stockés sur les profils utilisateur en fonction de l'identifiant utilisateur unique (UUID) transmis à Movable Ink.

Pour plus d'informations sur les Stories, l'API Customer Data de Movable Ink et la manière dont Movable Ink exploite les données comportementales, consultez les articles suivants du centre d'assistance :

- [Alimenter le contenu avec des données comportementales](https://support.movableink.com/hc/en-us/sections/360001239453-Power-content-with-behavioral-data)
- [Introduction et guide de l'API Customer Data](https://support.movableink.com/hc/en-us/articles/13815957200663-Customer-Data-API-introduction-and-guide)
- [FAQ : API Customer Data](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Movable Ink | Un compte Movable Ink est requis pour bénéficier de ce partenariat. |
| Identifiants API Movable Ink | L'équipe Solutions de Movable Ink générera des identifiants API pour vous. Les identifiants API se composent de :{::nomarkdown}<ul><li>Une URL d'endpoint (où les données seront envoyées)</li><li>Un nom d'utilisateur et un mot de passe (utilisés pour authentifier l'API)</li></ul>{:/} Si vous le souhaitez, Movable Ink peut fournir le nom d'utilisateur et le mot de passe sous forme de valeur encodée en base64 à utiliser comme valeur d'en-tête d'autorisation basique. |
| Payloads d'événements comportementaux | Vous devrez partager vos payloads d'événements avec l'équipe Expérience Client de Movable Ink. Consultez la section [Partage des payloads d'événements](#event-payloads) avec Movable Ink pour plus de détails. |
| Ressources créatives et logique métier | Vous devrez partager des ressources créatives avec Movable Ink, notamment des fichiers Adobe Photoshop (PSD) indiquant à Movable Ink comment construire le bloc, ainsi qu'une image de secours. Vous devrez également fournir la logique métier définissant comment et quand afficher le bloc de contenu activé par le partenaire. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Créer une campagne webhook dans Braze {#step-1-create-a-webhook-campaign-in-braze}

#### Étape 1a : Créer une nouvelle campagne {#step-1a-create-a-new-campaign}

1. Dans Braze, [créez une campagne webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
2. Donnez un nom et une description facultative à votre campagne.
3. Sélectionnez **Blank Template** comme modèle.

#### Étape 1b : Ajouter vos identifiants API Customer Data {#step-1b-add-your-customer-data-api-credentials}

1. Dans le champ **Webhook URL**, saisissez l'URL de l'endpoint Movable Ink.

![Onglet Compose du compositeur webhook dans Braze avec l'URL de l'endpoint Movable Ink et le corps de requête défini sur paires clé-valeur JSON.]({% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}){: style="max-width:75%" }

{:start="2"}
2. Sélectionnez l'onglet **Settings**.
3. Ajoutez les en-têtes de requête suivants en tant que paires clé-valeur :

| Clé | Valeur |
| --- | --- |
| Content-Type | application/json |
| Authorization | Saisissez l'authentification basique que vous avez reçue de Movable Ink. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 1b : Ajouter vos identifiants API Customer Data" }

![Onglet Settings du compositeur webhook dans Braze avec des paires clé-valeur pour Content-Type et Authorization.]({% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}){: style="max-width:75%" }

#### Étape 1c : Configurer votre payload {#step-1c-configure-your-payload}

1. Retournez dans l'onglet **Compose**.
2. Pour votre **Request Body**, créez votre propre corps de requête avec des paires clé-valeur JSON ou saisissez votre payload d'événement en tant que texte brut. Reportez-vous aux [exemples de payloads](#sample-payloads) pour des exemples d'événements eCommerce standard.

![Onglet Compose du compositeur webhook dans Braze avec des paires clé-valeur JSON pour l'ID, l'horodatage, l'ID utilisateur et le type d'événement.]({% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}){: style="max-width:75%" }

#### Étape 1d : Tester votre webhook {#step-1d}

Vous devrez partager un exemple de payload avec votre équipe Expérience Client de Movable Ink. Vous pouvez générer ce payload dans l'onglet **Test** en fonction du payload que vous avez construit.

{% alert important %}
Movable Ink recommande d'attendre pour tester votre webhook dans Braze jusqu'à ce que votre équipe Expérience Client de Movable Ink ait confirmé qu'elle a terminé le mappage et est prête à recevoir un test. Si ce mappage n'est pas terminé, vous recevrez probablement une erreur lors du test.
{% endalert %}

Pour tester votre webhook, procédez comme suit :

1. Sélectionnez l'onglet **Test**.
2. Prévisualisez le message en tant qu'utilisateur pour voir un exemple de payload d'événement pour cet utilisateur. Vous pouvez choisir entre prévisualiser en tant qu'utilisateur aléatoire, utilisateur spécifique ou utilisateur personnalisé.
3. Si tout semble correct, cliquez sur **Send test** pour envoyer une requête de test.

![Message de réponse du webhook dans Braze affichant une réponse 200 OK.]({% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}){: style="max-width:75%" }

### Étape 2 : Finaliser la configuration de votre campagne {#step-2-finalize-your-campaign-setup}

#### Étape 2a : Planifier votre campagne {#step-2a-schedule-your-campaign}

Lorsque vous avez terminé de composer et de tester le webhook, [planifiez votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

Braze prend en charge les livraisons planifiées, par événement et déclenchées par API. La [livraison par événement]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/) est généralement la mieux adaptée à la plupart des cas d'utilisation d'événements comportementaux. Pour toute question sur ce qui convient le mieux à votre cas d'utilisation, contactez vos gestionnaires de la satisfaction client Braze et Movable Ink.

Pour la livraison par événement :

1. Spécifiez l'action de déclenchement. Il s'agit de l'événement qui déclenchera le webhook vers Movable Ink.
2. Assurez-vous que le **Schedule Delay** est réglé sur **Immediately**. Les données d'événement doivent être envoyées à Movable Ink immédiatement après l'événement, sans délai.
3. Définissez la durée de la campagne en spécifiant une heure de début. Une heure de fin n'est probablement pas nécessaire, mais elle peut être définie si le cas d'utilisation l'exige.

{% alert note %}
Pour vous assurer que les données sont diffusées en temps réel vers Movable Ink, ne sélectionnez pas **Send campaign to users in their local time zone**.
{% endalert %}

#### Étape 2b : Spécifier votre audience {#step-2b-specify-your-audience}

Ensuite, déterminez quels utilisateurs vous souhaitez cibler pour cette campagne. Pour plus de détails, consultez [Ciblage des utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/).

Veillez à ne pas utiliser de test A/B dans votre campagne en décochant la case **Control Group**. Si un groupe de contrôle est inclus, les données d'un pourcentage d'utilisateurs ne seront pas envoyées à Movable Ink. L'intégralité de votre audience devrait être dirigée vers la variante plutôt que vers le groupe de contrôle.

![Panneau de test A/B dans une campagne Braze avec une distribution de variante de 100 % attribuée à la variante 1, et aucun groupe de contrôle.]({% image_buster /assets/img/movable_ink/cd_api_webhook_ab.png %})

#### Étape 2c : Choisir des événements de conversion (facultatif) {#step-2c-choose-conversion-events-optional}

Si vous le souhaitez, vous pouvez attribuer des événements de conversion à cette campagne dans Braze.

Cependant, étant donné que le webhook est uniquement destiné à diffuser des données, l'attribution à ce niveau est probablement moins utile que l'analyse de l'attribution au niveau de la campagne une fois que les données comportementales de Braze sont utilisées pour personnaliser le contenu.

### Étape 3 : Lancer la campagne {#step-3-launch-the-campaign}

Vérifiez votre configuration de webhook et lancez votre campagne.

## Considérations {#considerations}

### S'aligner sur un identifiant utilisateur unique {#aligning-on-a-unique-user-identifier}

Assurez-vous que la valeur de l'identifiant utilisateur unique (UUID) que vous utilisez comme `mi_u` est disponible dans Braze et peut être incluse dans les payloads d'événements envoyés à Movable Ink.

Cela garantit que les événements comportementaux auxquels Movable Ink fait référence lors de la génération d'une image sont associés au même client pour lequel les événements comportementaux ont été reçus. Si la valeur UUID n'est pas identique à l'`external_id` de Braze, l'UUID doit être capturé et transmis à Braze en tant qu'attribut ou dans les propriétés d'événement d'un événement Braze pour exploiter cet identifiant.

Braze suit le comportement des utilisateurs sur plusieurs plateformes (telles que le web et les applications mobiles), de sorte qu'un seul utilisateur peut avoir plusieurs identifiants anonymes distincts. Ces identifiants peuvent être fusionnés dans le profil utilisateur unique connu de Stories lorsqu'un événement `identify` est envoyé à Movable Ink, à condition que l'événement `identify` inclue à la fois un identifiant anonyme et l'identifiant unique connu.

Une fois que Movable Ink reçoit un `user_id` pour un utilisateur donné, tous les événements futurs pour cet utilisateur doivent inclure ce même `user_id`.

### Partage des payloads d'événements avec Movable Ink {#event-payloads}

Avant de configurer le connecteur vers l'API Customer Data de Movable Ink, assurez-vous de partager vos payloads d'événements avec l'équipe Expérience Client de Movable Ink. Cela permet à Movable Ink de mapper vos événements sur leur schéma d'événements et évitera tout appel API rejeté ou échoué.

Vous pouvez générer un payload d'événement dans Braze en utilisant n'importe quelles propriétés d'événement. Générez un exemple de payload pour un utilisateur aléatoire ou en recherchant un ID utilisateur spécifique. Reportez-vous à l'[étape 1d](#step-1d) ci-dessus pour plus de détails.

Partagez cet exemple de payload avec votre équipe Expérience Client de Movable Ink. Assurez-vous qu'il ne contient aucune information personnelle sensible identifiable (telle qu'une adresse e-mail, un numéro de téléphone ou des dates de naissance complètes).

Pour en savoir plus sur les propriétés d'événements personnalisés et le format attendu des données contenues dans les propriétés, consultez [Propriétés d'événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/).

### Utilisateurs connus et utilisateurs anonymes {#known-versus-anonymous-users}

Dans Braze, les événements peuvent être enregistrés sous un profil utilisateur anonyme. Les identifiants liés au profil utilisateur lors de l'enregistrement des événements dépendent de la manière dont l'utilisateur a été créé (via le SDK Braze ou les API) et de son stade actuel dans le cycle de vie utilisateur.

#### Transférer uniquement les événements Braze pour les utilisateurs connus {#only-forwarding-braze-events-for-known-users}

Dans votre campagne webhook, utilisez le filtre `External User ID` pour cibler uniquement les utilisateurs qui possèdent un `external_id` avec le filtre `External User ID` `is not blank`.

#### Transférer les événements Braze pour les utilisateurs anonymes et connus {#forwarding-braze-events-for-anonymous-and-known-users}

Si vous souhaitez transférer les événements Braze d'utilisateurs anonymes (utilisateurs avant qu'un `external_id` ne soit attribué à leur profil), vous devrez décider quel identifiant utiliser comme `anonymous_id` pour Movable Ink jusqu'à ce qu'un `external_id` soit disponible. Choisissez un `anonymous_id` qui restera constant sur votre profil utilisateur Braze. Vous pouvez utiliser la logique Liquid dans le corps du webhook pour décider s'il faut transmettre un `anonymous_id` ou un `user_id`.

Pour en savoir plus, consultez les exemples de webhooks sous [exemples de payloads](#sample-payloads).

## Exemples de payloads {#sample-payloads}

### Événement de consultation de produit {#product-view-event}

{% tabs local %}
{% tab Example Braze Trigger Event %}

{% raw %}

```json
{
  "events": [
    {
      "email": "test@braze.com",
      "name": "Product Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "categories": [
          {
            "id": "Bathroom",
            "url": "https://example.com/cat/bathroom"
          }
        ],
        "meta": {
          "color": "green"
        },
        "title": "All-Purpose Cleaning Wipes",
        "price": 1.99,
        "id": "56544",
        "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "Bathroom",
        "url": "https://example.com/cat/bathroom"
      }
    ],
    "meta": {
      "color": "green"
    },
    "title": "All-Purpose Cleaning Wipes",
    "price": 1.99,
    "id": "56544",
    "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'

```

{% endraw %}
{% endtab %}
{% tab Example webhook %}

Dans cet exemple, une adresse e-mail hachée est utilisée comme `anonymous_id` pour les utilisateurs qui ne possèdent pas d'`external_id`.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

// Condition logic to determine which identifier to use. If an external_id is available use that, otherwise use the anonymous_id
{% if {{${user_id}}} %}
{% capture user_identifier %}"user_id": "{{${user_id}}}"{% endcapture %}
{% else %}
{% capture user_identifier %}"anonymous_id": "{{anon_id}}"{% endcapture %}
{% endif %}

{
  {{user_identifier}}
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "{{event_properties.${categories}[0].id}}",
        "url": "{{event_properties.${categories}[0].url}}"
      }
    ],
    "meta": {
      "color": "{{event_properties.${meta}.color}}"
    },
    "title": "{{event_properties.${title}}}",
    "price": "{{event_properties.${price}}}",
    "id": "{{event_properties.${id}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
}

```

{% endraw %}
{% endtab %}
{% endtabs %}

### Événement de consultation de catégorie {#category-view-event}

{% tabs local %}
{% tab Example Braze Trigger Event %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Category Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "id": "bathroom-1",
        "title": "Bathroom Stuff",
        "url": "https://www.example.com/categories/bathroom"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "category_viewed",
  "properties": {
    "id": "bathroom-1",
    "title": "Bathroom Stuff",
    "url": "https://www.example.com/categories/bathroom"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'
```

{% endraw %}

{% endtab %}
{% tab Example webhook %}

Cet exemple montre un webhook qui suit les événements uniquement pour les utilisateurs connus (utilisateurs possédant un `external_id`).

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

{
  "event": "category_viewed",
  "properties": {
    "id": "{{event_properties.${id}}}",
    "title": "{{event_properties.${title}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}

### Événement d'identification {#identify-event}

{% tabs local %}
{% tab Example Braze Trigger Event %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Account Created",
      "time": "2023-12-06T19:20:45+01:00"
    }
  ]
}
```

{% endraw %}
{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "jg0iq5gd30dqpwn8zmx05p06mzjmjir4r8",
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "identify",
  "user_id": "mycustomerid123"
}'
```

{% endraw %}
{% endtab %}
{% tab Example webhook %}

Dans cet exemple, une adresse e-mail hachée est utilisée comme `anonymous_id` pour les utilisateurs qui ne possèdent pas d'`external_id`.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

{
  "anonymous_id": "{{anon_id}}",
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "identify",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}