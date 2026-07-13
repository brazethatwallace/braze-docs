---
nav_title: Rokt Calendar
article_title: Rokt Calendar
description: "Cet article de référence présente le partenariat entre Braze et Rokt Calendar, une technologie de marketing de calendrier dynamique qui permet aux marques de diffuser des événements personnalisés et des communications promotionnelles sous forme d'événements de calendrier et de notifications."
page_type: partner
search_tag: Partner
noindex: true
hidden: true
---

# Rokt Calendar

> [Rokt Calendar](https://www.rokt.com/rokt-calendar/) est une technologie de marketing de calendrier dynamique qui permet aux marques de diffuser des événements personnalisés et des communications promotionnelles sous forme d'événements de calendrier et de notifications.

_Cette intégration est maintenue par Rokt Calendar._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et de Rokt Calendar permet de transmettre vos abonnés Rokt Calendar et leurs données vers Braze via un webhook Braze. Vous pouvez ensuite utiliser ces données dans des Canvas Braze pour le ciblage des parcours et la segmentation de l'audience à l'aide de l'un des [attributs personnalisés Rokt Calendar](#audience-segmentation) suivants.

## Conditions préalables {#prerequisites}

| Condition  | Description |
| ------------ | ----------- |
| Compte Rokt Calendar | Un compte Rokt Calendar spécifique au client est nécessaire pour profiter de ce partenariat. Contactez [sales-calendar@rokt.com](mailto:sales-calendar@rokt.com) pour parler à un gestionnaire de compte.  |
| Configuration de Rokt Calendar | Votre gestionnaire de compte Rokt Calendar travaillera avec vous pour configurer le calendrier de manière à ce qu'il corresponde au mieux à vos besoins, y compris les paramètres tels que :<br>- Drapeau de fusion<br>- Drapeau de repli de l'identifiant de l'abonné (SubscriberID)<br>- Capture d'e-mail, si nécessaire |
| Identifiants OAuth Rokt Calendar | Cette clé fournie par votre gestionnaire de compte Rokt Calendar vous permettra de connecter vos comptes Braze et Rokt Calendar.<br><br>Elle peut être créée dans le tableau de bord de Braze sous **Paramètres** > **Contenu connecté**. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`. Vous devrez fournir cette clé à votre gestionnaire de compte Rokt Calendar.<br><br>Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| [Endpoint REST Braze]({{site.baseurl}}/api/basics/#endpoints) | L'URL de votre endpoint REST. Votre endpoint dépendra de l'URL Braze de votre instance. |
| ID externe de l'abonné | Il s'agit de l'identifiant utilisé par le processus d'abonnement Rokt Calendar pour faire correspondre l'abonné au calendrier avec l'utilisateur Braze. C'est un élément que vous transmettez à Rokt Calendar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Segmentation de l'audience {#audience-segmentation}

Lorsque Rokt Calendar crée un nouvel utilisateur ou fait correspondre un abonné existant avec un utilisateur Braze, Rokt Calendar envoie les attributs d'abonnement personnalisés suivants que vous pouvez filtrer dans Braze :

| Attribut personnalisé  | Définition       | Exemple          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | Code du compte Rokt Calendar | `brazetest/f5733866ade2` et `brazetest/ff10919f1078` |
| `rokt:account_id` | ID du compte Rokt Calendar | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | Nom du compte Rokt Calendar | `Braze Test/f5733866ade2` |
| `rokt:calendar_code` | Code du calendrier Rokt Calendar | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | ID du calendrier Rokt Calendar | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | Titre du calendrier Rokt Calendar | `Test Calendar 1/f5733866ade2` |
| `rokt:country_code` | Code pays lié à l'abonnement créé | `AU/f5733866ade2` |
| `rokt:device_name` | Type d'appareil lié à l'abonnement créé | `Desktop/f5733866ade2` |
| `rokt:geo_country` | Pays d'origine lié à l'abonnement créé | `Australia/f5733866ade2` |
| `rokt:optIn1` | Si l'utilisateur a accepté la première des deux options d'inscription liées à l'abonnement créé | `True/f5733866ade2` |
| `rokt:optIn2` | Si l'utilisateur a accepté la deuxième des deux options d'inscription liées à l'abonnement créé | `True/f5733866ade2` |
| `rokt:source` | La source de l'abonnement créé | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | L'adresse e-mail saisie par l'utilisateur au cours du processus d'abonnement | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | L'ID de l'abonnement, servant d'identifiant unique, lié à l'abonnement créé | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | Méthode d'abonnement (webcal/Google) liée à l'abonnement créé | `WebCal/f5733866ade2` |
| `rokt:tags` | Étiquettes du calendrier utilisées en rapport avec l'abonnement créé | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Audience segmentation #audience-segmentation" }

Rokt Calendar déclenche également un événement personnalisé `subscribe` dès que l'utilisateur s'est abonné à votre calendrier Rokt. Cet événement peut être utilisé dans la segmentation Braze ou comme déclencheur d'une campagne ou d'un composant Canvas.

## Intégration {#integration}

### Étape 1 : Créer une audience d'abonnés au calendrier {#step-1-building-an-audience-of-calendar-subscribers}

Pour envoyer des événements de calendrier à partir d'un Canvas, vous devez d'abord avoir configuré un calendrier Rokt avec des utilisateurs déjà abonnés. Pour ce faire, vous devrez indiquer à vos utilisateurs où et comment s'abonner au calendrier. Rokt Calendar vous recommande de :

#### Fournir des points d'intégration des abonnements {#provide-subscription-integration-points}
Pour créer une audience d'abonnés au calendrier, vous devez proposer une destination vers laquelle l'utilisateur peut naviguer et s'abonner. Voici quelques exemples de points d'intégration des abonnements :
  - Ajouter un bouton calendrier à votre site web
  - Ajouter un lien vers le calendrier dans un e-mail ou un SMS
  - Ajouter un bouton calendrier à votre application
  - Ajouter un lien vers le calendrier sur les réseaux sociaux

#### Promouvoir le calendrier {#promote-the-calendar}
Pour créer une audience d'abonnés, vous devrez promouvoir le calendrier auprès de votre audience afin qu'elle sache comment s'abonner. Voici quelques exemples de promotion du calendrier :
  - Publications sur les réseaux sociaux
  - Newsletters et mises à jour par e-mail
  - Articles de blog
  - Notifications in-app

### Étape 2 : Créer un webhook Rokt Calendar dans Braze {#step-2-create-a-rokt-calendar-webhook-in-braze}

Dans Braze, vous pouvez configurer une campagne webhook ou un webhook dans un Canvas pour :

- Envoyer un nouvel événement personnalisé : permet d'ajouter de nouveaux événements au calendrier d'un segment d'abonnés.
- Mettre à jour un événement personnalisé : permet de mettre à jour un événement existant dans les calendriers des abonnés.

Pour créer un modèle de webhook Rokt Calendar à utiliser dans de futures campagnes ou Canvas, accédez à **Modèles** > **Modèles de webhook** dans la plateforme Braze.

Si vous souhaitez créer une campagne webhook Rokt Calendar ponctuelle ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d'une nouvelle campagne.

{% tabs %}
{% tab Send a new event %}
Une fois que vous avez sélectionné le modèle de webhook Rokt Calendar, vous devriez voir ce qui suit :
- **Webhook URL** : {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **Request Body** : Raw Text
{% endtab %}
{% tab Update an existing event %}
Une fois que vous avez sélectionné le modèle de webhook Rokt Calendar, vous devriez voir ce qui suit :
- **Webhook URL** : {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **Request Body** : Raw Text
{% endtab %}
{% endtabs %}

#### En-têtes et méthode de la requête {#request-headers-and-method}

Rokt Calendar requiert un `HTTP Header` pour l'autorisation qui inclut le nom de votre identifiant de contenu connecté Rokt Calendar. Les éléments suivants sont déjà inclus dans le modèle sous forme de paires clé-valeur, mais dans l'onglet **Settings**, vous devez remplacer `<Rokt-Calendar-API>` par le nom de l'identifiant trouvé dans `Manage Settings > Connected Content > Credential`.

{% raw %}
- **HTTP Method** : POST
- **Request Header** :
  - **Authorization** : Bearer `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Content-Type** : application/json
{% endraw %}

#### Corps de la requête {#request-body}

{% tabs local %}
{% tab Send a new event %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  },
  "subscriptionIds": ["{{custom_attribute.${rokt:subscription_id}| join: '","'  }}"]
}
```
{% endraw %}
{% endtab %}
{% tab Update an existing event %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  }
}
```
{% endraw %}
{% endtab %}
{% tab Event details %}
Les champs suivants contiennent des informations qui peuvent être personnalisées au niveau de l'événement.

