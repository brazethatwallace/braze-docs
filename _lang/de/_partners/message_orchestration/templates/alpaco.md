---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/alpaco/
description: "Die Integration von Braze und Alpaco erlaubt Ihnen den Export von markenkonformen, Liquid-kompatiblen E-Mail-Templates und Content Blocks nach Braze, die sofort in E-Mails und In-App-Nachrichten einsatzbereit sind."
page_type: partner
search_tag: Partner
---

# Alpaco

> [Alpaco](https://alpaco.email/) ist ein Online-Creative-Management-Tool, das einen Drag-and-Drop-Editor zur Erstellung wiederverwendbarer, markensicherer Inhalte für Braze bietet. Die Integration von Alpaco und Braze erlaubt es Ihnen, Content Blocks, E-Mail-Templates und In-App-Templates zu exportieren.

_Diese Integration wird von Alpaco gepflegt._

{% alert note %}
Alpaco unterstützt [alle Liquid-Variablen](https://shopify.github.io/liquid/) und somit auch alle Liquid-Variablen, die in Ihren Braze-Konfigurationen verwendet werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ------------| ----------- |
| Alpaco-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Alpaco-Konto. |
| Braze-Representational State Transfer-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit vollständigen **Templates**-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Cluster-Instanz | Ihre Braze-[Cluster-Instanz]({{site.baseurl}}/api/basics/#endpoints) ist auf Ihr Braze-Dashboard und Ihren Representational State Transfer-Endpunkt abgestimmt. <br><br> Wenn Ihre Dashboard-URL zum Beispiel `https://dashboard-03.braze.com` lautet, ist Ihr Endpunkt `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

- Exportieren Sie vollständig gestaltete **E-Mail-Templates** zur Verwendung in Braze-Campaigns und transaktionalem Messaging.
- Erstellen und verwalten Sie **modulare Content Blocks** (z. B. Kopfzeilen, Fußzeilen, Aktionen), die über mehrere Kanäle hinweg wiederverwendet werden können.
- Entwerfen Sie ansprechende **In-App-Nachrichten** mit der gleichen kreativen Flexibilität wie bei E-Mails, sodass Sie auf einfache Weise konsistente, markengerechte Erlebnisse über alle Kanäle hinweg liefern können.
- Ermöglichen Sie **Personalisierung** durch Einbindung von Braze-unterstützten Liquid-Tags wie `{{first_name}}` oder `{{custom_attribute}}`.
- Sorgen Sie für **Markenkonsistenz**, indem Sie das kreative Design in Alpaco zentralisieren und Updates mit einem einzigen Export an Braze pushen.

## Integration

Stellen Sie dem Customer-Success-Team von Alpaco Ihren Braze-Representational State Transfer-API-Schlüssel und Ihre Cluster-Instanz zur Verfügung. Das Team wird dann die erste Integration für Sie einrichten.

{% alert note %}
Dies ist eine einmalige Einrichtung, und alle zukünftigen Exporte werden automatisch diesen API-Schlüssel verwenden.
{% endalert %}

## Exportieren von Alpaco-Nachrichten nach Braze {#exporting-alpaco-messages-to-braze}

### 1. Schritt: Erstellen Sie ein Template in Alpaco {#step-1-create-a-template-in-alpaco}

Erstellen Sie in Alpaco ein Template, das Ihre Markenidentität zum Ausdruck bringt. Wenn Sie fertig sind, wählen Sie **Save**.

![Alpaco-Template erstellen]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### 2. Schritt: Entwerfen Sie eine Nachricht unter Verwendung des Templates {#step-2-draft-a-message-using-the-template}

Als Nächstes gehen Sie in die Alpaco-Lobby und verwenden Ihr Template, um eine E-Mail, eine In-App-Nachricht oder einen Content Block zu erstellen. Um Ihre Nachricht vor dem Exportieren noch einmal zu überprüfen, wählen Sie **Review**.

![Alpaco-E-Mail erstellen]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### 3. Schritt: Exportieren Sie Ihre Nachricht nach Braze {#step-3-export-your-message-to-braze}

Wählen Sie **Export**, wählen Sie dann die Braze-Integration und geben Sie an, ob Sie ein E-Mail-Template oder einen Content Block exportieren.

Wenn Sie nach dem Export Änderungen vornehmen, können Sie den Inhalt aus Alpaco erneut exportieren, um ihn in Braze zu Update or aktualisieren or aktualisieren.

![Alpaco-E-Mail exportieren]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Verwendung von Alpaco-Templates und -Blöcken in Braze {#using-alpaco-templates-and-blocks-in-braze}

Je nach Art des exportierten Inhalts wird Ihr Template in einem der folgenden Abschnitte angezeigt:

- **Templates und Medien > E-Mail-Templates**
- **Templates und Medien > Content Blocks**

Die Templates von Alpaco sind ideal für Unternehmen, die die Markenkonsistenz zentral verwalten möchten. Sie unterstützen auch die in Braze integrierten Tags zur einfachen Kategorisierung und Verwaltung von Inhalten.