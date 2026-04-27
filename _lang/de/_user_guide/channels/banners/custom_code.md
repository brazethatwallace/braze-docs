---
nav_title: Angepasster Code und JavaScript-Brücke
article_title: Angepasster Code und JavaScript-Brücke für Banner
page_order: 2
page_type: reference
description: "Erfahren Sie, wie Sie angepasstes HTML in Bannern und die JavaScript-Brücke verwenden können, um Klicks zu protokollieren und Braze-Aktionen zu triggern."
channel:
  - banners
---

# Angepasster Code und JavaScript-Brücke für Banner {#custom-code-and-javascript-bridge-for-banners}

> Wenn Sie den Editor-Block **Benutzerdefinierter Code** im Banner-Composer verwenden, müssen Sie `brazeBridge.logClick()` innerhalb Ihres angepassten HTML aufrufen, um Klicks zu protokollieren. Banner verwenden dieselbe JavaScript-Brücke wie HTML-In-App-Nachrichten, daher gelten dieselben Methoden und Muster.

Wenn Sie in Ihrem Banner-Design angepasstes HTML verwenden, kann das Braze SDK nicht automatisch Klick-Listener an Elemente innerhalb Ihres angepassten Codes anhängen. Sie müssen `brazeBridge.logClick()` explizit für alle anklickbaren Elemente (Links, Buttons und Ähnliches) aufrufen, die Sie im Analytics-Tool der Campaign verfolgen möchten.

Um beispielsweise einen Klick zu protokollieren, wenn Nutzer:innen in Ihrem angepassten HTML auf einen Button tippen:

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Die vollständige JavaScript-Bridge-Referenz, einschließlich aller verfügbaren Methoden und Optionen für Klick-Tracking, finden Sie im folgenden Abschnitt.

## JavaScript-Brücke {#javascript-bridge}

{% include javascript_bridge/reference.md %}