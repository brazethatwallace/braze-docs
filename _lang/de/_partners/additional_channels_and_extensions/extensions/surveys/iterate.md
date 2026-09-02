---
nav_title: Iterate
article_title: Iterate
alias: /partners/iterate/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Iterate, die es Ihnen ermöglicht, Kundendaten durch Umfragen anzureichern, um zusätzliche Insights zu gewinnen."
page_type: partner
search_tag: Partner

---

# Iterate

> [Iterate](https://iteratehq.com) bietet Umfrage- und Feedback-Tools, mit denen Sie von Ihren Kund:innen lernen können, und stellt benutzerfreundliche Forschungserlebnisse bereit, die zu Ihrer Marke passen.

_Diese Integration wird von Iterate gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Iterate in Braze ermöglicht es Ihnen, Iterate-Umfragen nativ und nahtlos in Ihrem Produkt oder Ihren Campaigns bereitzustellen. Umfrageantworten können als angepasste Nutzer:innen-Attribute in Braze aufgezeichnet werden, sodass Sie sich ein vollständiges Bild Ihrer Nutzer:innen machen oder leistungsstarke neue Zielgruppen und Segmente erstellen können.

Mit dem in Ihrer App oder Website installierten Braze SDK or Software-Development-Kit können Sie die in Braze verfügbaren Segmentierungs- und Targeting-Tools nutzen, um Umfragen über In-App-Nachrichten an einen bestimmten Teil Ihrer Zielgruppe zuzustellen – basierend auf einem beliebigen Auslöser oder angepassten Segment. Iterate-Umfragen können auch direkt in Ihre E-Mail-Campaigns eingebettet oder als Links in Ihre Push- oder andere Campaign-Typen eingebunden werden.

## Voraussetzungen {#prerequisites}

| Anforderung | Herkunft |
|---|---|
| Iterate-Konto | Ein [Iterate-Konto](https://iteratehq.com) ist erforderlich, um diese Partnerschaft zu nutzen. |
| Braze Representational State Transfer-API-Schlüssel | Ein Braze Representational State Transfer-API-Schlüssel mit `users.track`-Berechtigungen. Um Umfragen über Braze In-App Messages zu versenden, benötigen Sie außerdem die Berechtigung `kpi.mau.data_series`.<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze Representational State Transfer-Endpunkt | Ihre Representational State Transfer-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Mit Iterate können Sie nahezu alle Arten von Daten erfassen – von persönlichen Informationen (Name, Alter, E-Mail) über Performance-Daten (Net Promoter Score, Kundenzufriedenheit, Sternebewertungen) und Präferenzen (bevorzugtes Gerät, bevorzugte Kommunikationshäufigkeit) bis hin zu Persönlichkeitsmerkmalen (Lieblingsbuch, Hunde- oder Katzenmensch). Was Sie fragen, bleibt ganz Ihnen überlassen – ebenso wie die Art der Daten, die Sie erfassen, oder die Zielgruppen, die Sie aufbauen möchten.

## Integration

### Erste Schritte: Braze mit Iterate verbinden {#getting-started-connect-braze-with-iterate}

Melden Sie sich bei Ihrem Iterate-Konto an und fügen Sie Ihren Braze Representational State Transfer-Endpunkt und Ihren Representational State Transfer-API-Schlüssel auf der Seite **Unternehmenseinstellungen** hinzu.

### Umfragen als In-App-Nachricht zustellen {#deliver-surveys-as-an-in-app-message}

#### 1. Schritt: Erstellen Sie Ihre Umfrage {#step-1-create-your-survey}

Bevor Sie Ihre Umfrage erstellen, aktivieren Sie in den Iterate-Einstellungen den Schalter **Enable in-app message surveys**.

Erstellen Sie anschließend eine neue Umfrage in Iterate und fügen Sie relevante Umfragefragen hinzu. Bei Bedarf können Sie auch eine Eingabeaufforderung einfügen, die vor der Umfrage angezeigt wird. Wählen Sie als Umfragetyp **Send via Braze In-App Message** aus.

Sobald Ihre Umfrage fertiggestellt ist, kopieren Sie auf dem Tab **Publish** das Code-Snippet unter **Copy and paste your embed code**.

#### 2. Schritt: Teilen Sie Ihre Umfrage {#step-2-share-your-survey}

Erstellen Sie in Braze eine neue In-App-Messaging-Campaign, wählen Sie als Messaging-Typ **Custom Code** aus und fügen Sie Ihr Code-Snippet in die Nachricht ein. Wählen Sie anschließend als Klickverhalten der Nachricht **Wait for User to Dismiss**.

Richten Sie Ihre Campaign wie jede andere In-App-Messaging-Campaign ein, indem Sie eine Zustellmethode wählen und eine Zielgruppe festlegen.

### Umfragen per E-Mail oder Push zustellen {#deliver-surveys-through-email-or-push}

#### 1. Schritt: Erstellen Sie Ihre Umfrage

Erstellen Sie eine neue E-Mail- oder Link-Umfrage in Iterate und fügen Sie relevante Umfragefragen hinzu. Nachdem Sie die Fragen formuliert und das Design angepasst haben, wählen Sie **Send survey > Integrations > Braze**.

Anschließend sehen Sie die Konfigurationsoptionen zum Senden von Antworten an Braze. Aktivieren Sie die Integration, um das Senden von Antworten für diese Umfrage an Braze zu ermöglichen.

#### 2. Schritt: Teilen Sie Ihre Umfrage

Ihre Umfrage kann auf zwei Arten geteilt werden: indem Sie die erste Frage in Ihre Nachricht einbetten oder einen direkten Link zur Umfrage auf der Iterate-Plattform einfügen.

![Iterate-Link-Optionen]({% image_buster /assets/img/iterate.png %})

- **Code einbetten**
  - Kopieren Sie das Code-Snippet unter **Email embed code** im Abschnitt „Braze-Integration“ auf dem Tab **Send survey**. Fügen Sie den Code in den HTML-Code Ihrer Braze-E-Mail an der Stelle ein, an der der Anfang der Umfrage erscheinen soll.
  - Wenn Sie Schwierigkeiten bei der Darstellung der Umfragefragen haben oder diese falsch formatiert erscheinen, müssen Sie im Nachrichten-Editor auf den Tab **Sending Info** gehen und die Option **Inline CSS** deaktivieren.
- **Link einfügen**
  - Kopieren Sie den Link unter **Survey Link** im Abschnitt „Braze-Integration“ auf dem Tab **Send survey**. Beachten Sie, dass das im Link enthaltene Liquid {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} beim Senden automatisch für jede:n Nutzer:in ersetzt wird.

### Nächste Schritte: Folgekampagnen aufbauen {#next-steps-build-follow-up-campaigns}

Wenn Nutzer:innen antworten, werden ihre Profile in Echtzeit mit Daten befüllt. Diese Daten können verwendet werden, um Nutzer:innen zu segmentieren und personalisierte Folgekampagnen zu versenden. Wenn Sie beispielsweise die Frage „Gefallen Ihnen unsere Produkte?“ gestellt haben, könnten Sie Segmente von Nutzer:innen erstellen, die das angepasste Nutzer:innen-Attribut `Do you enjoy our products?` haben und mit „Ja“ oder „Nein“ geantwortet haben, und diese Nutzer:innen gezielt ansprechen.

## Angepasste Events in Braze {#braze-custom-events}

Wenn Nutzer:innen eine Umfragefrage beantworten, triggert Iterate ein angepasstes Event innerhalb von Braze namens `survey-question-response`. Angepasste Events ermöglichen es Ihnen, eine beliebige Anzahl und Art von Folgekampagnen zu Trigger or triggern or triggern.

## Namen von Nutzer:innen-Attributen anpassen {#customize-user-attribute-names}

Standardmäßig entspricht das für eine Frage erstellte Nutzer:innen-Attribut dem Fragetext.
In einigen Fällen möchten Sie dies möglicherweise anpassen. Klicken Sie dazu im Schritt **Umfrage erstellen** auf das Dropdown-Menü **Customize user attribute names** und geben Sie die gewünschten angepassten Namen ein.