---
nav_title: Dynamische Code-Generierung
article_title: Dynamische Code-Generierung mit Punchh
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie die dynamische Code-Generierung von Punchh in Braze verwenden."
page_type: partner
search_tag: Partner
---

# Dynamische Code-Generierung mit Punchh {#dynamic-code-generation-with-punchh}

> Ein Gutscheincode ist ein eindeutiger Code, der von einer einzelnen Nutzer:in verwendet werden kann (entweder einmalig oder mehrfach). Das Punchh-Framework generiert Gutscheincodes, die in einer mobilen App oder am Point-of-Sale (POS)-System verarbeitet werden können.

_Diese Integration wird von Punchh gepflegt._

## Über die Integration {#about-the-integration}

Mit dem Punchh-Coupon-Framework und Braze können Sie die folgenden Szenarien realisieren:

- Generieren Sie einen Gutscheincode, wenn der Gast in einer E-Mail auf einen Link zur Gutscheingenerierung klickt: Der Gutscheincode wird dynamisch generiert und auf einer Webseite angezeigt.
- Generieren Sie einen Gutscheincode, wenn der Gast eine E-Mail öffnet: Der Gutscheincode wird dynamisch generiert und als Bild in der E-Mail angezeigt.

## Integration der dynamischen Gutscheincode-Generierung {#integrating-dynamic-coupon-code-generation}

### 1. Schritt: Gutscheinkampagne erstellen {#step-1-create-a-coupon-campaign}

1. Erstellen Sie mit einer Punchh-Gutscheinkampagne eine dynamische Generierungs-Gutscheinkampagne, wie in der folgenden Abbildung gezeigt.
2. Das Punchh-Coupon-Framework generiert die folgenden Parameter, um die dynamische Gutscheingenerierung zu ermöglichen:
    - Token / Textbaustein zur dynamischen Gutscheingenerierung: Dies ist ein vom System generiertes Sicherheits-Token / Textbaustein für die Verschlüsselung.
    - URL zur dynamischen Gutscheingenerierung: Diese URL wird als Link oder Bild in die E-Mail eingebettet, je nach Bedarf des Unternehmens.

![Das Formular für die Erstellung einer Gutscheinkampagne in Punchh.]({% image_buster /assets/img/punchh/punchh8.png %}){: style="max-width:60%;"}

### 2. Schritt: Signatur generieren und URL konstruieren {#step-2-generate-signature-and-construct-url}

Die Bibliothek JWT.IO dekodiert, überprüft und generiert JSON-Web-Tokens, eine offene, dem Industriestandard RFC 7519 entsprechende Methode zur sicheren Darstellung von Claims zwischen zwei Parteien.

Die folgenden `ClaimType`-Namen können verwendet werden, um die Eindeutigkeit von Gästen und Gutscheinen zu gewährleisten:

- `campaign_id`: steht für die vom System generierte Punchh-Campaign-ID.
- `email`: steht für die E-Mail-Adresse der Nutzer:in.
- `first_name`: erfasst den Vornamen der Nutzer:in.
- `last_name`: erfasst den Nachnamen der Nutzer:in.

Um die dynamische Gutscheincode-API von Punchh zu nutzen, muss ein JWT-Token / Textbaustein erstellt werden. Fügen Sie die folgende Liquid-Vorlage in Ihrem Braze-Dashboard in den Nachrichtentext des Kanals ein, den Sie verwenden möchten:

{% raw %}
```liquid
{% assign header = '{"alg":"HS256","typ":"JWT"}' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% capture payload_raw %}

{
  "campaign_id": "CAMPAIGN_ID",
  "email": "{{${email_address}}}",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}"
}

{% endcapture %}

{% assign payload = payload_raw | replace: ' ', '' | replace: '\n', '' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign unsigned_token = header | append: "." | append: payload %}

{% assign secret = "DYNAMIC_COUPON_GENERATION_TOKEN" %}

{% assign signature_raw = unsigned_token | hmac_sha256_base64: secret %}

{% assign signature = signature_raw | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign jwt = unsigned_token | append: "." | append: signature %}

```
{% endraw %}


Ersetzen Sie Folgendes:

| Platzhalter | Beschreibung |
|--------------------|------------------------------------------------------|
| `DYNAMIC_COUPON_GENERATION_TOKEN` | Ihr Token / Textbaustein zur dynamischen Gutscheingenerierung. |
| `CAMPAIGN_ID` | Ihre Campaign-ID. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2. Schritt: Signatur generieren und URL konstruieren" }

### 3. Schritt: Gutscheincode an den Nachrichtentext anhängen {#step-3-append-coupon-code-to-message-body}

