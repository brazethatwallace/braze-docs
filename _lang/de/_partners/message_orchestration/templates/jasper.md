---
nav_title: Jasper
article_title: Jasper
description: "Dieser Referenzartikel beschreibt die Integration zwischen Braze und Jasper."
alias: /partners/jasper/
page_type: partner
search_tag: Partner
---

# Jasper

> [Jasper](https://www.jasper.ai/) ist eine KI-gestützte Content-Plattform, die Ihre Marke in die Lage versetzt, qualitativ hochwertige, markengerechte Inhalte über verschiedene Kanäle – einschließlich Blogs, Anzeigen und Social Media – zu erstellen, zu verwalten und zu skalieren.

_Diese Integration wird von Jasper gepflegt._

## Übersicht {#overview}

Die Integration von Jasper und Braze ermöglicht es Ihnen, die Erstellung von Inhalten und die Durchführung von Kampagnen zu optimieren. Mit Jasper können Ihre Marketing-Teams in wenigen Minuten hochwertige, markengerechte Texte erstellen. Braze erleichtert anschließend die Zustellung dieser Nachrichten an die richtige Zielgruppe zum optimalen Zeitpunkt. Diese Integration fördert nahtlose Arbeitsabläufe, reduziert den manuellen Aufwand und sorgt für bessere Engagement-Ergebnisse.

Die Vorteile dieser Integration sind unter anderem:

- **Schnelle Kampagnendurchführung:** Starten Sie Kampagnen in Minuten, nicht in Wochen.
- **Konsistente Markensprache:** Verwenden Sie Jasper-Templates, um sicherzustellen, dass die erstellten Texte den Markenrichtlinien genau entsprechen.
- **Gezielte Generierung von Inhalten:** Erstellen Sie hochgradig angepasstes Messaging mit Zielgruppen-Segmenten, Style Guides und proprietären Wissensartikeln.
- **Dynamische Personalisierung:** Verwenden Sie Liquid-Platzhalter wie {% raw %}`{{${first_name}}}`{% endraw %} für eine skalierbare Personalisierung innerhalb von Braze.
- **Fehlerreduzierung:** Automatisierte Arbeitsabläufe minimieren Copy-Paste-Fehler und reduzieren manuelle Schritte.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Jasper-Konto | Sie benötigen ein Jasper-Konto, um diese Partnerschaft nutzen zu können. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit den folgenden Berechtigungen. <br> <br>`templates.email.create` <br> `templates.email.update` <br>`content_blocks.create` <br>`content_blocks.update` <br><br>Dieser Schlüssel kann im Braze-Dashboard generiert werden, indem Sie zu **Einstellungen > API-Schlüssel** navigieren. |
| Braze-REST-Endpunkt | Ihre URL für den REST-Endpunkt. Ihr spezifischer Endpunkt hängt von der Braze-URL für Ihre Instanz ab. Weitere Einzelheiten finden Sie in der Dokumentation zu [Braze API-Grundlagen: Endpunkte]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .rest-td-br-2 aria-label="Voraussetzungen" }

## Integrationsmethoden {#integration-methods}

Es gibt zwei Methoden zur Erstellung von Inhalten in Jasper und zum Aktualisieren von Braze-Templates:

1. Verwenden Sie die Jasper API direkt
2. Verwenden Sie Jasper Studio, um eine für Braze geeignete angepasste App zu erstellen

{% tabs %}
{% tab Jasper API %}

## Methode: Jasper API direkt verwenden {#method-use-jasper-api-directly}

Diese Methode ist ideal für die programmgesteuerte Erstellung und Aktualisierung von E-Mail-HTML-Templates in Braze und umgeht die manuelle Einrichtung in Jasper und Braze.

### 1. Schritt: Jasper einrichten {#step-1-set-up-jasper}

