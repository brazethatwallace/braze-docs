---
nav_title: "E-Mail-Objekt"
article_title: E-Mail-Messaging-Objekt
page_order: 5
page_type: reference
channel: email
description: "Dieser Referenzartikel erläutert die verschiedenen Komponenten des E-Mail-Objekts von Braze."

---

# E-Mail-Objekt {#email-object}

> Mit dem Objekt `email` können Sie über unsere [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging) E-Mails ändern oder erstellen.

## E-Mail-Objekt

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

- [App-Bezeichner]({{site.baseurl}}/api/identifier_types)
  - Jede gültige `app_id` einer in Ihrem Workspace konfigurierten App funktioniert für alle Nutzer:innen in Ihrem Workspace, unabhängig davon, ob die jeweiligen Nutzer:innen die spezifische App in ihrem Profil haben oder nicht.
- Weitere Informationen und Best Practices zu Preheadern finden Sie unter [E-Mail-Styling]({{site.baseurl}}/user_guide/channels/email/best_practices/email_styling).

{% alert warning %}
Braze empfiehlt, keine Google-Drive-Links für die `url` Ihres Anhangs zu verwenden, da dies die Aufrufe unserer Server zum Abrufen der Datei blockieren und dazu führen kann, dass die E-Mail-Nachricht nicht gesendet wird.
{% endalert %}

Gültige Anhangstypen sind: `txt`, `csv`, `log`, `css`, `ics`, `jpg`, `jpe`, `jpeg`, `gif`, `png`, `bmp`, `psd`, `tif`, `tiff`, `svg`, `indd`, `ai`, `eps`, `doc`, `docx`, `rtf`, `odt`, `ott`, `pdf`, `pub`, `pages`, `mobi`, `epub`, `mp3`, `m4a`, `m4v`, `wma`, `ogg`, `flac`, `wav`, `aif`, `aifc`, `aiff`, `mp4`, `mov`, `avi`, `mkv`, `mpeg`, `mpg`, `wmv`, `xls`, `xlsx`, `ods`, `numbers`, `odp`, `ppt`, `pptx`, `pps`, `key`, `zip`, `vcf` und `pkpass`.

Eine `email_template_id` kann am Ende jedes mit dem HTML-Editor erstellten E-Mail-Templates abgerufen werden. Das folgende Beispiel zeigt, wie diese ID aussieht:

![API-Bezeichner-Bereich eines HTML-E-Mail-Templates.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:70%;"}

## Beispiel eines E-Mail-Objekts mit Anhang {#example-email-object-with-attachment}

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

## Authentifizierung für E-Mail-Dateianhänge {#authentication-for-email-file-attachments}

Verwenden Sie gespeicherte Zugangsdaten für Basic-Authentifizierung, wenn eine Anhangs-URL eine Anmeldung erfordert. Dies gilt für Anhänge im E-Mail-Objekt bei [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) und für das `attachments`-Array auf oberster Ebene bei [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).

1. Gehen Sie zu **Einstellungen** > **Connected Content**.
2. Wählen Sie **Zugangsdaten hinzufügen** aus.
3. Wählen Sie **Basic-Authentifizierung** aus.
4. Geben Sie einen Namen für die Zugangsdaten, einen Benutzernamen und ein Passwort ein.
5. Fügen Sie jedem Anhang, der eine Authentifizierung erfordert, eine `basic_auth_credential`-Eigenschaft hinzu und setzen Sie diese auf den Namen der Zugangsdaten. Das folgende Beispiel verwendet den Namen `company_basic_auth_credential_name` in einem E-Mail-Objekt:

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

## Abruf, Caching und Performance von Anhängen {#attachment-retrieval-caching-and-performance}

Wenn Braze eine Datei von einer Anhang-`url` abruft:

- **Caching:** Braze kann eine kürzlich abgerufene Datei bis zu ungefähr 24 Stunden wiederverwenden. Wenn jeder Versand sofort eine neue Version der Datei verwenden soll, nutzen Sie eine eindeutige URL pro Version (zum Beispiel einen Pfad oder Query-Parameter, der sich bei Dateiänderungen ändert).
- **Timeouts:** Hosts sollten schnell antworten. Wenn die Anhang-URL langsam ist oder hängt, kann der Nachrichtenversand fehlschlagen – streben Sie Antwortzeiten von etwa zwei Minuten an.
- **Sicherheit:** Fügen Sie keine personenbezogenen Daten (PII) oder Geheimnisse in Anhang-URLs ein (einschließlich Query-Strings), da URLs in Logs oder nachgelagerten Systemen erscheinen können.
- **Firewalls:** Wenn die URL nur aus bestimmten Netzwerken erreichbar ist, erlauben Sie den Datenverkehr von Braze gemäß der [Connected-Content-IP-Allowlisting]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting). Verwenden Sie [Basic-Authentication-Zugangsdaten](#authentication-for-email-file-attachments), wenn die Datei eine Anmeldung erfordert.