#### Verlinkung zur Punchh-Webseite {#linking-to-punchh-web-page}

Um einen Link zu einer von Punchh gehosteten Webseite zu erstellen, fügen Sie `{% raw %}{{jwt}}{% endraw %}` an die dynamische Generierungs-URL an, [die Sie zuvor erstellt haben](#step-1-create-a-coupon-campaign-in-punchh). Ihr Link sollte ähnlich wie der folgende aussehen:

{% raw %}
```
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX?sign={{jwt}}
```
{% endraw %}

Wenn Nutzer:innen auf die Gutschein-URL klicken, werden sie auf eine von Punchh gehostete Webseite weitergeleitet, auf der der generierte Gutschein angezeigt wird.

![Beispiel für eine Bestätigungsnachricht, nachdem Nutzer:innen erfolgreich einen Gutscheincode generiert haben.]({% image_buster /assets/img/punchh/punchh7.png %})

#### Code über JSON als reinen Text extrahieren {#extracting-code-via-json-as-plain-text}

Um eine JSON-Antwort zurückzugeben, fügen Sie `{% raw %}{{jwt}}{% endraw %}` an die dynamische Generierungs-URL an, [die Sie zuvor erstellt haben](#step-1-create-a-coupon-campaign-in-punchh), und fügen Sie dann `.json` nach dem Token / Textbaustein in den URL-String ein. Ihr Link sollte ähnlich wie der folgende aussehen:

{% raw %}
```liquid
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}}
```
{% endraw %}

Sie könnten dann [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/) nutzen, um den Code als reinen Text in jeden Nachrichtentext einzufügen. Zum Beispiel:

{% raw %}
```liquid
{% connected_content https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}} :save punchh_coupon %}
{{punchh_coupon.coupon}}
````
{% endraw %}

#### Gutscheincode als Bild in E-Mail-Inhalte einbinden {#linking-an-image-inside-email-content}

So verknüpfen Sie den Gutscheincode mit einem Bild:

1. Fügen Sie `{% raw %}{{jwt}}{% endraw %}` an die dynamische Generierungs-URL an, [die Sie zuvor erstellt haben](#step-1-create-a-coupon-campaign-in-punchh).
2. Fügen Sie `.png` nach dem Token / Textbaustein in den URL-String ein.
3. Betten Sie Ihren Link in einen HTML-{% raw %}`<img>`{% endraw %}-Tag ein.

{% tabs local %}
{% tab Beispiel-Eingabe %}
{% raw %}
```liquid
<img src="https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.png?sign={{jwt}}">
````
{% endraw %}
{% endtab %}

{% tab Beispiel-Ausgabe %}
![Gerenderte Ausgabe des Gutscheincode-Bild-Tags.]({% image_buster /assets/img/punchh/punchh9.png %})
{% endtab %}
{% endtabs %}

## Fehlermeldungen {#error-messages}

| Fehlercode | Fehlermeldung | Beschreibung |
| --- | --- | --- |
| `coupon_code_expired` | This promo code has expired | Der Code wird nach dem konfigurierten Verfallsdatum verwendet. |
| `coupon_code_success` | Congratulations, Promo Code Applied Successfully. | Der Code wurde erfolgreich verwendet. |
| `coupon_code_error` | Please enter a valid promo code | Der verwendete Code ist ungültig. |
| `coupon_code_type_error` | Incorrect coupon type. This coupon can only be redeemed at `%{coupon_type}`. | Wenn ein Code, der am POS verwendet werden soll, in der mobilen App verwendet wird, tritt dieser Fehler auf. |
| `usage_exceeded` | The usage for this coupon code's campaign is full. Please try next time. | Die Nutzung des Codes übersteigt die Anzahl der Nutzer:innen, die ihn verwenden dürfen. Wenn die Dashboard-Konfiguration beispielsweise die Verwendung eines Codes durch 3.000 Nutzer:innen zulässt und die Anzahl der Nutzer:innen 3.000 übersteigt, wird dieser Fehler angezeigt. |
| `usage_exceeded_by_guest` | This promo code has already been processed. | Die Nutzung des Codes durch eine Nutzer:in übersteigt die Anzahl der möglichen Nutzungen. Die Dashboard-Konfiguration erlaubt es beispielsweise, dass ein einzelner Code dreimal von einer Nutzer:in verwendet werden kann. Wird er häufiger verwendet, tritt dieser Fehler auf. |
| `already_used_by_other_guest` | This promo code has already been used by some other guest. | Eine andere Nutzer:in hat den Code bereits verwendet. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehlermeldungen" }