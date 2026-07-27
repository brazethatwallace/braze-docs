---
nav_title: Mailizio
article_title: Mailizio
alias: /partners/mailizio
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Mailizio, einer Plattform zur Erstellung und Verwaltung von E-Mails, mit der Sie wiederverwendbare, markensichere Inhalte erstellen und nach Braze exportieren können."
page_type: partner
search_tag: Partner

---

# Mailizio

> [Mailizio](https://mailizio.com/) ist eine Plattform zur Erstellung und Verwaltung von E-Mails, mit der Sie wiederverwendbare, markensichere Inhalte mit einem intuitiven visuellen Editor erstellen können. Mit der Integration von Mailizio in Braze können Sie Ihre Content Blocks und E-Mail-Templates exportieren und dann automatisch In-App-Nachrichten aus denselben Assets generieren, was eine schnelle und vollständig kontrollierte Campaign-Bereitstellung ermöglicht.

_Diese Integration wird von Mailizio gepflegt._

## Über die Integration {#about-the-integration}

Mit der Integration von Mailizio und Braze können Sie dynamische E-Mail-Templates mit dem Mailizio-Editor entwerfen, Liquid-Variablen nutzen, wie sie in Ihren Braze-Konfigurationen verwendet werden, und diese für eine optimierte Campaign-Ausführung an Braze pushen.

## Anwendungsfälle {#use-cases}

- Pushen Sie versandfertige E-Mail-Templates für Campaigns und Transaktionsnachrichten direkt in Braze.
- Erstellen Sie wiederverwendbare Inhaltsmodule (Kopfzeilen, Fußzeilen, Aktionen und mehr), um die Produktion über mehrere Campaigns und Kanäle hinweg zu optimieren.
- Generieren Sie In-App-Nachrichten aus E-Mails: Mailizio identifiziert relevante Abschnitte Ihrer E-Mail und ermöglicht Ihnen den Export des HTML-Codes zur Verwendung in Ihren In-App-Campaigns.
- Personalisieren Sie in großem Umfang mit Braze-kompatiblen Liquid-Variablen sowohl in E-Mails als auch in In-App-Nachrichten.
- Halten Sie Ihr Branding konsistent, indem Sie Ihre kreativen Assets in Mailizio verwalten und in Braze mit einem einzigen Export aktualisieren.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Mailizio-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Mailizio-Konto. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit vollständigen **Templates**-Berechtigungen.<br><br>Sie können einen Braze-REST-API-Schlüssel im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellen. |
| Braze-REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Stellen Sie Ihrem Mailizio Customer-Success-Manager Ihren Braze-REST-API-Schlüssel und Ihre Cluster-Instanz zur Verfügung. Das Mailizio-Team richtet dann die erste Integration für Sie ein.

{% alert important %}
Dies ist eine einmalige Einrichtung, und alle zukünftigen Exporte verwenden automatisch diesen API-Schlüssel.
{% endalert %}

### 1. Schritt: Erstellen Sie eine E-Mail in Mailizio {#step-1-create-an-email-in-mailizio}

Erstellen Sie in Mailizio mit dem Drag-and-Drop-Editor eine E-Mail, die Ihre Markenidentität widerspiegelt, und klicken Sie dann auf **Save**, um Ihre Arbeit zu sichern.

![Screenshot des Drag-and-Drop-Editors]({% image_buster /assets/img/mailizio/screenshot_1.png %})

### 2. Schritt: Exportieren Sie Ihr E-Mail-Template nach Braze {#step-2-export-your-email-template-to-braze}

Wenn Sie fertig sind, klicken Sie auf **Export Newsletter**. Wählen Sie im Popup-Fenster **Braze-email** aus und bestätigen Sie den Export.

Wenn Sie Ihre Inhalte später aktualisieren, exportieren Sie sie erneut aus Mailizio, um sie in Braze zu aktualisieren.

![Screenshot des Export-Modals]({% image_buster /assets/img/mailizio/screenshot_2.png %})

{% alert important %}
Sie können Content Blocks auf die gleiche Weise mit dem **Module**-Editor von Mailizio erstellen und exportieren.
{% endalert %}

## Nutzung {#usage}

Ihre hochgeladene Mailizio-Vorlage finden Sie in Ihrem Braze-Konto im Bereich **Templates und Medien > E-Mail-Templates**. Mit diesem E-Mail-Template können Sie jetzt damit beginnen, ansprechende E-Mail-Nachrichten an Ihre Kund:innen zu versenden!