---
nav_title: Constructor
article_title: Constructor
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Constructor. Diese Partnerschaft ermöglicht es Ihnen, Constructors Offsite Product Discovery zu nutzen, um dynamisch personalisierte Produktempfehlungen in Braze-Nachrichten zu erstellen und zuzustellen."
alias: /partners/constructor/
page_type: partner
search_tag: Partner
---

# Constructor

> [Constructor](https://constructor.com/) ist eine Such- und Produktentdeckungsplattform, die KI und maschinelles Lernen einsetzt, um personalisierte Suchen, Empfehlungen und Browsing-Erlebnisse für E-Commerce- und Einzelhandels-Websites bereitzustellen.

Mit der Integration von Braze und Constructor können Sie die Offsite Product Discovery von Constructor nutzen, um dynamisch personalisierte Produktempfehlungen in Braze-Nachrichten zu erstellen und zuzustellen.

## Anwendungsfälle {#use-cases}

- **Warenkorb-Abbruch und Nachbestellungs-Follow-ups**: Erstellen Sie dynamische Produktempfehlungen auf Grundlage des Nutzerverhaltens und des Warenkorb-Inhalts, um personalisierte Erinnerungen an abgebrochene Warenkörbe oder Vorschläge für Nachbestellungen zu versenden.
- **Ähnliche Produktempfehlungen für Artikel im abgebrochenen Warenkorb**: Schlagen Sie ähnliche Produkte zu Artikeln vor, die im Warenkorb einer Nutzerin oder eines Nutzers verblieben sind, um das Engagement aufrechtzuerhalten und Alternativen anzubieten.
- **Erinnerungen an kürzlich angesehene Artikel**: Benachrichtigen Sie Nutzer:innen über Artikel, die sie kürzlich angesehen, aber noch nicht gekauft haben, und ermutigen Sie sie, ihren Kauf abzuschließen.
- **Aktionskampagnen**: Versenden Sie personalisierte Aktionsnachrichten mit kuratierten Produktempfehlungen, die auf die Präferenzen der Nutzer:innen zugeschnitten sind – für saisonale Verkäufe oder Sonderangebote.
- **Visuell ähnliche Produktvorschläge**: Empfehlen Sie visuell ähnliche Artikel zu denen, die Nutzer:innen kürzlich angesehen haben, und helfen Sie ihnen, verwandte Optionen zu entdecken, die sie bevorzugen könnten.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|-------------|-------------|
| Constructor-Konto | Ein Constructor-Konto mit aktiviertem Offsite-Discovery-Dienst ist erforderlich, um diese Partnerschaft zu nutzen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Arbeiten Sie mit Ihrem Constructor-Onboarding-Team zusammen, um den Integrationsprozess abzuschließen. Stellen Sie sicher, dass Verhaltensdaten von Ihrer Website oder anderen relevanten Datenquellen verfügbar sind, um personalisierte Produktempfehlungen zu ermöglichen. Ihr Constructor-Onboarding-Team hilft Ihnen auch bei der Konfiguration der notwendigen HTML-Snippets für die Verwendung in Braze-Nachrichten.

## Offsite-Discovery-API-URL von Constructor {#constructors-offsite-discovery-api-url}

Sie können die Offsite-Discovery-API-URL von Constructor verwenden, um Produktbilder zu rendern und Nutzer:innen auf die entsprechende Produktdetailseite zu leiten. Im Folgenden finden Sie eine Aufschlüsselung der Endpunkt-Struktur und ein Beispiel für die Verwendung:

### Beispiel {#example}

```html
<a href="https://offsite-discovery.cnstrc.com/v1/product/url?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]" target="_blank">
  <img
    src="https://offsite-discovery.cnstrc.com/v1/product/image?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]"
    width="200"
    border="0"
    alt="Shop Now"
  />
</a>
```

### Parameter {#parameters}

| Parameter | Beschreibung |
|-------------|-------------|
| `position` | Bezieht sich auf die Rangfolge des empfohlenen Artikels innerhalb der Vorschlagsliste (z. B. `position = 2`). <br>![Positionsrangfolge des Artikels.]({% image_buster /assets/img/constructor/constructor_position.png %}) |
| `ui` | Stellt den Bezeichner der Nutzerin oder des Nutzers dar, der für die Personalisierung der Empfehlungsergebnisse entscheidend ist. Setzen Sie den Parameter `ui` auf die `external_id` der geschäftskunden in Braze. Wird dieser Parameter weggelassen, gibt Constructor allgemeine Empfehlungen anstelle von nutzerspezifischen zurück. |
| `pod_id` | Bezeichner für den Pod, der die Strategie und die Searchandising-Regeln für Empfehlungen enthält (z. B. erzeugt ein Pod mit einer Bestseller-Strategie personalisierte Bestseller). |
| `key` | Der Constructor-Indexschlüssel für diese geschäftskunden. |
| `style_id` | Legt fest, welche Bilder für die Produktkarte angezeigt werden. Zum Beispiel zeigen verschiedene `style_ids` unterschiedliche Produktkartenbilder an. |
| `campaign_id` | Eindeutige ID für die E-Mail-Kampagne. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Parameter" }

### Optionale Eingaben {#optional-inputs}

| Eingabe | Beschreibung |
|-------------|-------------|
| `item_id` | Stellt den Ausgangsartikel dar. Notwendig für artikelbasierte Strategien wie alternative, ergänzende oder Bündel-Empfehlungen. Zum Beispiel ist der erste Artikel in einer E-Mail der Ausgangsartikel, die nachfolgenden Artikel sind Alternativen. |
| `num_results` | Anzahl der Produkte, die der E-Mail hinzugefügt werden sollen. Der Standardwert ist 10, maximal 100. Zum Beispiel bedeutet `num_results = 3`, dass drei Empfehlungen hinzugefügt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Optionale Eingaben" }