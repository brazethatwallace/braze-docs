---
nav_title: "AMP für E-Mail"
article_title: "AMP für E-Mail"
alias: /amphtml/
page_order: 11
description: "Dieser Referenzartikel bietet einen Überblick über AMP für E-Mail und gängige Anwendungsfälle."
channel:
  - email

---

# AMP für E-Mail {#amp-for-email}

> Mit [AMP für E-Mail](https://amp.dev/about/email) können Sie interaktive Elemente zu Ihren E-Mails hinzufügen und die Kommunikation mit Ihren Kund:innen verbessern, indem Sie ein vollständiges Erlebnis direkt in den Posteingang Ihrer Nutzer:innen liefern. AMP macht dies durch die Verwendung verschiedener Komponenten möglich, die beim Erstellen ansprechender E-Mail-Angebote wie Umfragen, Feedback-Fragebögen, Abstimmungskampagnen, Bewertungen, Abo-Center und mehr helfen können. Tools wie diese bieten Möglichkeiten, Engagement und Bindung zu steigern.

## Anforderungen {#requirements}

Braze ist nicht dafür verantwortlich, dass sich Nutzer:innen bei Google Registrierung oder die erforderlichen Sicherheitsanforderungen erfüllen. AMP für E-Mail ist nur für SparkPost und SendGrid verfügbar.

| Anforderung   | Beschreibung |
| --------------| ----------- |
| AMP für E-Mail aktiviert | AMP ist für alle Nutzer:innen verfügbar. |
| Gmail-Konto-Aktivierung | Siehe [Gmail-Konto aktivieren](#enabling-gmail-account). |
| Google-Sender-Authentifizierung | Gmail [authentifiziert den Sender](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication) von AMP-E-Mails mit DKIM, SPF und DMARC. Diese müssen für Ihr Konto eingerichtet werden. <br><br>- [Domain Keys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM) <br>- [Sender Policy Framework](https://en.wikipedia.org/wiki/Sender_Policy_Framework)(SPF)<br>- [Domain-based Message Authentication, Reporting, and Conformance](https://en.wikipedia.org/wiki/DMARC)(DMARC)
| AMP-E-Mail-Elemente | Eine überzeugende AMP-E-Mail beinhaltet den strategischen Einsatz verschiedener Komponenten. Weitere Informationen finden Sie im Tab „Grundlagen“ im Abschnitt [Komponenten](#components). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anforderungen" }

### Unterstützte E-Mail-Clients {#supported-email-clients}

Bevor Sie AMP-E-Mails an Nutzer:innen senden können, müssen Sie sich bei unseren E-Mail-Clients Registrierung. Der Registrierungsprozess umfasst das Senden einer Test-AMP-HTML-E-Mail zur Genehmigung. Die Genehmigungszeiten variieren je nach Client. Folgen Sie den Registrierungslinks für weitere Informationen.

| Client | Registrierungslink |
| ------ | -------- |
| Gmail | [Google](https://developers.google.com/gmail/ampemail/register) |
| FairEmail | [FairEmail](https://email.faircode.eu/) |
| Yahoo | [Yahoo](https://senders.yahooinc.com/amp/) |
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Unterstützte E-Mail-Clients" }

Eine vollständige Liste der unterstützten E-Mail-Clients finden Sie in der [AMP-Dokumentation](https://amp.dev/support/faq/email-support).

#### An nicht registrierte Anbieter senden {#send-to-unregistered-providers}

Wenn Sie eine AMP-E-Mail an Anbieter wie Yahoo oder Mail.ru senden, bevor Sie deren Registrierungsprozess abgeschlossen haben, ignorieren diese Anbieter den AMP-Teil der E-Mail und zeigen stattdessen die HTML- oder Klartext-Fallback-Version an. Der AMP-Teil selbst verursacht keine Zustellbarkeitsprobleme für nicht registrierte Absender.

### Gmail-Konto aktivieren {#enabling-gmail-account}

Gehen Sie zu Ihren Gmail-Einstellungen und wählen Sie unter **Allgemein** die Option **Dynamische E-Mails aktivieren** aus.

![Ein Beispiel für Gmail-Einstellungen mit aktiviertem Kontrollkästchen „Dynamische E-Mails aktivieren“.]({% image_buster /assets/img/dynamic-content.png %})

## API-Nutzung {#api-usage}

Sie können AMP für E-Mail auch mit unserer API verwenden. Wenn Sie einen der Braze [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging) zum Senden einer E-Mail verwenden, fügen Sie `amp_body` als Objektspezifikation hinzu, wie im folgenden Abschnitt gezeigt.

### E-Mail-Objektspezifikation {#email-object-specification}

```json
{
  "app_id": (required, string) see app identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <user@example.com>"),
  "reply_to": (optional, valid email address in the format "user@example.com" - defaults to your workspace's default reply to if not set),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "amp_body": (optional, updates the text-amp-html MIME type) the email body in AMP HTML. The MIME (Multipurpose Internet Mail Extensions) type to be referenced is "text/x-amp-html",
  "body": (required unless email_template_id is given, valid HTML),
  "preheader": (optional*, string) Recommended length 50-100 characters,
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid key-value hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid key-value hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array), array of JSON objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header,
}
```

## Ihre AMP-E-Mail erstellen {#create-your-amp-email}

Erstellen Sie zunächst Ihre AMP-E-Mail mit [Komponenten](#components). Verwenden Sie dann die [Braze-API](#api-usage), um Ihre Nachricht zu senden, und stellen Sie sicher, dass `amp_body` für Ihr AMP-HTML enthalten ist.

Zusätzlich zum AMP-HTML benötigen wir eine reguläre HTML-`body`-Version und empfehlen eine `plaintext_body`-Version Ihrer AMP-E-Mail. Alle AMP-E-Mails werden als Multipart gesendet, d. h. Braze sendet eine E-Mail, die HTML, Klartext und AMP-HTML unterstützt. Dies ist nützlich, falls Ihre E-Mail über einen Anbieter gesendet wird, der AMP für E-Mail noch nicht unterstützt, da die E-Mail automatisch auf die entsprechende Version basierend auf den Nutzer:innen und ihrem Gerät zurückfällt.

{% alert note %}
Wenn Sie eine AMP-E-Mail erstellen, stellen Sie sicher, dass Sie sich im AMP-Editor befinden, da AMP-Code nicht zum HTML-Editor hinzugefügt werden sollte.
{% endalert %}

Weitere Ressourcen:

- [AMP-Tutorial](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- [Beispielcode](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73), um zu sehen, wie das Endergebnis aussehen sollte.
- [AMP-E-Mail-Komponentenbibliothek](https://amp.dev/documentation/components/?format=email/)

### Komponenten {#components}

Beim Erstellen der AMP-Elemente empfehlen wir, sich mit Ihrem Entwicklerteam abzustimmen und Design-Ressourcen und -Elemente für eine zusätzliche Verfeinerung einzubeziehen.

{% tabs %}
  {% tab Grundlagen %}

Jedes dieser Elemente ist im Body Ihrer AMP-E-Mail erforderlich.

| Komponente | Beschreibung | Beispiel |
|---------|--------------|---------|
| Identifikation <br><br> `⚡4email` oder `amp4email`| Identifiziert Ihre E-Mail als AMP-HTML-E-Mail. | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| AMP-Runtime laden <br><br> `<script>` | Ermöglicht die Ausführung von AMP in Ihrer E-Mail mithilfe von JavaScript. | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| CSS-Boilerplate | Blendet Inhalte aus, bis AMP geladen ist. <br> E-Mail-Anbieter, die AMP-E-Mails unterstützen, erzwingen Sicherheitsprüfungen, die nur geprüfte AMP-Skripte in ihren Clients ausführen lassen. | `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Komponenten" }

  {% endtab %}
  {% tab Dynamisch %}

Verwenden Sie diese Komponenten, um dynamische Layouts und Verhaltensweisen in Ihren E-Mails zu erstellen.

| Komponente | Beschreibung | Erforderliches Skript |
|---------|--------------|---------|
| [Akkordeon](https://amp.dev/documentation/components/amp-accordion?format=email) <br><br> `amp-accordion`| Ermöglicht es Nutzer:innen, die Inhaltsübersicht anzuzeigen und zu einem beliebigen Abschnitt zu springen. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [Formulare](https://amp.dev/documentation/components/amp-form?format=email) <br><br> `amp-form`| Erstellen Sie Formulare zum Absenden von Eingabefeldern in einem AMP-Dokument. | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Komponenten" }

{% alert note %}
Jede Komponente, die eine Authentifizierung der Nutzer:innen erfordert, muss [Google-Zugriffstoken](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) oder [Proxy-Assertion-Token / Textbaustein](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens) verwenden.
{% endalert %}
  {% endtab %}
  {% tab Kreativ %}

  Werden Sie kreativ mit AMP-Komponenten, die Ihnen helfen können, Ihre E-Mail auf Ihre Zielgruppe zuzuschneiden.

| Komponente | Beschreibung | Erforderliches Skript |
|---------|--------------|---------|
| [Animiertes Bild](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-anim`| Zeigt ein animiertes Bild (normalerweise ein GIF) an, das über die Runtime verwaltet wird. | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [Karussell](https://amp.dev/documentation/components/amp-carousel?format=email) <br><br> `amp-carousel`| Zeigt mehrere ähnliche Inhalte entlang einer horizontalen Achse an. | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [Bild](https://amp.dev/documentation/components/amp-img?format=email) | Ein von der Runtime verwalteter Ersatz für das HTML-`img`-Tag. <br>  Sie können auch eine [Lightbox für Ihr Bild](https://amp.dev/documentation/components/amp-image-lightbox?format=email) erstellen. | `<amp-img alt="A view of the sea"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Komponenten" }

{% alert note %}
Jede Komponente, die eine Authentifizierung der Nutzer:innen erfordert, muss [Google-Zugriffstoken](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) oder [Proxy-Assertion-Token / Textbaustein](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens) verwenden.
{% endalert %}

  {% endtab %}
  {% tab Sonstiges %}

| Komponente | Beschreibung |
|---------|--------------|
| [Datenbindung und Ausdrücke](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-bind`| Fügt Ihren AMP-Seiten angepasste zustandsabhängige Interaktivität über Datenbindung und JavaScript-ähnliche Ausdrücke hinzu. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Komponenten" }

{% alert note %}
Jede Komponente, die eine Authentifizierung der Nutzer:innen erfordert, muss [Google-Zugriffstoken](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) oder [Proxy-Assertion-Token / Textbaustein](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens) verwenden.
{% endalert %}

{% endtab %}
{% endtabs %}

Eine vollständige Liste der AMP-Komponenten finden Sie in der [AMP-Dokumentation](https://amp.dev/documentation/components/?format=email).

### Anwendungsfälle {#use-cases}

{% tabs local %}
{% tab Interaktive Umfragen %}

Mit der Komponente `<amp-form>` können Sie interaktive Umfragen erstellen, die ausgefüllt werden können, ohne den E-Mail-Posteingang zu verlassen. Dies kann erreicht werden, indem Sie `<amp-form>` verwenden, um die Umfrageantwort zu übermitteln, und dann Ihr Backend diese aggregierten Daten bereitstellen lassen.

Einige Beispiele sind:
* Konferenz-Umfrage-E-Mail
* Dynamisch aktualisierte Elemente im Feed
* Artikel-Lesezeichen-E-Mail

Mit dieser Komponente können Nutzer:innen Feldwerte absenden oder löschen. Abhängig davon, wie Sie Ihre E-Mail einrichten, können Sie den Nutzer:innen auch zusätzliche Hinweise geben, z. B. ob die Umfrageübermittlung erfolgreich war, oder die Antworten Ihrer Nutzer:innen mit Umfrageergebnissen anzeigen (z. B. bei einer Abstimmungskampagne).

{% endtab %}
{% tab Einklappbare Inhalte %}

Erweitern Sie Ihre Inhaltsabschnitte mit der Komponente `<amp-accordion>`. Diese Komponente ermöglicht es Ihnen, zusammenklappbare und erweiterbare Inhaltsabschnitte anzuzeigen, sodass Betrachter:innen die Inhaltsübersicht überblicken und zu einem beliebigen Abschnitt springen können.

Wenn Sie dazu neigen, lange Bildungsartikel oder personalisierte Empfehlungen zu senden, bietet dies eine Möglichkeit für Betrachter:innen, die Inhaltsübersicht zu überblicken und zu einem beliebigen Abschnitt oder einer bestimmten Produktempfehlung zu springen, um weitere Details zu erhalten. Dies kann besonders für mobile Nutzer:innen hilfreich sein, bei denen bereits wenige Sätze in einem Abschnitt Scrollen erfordern.
{% endtab %}
{% tab Bildlastige E-Mails %}

Wenn Sie dazu neigen, E-Mails mit vielen professionellen Fotos zu senden, wie es bei Einzelhandelsmarken üblich ist, können Sie die Komponente `<amp-image-lightbox>` verwenden, die es Nutzer:innen ermöglicht, mit einem Bild zu interagieren, das sie anspricht. Wenn Nutzer:innen auf das Bild klicken, zeigt diese Komponente das Bild in der Mitte der Nachricht an und erzeugt einen Lightbox-Effekt.

Darüber hinaus ermöglicht die Komponente `<amp-image-lightbox>` den Nutzer:innen, eine detaillierte Bildbeschreibung anzuzeigen. Sie können dieselbe Komponente für mehr als ein Bild verwenden. Wenn Sie beispielsweise mehrere Bilder in Ihrer E-Mail haben und Nutzer:innen auf eines der Bilder klicken, wird das Bild in der Lightbox angezeigt.

{% endtab %}
{% tab Textbasierte E-Mails %}

Für E-Mails, die hauptsächlich auf Textinhalte setzen, ermöglicht Ihnen die Komponente `<amp-fit-text>`, die Größe und Anpassung von Text innerhalb eines bestimmten Bereichs zu verwalten.

Beispiele sind:

- Skalierung des Textes, um in einen Bereich zu passen
- Skalierung des Textes, um in den Bereich zu passen, unter Verwendung einer maximalen Schriftgröße, wobei Sie die maximale Schriftgröße festlegen können
- Abschneiden des Textes, wenn der Inhalt den Bereich überschreitet

{% endtab %}
{% endtabs %}

### amp-mustache verwenden {#use-amp-mustache}

Ähnlich wie Liquid unterstützt AMP eine Skriptsprache für fortgeschrittenere Anwendungsfälle. Diese Komponente heißt [`amp-mustache`](https://amp.dev/documentation/components/amp-mustache/?format=email). Wenn Sie Mustache-Markup-Sprache einbinden, müssen Sie sie mit dem [`raw`](https://shopify.github.io/liquid/tags/raw/)-Tag von Liquid umschließen. Beachten Sie, dass Liquid und Mustache eine ähnliche Syntax verwenden.

Indem Sie Ihren Inhalt mit dem `raw`-Tag umschließen, ignoriert die Braze-Verarbeitungs-Engine alle Inhalte zwischen den `raw`-Tags und sendet die Mustache-Variable, die Ihr Team benötigt.

## Metriken und Analytics {#metrics-and-analytics}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Metriken und Analytics">
  <caption>Metriken und Analytics</caption>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Öffnungen gesamt</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Opens' %} Bei AMP-E-Mails sind dies die Gesamtöffnungen für die HTML- und Klartext-Versionen.</td>
        </tr>
        <tr>
            <td class="no-split">Klicks gesamt</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %} Bei AMP-E-Mails sind dies die Gesamtklicks in den HTML- und Klartext-Versionen.</td>
        </tr>
        <tr>
            <td class="no-split">AMP-Öffnungen</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split">AMP-Klicks</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}</td>
        </tr>
    </tbody>
</table>

## Testen und Fehlerbehebung {#test-and-troubleshoot}


Bevor Sie Ihre AMP-E-Mail senden, empfehlen wir:

- Testen Sie gemäß diesen [Gmail-Richtlinien](https://developers.google.com/gmail/ampemail/testing-dynamic-email).
- Verwenden Sie den [Gmail AMP for Email Playground](https://amp.gmail.dev/playground/), um AMP-Markup zu validieren.
  - Wenn Ihre AMP-E-Mail Liquid-Tags verwendet, ersetzen Sie diese durch statische Platzhalterwerte, bevor Sie sie in den Gmail AMP for Email Playground einfügen. Nicht gerenderte Liquid-Tags verursachen Validierungsfehler.

Damit Ihre AMP-E-Mail an ein beliebiges Gmail-Konto zugestellt werden kann, muss die E-Mail die folgenden Bedingungen erfüllen:

- Die Sicherheitsanforderungen für AMP für E-Mail müssen erfüllt sein.
- Der AMP-MIME-Teil muss ein gültiges AMP-Dokument enthalten.
- Die E-Mail sollte den AMP-MIME-Teil vor dem HTML-MIME-Teil enthalten.
- Der AMP-MIME-Teil muss kleiner als 100&nbsp;KB sein.

Beachten Sie, dass Gesamtklicks und eindeutige Klicks keine Klicks berücksichtigen, die aus einer AMP-Nachricht stammen (nur HTML und Klartext). AMP-spezifische Klicks werden der Metrik *amp_click* zugeordnet.

Wenn keine dieser Bedingungen den Fehler verursacht, kontaktieren Sie den [Support]({{site.baseurl}}/support_contact).

### Gmail-Posteingang für die Darstellung von AMP-E-Mails konfigurieren {#configure-gmail-inbox-to-render-amp-emails}

Sie können Ihren Gmail-Posteingang zu Testzwecken für die Darstellung von AMP-E-Mails konfigurieren, indem Sie Folgendes tun:

1. Wählen Sie in Gmail **Einstellungen** in der Symbolleiste Ihres Posteingangs aus.
2. Wählen Sie **Alle Einstellungen anzeigen** aus.
3. Gehen Sie im Tab **Allgemein** zum Abschnitt **Dynamische E-Mails** und bestätigen Sie, dass das Kontrollkästchen **Dynamische E-Mails aktivieren** aktiviert ist.
4. Wählen Sie als Nächstes **Entwicklereinstellungen** und aktivieren Sie das Kontrollkästchen **Dynamische E-Mails von diesem Absender immer zulassen:**.
5. Geben Sie dieselbe Domain ein, die in der Absenderadresse Ihrer Testnachricht verwendet wird.
6. Speichern Sie Ihre Änderungen.

Jetzt können Sie die Test-E-Mail an Ihr Gmail-Konto senden, und AMP-E-Mails sollten in Gmail dargestellt werden.

### Häufig gestellte Fragen {#frequently-asked-questions}

#### Sollte ich bei AMP-E-Mails segmentieren? {#should-i-segment-with-amp-emails}

Wir empfehlen, nicht zu segmentieren, um an alle verschiedenen Nutzer:innentypen zu senden. Das liegt daran, dass wir AMP-Nachrichten als Multipart senden, wobei verschiedene Versionen in der ursprünglichen E-Mail enthalten sind. Wenn Nutzer:innen die AMP-Version nicht sehen können, wird automatisch auf HTML zurückgefallen.