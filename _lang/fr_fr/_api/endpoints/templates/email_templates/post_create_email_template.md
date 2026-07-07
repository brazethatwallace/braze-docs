---
nav_title: "POST : Créer un modèle d'e-mail"
article_title: "POST : Créer des modèles d'e-mail"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Créer des modèles d'e-mail."
---
{% api %}
# Créer un modèle d'e-mail {#create-email-template}
{% apimethod post %}
/templates/email/create
{% endapimethod %}

> Utilisez cet endpoint pour créer des modèles d'e-mail sur le tableau de bord de Braze.

Ces modèles seront disponibles sur la page **Modèles et médias**. La réponse de cet endpoint comprend un champ `email_template_id` qui peut être utilisé pour mettre à jour le modèle lors des prochains appels d'API.

{% alert tip %}
Vous pouvez également appeler cet endpoint via le [serveur MCP de Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server) en utilisant la fonction [`create_email_template`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#templates). Cela permet à des outils d'intelligence artificielle comme Claude et Cursor de créer des modèles d'e-mail à l'aide de requêtes en langage naturel.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key) avec l'autorisation `templates.email.create`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "template_name": (required, string) The name of your email template,
   "subject": (required, string) The email template subject line,
   "body": (required, string) The email template body that may include HTML,
   "plaintext_body": (optional, string) A plaintext version of the email template body,
   "preheader": (optional, string) The email preheader used to generate previews in some clients,
   "tags": (optional, Array of Strings) Tags must already exist,
   "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature is used on this template.
 }
```

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `template_name` | Requis | Chaîne de caractères | Nom de votre modèle d'e-mail. |
| `subject` | Requis | Chaîne de caractères | Ligne d'objet du modèle d'e-mail. |
| `body` | Requis | Chaîne de caractères | Corps du modèle d'e-mail pouvant inclure du HTML. Jusqu'à 400&nbsp;Ko. |
| `plaintext_body` | Facultatif | Chaîne de caractères | Une version en texte brut du corps du modèle d'e-mail. |
| `preheader` | Facultatif | Chaîne de caractères | Accroche de l'e-mail utilisée pour générer des aperçus chez certains clients. |
| `tags` | Facultatif | Chaîne de caractères | Les [étiquettes]({{site.baseurl}}/user_guide/messaging/governance/tags) doivent déjà exister. |
| `should_inline_css` | Facultatif | Valeur booléenne | Active ou désactive la fonctionnalité `inline_css` par modèle. S'il n'est pas fourni, Braze utilisera le paramètre par défaut pour le groupe d'applications. `true` ou `false` est attendu. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool.",
  "tags": ["Tag1", "Tag2"]
}'
```

## Exemple de réponse {#example-response}

```json
{
  "email_template_id": "232b6d29-7e41-4106-a0ab-1c4fe915d701",
  "message": "success"
}
```

## Résolution des problèmes {#troubleshooting}

Le tableau suivant répertorie les erreurs possibles et les étapes de résolution associées, le cas échéant.

| Erreur | Résolution des problèmes |
| --- | --- |
| Le nom du modèle est obligatoire | Saisissez un nom de modèle. |
| Les étiquettes doivent être un tableau | Les étiquettes doivent être formatées sous forme de tableau de chaînes de caractères, par exemple `["marketing", "promotional", "transactional"]`. |
| Toutes les étiquettes doivent être des chaînes de caractères | Assurez-vous que vos étiquettes sont encadrées par des guillemets (`""`). |
| Certaines étiquettes sont introuvables | Pour ajouter une étiquette lors de la création d'un modèle d'e-mail, l'étiquette doit déjà exister dans Braze. |
| L'e-mail doit comporter des noms de Content Blocks valides | L'e-mail peut contenir des Content Blocks qui n'existent pas dans cet environnement. |
| Valeur non valide pour `should_inline_css`. `true` ou `false` était attendu | Ce paramètre accepte uniquement les valeurs booléennes (true ou false). Assurez-vous que la valeur de `should_inline_css` n'est pas encadrée par des guillemets (`""`), sinon elle est envoyée comme chaîne de caractères. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }

{% endapi %}