| Champ             | Définition       | Exemple          |
| ----------------  | ---------------- | ---------------- |
| `eventId` <br>***Requis** | Un identifiant unique pour l'événement à ajouter ou à mettre à jour | `Event_00001`
| `eventTitle` <br>***Requis** | Le titre de l'événement tel qu'il apparaîtrait dans le calendrier | Summer Sale 2019
| `eventDescr` | La description de l'événement telle qu'elle apparaîtrait dans le calendrier | The sale is on for three days; click this link `www.mybusiness.com/sale` to see the offers. |
| `eventLocation` | L'emplacement de l'événement tel qu'il apparaîtrait dans le calendrier. Notez qu'il est souvent utilisé comme un deuxième appel à l'action, complémentaire au eventTitle. | Open the event to get 50% off |
| `eventStart` <br>***Requis**  | La date et l'heure de début de l'événement telles qu'elles apparaissent dans le calendrier | `2019-02-21T15:00:00` |
| `eventEnd` <br>***Requis**  | La date et l'heure de fin de l'événement telles qu'elles apparaissent dans le calendrier | `2019-02-21T16:00:00` |
| `eventTz` <br>***Requis**  | Le fuseau horaire de l'événement tel qu'il apparaîtrait dans le calendrier. Notez que la liste des fuseaux horaires applicables se trouve [ici](https://roktcalendar-api.readme.io/docs/timezones). | `Eastern Standard Time` |
| `notifyBefore` <br>***Requis**  | Le délai de rappel de l'événement tel qu'il apparaîtrait dans le calendrier. Notez qu'il est exprimé en minutes. | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Request body" }
{% endtab %}
{% endtabs %}

{% alert tip %}
Pour une liste des fuseaux horaires valides, consultez [https://roktcalendar-api.readme.io/reference/timezones](https://roktcalendar-api.readme.io/reference/timezones).
{% endalert %}

### Étape 3 : Prévisualiser votre requête {#step-3-preview-your-request}

Prévisualisez votre requête dans le panneau **Preview** ou accédez à l'onglet **Test**, où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser le vôtre pour tester votre webhook.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page ! <br>Les modèles de webhook mis à jour se trouvent dans la liste **Modèles de webhook enregistrés** lors de la création d'une nouvelle [campagne webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}