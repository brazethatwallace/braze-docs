---
nav_title: Empfohlene Events
article_title: Empfohlene Events
alias: /recommended_events/
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt empfohlene Events – Empfehlungen von Braze für E-Commerce-Events."
---

# Empfohlene Events {#recommended-events}

> Empfohlene Events bilden die gängigsten E-Commerce-Anwendungsfälle ab. Durch die Nutzung empfohlener Events erhalten Sie Zugang zu vorgefertigten Canvas-Templates, Reporting-Dashboards, die den Kundenlebenszyklus abbilden, und vieles mehr.

Beispielsweise könnten Sie ein angepasstes Event namens „cart_updated“ oder „update_to_cart“ haben, um zu erfassen, wenn Nutzer:innen Produkte in ihrem Warenkorb hinzugefügt, entfernt oder aktualisiert haben. Für empfohlene Events stellt Braze das Event-Template bereit, das einen definierten Namen und relevante Eigenschaften für dieses Event enthält.

{% alert important %}
Empfohlene Events befinden sich derzeit im Early Access. Kontaktieren Sie Ihren Braze Customer-Success-Manager, wenn Sie an der Teilnahme an diesem Early Access interessiert sind. <br><br>Wenn Sie den neuen [Shopify-Konnektor]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector) nutzen, stehen diese empfohlenen Events automatisch über die Integration zur Verfügung.
{% endalert %}

## So funktioniert es {#how-it-works}

Braze wendet eine spezielle Validierung auf alle empfohlenen Events an, und einige empfohlene Events verfügen über spezielle Nachbearbeitungsaktionen. Für bestimmte branchenspezifische empfohlene Events kann Braze eine spezielle Behandlung unterstützen, wie z. B. neue aktionsbasierte Trigger für Campaigns und Canvases.

Empfohlene Events funktionieren ähnlich wie [angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events/). Sie können empfohlene Events aus Currents exportieren, sie auf eine Blocklist setzen und im Reporting verwenden. Sie können auch Daten zum Tracking dieser Events über das [Braze SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/) oder den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) an Braze senden.

### Empfohlene E-Commerce-Events {#ecommerce-recommended-events}

[Empfohlene E-Commerce-Events]({{site.baseurl}}/ecommerce_events/) basieren auf empfohlenen Events. Diese empfohlenen E-Commerce-Events erfassen Aktionen Ihrer Kund:innen, wie das Ansehen eines Produkts, das Aktualisieren des Warenkorbs oder das Starten des Checkout-Prozesses.

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

#### E-Commerce-Canvas-Templates {#ecommerce-canvas-templates}

Entdecken Sie unsere speziellen [E-Commerce-Anwendungsfälle]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/) für weitere Ideen, wie Sie vorgefertigte Braze-Canvas-Templates nutzen können, um wichtige Strategien umzusetzen.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Sind empfohlene Events dasselbe wie angepasste Events? {#are-recommended-events-the-same-as-custom-events}

Nein. Braze definiert festgelegte Datenschemata für empfohlene Events. Dazu gehören erforderliche und optionale Event-Eigenschaften, die in Braze einen Validierungsprozess durchlaufen. [Angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) sind spezifische Aktionen oder Updates Ihrer Nutzer:innen in Ihrer App oder auf Ihrer Website, die Sie tracken möchten. Sie können den Event-Namen und das, was getrackt wird, individuell anpassen.

### Kann ich den Namen der empfohlenen Events anpassen? {#can-i-customize-the-name-of-the-recommended-events}

Nein. Empfohlene Events haben standardisierte Event-Namen und Eigenschaften. Diese Standardisierungen sorgen für Konsistenz in Ihren Daten.

### Kann ich weiterhin Kauf-Events verwenden, um Käufe zu protokollieren? {#can-i-still-use-purchase-events-to-log-purchases}

Mit der Einführung der empfohlenen E-Commerce-Events wird Braze das Legacy-Kauf-Event in Zukunft auslaufen lassen. Wenn Sie derzeit das Kauf-Event verwenden, werden Sie rechtzeitig über die Abkündigungspläne informiert. In der Zwischenzeit können Sie die Kauf-Events bis zum offiziellen Abkündigungsdatum weiterhin nutzen.