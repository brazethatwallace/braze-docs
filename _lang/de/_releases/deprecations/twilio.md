---
nav_title: Twilio-Partnerschaft
alias: /partners/twilio/

description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Twilio."
page_type: update
channel:
  - SMS
  - Webhook
---

# Twilio

{% alert warning %}
Beachten Sie, dass der Support für die Twilio-Webhook-Integration am 31. Januar 2020 eingestellt wird. Wenn Sie mit Braze weiterhin auf SMS-Dienste zugreifen möchten, lesen Sie unsere [SMS-Dokumentation]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/).
{% endalert %}

In diesem Beispiel konfigurieren wir den Braze-Webhook-Kanal, um SMS und MMS über die [Twilio-API zum Versenden von Nachrichten](https://www.twilio.com/docs/api/rest/sending-messages) an Ihre Nutzer:innen zu senden. Auf dem Dashboard steht Ihnen ein Twilio-Webhook-Template zur Verfügung, das Ihnen die Arbeit erleichtert.

## HTTP-URL

Die Webhook-URL wird von Twilio in Ihrem Dashboard bereitgestellt. Diese URL ist eindeutig für Ihr Twilio-Konto, da sie Ihre Twilio-Konto-ID (`TWILIO_ACCOUNT_SID`) enthält.

In unserem Twilio-Beispiel lautet die Webhook-URL `https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json`. Sie finden diese URL im Abschnitt *Getting Started* der Twilio-Konsole.

![Twilio-Konsole]({% image_buster /assets/img_archive/Twilio_Console.png %})

## Anfragetext {#request-body}

Die Twilio-API erwartet, dass der Anfragetext URL-kodiert ist, daher müssen wir zunächst den Anfragetyp im Braze-Webhook-Composer auf `Raw Text` ändern. Die erforderlichen Parameter für den Anfragetext sind *To*, *From* und *Body*.

Der folgende Screenshot zeigt ein Beispiel dafür, wie Ihre Anfrage aussehen könnte, wenn Sie eine SMS an die Telefonnummer jeder Nutzerin bzw. jedes Nutzers mit dem Text „Hello from Braze!“ senden.

- Sie benötigen gültige Telefonnummern in jedem Kundenprofil Ihrer Zielgruppe.
- Um das Anfrageformat von Twilio zu erfüllen, verwenden Sie den Liquid-Filter `url_param_escape` für den Inhalt Ihrer Nachrichten. Dieser Filter kodiert einen String so, dass alle Zeichen in einer HTML-Anfrage zulässig sind. Zum Beispiel ist das Pluszeichen (`+`) in der Telefonnummer `+12125551212` in URL-kodierten Daten nicht zulässig und wird in `%2B12125551212` umgewandelt.

![Webhook-Anfragetext]({% image_buster /assets/img_archive/Webhook_Body.png %})

## Anfrage-Header und Methode {#request-headers-and-method}

Twilio benötigt zwei Anfrage-Header: den Content-Typ der Anfrage und einen [HTTP-Basic-Authentication-Header](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side). Fügen Sie diese zu Ihrem Webhook hinzu, indem Sie auf das Zahnradsymbol neben dem Webhook-Composer klicken und dann zweimal auf *Add New Pair* klicken.

Header-Name | Header-Wert
--- | ---
Content-Type | `application/x-www-form-urlencoded`
Authorization | `{% raw %}Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}`

Ersetzen Sie `TWILIO_ACCOUNT_SID` und `TWILIO_AUTH_TOKEN` durch die Werte aus Ihrem Twilio-Dashboard. Der API-Endpunkt von Twilio erwartet eine HTTP-POST-Anfrage. Wählen Sie daher diese Option in der Dropdown-Liste für die *HTTP-Methode*.

![Webhook-Methode]({% image_buster /assets/img_archive/Webhook_Method.png %})

## Vorschau Ihrer Anfrage {#preview-your-request}

Verwenden Sie den Webhook-Composer, um eine Vorschau der Anfrage für eine:n zufällige:n Nutzer:in oder für eine:n Nutzer:in mit bestimmten Zugangsdaten zu erstellen und sicherzustellen, dass die Anfrage korrekt dargestellt wird.

![Webhook-Vorschau]({% image_buster /assets/img_archive/Webhook_Preview.png %})