---
nav_title: Denada
article_title: Denada
alias: /partners/denada/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Denada, einer KI or künstliche Intelligenz-gestützten Plattform für Marketing-Kreativmaterialien, mit der Sie markengerechte E-Mail-Templates durch natürliche Konversation erstellen und direkt nach Braze exportieren können."
page_type: partner
search_tag: Partner
---

# Denada

> [Denada](https://heydenada.com) ist eine KI or künstliche Intelligenz-gestützte Plattform für Marketing-Kreativmaterialien, mit der Fachexpert:innen markengerechte Marketingmaterialien durch natürliche Konversation erstellen können. Mit Denada können Teams von der Ideenfindung bis zum fertigen E-Mail-Inhalt gelangen – ganz ohne Designkenntnisse.

_Diese Integration wird von Denada gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Denada ermöglicht es Ihnen, in Denada erstellte E-Mail-Templates direkt nach Braze zu exportieren – einschließlich des automatischen Bild-Uploads in die Braze-Medienbibliothek. Dies vereinfacht den Prozess von der kreativen Ideenfindung bis zur Kampagnenausführung.

## Voraussetzungen {#prerequisites}

Folgendes ist für die Nutzung dieser Integration erforderlich:

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Denada-Konto | Ein [Denada-Konto](https://app.heydenada.com) ist für die Nutzung dieser Integration erforderlich. |
| Representational State Transfer-API-Schlüssel von Braze | Ein Representational State Transfer-API-Schlüssel von Braze mit vollständigen **Templates**-Berechtigungen. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Representational State Transfer-Endpunkt | [Ihre Representational State Transfer-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL Ihrer Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Denada wurde für Marketer und Fachexpert:innen entwickelt, die markengerechte E-Mail-Inhalte ohne Design- oder Programmierkenntnisse erstellen möchten. Es eignet sich besonders für alle, die:
- Konversationelle KI or künstliche Intelligenz nutzen möchten, um schnell E-Mail-Templates zu generieren und direkt nach Braze zu übertragen
- Bestehende Braze-E-Mail-Templates überarbeiten müssen, indem sie aus Denada erneut exportieren – mit Konflikterkennung und Überschreibungsunterstützung
- Automatischen Bild-Upload und automatische Bildverwaltung in der Braze-Medienbibliothek beim Export wünschen

## Integration

### Schritt 1: Integration konfigurieren {#step-1-configure-your-integration}

Wählen Sie in Denada Ihren Unternehmensnamen im Profilmenü aus und gehen Sie dann zu **Team settings** > **Add integration**.

Wählen Sie **Braze** als Integration aus, geben Sie dann Ihren Braze-**API-Schlüssel** ein und wählen Sie Ihren **Representational State Transfer-API-Endpunkt** aus der Liste der verfügbaren Regionen aus.

{% alert note %}
Dies ist eine einmalige Einrichtung. Sobald Ihre Zugangsdaten validiert sind, wird Ihre Konfiguration für alle zukünftigen Exporte gespeichert.
{% endalert %}

### Schritt 2: Ein Template nach Braze exportieren {#step-2-export-a-template-to-braze}

Öffnen Sie in Denada ein E-Mail-Template im Editor und wählen Sie **Export** > **Braze**.

Geben Sie einen Template-Namen und eine Betreffzeile für die E-Mail ein. Wählen Sie Ihre bevorzugte Bildverarbeitung:
- **Upload new:** Alle Bilder in die Braze-Medienbibliothek hochladen.
- **Use existing:** Zuvor hochgeladene Bilder wiederverwenden, sofern verfügbar.

Wenn bereits ein Template mit demselben Namen in Braze existiert, erkennt Denada den Konflikt und fordert Sie auf zu bestätigen, ob das bestehende Template überschrieben oder ein neues erstellt werden soll.

Wählen Sie **Export**. Denada rendert das Template in HTML, lädt Bilder nach Braze hoch und erstellt oder aktualisiert das E-Mail-Template in Ihrem Braze-Konto.

## Nutzung der Integration {#using-the-integration}

Sie finden Ihre hochgeladenen Denada-E-Mails in Braze unter **Templates und Medien** > **E-Mail-Templates**. Sie können sofort in jeder Braze-Campaign oder jedem Canvas verwendet werden.

Denada verfolgt vorherige Exporte, sodass nachfolgende Exporte desselben Templates das bestehende Braze-Template Update or aktualisieren or aktualisieren können, anstatt Duplikate zu erstellen.