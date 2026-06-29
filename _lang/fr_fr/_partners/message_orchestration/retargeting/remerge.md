---
nav_title: Remerge
article_title: Remerge
alias: /partners/remerge/
description: "Cet article de référence présente le partenariat entre Braze et Remerge, une application conçue pour le reciblage à grande échelle, qui vous fournit des outils pour segmenter efficacement les audiences d'applications et recibler les utilisateurs."
page_type: partner
search_tag: Partner

---

# Remerge

> [Remerge](https://www.remerge.io/) est un outil conçu pour le reciblage d'applications à grande échelle, qui vous fournit les outils nécessaires pour segmenter efficacement les audiences d'applications et recibler les utilisateurs.

_Cette intégration est maintenue par Remerge._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Remerge vous permet de développer des campagnes marketing du cycle de vie cross-canal robustes en envoyant les données des utilisateurs à Remerge via des événements webhook afin de recibler les utilisateurs par le biais de leur plateforme mobile de gestion de la demande.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Remerge | Un compte Remerge est nécessaire pour profiter de ce partenariat. |
| Clé webhook Remerge | Cette clé sera fournie par Remerge. |
| ID de l'application Android | Votre identifiant unique d'application Braze pour Android (tel que « com.example »). |
| ID de l'application iOS | Votre identifiant unique d'application Braze pour iOS (tel que « 012345678 »). |
| Activer la collecte IDFA dans le SDK Braze | La collecte IDFA est facultative dans le SDK Braze et désactivée par défaut. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Intégration {#integration}

### Étape 1 : Créer votre modèle de webhook Braze {#step-1-create-your-braze-webhook-template}

Pour créer un modèle de webhook Remerge pour de futures campagnes ou Canvas, accédez à **Contenu** > **Webhook** dans la plateforme Braze. Sélectionnez ensuite **Créer un modèle de webhook**.


Si vous souhaitez créer une campagne webhook Remerge ponctuelle ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d'une nouvelle campagne.

Dans votre nouveau modèle de webhook, remplissez les champs suivants :
- **Request Body** : Raw Text
- **Webhook URL** :
{% raw %}
```liquid
{% assign event_name = 'your_remerge_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'event_name','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

https://remerge.events/event?partner=braze&app_id=\{% if most_recently_used_device.${idfa} == blank %}android_app_id{% else %}iOS_app_id{% endif %}&key=1cs3p12k&ts='now' | date: '%s' }}&{% if {{most_recently_used_device.${idfa} == blank%}aaid=custom_attribute.${aaid}{% else %}idfa=most_recently_used_device.${idfa{%endif%}&event=event_name&non_app_event=true&data=json | url_param_escape

{% if most_recently_used_device.${idfa} == blank and custom_attribute.${aaid} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

Dans l'URL du webhook, vous devez :
- Utiliser l'API `https://remerge.events/event` pour envoyer vos événements webhook.
- Définir le nom de l'événement. Ce nom apparaîtra dans votre tableau de bord [remerge.io](https://www.remerge.io/).
- Transmettre l'identifiant d'application unique de votre application pour Android (tel que « com.example ») et iOS (tel que « 012345678 ») à Remerge.
- Définir une clé ; Remerge vous la fournira.

![L'URL du webhook et la prévisualisation du message affichées dans le générateur de webhooks de Braze.]({% image_buster /assets/img_archive/webhook_remerge_preview.png %})

{% alert important %}
Braze ne collecte pas automatiquement l'IDFA/AAID de l'appareil, vous devez donc enregistrer ces valeurs vous-même. Sachez que vous pouvez avoir besoin du consentement de l'utilisateur pour collecter ces données.
{% endalert %}

#### En-têtes de requête et méthode {#request-headers-and-method}

Le webhook Remerge nécessite une méthode HTTP et un en-tête de requête.

- **HTTP Method** : GET
- **Request Headers** :
  - **Content-Type** : application/json

![Les en-têtes de requête, la méthode HTTP et la prévisualisation du message affichés dans le générateur de webhooks de Braze.]({% image_buster /assets/img_archive/httpmethod_remerge.png %})

#### Corps de la requête {#request-body}

Vous n'avez pas besoin de définir un corps de requête pour ce webhook.

## Étape 2 : Prévisualiser votre requête {#step-2-preview-your-request}

Prévisualisez le message pour vous assurer que la requête s'affiche correctement pour les différents utilisateurs. Nous vous recommandons de prévisualiser et d'envoyer des requêtes de test pour les utilisateurs Android et iOS. Si la requête aboutit, l'API répondra avec `HTTP 204`.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page ! <br>Les modèles de webhook mis à jour se trouvent dans la liste **Modèles de webhook enregistrés** lors de la création d'une nouvelle [campagne webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}