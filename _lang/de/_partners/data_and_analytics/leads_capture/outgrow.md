---
nav_title: Outgrow
article_title: Outgrow
alias: /partners/outgrow/
description: "Dieser Artikel enthält eine umfassende Anleitung zur Konfiguration einer nativen Integration zwischen Outgrow und Braze für eine verbesserte Synchronisierung von Nutzerdaten und personalisierte Kampagnen."
page_type: partner
search_tag: Partner
---

# Outgrow

> [Outgrow](https://outgrow.co/) ist eine Plattform für interaktive Inhalte, mit der Sie Quiz, Rechner, Umfragen und andere Arten von ansprechenden Inhalten erstellen können, um Nutzerdaten und Insights zu sammeln. Mit der Integration von Braze und Outgrow können Sie Nutzerdaten aus Outgrow automatisch in Braze übertragen und so hochgradig personalisierte und zielgerichtete Kampagnen ermöglichen.

Wenn Sie die Integration von Braze und Outgrow für interaktive Inhalte nutzen, profitieren Sie unter anderem von folgenden Vorteilen:

- **Verbesserte Personalisierung**: Erfassen Sie Daten aus Outgrow-Quizzes, Umfragen und Rechnern, die angepassten Attributen in Braze zugeordnet werden können. Diese Daten ermöglichen eine präzise Segmentierung und personalisierte Kampagnen.
- **Echtzeit-Datensynchronisierung**: Empfangen Sie Outgrow-Daten in Braze in Realtime, sodass Sie sofort auf Nutzer:innen-Insights reagieren können. Dies ermöglicht zeitnahe Nachfassaktionen oder personalisierte Nachrichten, die auf den letzten Interaktionen der Nutzer:innen basieren.
- **Optimierte Datenverwaltung**: Automatisieren Sie den Datentransfer zwischen Outgrow und Braze. So vermeiden Sie manuelle Datenexporte und -importe, reduzieren Datenabweichungen und sparen Zeit.
- **Verbesserte Nutzererfahrung**: Nutzen Sie Insights der Nutzer:innen, um relevantere Erlebnisse zu schaffen, die zu höherer Zufriedenheit, Bindung und Lifetime-Value führen.
- **Flexibles Targeting und Segmentierung**: Verfeinern Sie die Segmentierung in Braze mithilfe von Outgrow-Daten, um Nutzer:innen auf der Grundlage bestimmter Interaktionen (z. B. Quiz-Ergebnisse oder Antworten auf Umfragen) anzusprechen und Kampagnen zu erstellen, die bei Ihren Nutzer:innen auf Resonanz stoßen.

## Voraussetzungen {#prerequisites}

Bevor Sie die Integration von Outgrow und Braze einrichten, vergewissern Sie sich, dass Sie über Folgendes verfügen:

| Anforderung | Beschreibung |
|-------------|-------------|
| **Outgrow-Konto** | Ein registriertes Outgrow-Konto zur Konfiguration und Verwaltung der Einstellungen für interaktive Inhalte und Datenübertragungen |
| **Braze-Konto** | Ein Braze-Konto mit Zugriff auf REST-API-Zugangsdaten |
| **API-Schlüssel** | Ein API-Schlüssel von Braze mit der Berechtigung `users.track`, um die Übertragung von Nutzerdaten zu ermöglichen |
| **Angepasste Attribute in Braze** | Angepasste Attribute, die in Braze eingerichtet wurden, um Outgrow-Antworten zu erfassen (z. B. Quiz-Ergebnisse, Segmente und andere) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

Folgen Sie diesen Schritten, um die Integration von Braze und Outgrow zu konfigurieren:

### 1. Schritt: Braze-API-Schlüssel generieren {#step-1-generate-braze-api-key}

1. Gehen Sie in Ihrem Braze-Konto zu **Developer Console** > **API Settings**.
2. Wählen Sie **Create New API Key**.
3. Benennen Sie Ihren API-Schlüssel, aktivieren Sie die Berechtigung `users.track` und speichern Sie den API-Schlüssel.

### 2. Schritt: Braze-Integration in Outgrow konfigurieren {#step-2-configure-the-braze-integration-in-outgrow}

1. Melden Sie sich bei Ihrem Outgrow-Konto an.
2. Gehen Sie im Dashboard zu **Integrations**.
3. Wählen Sie aus der Liste der verfügbaren Integrationen **Braze** aus.
4. Geben Sie Ihren **Braze API Key** und die **REST API Endpoint URL** ein:
   - **API Key**: Geben Sie den API-Schlüssel ein, der in Braze generiert wurde
   - **REST Endpoint URL**: Geben Sie den Endpunkt für Ihre Braze-Instanz ein (z. B. `https://rest.iad-01.braze.com`)
5. Wählen Sie **Save**, um die Integration zu aktivieren.

### 3. Schritt: Outgrow-Daten auf Braze-Attribute abbilden {#step-3-map-outgrow-data-to-braze-attributes}

In Outgrow können Sie Antworten aus interaktiven Inhalten (wie Quiz-Ergebnisse, angepasste Segmente oder Engagement-Scores) angepassten Attributen in Braze zuordnen.

1. Legen Sie in den Outgrow-**Integration Settings** für Braze fest, welche Outgrow-Antworten den Braze-Attributen zugeordnet werden sollen.
2. Stellen Sie sicher, dass jede ausgewählte Antwort mit einem angepassten Attribut in Braze übereinstimmt. Zum Beispiel:
   - Quiz-Ergebnis wird `outgrow_quiz_score` zugeordnet.
   - Angepasstes Segment wird `outgrow_custom_segment` zugeordnet.
3. Speichern Sie Ihre Zuordnungseinstellungen.

### 4. Schritt: Integration testen {#step-4-test-the-integration}

Nachdem Sie die Integration konfiguriert haben, führen Sie einen Test durch, um zu überprüfen, ob die Daten ordnungsgemäß von Outgrow zu Braze übertragen werden.

1. Veröffentlichen Sie ein Outgrow-Erlebnis (z. B. ein Quiz oder einen Rechner) und schließen Sie es als Testnutzer:in ab.
2. Gehen Sie in Ihrem Braze-Konto zum Abschnitt **User Profile** und prüfen Sie, ob die Attribute aktualisiert wurden (z. B. `outgrow_quiz_score` oder `outgrow_custom_segment`).
3. Überprüfen Sie, ob die Daten unter den entsprechenden angepassten Attributen korrekt ausgefüllt sind.

## Verwendung von Outgrow-Daten in Braze für Segmentierung und Targeting {#using-outgrow-data-in-braze-for-segmentation-and-targeting}

### Segmente in Braze mit Outgrow-Daten erstellen {#creating-segments-in-braze-with-outgrow-data}

Mit der Integration können Sie Braze-Segmente erstellen, die auf angepassten Attributen basieren, die aus Outgrow-Antworten befüllt werden.

1. Gehen Sie in Braze zu **Engagement** > **Segments** und wählen Sie **Create New Segment**.
2. Benennen Sie Ihr Segment und setzen Sie Filter auf der Grundlage von Outgrow-Daten. Zum Beispiel:
   - Filtern Sie nach `outgrow_quiz_score`, um Nutzer:innen anzusprechen, die über einem bestimmten Schwellenwert abgeschnitten haben.
   - Filtern Sie nach `outgrow_custom_segment`, um Nutzer:innen anzusprechen, die zu einem bestimmten, von Outgrow definierten Segment gehören.
3. Speichern Sie Ihr Segment zur Verwendung in Campaigns und Canvases.

### Campaigns mit von Outgrow definierten Segmenten starten {#launching-campaigns-with-outgrow-defined-segments}

Mit den angepassten Segmenten, die aus Outgrow-Daten erstellt wurden, können Sie Ihre Braze-Campaigns personalisieren und Nutzer:innen auf der Grundlage ihrer Reaktionen auf interaktive Inhalte ansprechen. Um dies zu tun und ein personalisiertes Nutzererlebnis zu schaffen, folgen Sie diesen Schritten:

1. Gehen Sie in Braze zu **Engagement** > **Campaigns**.
2. Wählen Sie **Create Campaign** und wählen Sie die Art Ihrer Campaign (E-Mail, Push, In-App-Nachricht oder andere).
3. Wählen Sie im Schritt für das Zielgruppen-Targeting das Segment aus, das aus den Outgrow-Attributen erstellt wurde (z. B. Nutzer:innen mit bestimmten Quiz-Ergebnissen oder Segmenten).
4. Passen Sie den Inhalt und die Einstellungen Ihrer Campaign an und starten Sie sie dann.

## Fehlerbehebung bei häufigen Problemen {#troubleshooting-common-issues}

| Problem | Lösung |
|---------|--------|
| **Daten werden nicht an Braze übertragen** | Überprüfen Sie, ob der API-Schlüssel und die Endpunkt-URL in Ihren Outgrow-Integrationseinstellungen korrekt sind. Stellen Sie sicher, dass für den API-Schlüssel die Berechtigung `users.track` aktiviert ist. |
| **Falsche Datenzuordnung** | Stellen Sie sicher, dass jede zugeordnete Outgrow-Antwort einem gültigen angepassten Attribut in Braze entspricht und dass die Attributnamen genau übereinstimmen. |
| **Segment filtert nicht korrekt** | Stellen Sie sicher, dass angepasste Attribute in Braze richtig eingerichtet sind und Daten empfangen. Überprüfen Sie die Logik Ihres Segment-Filters erneut. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting common issues" }

## Zusätzliche Hinweise {#additional-considerations}

- **Datenschutz**: Halten Sie sich bei der Übertragung von Nutzerdaten zwischen Plattformen an die Datenschutzbestimmungen (z. B. DSGVO und CCPA).
- **Rate-Limits**: Outgrow-Daten werden in Realtime an Braze gesendet, aber für große Datenmengen können Rate-Limits der Braze API gelten. Planen Sie entsprechend für hochfrequentierte Erlebnisse.
- **Konfiguration angepasster Attribute**: Überprüfen Sie, ob die angepassten Attribute in Braze, die in dieser Integration verwendet werden, korrekt konfiguriert sind, um die von Outgrow gesendeten Daten zu erfassen.

Weitere Hilfe finden Sie in der [Outgrow-Dokumentation](https://support.outgrow.co/docs/configuring-native-integration-between-outgrow-braze) oder kontaktieren Sie den Outgrow-Support.