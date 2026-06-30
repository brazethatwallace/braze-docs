---
nav_title: "POST : Mise à jour du modèle d'e-mail"
article_title: "POST : Mettre à jour les modèles d'e-mail"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Mettre à jour les modèles d'e-mail."

---
{% api %}
# Mettre à jour les modèles d'e-mail existants {#update-existing-email-templates}
{% apimethod post %}
/templates/email/update
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour des modèles d'e-mail sur le tableau de bord de Braze.

Vous pouvez accéder à l'`email_template_id` d'un modèle d'e-mail en naviguant jusqu'à lui sur la page **Modèles et médias**. L'[endpoint Créer un modèle d'e-mail]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) renvoie également une référence `email_template_id`.

Tous les champs autres que l'`email_template_id` sont facultatifs, mais vous devez spécifier au moins un champ à mettre à jour.

{% alert tip %}
Vous pouvez également appeler cet endpoint via le [serveur MCP de Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server) en utilisant la fonction [`update_email_template`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#templates). Cela permet à des outils d'intelligence artificielle comme Claude et Cursor de mettre à jour des modèles d'e-mail via des requêtes en langage naturel.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#afb25494-3350-458d-932d-5bf4220049fa {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key) avec l'autorisation `templates.email.update`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "email_template_id": (required, string) Your email template's API Identifier,
  "template_name": (optional, string) The name of your email template,
  "subject": (optional, string) The email template subject line,
  "body": (optional, string) The email template body that may include HTML,
  "plaintext_body": (optional, string) A plaintext version of the email template body,
  "preheader": (optional, string) The email preheader used to generate previews in some clients,
  "tags": (optional, array of Strings) Tags must already exist,
  "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature will be applied to the template.
}
```

## Paramètres de la requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `email_template_id` | Requis | Chaîne de caractères | L'[identifiant API de votre modèle d'e-mail]({{site.baseurl}}/api/identifier_types). |
| `template_name` | Facultatif | Chaîne de caractères | Nom de votre modèle d'e-mail. |
| `subject` | Facultatif | Chaîne de caractères | Ligne d'objet du modèle d'e-mail. |
| `body` | Facultatif | Chaîne de caractères | Corps du modèle d'e-mail pouvant inclure du HTML. |
| `plaintext_body` | Facultatif | Chaîne de caractères | Une version en texte brut du corps du modèle d'e-mail. |
| `preheader` | Facultatif | Chaîne de caractères | Accroche de l'e-mail utilisée pour générer des aperçus chez certains clients. |
| `tags` | Facultatif | Chaîne de caractères | Les [étiquettes]({{site.baseurl}}/user_guide/messaging/governance/tags) doivent déjà exister. |
| `should_inline_css` | Facultatif | Valeur booléenne | Active ou désactive la fonctionnalité `inline_css` par modèle. Si non renseigné, Braze utilisera le paramètre par défaut de l'AppGroup. `true` ou `false` est attendu. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de la requête" }

## Exemple de requête {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "email_template_id": "email_template_id",
  "template_name": "Weekly Newsletter",
  "subject": "This Week'\''s Styles",
  "body": "Check out this week'\''s digital lookbook to inspire your outfits. Take a look at https://www.braze.com/",
  "plaintext_body": "This is the updated text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "We want you to have the best looks this summer",
  "tags": ["Tag1", "Tag2"]
}'
```

## Résolution des problèmes {#troubleshooting}

Le tableau suivant répertorie les erreurs possibles et les étapes de résolution associées, le cas échéant.

| Erreur | Résolution |
| --- | --- |
| Le nom du modèle est obligatoire | Saisissez un nom de modèle. |
| Les étiquettes doivent être un tableau | Les étiquettes doivent être formatées sous forme de tableau de chaînes de caractères, par exemple `["marketing", "promotional", "transactional"]`. |
| Toutes les étiquettes doivent être des chaînes de caractères | Assurez-vous que vos étiquettes sont encadrées par des guillemets (`""`). |
| Certaines étiquettes sont introuvables | Pour ajouter une étiquette lors de la création d'un modèle d'e-mail, l'étiquette doit déjà exister dans Braze. |
| Valeur non valide pour `should_inline_css`. `true` ou `false` était attendu | Ce paramètre accepte uniquement les valeurs booléennes (true ou false). Assurez-vous que la valeur de `should_inline_css` n'est pas encadrée par des guillemets (`""`), ce qui entraînerait l'envoi de la valeur en tant que chaîne de caractères. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }

{% endapi %}