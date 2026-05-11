---
nav_title: Jasper
article_title: Jasper
description: "Cet article de référence présente l'intégration entre Braze et Jasper."
alias: /partners/jasper/
page_type: partner
search_tag: Partner
---

# Jasper

> [Jasper](https://www.jasper.ai/) est une plateforme de contenu alimentée par l'intelligence artificielle qui donne à votre marque les moyens de créer, de gérer et de mettre à l'échelle un contenu de haute qualité et conforme à la marque sur différents canaux, notamment les blogs, les publicités et les réseaux sociaux.

_Cette intégration est maintenue par Jasper._

## Aperçu {#overview}

L'intégration de Jasper et Braze vous permet de rationaliser la création de contenu et l'exécution des campagnes. Avec Jasper, vos équipes marketing peuvent générer en quelques minutes des textes de haute qualité et conformes à la marque. Braze facilite ensuite la distribution de ces messages à la bonne audience au moment optimal. Cette intégration favorise des flux de travail fluides, réduit les efforts manuels et permet d'obtenir de meilleurs résultats en matière d'engagement.

Les avantages de cette intégration sont les suivants :

- **Exécution rapide des campagnes :** Lancez des campagnes en quelques minutes, pas en quelques semaines.
- **Voix de marque cohérente :** Utilisez les modèles Jasper pour vous assurer que le texte généré respecte strictement les directives de marque.
- **Génération de contenu ciblé :** Créez des messages hautement personnalisés avec des segments d'audience, des guides de style et des éléments de connaissance exclusifs.
- **Personnalisation dynamique :** Utilisez des marques substitutives Liquid, comme {% raw %}`{{${first_name}}}`{% endraw %}, pour une personnalisation évolutive au sein de Braze.
- **Réduction des erreurs :** Les flux de travail automatisés minimisent les erreurs de copier-coller et réduisent les étapes manuelles.

## Conditions préalables {#prerequisites}

| Condition   | Description  |
| ------------------- | ---------------- |
| Compte Jasper      | Vous devez disposer d'un compte Jasper pour utiliser ce partenariat. |
| Clé API REST de Braze  | Une clé API REST de Braze avec les autorisations suivantes. <br>  <br>`templates.email.create` <br> `templates.email.update` <br>`content_blocks.create` <br>`content_blocks.update` <br><br>Cette clé peut être générée dans le tableau de bord de Braze en naviguant vers **Paramètres > Clés API**.  |
| Endpoint REST de Braze | L'URL de votre endpoint REST. Votre endpoint spécifique dépend de l'URL de Braze pour votre instance. Consultez la documentation [Braze API Basics : Endpoints]({{site.baseurl}}/api/basics/#endpoints) pour plus de détails. |
{: .reset-td-br-1 .rest-td-br-2 role="presentation" }

## Méthodes d'intégration {#integration-methods}

Il existe deux méthodes pour générer du contenu dans Jasper et mettre à jour les modèles de Braze :

1. Utiliser directement l'API Jasper
2. Utiliser Jasper Studio pour créer une application personnalisée prête pour Braze

{% tabs %}
{% tab API Jasper %}

## Méthode : utiliser directement l'API Jasper {#method-use-jasper-api-directly}

Cette méthode est idéale pour créer et mettre à jour par programme des modèles HTML d'e-mail dans Braze, en évitant la configuration manuelle dans Jasper et Braze.

### Étape 1 : Configurer Jasper {#step-1-set-up-jasper}

1. Suivez les instructions de la section [Mise en route](https://developers.jasper.ai/docs/getting-started-1) pour générer votre clé API Jasper.
2. Utilisez le modèle préconstruit de Jasper, optimisé pour générer des modèles d'e-mail HTML de Braze, dont l'ID de modèle est `skl_BC53D8AC5B4B47E8BE557EBB706E9B47`.
3. Collectez les valeurs des champs suivants, nécessaires pour effectuer une requête de génération de contenu pour un modèle d'e-mail HTML de Braze.

| Champ | Description |
| --- | --- |
| `emailObjective` | Définissez clairement l'objectif de l'e-mail. |
| `ctaLink` | L'URL de votre appel à l'action. |
| `unsubscribeLink` | Requis pour les e-mails marketing. |
| `brandColor` | La couleur principale de votre marque au format hexadécimal (par exemple, `#4dfa8a`). |
{: .reset-td-br-1 .rest-td-br-2 role="presentation" }

**Champs facultatifs**

| Champ | Description |
| --- | --- |
| `toneId` | Voix de la marque |
| `audienceId` | Segmentation d'audience |
| `styleId` | Guide de style |
| `knowledgeIds` | Contexte de contenu enrichi. Vous pouvez ajouter jusqu'à trois ID. |
{: .reset-td-br-1 .rest-td-br-2 role="presentation" }

{: start="4"}
4. Générez votre résultat en exécutant le modèle via l'API Jasper. Cela produira un payload JSON contenant les éléments `subject`, `preheader` et `body` (contenu HTML).

{% subtabs %}
{% subtab Exemple de requête %}

### Exemple de requête {#sample-request}

{% raw %}
```bash
curl --location 'https://api.jasper.ai/v1/templates/skl_BC53D8AC5B4B47E8BE557EBB706E9B47/run?toneId=ton_811696974b3c4db4b3ac0041685c3b7c&knowledgeIds=kno_0a62fc17529e4fe69a71f30b6f0e88a7&audienceId=aud_0199117a690a7cc98481f8700916e2a6' \
--header 'Content-Type: application/json' \
--header 'x-api-key: ••••••' \
--data '{
  "inputs": {
    "emailObjective": "Announce a webinar and highlight Jasper + Braze integration benefits. Use {{${firstname}}} in the subject and body. Body length ~400 words. Include CTA buttons for registration and footer with unsubscribe link. Apply brand color to buttons and links.",
    "ctaLink": "https://yourbrand.com/register",
    "unsubscribeLink": "{{${unsubscribe_link}}}",
    "brandColor":"#4dfa8a"
  },
  "options": {
    "outputCount": 1,
    "outputLanguage": "English",
    "inputLanguage": "English",
    "languageFormality": "less"
  }
}'
```
{% endraw %}

{% endsubtab %}
{% subtab Exemple de sortie %}

### Exemple de sortie {#sample-output}
```
{
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}
```
{% endsubtab %}
{% endsubtabs %}

### Étape 2 : Configurer Braze {#step-2-set-up-braze}

À l'aide des éléments `subject`, `preheader` et `body` générés par Jasper à l'étape 1, effectuez une requête POST auprès de l'API REST de Braze pour [créer un nouveau modèle d'e-mail]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/). Assurez-vous que votre clé API REST de Braze dispose des autorisations `templates.email.create` et `templates.email.update`.

### Exemple de requête API de Braze pour créer un modèle d'e-mail {#sample-braze-api-request-to-create-an-email-template}

```bash
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endtab %}
{% tab Jasper Studio %}

## Méthode : créer une application personnalisée prête pour Braze avec Jasper Studio {#method-build-a-braze-ready-custom-app-with-jasper-studio}

Jasper Studio est une plateforme no-code au sein de Jasper qui vous permet de créer des applications d'intelligence artificielle sur mesure sans nécessiter d'assistance informatique. Vous pouvez concevoir une application personnalisée qui génère des structures JSON spécifiquement formatées pour l'API Braze, ou générer du contenu qui peut être ajouté manuellement à vos messages Braze.

1. Sur l'écran d'accueil de Jasper, sélectionnez **Create an App**.
2. Spécifiez l'application que vous souhaitez créer, telle que **Braze HTML Email Template** ou **Content Block Template**.
3. Modifiez les champs d'invite de saisie générés par Jasper. Pour un modèle d'e-mail HTML, vous pouvez inclure des formulaires de saisie pour la ligne d'objet, l'accroche, le corps HTML, les étiquettes, la bascule CSS en ligne et le nom du modèle.
4. Intégrez des éléments de connaissance avec des conseils sur les bonnes pratiques Liquid pour une personnalisation cohérente et un contenu dynamique.
5. Affinez les instructions fournies au grand modèle de langage (LLM) pour la génération de contenu.
6. Fournissez un exemple de la sortie souhaitée, qui peut inclure une sortie JSON automatisée formatée pour les payloads de Braze.
7. Générez et exportez les éléments suivants :
- **Copier/coller direct :** Le contenu peut être copié et collé directement dans la plateforme Braze.
- **Sortie JSON :** Générez une sortie JSON. Ce payload peut ensuite être utilisé pour appeler directement l'endpoint de Braze via `curl` ou un middleware, ou être intégré dans votre flux de travail des opérations d'e-mail.

![Application personnalisée Jasper pour Braze.]({% image_buster /assets/img/jasper/jasper_custom_app.png %})

{% subtabs %}
{% subtab Exemple de sortie JSON (application personnalisée) %}

## Exemple de sortie JSON (application personnalisée) {#sample-json-output-custom-app}

{% raw %}
```json
{
  "template_name": "email_webinar_2025",
  "subject": "Join Our Webinar, {{${firstname}}}!",
  "preheader": "Unlock the potential of seamless integration.",
  "body": "<html> ... </html>",
  "tags": ["jasperapi"],
  "should_inline_css": true
}
```
{% endraw %}

{% endsubtab %}
{% subtab Exemple de requête API de Braze (avec la sortie de l'application personnalisée) %}

## Exemple de requête API de Braze (avec la sortie de l'application personnalisée) {#sample-braze-api-request-using-custom-app-output}

{% raw %}
```bash
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endraw %}

{% endsubtab %}
{% endsubtabs %}

Par ailleurs, si vous êtes marketeur, vous pouvez créer votre application personnalisée en l'alignant sur les directives de marque afin de générer du contenu sans HTML ni copier-coller, et utiliser les modèles de Braze pour la mise en forme.

{% endtab %}
{% endtabs %}

{% alert note %}
Pour obtenir une assistance supplémentaire, consultez la [documentation de l'API Jasper](https://developers.jasper.ai/reference/gettemplate-1) et le [centre d'aide de Jasper Studio](https://help.jasper.ai/hc/en-us/articles/36783295610395-Jasper-Studio).
{% endalert %}