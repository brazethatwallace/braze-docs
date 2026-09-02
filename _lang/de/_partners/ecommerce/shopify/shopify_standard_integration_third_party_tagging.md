---
nav_title: Shopify Standard-Integration mit Tagging von Drittanbietern
article_title: Shopify Standard-Integration mit Tagging von Drittanbietern
description: "Dieser Referenzartikel beschreibt, wie Sie die standardmäßige Shopify-Integration mit einem Tagging-Tool eines Drittanbieters einrichten."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration_third_party_tagging/
page_order: 2
---

# Shopify Standard-Integration mit Tagging-Tool von Drittanbietern {#shopify-standard-integration-with-third-party-tagging-tool}

> Diese Seite führt Sie durch die Verwendung von Drittanbieter-Tools wie Google Tag Manager:in mit der [Shopify-Standardintegration]({{site.baseurl}}/shopify_standard_integration), um das Braze Web SDK or Software-Development-Kit zu initialisieren und zu laden.

Für Shopify-Online-Shops empfehlen wir die Verwendung der Standard-Integrationsmethode von Braze, um die Braze SDKs auf Ihrer Website zu unterstützen. Wir verstehen jedoch, dass Sie möglicherweise ein Drittanbieter-Tool wie Google Tag Manager:in bevorzugen. Wenn Sie sich dafür entscheiden, ein Drittanbieter-Tool mit dem Shopify-Konnektor von Braze zu verwenden, beachten Sie, dass die Braze-Integration und die App-Einbettung das SDK or Software-Development-Kit während des Bestellvorgangs verwalten.

## Anforderungen {#requirements}

- **Konsistenter API-Schlüssel zwischen Ihrem Drittanbieter-Tool und dem Shopify-Konnektor:** Der API-Schlüssel muss sowohl in Braze als auch in Ihrem Drittanbieter-Tool konsistent sein. Dadurch wird die Erstellung doppelter Nutzer:innen verhindert und die Kompatibilität zwischen den SDKs aufrechterhalten.
  - **Speicherort des API-Schlüssels:** Nach dem Onboarding über den Standardintegrationspfad erstellt die Integration automatisch eine Braze-Web-App mit dem Namen „Shopify“. Rufen Sie den API-Schlüssel innerhalb der Integration ab, der mit der Konfiguration Ihres Drittanbieter-Tools verwendet wird.
- **Konsistente SDK or Software-Development-Kit-Versionen zwischen Ihrem Drittanbieter-Tool und dem Shopify-Konnektor:** Neue Kund:innen werden während der Einrichtung auf der neuesten SDK or Software-Development-Kit-Version bereitgestellt. Ihr Drittanbieter-Tool muss dieselbe SDK or Software-Development-Kit-Version verwenden, die in den Braze-Integrationseinstellungen konfiguriert ist. Bestehende Kund:innen werden benachrichtigt, wenn eine neuere Version verfügbar ist, und können Upgrades selbstständig über die Integrationseinstellungen durchführen.
- **Konsistentes SDK or Software-Development-Kit-Initialisierungs-Timing:** In Ihren Shopify-Standardintegrationseinstellungen können Sie die SDKs auswählen, die entweder beim Sitzungsstart oder bei der Kontoanmeldung initialisiert werden sollen. Diese Einstellung sollte zwischen Ihrem Drittanbieter-Tool und Braze konsistent sein. Inkonsistenzen könnten zu nachgelagerten Problemen bei der Nutzer:innen- und Datensynchronisierung führen.

{% alert note %}
Wir empfehlen die ausschließliche Verwendung der Standard-Integrationsmethode, anstatt sie zusammen mit Tag-Managern von Drittanbietern einzusetzen, da dies zu Konflikten zwischen dem Braze SDK or Software-Development-Kit und Drittanbieter-Tools führen kann. Wenn Sie ein Drittanbieter-Tool verwenden, testen Sie, ob alles wie erwartet funktioniert.
{% endalert %}

## Einrichten der Integration mit einem Drittanbieter-Tool {#setting-up-the-integration-with-a-third-party-tool}

Wenn Sie von den angegebenen Schritten abweichen, kann dies zu unerwarteten Problemen führen. Halten Sie sich daher genau an die Anweisungen.

1. Befolgen Sie die vorgegebenen Schritte zur [Einrichtung der Shopify-Standardintegration]({{site.baseurl}}/shopify_standard_integration). Aktivieren Sie beim [Aktivieren der Braze Web SDKs]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration#step-2-enable-braze-web-sdks) das Kontrollkästchen, das angibt, dass Sie ein Drittanbieter-Tool verwenden, um das Braze Web SDK or Software-Development-Kit zu Ihrer Shopify-Website hinzuzufügen.
2. Gehen Sie zu **Einstellungen** > **App-Einstellungen**, wählen Sie die **Shopify**-Web-App aus und kopieren Sie dann den **API key for Shopify on Web**.
3. Fügen Sie den API-Schlüssel in die Web-SDK or Software-Development-Kit-Konfiguration Ihres Drittanbieter-Tools ein und setzen Sie die SDK or Software-Development-Kit-Version so, dass sie mit der Braze-Shopify-Integration übereinstimmt.

{% alert note %}
Wenn Sie Google Tag Manager:in verwenden, stellen Sie sicher, dass die SDK or Software-Development-Kit-Versionen sowohl in GTM als auch in Ihrer Braze-Shopify-Integrationskonfiguration übereinstimmen.
{% endalert %}

## Erfassen von Shopify-Daten und Synchronisieren von Nutzer:innen {#capturing-shopify-data-and-syncing-users}

Solange das Web SDK or Software-Development-Kit über ein Drittanbieter-Tool im Frontend Ihrer Shopify-Website zugänglich ist, erfasst die Standardintegration die Shopify-Daten und synchronisiert die Nutzer:innen wie erwartet.

## Überlegungen und Haftungsausschlüsse {#considerations-and-disclaimers}

- **Initialisierungseinstellungen:** Wenn Sie Ihre Initialisierungseinstellungen über Ihr Drittanbieter-Tool ändern, kann die Synchronisierung von Nutzer:innen und Daten beeinträchtigt werden. Wenn Sie sich beispielsweise dafür entscheiden, Ihr SDK or Software-Development-Kit zu initialisieren, wenn ein Cookie-Zustimmungsformular akzeptiert wird, erhält Braze kein Tracking für anonyme Nutzer:innen oder Daten, bis die Nutzer:innen zustimmen.
- **Das direkte Setzen von Attributen über `dataLayer` wird nicht unterstützt:** Verwenden Sie `window.braze` anstelle von `dataLayer`, um Attribute festzulegen.
- **Potenzielle doppelte Nutzer:innen:** Wenn der API-Schlüssel in Braze und Ihrem Drittanbieter-Tool nicht übereinstimmt, werden möglicherweise doppelte Nutzer:innen erstellt.
- **SDK or Software-Development-Kit-Inkompatibilität:** Die Verwendung einer falschen Versionsnummer kann zu Problemen mit SDK or Software-Development-Kit-Methoden führen.