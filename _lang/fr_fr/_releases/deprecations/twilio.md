---
nav_title: Partenariat Twilio
alias: /partners/twilio/

description: "Cet article présente le partenariat entre Braze et Twilio."
page_type: update
channel:
  - SMS
  - Webhook
---

# Twilio

{% alert warning %}
Notez que le support pour l'intégration du webhook Twilio sera interrompu le 31 janvier 2020. Si vous souhaitez continuer à accéder aux services SMS avec Braze, consultez notre [documentation sur les SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/).
{% endalert %}

Pour cet exemple, nous allons configurer le canal webhook de Braze pour envoyer des SMS et des MMS à vos utilisateurs, via l'[API d'envoi de messages](https://www.twilio.com/docs/api/rest/sending-messages) de Twilio. Pour plus de commodité, un modèle de webhook Twilio est inclus dans le tableau de bord.

## URL HTTP {#http-url}

L'URL du webhook est fournie par Twilio dans votre tableau de bord. Cette URL est propre à votre compte Twilio, car elle contient votre ID de compte Twilio (`TWILIO_ACCOUNT_SID`).

Dans notre exemple Twilio, l'URL du webhook est `https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json`. Vous trouverez cette URL dans la section *Getting Started* de la console Twilio.

![Twilio_Console]({% image_buster /assets/img_archive/Twilio_Console.png %})

## Corps de la requête {#request-body}

L'API Twilio s'attend à ce que le corps de la requête soit encodé en URL. Il faut donc commencer par changer le type de requête dans le compositeur de webhook de Braze en `Raw Text`. Les paramètres requis pour le corps de la requête sont *To*, *From* et *Body*.

La capture d'écran suivante illustre l'aspect de votre requête si vous envoyez un SMS au numéro de téléphone de chaque utilisateur, avec le corps du message « Hello from Braze! ».

- Vous devez disposer de numéros de téléphone valides sur chaque profil utilisateur de votre audience cible.
- Pour respecter le format de requête de Twilio, utilisez le filtre Liquid `url_param_escape` sur le contenu de votre message. Ce filtre encode une chaîne de caractères afin que tous les caractères soient autorisés dans une requête HTML ; par exemple, le caractère plus (`+`) dans le numéro de téléphone `+12125551212` est interdit dans les données encodées en URL et sera converti en `%2B12125551212`.

![Webhook Body]({% image_buster /assets/img_archive/Webhook_Body.png %})

## En-têtes et méthode de requête {#request-headers-and-method}

Twilio nécessite deux en-têtes de requête : le Content-Type de la requête et un en-tête d'[authentification HTTP Basic](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side). Ajoutez-les à votre webhook en cliquant sur l'icône d'engrenage à côté du compositeur de webhook, puis en cliquant deux fois sur *Add New Pair*.

Nom de l'en-tête | Valeur de l'en-tête
--- | ---
Content-Type | `application/x-www-form-urlencoded`
Authorization | `{% raw %}Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}`

Assurez-vous de remplacer `TWILIO_ACCOUNT_SID` et `TWILIO_AUTH_TOKEN` par les valeurs de votre tableau de bord Twilio. Enfin, l'endpoint de l'API Twilio attend une requête HTTP POST ; choisissez donc cette option dans le menu déroulant *HTTP Method*.

![Webhook Method]({% image_buster /assets/img_archive/Webhook_Method.png %})

## Prévisualiser votre requête {#preview-your-request}

Utilisez le compositeur de webhook pour prévisualiser la requête pour un utilisateur aléatoire ou pour un utilisateur disposant d'identifiants particuliers, afin de vous assurer que la requête s'affiche correctement.

![Webhook Preview]({% image_buster /assets/img_archive/Webhook_Preview.png %})