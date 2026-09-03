---
nav_title: "Objet E-mail"
article_title: Objet Messagerie e-mail
page_order: 5
page_type: reference
channel: email
description: "Cet article de référence explique les différents composants de l'objet e-mail de Braze."

---

# Objet e-mail {#email-object}

> L'objet `email` vous permet de modifier ou de créer des e-mails par l'intermédiaire de nos [endpoints d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging).

## Objet e-mail

```json
{
  "app_id": (required, string), see App Identifier,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <user@example.com>"),
  "reply_to": (optional, valid email address in the format "user@example.com" - defaults to your workspace's default reply to if not set) - use "NO_REPLY_TO" to set reply-to address to null,
  "bcc": (optional, one of the BCC addresses defined in your workspace's email settings) if provided and the BCC feature is enabled for your account, this address gets added to your outbound message as a BCC address,
  "body": (required unless email_template_id is given, valid HTML),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "preheader": (optional*, string) recommended length 50-100 characters,
  "email_template_id": (optional, string) if provided, Braze uses the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case Braze overrides the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid Key-Value Hash) extra hash - for SendGrid users, this is passed to SendGrid as Unique Arguments,
  "headers": (optional, valid Key-Value Hash) hash of custom extensions headers (available for SparkPost, SendGrid, or Amazon SES),
  "should_inline_css": (optional, boolean) whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name", "url", and optionally "basic_auth_credential",
    "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
    "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
    "basic_auth_credential": (optional, string) the name of the stored basic authentication credential to use when the attachment URL requires a login,
}
```

- [Identifiant d'application]({{site.baseurl}}/api/identifier_types)
  - Tout `app_id` valide provenant d'une application configurée dans votre espace de travail fonctionne pour tous les utilisateurs de votre espace de travail, que l'utilisateur ait ou non l'application spécifique dans son profil.
- Pour plus d'informations et les bonnes pratiques concernant les accroches, consultez la section [Mise en forme des e-mails]({{site.baseurl}}/user_guide/channels/email/best_practices/email_styling).

{% alert warning %}
Braze vous recommande d'éviter d'utiliser des liens Google Drive pour l'`url` de vos pièces jointes, car cela peut bloquer les appels de nos serveurs pour récupérer le fichier et empêcher l'envoi de l'e-mail.
{% endalert %}

Les types de pièces jointes valides incluent : `txt`, `csv`, `log`, `css`, `ics`, `jpg`, `jpe`, `jpeg`, `gif`, `png`, `bmp`, `psd`, `tif`, `tiff`, `svg`, `indd`, `ai`, `eps`, `doc`, `docx`, `rtf`, `odt`, `ott`, `pdf`, `pub`, `pages`, `mobi`, `epub`, `mp3`, `m4a`, `m4v`, `wma`, `ogg`, `flac`, `wav`, `aif`, `aifc`, `aiff`, `mp4`, `mov`, `avi`, `mkv`, `mpeg`, `mpg`, `wmv`, `xls`, `xlsx`, `ods`, `numbers`, `odp`, `ppt`, `pptx`, `pps`, `key`, `zip`, `vcf` et `pkpass`.

Un `email_template_id` peut être récupéré en bas de n'importe quel modèle d'e-mail créé avec l'éditeur HTML. Voici un exemple de ce à quoi ressemble cet ID :

![Section de l'identifiant API d'un modèle d'e-mail HTML.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:70%;"}

## Exemple d'objet e-mail avec pièce jointe {#example-email-object-with-attachment}

```json
{
  "external_user_ids": ["YOUR_EXTERNAL_USER_ID"],
  "messages":{
     "email":{
        "app_id":"YOUR_APP_ID",
        "attachments":[{
            "file_name":"YourFileName",
            "url":"https://exampleurl.com/YourFileName.pdf"
         }]
     }
  }
}
```

## Authentification pour les pièces jointes d'e-mail {#authentication-for-email-file-attachments}

Utilisez un identifiant d'authentification basique enregistré lorsqu'une URL de pièce jointe nécessite une connexion. Cela s'applique aux pièces jointes de l'objet e-mail sur [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) et au tableau `attachments` de niveau supérieur sur [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).

1. Allez dans **Paramètres** > **Contenu connecté**.
2. Sélectionnez **Ajouter un identifiant**.
3. Sélectionnez **Authentification basique**.
4. Saisissez un nom d'identifiant, un nom d'utilisateur et un mot de passe.
5. Incluez une propriété `basic_auth_credential` sur chaque pièce jointe nécessitant une authentification et définissez-la sur le nom de cet identifiant. L'exemple suivant utilise le nom d'identifiant `company_basic_auth_credential_name` dans un objet e-mail :

```json
{
  "external_user_ids": ["recipient_user_id"],
  "messages":{
    "email":{
      "app_id": "153e8a29-fd6d-4f77-ade7-1a4ca08d457a",
      "subject": "Basic auth attachment test",
      "from": "mail <mail@example.com>",
      "body": "my attachment test",
      "attachments":[
        { "file_name":"checkout_receipt.pdf",
        "url":"https://fileserver.company.com/user123-checkout_receipt.pdf",
        "basic_auth_credential": "company_basic_auth_credential_name" }
      ]
    }
  }
}
```

## Récupération, mise en cache et performance des pièces jointes {#attachment-retrieval-caching-and-performance}

Lorsque Braze récupère un fichier à partir d'une `url` de pièce jointe :

- **Mise en cache :** Braze peut réutiliser un fichier récemment récupéré pendant environ 24 heures. Si chaque envoi doit récupérer immédiatement une nouvelle version du fichier, utilisez une URL distincte par version (par exemple, un chemin ou un paramètre de requête qui change lorsque le fichier change).
- **Délais d'attente :** Les serveurs hôtes doivent répondre rapidement. Si l'URL de la pièce jointe est lente ou ne répond pas, l'envoi du message peut échouer — visez des réponses en deux minutes environ.
- **Sécurité :** Ne placez pas de données d'identification personnelle (PII) ni de secrets dans les URL des pièces jointes (y compris les chaînes de requête), car les URL peuvent apparaître dans les journaux ou les systèmes en aval.
- **Pare-feux :** Si l'URL n'est accessible que depuis des réseaux spécifiques, autorisez le trafic en provenance de Braze conformément à la [liste d'autorisation des IP pour le contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting). Utilisez des [identifiants d'authentification basique](#authentication-for-email-file-attachments) lorsque le fichier nécessite une connexion.