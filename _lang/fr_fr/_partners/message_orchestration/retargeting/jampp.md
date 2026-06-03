---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "Cet article de référence présente le partenariat entre Braze et Jampp, une plateforme de marketing à la performance utilisée pour acquérir et recibler des clients mobiles."
page_type: partner
search_tag: Partner

---

# Jampp

> [Jampp](https://www.jampp.com/) est une plateforme de marketing à la performance utilisée pour acquérir et recibler des clients mobiles. Jampp associe les données comportementales à la technologie prédictive et programmatique pour générer du chiffre d'affaires pour les annonceurs en affichant des publicités personnelles et pertinentes qui incitent les consommateurs à acheter pour la première fois ou plus souvent.

_Cette intégration est maintenue par Jampp._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Jampp permet aux utilisateurs de l'entreprise de synchroniser des événements dans Jampp via des événements webhook Braze. Ainsi, les clients peuvent ajouter des ensembles de données plus riches à leurs initiatives de reciblage au sein de leurs écosystèmes de publicité mobile.

Voici quelques exemples de situations dans lesquelles vous souhaiteriez recibler des clients à l'aide d'une publicité :
- Lorsque l'état de l'abonnement e-mail ou push d'un client change.
- La manière dont un client a interagi avec une campagne de communication Braze.
- Si le client a déclenché un géorepérage spécifique.

## Conditions préalables {#prerequisites}

Cette intégration prend en charge les applications iOS et Android.

| Exigence | Description |
|---|---|
| Compte Jampp | Un [compte Jampp](https://www.jampp.com/) est nécessaire pour bénéficier de ce partenariat. |
| ID de l'application Android | Votre identifiant unique d'application Braze pour Android (tel que « com.example »). |
| ID de l'application iOS | Votre identifiant unique d'application Braze pour iOS (tel que « 012345678 »). |
| Activer la collecte IDFA dans le SDK Braze | La collecte IDFA est facultative dans le SDK Braze et désactivée par défaut. |
| Collecte de l'ID publicitaire Google via un attribut personnalisé | La collecte de l'ID publicitaire Google est facultative pour les clients et peut être collectée en tant qu'[attribut personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types).
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Créer un modèle de webhook dans Braze {#step-1-create-a-webhook-template-in-braze}

Pour créer un modèle de webhook Jampp à utiliser dans de futures Campaigns ou Canvas, accédez à **Contenu** > **Webhook** dans le tableau de bord de Braze. Ensuite, sélectionnez **Créer un modèle de webhook**.

Si vous souhaitez réaliser une Campaign webhook Jampp ponctuelle ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d'une nouvelle Campaign.

Dans votre nouveau modèle de webhook, remplissez les champs suivants :
- **Request Body** : Raw Text
- **Webhook URL** :
{% raw %}
```liquid
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

http://tracking.jampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == blank %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=braze

{% if {{most_recently_used_device.${idfa}}} == blank and {{custom_attribute.${aaid}}} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

Dans l'URL du webhook, vous devez :
- Définir le nom de l'événement. Ce nom apparaîtra dans votre tableau de bord Jampp.
- Transmettre l'identifiant unique de votre application pour Android (tel que « com.example ») et iOS (tel que « 012345678 »).
- Insérer du [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid) pour l'attribut personnalisé approprié que vous suivez en tant qu'ID publicitaire Google. Notez que l'ID publicitaire Google est indiqué comme `aaid` dans cet exemple, mais vous devrez le remplacer par le nom de l'attribut personnalisé défini par vos développeurs.

![L'URL du webhook et la prévisualisation du message affichés dans le générateur de webhooks Braze.]({% image_buster /assets/img/jampp_webhook.png %})

{% alert important %}
Braze ne collecte pas automatiquement l'IDFA/AAID de l'appareil, vous devez donc enregistrer ces valeurs vous-même. Sachez que vous pouvez avoir besoin du consentement de l'utilisateur pour collecter ces données.
{% endalert %}

#### En-têtes de requête et méthode {#request-headers-and-method}

Le webhook Jampp nécessite une méthode HTTP et un en-tête de requête.

- **Méthode HTTP** : GET
- **En-têtes de requête** :
  - **Content-Type** : application/json

![Les en-têtes de requête, la méthode HTTP et la prévisualisation du message affichés dans le générateur de webhooks Braze.]({% image_buster /assets/img/jampp_method.png %})

#### Corps de la requête {#request-body}

Vous n'avez pas besoin de définir un corps de requête pour ce webhook.

### Étape 2 : Prévisualiser votre requête {#step-2-preview-your-request}

Prévisualisez le message pour vous assurer que la requête s'affiche correctement pour les différents utilisateurs. Nous vous recommandons de prévisualiser et d'envoyer des requêtes de test pour les utilisateurs Android et iOS. Si la requête aboutit, l'API répondra par `HTTP 204`.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page ! <br>Les modèles de webhook mis à jour se trouvent dans la liste **Modèles de webhook enregistrés** lors de la création d'une nouvelle [campagne webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}