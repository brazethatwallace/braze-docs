---
nav_title: Lexer
article_title: Lexer
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Lexer, einer Customer Data Platform, die Marketern Kundendaten an die Hand gibt, um verkaufsfördernde Erlebnisse zu schaffen."
alias: /partners/lexer/
page_type: partner
search_tag: Partner
---

# Lexer

> [Lexer](https://lexer.io/), eine speziell entwickelte Customer Data Platform für den Einzelhandel, hilft Marken, ihren Umsatz durch verbesserte Kundenerlebnisse zu steigern, indem sie eine robuste Datenanreicherung mit den intuitivsten Tools und fachkundiger Beratung kombiniert.

_Diese Integration wird von Lexer gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Lexer erlaubt es Ihnen, Daten zwischen den beiden Plattformen zu synchronisieren. Nutzen Sie Ihre Daten in Lexer, um wertvolle Segmente in Braze zu erstellen, oder importieren Sie Ihre bestehenden Segmente in Lexer, um Insights zu erhalten.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Partner-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Lexer-Konto. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit allen `user`-Berechtigungen (außer `user.delete`) und `segment.list`-Berechtigungen. Der Berechtigungssatz kann sich ändern, wenn Lexer die Unterstützung für weitere Braze-Objekte hinzufügt. Sie sollten also entweder jetzt mehr Berechtigungen erteilen oder ein Update dieser Berechtigungen in der Zukunft planen.<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST-Endpunkt | Ihre [URL für den REST-Endpunkt]({{site.baseurl}}/api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Amazon AWS S3-Bucket und Zugangsdaten | Bevor Sie mit der Integration beginnen, müssen Sie über Zugangsdaten für einen AWS S3-Bucket verfügen, der mit Ihrem Lexer-Hub verbunden ist (dies kann ein Bucket sein, den Sie erstellen, oder einer, den Lexer für Sie erstellt und verwaltet). Besuchen Sie [Lexer](https://learn.lexer.io/docs/amazon-s3) für eine Anleitung zu dieser Anforderung. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Navigieren Sie in Lexer zu **Manage > Integration**, wählen Sie die Kachel **Braze** aus und klicken Sie auf **Integrate Braze**. Geben Sie die folgenden Informationen an:
- **Braze REST endpoint**
- **Braze REST API key**
- **AWS Credentials**
  - **AWS S3 bucket name**
  - **AWS S3 [bucket region](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)**
  - **AWS S3 bucket path**: Dieser Pfad sollte mit dem Pfad übereinstimmen, den Sie bei der [Verbindung Ihres S3-Buckets mit Braze]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) angegeben haben. Dieses Feld sollte leer sein, wenn Sie Braze keine Angaben gemacht haben.
  - **AWS S3 secret access key**: Besuchen Sie Amazon für Informationen zur [Erstellung eines Zugangsschlüssels](https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/).
- **Braze export segment ID**: Die ID des Segments, das Sie in Braze erstellt haben und das alle Nutzer:innen enthält, die Sie in Lexer exportieren möchten. Wenn es Nutzer:innen gibt, die Sie nicht in Lexer exportieren möchten, können Sie sie aus dem Segment ausschließen, das Sie in Braze erstellt haben. Um den Bezeichner Ihres Segments zu finden, klicken Sie in Braze auf das gewünschte Segment und suchen Sie den **Segment-API-Bezeichner**.

![]({% image_buster /assets/img/lexer/braze_integrate_screen.png %})

### Auswahl einer AWS S3-Option (Lexer-verwaltet oder selbstverwaltet) {#choosing-an-aws-s3-option-lexer-managed-or-self-managed}
Die Verwendung eines von Lexer verwalteten Buckets ist die bevorzugte Methode, um Braze mit Ihrem Lexer-Hub zu verbinden, und reduziert den Einrichtungsaufwand. Lexer liefert Ihnen die einmaligen Details, die Sie zur Konfiguration von Braze benötigen.

Wenn Sie bereits einen S3-Bucket mit Braze verbunden haben und ihn für andere Zwecke verwenden, müssen Sie stattdessen Lexer Zugriff auf diesen selbstverwalteten Bucket gewähren, indem Sie die vorangehenden Schritte ausführen.

Diese Integration funktioniert, indem Sie Lexer Ihr bestehendes API-Token und Ihre Secrets zur Verfügung stellen, sodass Lexer diese Exporte in Ihrem Namen durchführen kann. Außerdem importiert sie Ihre Braze-Daten mit diesen Zugangsdaten und Ihrer S3-Konfiguration in Lexer, um Ihre Daten auf beiden Plattformen automatisch zu synchronisieren.

## Segmente an Braze senden {#sending-segments-to-braze}

### 1. Schritt: Aktivierung erstellen {#step-1-create-activation}

Lexer Activate aktualisiert automatisch Ihre Braze-Profile und fügt Attribute hinzu oder entfernt sie, wenn Kund:innen in Ihr Segment eintreten oder es verlassen.

1. Klicken Sie in Lexer unter **Lexer Activations** auf **ACTIVATE NEW AUDIENCE**.
2. Wählen Sie die entsprechende Braze-Aktivierung für diese Campaign aus.
3. Fügen Sie Ihr Segment hinzu.
4. Aktualisieren Sie den Namen Ihrer Zielgruppe; dieser wird in Braze zu Ihrem Attributwert.
5. Dies ist das angepasste Attribut, das wir in Braze aktualisieren werden. Wenden Sie sich zum Update an den [Lexer-Support](support@lexer.io).
6. Markieren Sie die entsprechende Listenaktion – in den meisten Fällen werden Sie Ihre Liste pflegen wollen.
7. Überprüfen Sie die Bedingungen und klicken Sie auf **SEND AUDIENCE**.

![]({% image_buster /assets/img/lexer/lexer.png %})

### 2. Schritt: Aktivierung überprüfen {#step-2-verify-activation}

Sobald Ihre Aktivierung in Activate als gesendet bestätigt wurde, werden Sie sehen, dass die Datensätze in Braze aktualisiert werden. Ihre Profile werden in Braze erst dann vollständig aktualisiert, wenn Sie eine Bestätigungs-E-Mail von Lexer erhalten haben.

### 3. Schritt: Erstellen Sie Ihr Braze-Segment {#step-3-create-your-braze-segment}

In Braze sehen Sie, dass der Name Ihrer Zielgruppe in Lexer jetzt ein Wert in Ihrem angepassten Attribut `lexer_audience` ist. Braze hat ein Limit von 100 Werten pro Attribut.

Um Ihr Segment zu erstellen, navigieren Sie zu **Segment > + Create Segment** und wählen Sie **Custom Attribute** als Filter. Wählen Sie als Nächstes `lexer_audience` als Attribut und den Namen der gewünschten Lexer-Zielgruppe aus. Wenn Sie fertig sind, **speichern** Sie Ihre Zielgruppe.

Sie können dieses neu erstellte Segment nun zu zukünftigen Campaigns und Canvases in Braze hinzufügen, um diese Endnutzer:innen anzusprechen.