1. Folgen Sie den Anweisungen unter [Erste Schritte](https://developers.jasper.ai/docs/getting-started-1), um Ihren Jasper-API-Schlüssel zu generieren.
2. Verwenden Sie das vorgefertigte Template von Jasper, das für die Erstellung von Braze-HTML-E-Mail-Templates optimiert ist und die Template-ID `skl_BC53D8AC5B4B47E8BE557EBB706E9B47` hat.
3. Erfassen Sie die Werte für die folgenden Felder, die für eine Anfrage zur Generierung von Inhalten für ein Braze-HTML-E-Mail-Template erforderlich sind.

| Feld | Beschreibung |
| --- | --- |
| `emailObjective` | Definieren Sie das Ziel der E-Mail klar und deutlich. |
| `ctaLink` | Die URL für Ihren Call-to-Action. |
| `unsubscribeLink` | Erforderlich für Marketing-E-Mails. |
| `brandColor` | Die Primärfarbe Ihrer Marke im Hexadezimalformat (zum Beispiel `#4dfa8a`). |
{: .reset-td-br-1 .rest-td-br-2 aria-label="1. Schritt: Jasper einrichten" }

**Optionale Felder**

| Feld | Beschreibung |
| --- | --- |
| `toneId` | Sprachstil der Marke |
| `audienceId` | Zielgruppen-Segmentierung |
| `styleId` | Style Guide |
| `knowledgeIds` | Erweiterter Inhaltskontext. Sie können bis zu drei IDs hinzufügen. |
{: .reset-td-br-1 .rest-td-br-2 aria-label="1. Schritt: Jasper einrichten" }

{: start="4"}
4. Generieren Sie Ihre Ausgabe, indem Sie das Template über die Jasper API ausführen. Dies erzeugt eine JSON-Nutzlast, die `subject`, `preheader` und `body` (HTML-Inhalte) enthält.

{% subtabs %}
{% subtab Sample request %}

### Beispielanfrage {#sample-request}

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
{% subtab Sample output %}

### Beispielausgabe {#sample-output}
```
{
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}
```
{% endsubtab %}
{% endsubtabs %}

### 2. Schritt: Braze einrichten {#step-2-set-up-braze}

Verwenden Sie die von Jasper in [Schritt 1](#step-1-set-up-jasper) generierten Werte für `subject`, `preheader` und `body`, um eine POST-Anfrage an die Braze REST API zu stellen und [ein neues E-Mail-Template zu erstellen]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/). Stellen Sie sicher, dass Ihr Braze REST-API-Schlüssel die Berechtigungen `templates.email.create` und `templates.email.update` hat.

### Beispiel einer Braze-API-Anfrage zur Erstellung eines E-Mail-Templates {#sample-braze-api-request-to-create-an-email-template}

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

## Methode: Eine für Braze geeignete angepasste App mit Jasper Studio erstellen {#method-build-a-braze-ready-custom-app-with-jasper-studio}

Jasper Studio ist eine No-Code-Plattform innerhalb von Jasper, die es Ihnen ermöglicht, maßgeschneiderte KI-Apps ohne IT-Unterstützung zu erstellen. Sie können eine angepasste App entwerfen, die JSON-Strukturen erzeugt, die speziell für die Braze API formatiert sind, oder Inhalte generieren, die manuell zu Ihren Braze-Nachrichten hinzugefügt werden können.

1. Wählen Sie auf Ihrem Jasper-Startbildschirm **Create an App** aus.
2. Geben Sie die App an, die Sie erstellen möchten, z. B. **Braze HTML Email Template** oder **Content Block Template**.
3. Bearbeiten Sie die Eingabeaufforderungsfelder, die Jasper generiert. Für ein HTML-E-Mail-Template können Sie Eingabeformulare für die Betreffzeile, den Preheader, den HTML-Body, die Tags, das Umschalten von Inline-CSS und den Namen des Templates einfügen.
4. Integrieren Sie Wissenseinbettungen mit Anleitungen zu Liquid-Best-Practices für konsistente Personalisierung und dynamischen Content.
5. Verfeinern Sie die Anweisungen, die dem Large Language Model (LLM) für die Inhaltserstellung zur Verfügung gestellt werden.
6. Geben Sie ein Beispiel für die gewünschte Ausgabe an, z. B. eine automatisierte JSON-Ausgabe, die für Braze-Nutzlasten formatiert ist.
7. Generieren und exportieren Sie Folgendes:
- **Direktes Kopieren/Einfügen:** Inhalte können direkt in die Braze-Plattform kopiert und eingefügt werden.
- **JSON-Ausgabe:** Generieren Sie eine JSON-Ausgabe. Diese Nutzlast kann dann verwendet werden, um den Braze-Endpunkt über `curl` oder Middleware direkt aufzurufen, oder sie kann in Ihren Workflow für E-Mail-Operationen integriert werden.

![Angepasste Jasper-Braze-App.]({% image_buster /assets/img/jasper/jasper_custom_app.png %})

{% subtabs %}
{% subtab Sample JSON output (custom app) %}

## Beispiel-JSON-Ausgabe (angepasste App) {#sample-json-output-custom-app}

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
{% subtab Sample Braze API request (using custom app output) %}

## Beispiel einer Braze-API-Anfrage (mit Ausgabe der angepassten App) {#sample-braze-api-request-using-custom-app-output}

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

Alternativ können Sie als Marketer eine angepasste App erstellen, die sich an den Markenrichtlinien orientiert, um Inhalte ohne HTML und Copy-and-Paste zu generieren, und Braze-Templates für das Styling verwenden.

{% endtab %}
{% endtabs %}

{% alert note %}
Weitere Hilfe finden Sie in der [Jasper-API-Dokumentation](https://developers.jasper.ai/reference/gettemplate-1) und im [Jasper Studio Help Center](https://help.jasper.ai/hc/en-us/articles/36783295610395-Jasper-Studio).
{% endalert %}