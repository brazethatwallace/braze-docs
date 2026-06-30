---
nav_title: Cas d'utilisation
article_title: Cas d'utilisation de la Transformation des données Braze
page_order: 2
page_type: reference
description: "Cet article de référence présente quelques cas d'utilisation de la Transformation des données Braze."
---

# Cas d'utilisation de la Transformation des données {#data-transformation-use-cases}

> Découvrez les cas d'utilisation possibles avec la Transformation des données Braze et une combinaison de webhooks provenant des plateformes externes données en exemple.

## Générer des prospects {#generating-leads}

Vous hébergez un formulaire Typeform de génération de prospects sur votre site web. Lorsque de nouveaux utilisateurs remplissent ce formulaire, vous pouvez :
- Créer de nouveaux utilisateurs dans Braze.
- Les ajouter à l'une de vos listes d'e-mails Braze.
- Synchroniser certaines de leurs réponses en tant qu'attributs personnalisés dans Braze, car leurs réponses sont des données first-party précieuses qui peuvent alimenter des expériences de communication personnalisées pour une utilisation future.

## Ouverture de tickets de service {#opening-service-tickets}

Lorsque les clients ouvrent des tickets de service client sur une plateforme comme Zendesk, vous pouvez :
- Écrire un événement personnalisé dans Braze lorsqu'un ticket Zendesk est créé.
- Écrire un événement personnalisé avec des propriétés d'événement dans Braze lorsqu'une note CSAT négative est fournie à Zendesk.

## Intégration avec Braze {#integrating-with-braze}

Braze dispose d'une intégration avec [Iterate]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/surveys/iterate), une plateforme d'informations et d'enquêtes clients. Grâce à la Transformation des données, vous pouvez enregistrer plusieurs réponses d'enquête sous un seul attribut personnalisé imbriqué, au lieu de recourir à l'intégration existante qui enregistre plusieurs attributs personnalisés.

## Synchroniser les attributs de contacts HubSpot {#sync-hubspot-contact-attributes}

Si vous utilisez HubSpot comme CRM et Braze pour l'envoi de messages, vous pouvez utiliser la Transformation des données pour convertir les payloads de webhooks HubSpot en mises à jour Braze `/users/track`.

Cet exemple vérifie la présence d'un `external_id`, copie l'objet utilisateur entrant et envoie tous les champs inclus à Braze en tant qu'attributs personnalisés.

```
function toBrazeTrackPayload(userObject) {
  if (!userObject.external_id) {
    throw new Error("Braze requires an 'external_id' field.");
  }

  return {
    attributes: [userObject]
  };
}

const brazePayload = toBrazeTrackPayload(payload);
return brazePayload;
```

## Exemple de code de transformation {#example-transformation-code}

Voici un exemple de payload provenant de Typeform, une plateforme d'enquête, qui est envoyé chaque fois qu'une réponse à l'enquête est reçue.

![Capture d'écran liée à l'exemple de code de transformation.]({% image_buster /assets/img/data_transformation/data_transformation2.png %})

{% tabs local %}
{% tab Transformation basique %}

Cet exemple prend les réponses à l'enquête comme attributs et écrit un événement pour indiquer que l'enquête a été complétée :

```
return {
  "attributes": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_rating": payload.form_response.answers[1].number
    }
  ],
  "events": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
}
```

{% endtab %}
{% tab Transformation avancée %}

Poursuivons avec l'exemple de transformation basique et introduisons une instruction `if` pour catégoriser l'utilisateur en fonction de l'une des réponses.

```
let nps_category;
let nps_number = payload.form_response.answers[1].number;
if (nps_number < 7) {
  nps_category = "Detractor";
} else if (nps_number == 7 || nps_number == 8) {
  nps_category = "Passive";
} else if (nps_number > 8) {
  nps_category = "Promoter";
}

return {
  "attributes": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_NPS_category": nps_category
    }
  ],
  "events": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
};
```
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/data_transformation/data_transformation2.png %}